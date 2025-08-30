# src/topology_builder.py

import networkx as nx
from pyvis.network import Network
import ipaddress
from datetime import datetime
import os

class TopologyBuilder:
    """
    Builds a network topology graph from parsed data and creates a visualization.
    """
    def __init__(self, network_data):
        self.network_data = network_data
        self.graph = nx.Graph()

    def build_graph(self):
        """
        Constructs the network graph using NetworkX based on parsed configurations.
        """
        # 1. Add all devices as nodes
        for device_name, data in self.network_data.items():
            device_type = self._get_device_type(device_name)
            self.graph.add_node(device_name, type=device_type, title=f"{device_type}: {device_name}")

        # 2. Add edges by finding connected interfaces
        # Create a list of all interfaces from all devices
        all_interfaces = []
        for device_name, data in self.network_data.items():
            for if_name, if_data in data.get('interfaces', {}).items():
                if 'ip_address' in if_data:
                    all_interfaces.append({
                        'device': device_name,
                        'interface_name': if_name,
                        'ip': if_data['ip_address'],
                        'mask': if_data['subnet_mask'],
                        'bandwidth': if_data.get('bandwidth')
                    })

        # Compare every interface with every other interface to find links
        for i in range(len(all_interfaces)):
            for j in range(i + 1, len(all_interfaces)):
                if1 = all_interfaces[i]
                if2 = all_interfaces[j]

                # Two interfaces are connected if they are in the same subnet
                try:
                    net1 = ipaddress.IPv4Interface(f"{if1['ip']}/{if1['mask']}").network
                    net2 = ipaddress.IPv4Interface(f"{if2['ip']}/{if2['mask']}").network
                    if net1 == net2 and if1['device'] != if2['device']:
                        # Add an edge with metadata
                        self.graph.add_edge(
                            if1['device'], 
                            if2['device'],
                            title=f"Link between {if1['device']} ({if1['interface_name']}) and {if2['device']} ({if2['interface_name']})",
                            bandwidth=if1.get('bandwidth', 'N/A')
                        )
                except (ipaddress.AddressValueError, ValueError) as e:
                    print(f"Warning: Could not process IP {if1['ip']} or {if2['ip']}. Error: {e}")
        
        return self.graph

    def visualize_topology(self, output_dir='reports'):
        """
        Creates an interactive HTML visualization of the network graph using Pyvis.
        """
        if not self.graph.nodes:
            print("Graph is empty, cannot generate visualization.")
            return

        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)
        
        # Create a Pyvis network
        net = Network(height="750px", width="100%", notebook=False, cdn_resources='remote', directed=False)
        
        # Add nodes with specific colors for device types
        for node, attrs in self.graph.nodes(data=True):
            color = "#f0a30a"  # Default (e.g., PC)
            if attrs.get('type') == 'Router':
                color = "#e03021"  # Red
            elif attrs.get('type') == 'Switch':
                color = "#217ce0"  # Blue
            
            net.add_node(node, label=node, title=attrs.get('title'), color=color)

        # Add edges from the graph
        for u, v, attrs in self.graph.edges(data=True):
            net.add_edge(u, v, title=attrs.get('title'))
            
        # Generate the visualization
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(output_dir, f'network_topology_{timestamp}.html')
        
        net.set_options("""
        const options = {
          "physics": {
            "barnesHut": {
              "gravitationalConstant": -30000,
              "centralGravity": 0.5,
              "springLength": 150
            },
            "minVelocity": 0.75
          }
        }
        """)
        net.show(filename, notebook=False)
        print(f"✅ Interactive topology visualization saved to '{filename}'")

    def _get_device_type(self, device_name):
        if device_name.startswith('R'):
            return 'Router'
        elif device_name.startswith('S'):
            return 'Switch'
        elif device_name.startswith('PC'):
            return 'PC'
        return 'Unknown'

