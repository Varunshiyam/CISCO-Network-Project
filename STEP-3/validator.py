# src/validator.py

import ipaddress
import networkx as nx
from collections import defaultdict

class NetworkValidator:
    """
    Performs validation and optimization analysis on the parsed network data and topology graph.
    """
    def __init__(self, network_data, graph):
        self.network_data = network_data
        self.graph = graph
        self.results = {}

    def run_all_checks(self):
        """
        Runs all validation and analysis checks and returns the results.
        """
        self.results['duplicate_ips'] = self._check_duplicate_ips()
        self.results['network_loops'] = self._check_network_loops()
        self.results['load_analysis'] = self._analyze_link_utilization()
        self.results['load_balancing_recommendations'] = self._recommend_load_balancing()
        # Placeholder for future checks
        self.results['missing_components'] = [] 
        self.results['vlan_issues'] = []
        self.results['gateway_issues'] = []
        self.results['mtu_mismatches'] = []

        return self.results

    def _check_duplicate_ips(self):
        """
        Checks for duplicate IP addresses within the same subnet across all devices.
        """
        issues = []
        subnet_map = defaultdict(list)
        
        # Group IPs by subnet
        for device, data in self.network_data.items():
            for if_name, if_data in data.get('interfaces', {}).items():
                if 'ip_address' in if_data and 'subnet_mask' in if_data:
                    try:
                        ip_interface = ipaddress.IPv4Interface(f"{if_data['ip_address']}/{if_data['subnet_mask']}")
                        subnet = str(ip_interface.network)
                        subnet_map[subnet].append({'device': device, 'ip': if_data['ip_address']})
                    except ValueError:
                        continue # Ignore invalid IP data
        
        # Find duplicates in each subnet
        for subnet, devices in subnet_map.items():
            ip_counts = defaultdict(list)
            for dev_info in devices:
                ip_counts[dev_info['ip']].append(dev_info['device'])
            
            for ip, dev_list in ip_counts.items():
                if len(dev_list) > 1:
                    issues.append(f"Duplicate IP {ip} found on devices: {', '.join(dev_list)} in subnet {subnet}")
        return issues

    def _check_network_loops(self):
        """
        Uses NetworkX to detect cyclical paths (loops) in the topology.
        """
        issues = []
        try:
            loops = list(nx.cycle_basis(self.graph))
            if loops:
                for loop in loops:
                    issues.append(f"Potential network loop detected involving: {' -> '.join(loop)}")
        except nx.NetworkXError as e:
            issues.append(f"Could not perform loop detection. Error: {e}")
        return issues

    def _analyze_link_utilization(self, traffic_per_pc=50000):
        """
        Analyzes link utilization based on a simple traffic model.
        Assumes each PC generates a fixed amount of traffic.
        """
        analysis = []
        pcs = [node for node, attr in self.graph.nodes(data=True) if attr.get('type') == 'PC']
        
        for u, v, attrs in self.graph.edges(data=True):
            bandwidth_kbps = attrs.get('bandwidth')
            if not bandwidth_kbps:
                continue

            # Simple model: assume traffic from all PCs could traverse this link
            # A more complex model would use routing paths
            potential_load = len(pcs) * traffic_per_pc
            utilization = (potential_load / (bandwidth_kbps * 1000)) * 100  # Convert kbps to bps
            
            if utilization > 80: # Threshold for high utilization
                analysis.append({
                    "link": f"{u}-{v}",
                    "utilization": round(utilization, 2),
                    "status": "Heavily utilized"
                })
        return analysis

    def _recommend_load_balancing(self):
        """
        Recommends alternative paths for heavily utilized links.
        """
        recommendations = []
        # This check depends on the results of the utilization analysis
        utilized_links = self.results.get('load_analysis', [])

        for link_info in utilized_links:
            if link_info['status'] == "Heavily utilized":
                u, v = link_info['link'].split('-')
                
                # Temporarily remove the overloaded edge to find alternate paths
                original_edge_data = self.graph.get_edge_data(u, v)
                self.graph.remove_edge(u, v)
                
                try:
                    paths = list(nx.all_simple_paths(self.graph, source=u, target=v, cutoff=5))
                    if paths:
                        recommendations.append(
                            f"For heavily utilized link {u}-{v}, consider distributing load across {len(paths)} alternate routes. "
                            f"Example alternate path: {' -> '.join(paths[0])}"
                        )
                    else:
                        recommendations.append(f"Link {u}-{v} is critical and has no simple alternate paths.")
                except nx.NetworkXNoPath:
                     recommendations.append(f"Link {u}-{v} is critical and has no alternate paths.")

                # Add the edge back for subsequent analysis
                self.graph.add_edge(u, v, **original_edge_data)

        return recommendations

