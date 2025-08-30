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
        # 1. Add all devices as nodes, determining their type for visualization.
        for device_name in self.network_data:
            device_type = self._get_device_type(device_name)
            self.graph.add_node(device_name, type=device_type, title=f"{device_type}: {device_name}")

        # 2. Create a comprehensive list of all interfaces to find connections.
        all_interfaces = []
        for device_name, data in self.network_data.items():
            for if_name, if_data in data.get('interfaces', {}).items():
                if 'ip_address' in if_data and 'subnet_mask' in if_data:
                    all_interfaces.append({
                        'device': device_name,
                        'interface_name': if_name,
                        'ip': if_data['ip_address'],
                        'mask': if_data['subnet_mask'],
                        'bandwidth': if_data.get('bandwidth')
                    })

        # 3. Compare every interface against every other to find matching subnets, which indicates a link.
        for i in range(len(all_interfaces)):
            for j in range(i + 1, len(all_interfaces)):
                if1 = all_interfaces[i]
                if2 = all_interfaces[j]

                # Two interfaces are connected if they belong to the same IP network.
                try:
                    net1 = ipaddress.IPv4Interface(f"{if1['ip']}/{if1['mask']}").network
                    net2 = ipaddress.IPv4Interface(f"{if2['ip']}/{if2['mask']}").network
                    if net1 == net2:
                        # Add an edge with metadata for bandwidth and interface details.
                        link_title = (f"Link: {if1['device']}({if1['interface_name']}) <-> "
                                      f"{if2['device']}({if2['interface_name']})\n"
                                      f"Bandwidth: {if1.get('bandwidth', 'N/A')} Kbps")
                        self.graph.add_edge(
                            if1['device'], 
                            if2['device'],
                            title=link_title,
                            bandwidth=if1.get('bandwidth')
                        )
                except (ipaddress.AddressValueError, ValueError) as e:
                    print(f"Warning: Could not process IP Address. Invalid data for {if1['device']} or {if2['device']}. Error: {e}")
        
        return self.graph

    def visualize_topology(self, output_dir='reports'):
        """
        Creates an interactive HTML visualization of the network graph using Pyvis.
        """
        if not self.graph.nodes:
            print("Error: The graph is empty. Cannot generate visualization.")
            return

        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)
        
        # Initialize Pyvis network with settings for a better layout
        net = Network(height="800px", width="100%", notebook=False, cdn_resources='remote', directed=False)
        
        # Add nodes with colors based on device type
        for node, attrs in self.graph.nodes(data=True):
            color = "#f0a30a"  # Orange for PC/Unknown
            if attrs.get('type') == 'Router':
                color = "#e03021"  # Red
            elif attrs.get('type') == 'Switch':
                color = "#217ce0"  # Blue
            
            net.add_node(node, label=node, title=attrs.get('title'), color=color, size=25)

        # Add all the edges from our NetworkX graph
        net.from_nx(self.graph)
            
        # Configure physics for a more stable, readable layout
        net.set_options("""
        const options = {
          "physics": {
            "barnesHut": {
              "gravitationalConstant": -40000,
              "centralGravity": 0.3,
              "springLength": 120,
              "springConstant": 0.05
            },
            "minVelocity": 0.75,
            "solver": "barnesHut"
          }
        }
        """)
        
        # Generate the HTML file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(output_dir, f'network_topology_{timestamp}.html')
        
        net.show(filename, notebook=False)
        print(f"✅ Interactive topology visualization saved to '{filename}'")

    def _get_device_type(self, device_name):
        """Helper function to determine device type from its hostname."""
        if device_name.upper().startswith('R'):
            return 'Router'
        elif device_name.upper().startswith('S'):
            return 'Switch'
        elif device_name.upper().startswith('PC'):
            return 'PC'
        return 'Unknown'

