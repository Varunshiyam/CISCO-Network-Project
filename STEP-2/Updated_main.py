# src/main.py

import json
from parser import NetworkConfigParser
from topology_builder import TopologyBuilder # <-- IMPORT THE NEW CLASS

def main():
    """
    Main function to run the network analysis tool.
    """
    print("Cisco Virtual Internship - Complete Network Analysis Tool")
    print("="*60)

    # --- Step 1: Parsing and Validation ---
    print("Step 1: Parsing device configurations...")
    
    config_dir = './config'
    parser = NetworkConfigParser(config_dir)
    network_data = parser.parse_directory()

    if not network_data:
        print("❌ Parsing failed. Halting execution.")
        return

    num_configs = len(network_data)
    print(f"✅ Parsed {num_configs} configurations successfully.\n")
    
    # --- Step 2: Constructing Topology ---
    print("Step 2: Constructing hierarchical network topology...")
    
    builder = TopologyBuilder(network_data)
    graph = builder.build_graph()
    
    num_nodes = graph.number_of_nodes()
    num_links = graph.number_of_edges()
    print(f"✅ Built topology: {num_nodes} nodes, {num_links} links\n")
    
    # Generate the interactive visualization
    builder.visualize_topology()
    
    print("\n--- Next Steps ---")
    print("The graph object is now ready for validation and simulation.")


if __name__ == "__main__":
    main()

