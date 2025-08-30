# src/parser.py

import os
import re
import json

class NetworkConfigParser:
    """
    Parses network device configuration files to extract key details like
    hostname, interfaces, IP addresses, bandwidth, and routing protocols.
    """
    def __init__(self, config_directory):
        self.config_directory = config_directory
        self.parsed_data = {}

    def parse_directory(self):
        """
        Parses all .txt files in the specified configuration directory.
        """
        try:
            config_files = [f for f in os.listdir(self.config_directory) if f.endswith('.txt')]
            if not config_files:
                print(f"Warning: No .txt configuration files found in '{self.config_directory}'")
                return None

            for file_name in config_files:
                file_path = os.path.join(self.config_directory, file_name)
                with open(file_path, 'r') as f:
                    content = f.read()
                    self._parse_file_content(content)
            
            return self.parsed_data
        except FileNotFoundError:
            print(f"Error: Directory not found at '{self.config_directory}'")
            return None

    def _parse_file_content(self, content):
        """
        Uses regular expressions to extract information from a single config file's content.
        """
        hostname = self._extract_hostname(content)
        if not hostname:
            return # Skip files without a hostname

        self.parsed_data[hostname] = {
            'hostname': hostname,
            'interfaces': self._extract_interfaces(content),
            'ospf': self._extract_routing_protocol(content, 'ospf'),
            'bgp': self._extract_routing_protocol(content, 'bgp')
        }

    def _extract_hostname(self, content):
        match = re.search(r"hostname\s+(\S+)", content)
        return match.group(1) if match else None

    def _extract_interfaces(self, content):
        interfaces = {}
        # Regex to find blocks of interface configurations
        interface_blocks = re.findall(r"interface\s+(\S+)\n(.*?)(?=\n!|\ninterface|$)", content, re.DOTALL)
        
        for name, config in interface_blocks:
            interface_details = {}
            
            # IP Address and Subnet Mask
            ip_match = re.search(r"ip\s+address\s+([\d\.]+)\s+([\d\.]+)", config)
            if ip_match:
                interface_details['ip_address'] = ip_match.group(1)
                interface_details['subnet_mask'] = ip_match.group(2)

            # Bandwidth
            bw_match = re.search(r"bandwidth\s+(\d+)", config)
            if bw_match:
                interface_details['bandwidth'] = int(bw_match.group(1))

            # VLAN configuration for switches
            vlan_match = re.search(r"switchport\s+access\s+vlan\s+(\d+)", config)
            if vlan_match:
                interface_details['vlan'] = int(vlan_match.group(1))
            
            if interface_details:
                interfaces[name] = interface_details
                
        return interfaces

    def _extract_routing_protocol(self, content, protocol_name):
        protocol_details = {}
        # Regex to find the routing protocol block
        proto_match = re.search(r"router\s+" + protocol_name + r"\s+(\d+)\n(.*?)(?=\n!|$)", content, re.DOTALL)
        
        if proto_match:
            protocol_details['process_id'] = int(proto_match.group(1))
            config_block = proto_match.group(2)
            
            # Find all network statements
            networks = re.findall(r"network\s+([\d\.]+)\s+([\d\.]+)\s+area\s+(\d+)", config_block)
            if networks:
                protocol_details['networks'] = [
                    {'network': net[0], 'wildcard': net[1], 'area': int(net[2])} for net in networks
                ]
        
        return protocol_details if protocol_details else None
