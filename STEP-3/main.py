# src/main.py

import json
from parser import NetworkConfigParser
from topology_builder import TopologyBuilder
from validator import NetworkValidator

def print_results(results):
    """Helper function to print validation results in a readable format."""
    print("\n--- Validation Results ---")
    for check, issues in results.items():
        if not issues:
            print(f"✅ {check.replace('_', ' ').title()}: No issues found.")
        else:
            print(f"❌ {check.replace('_', ' ').title()}: {len(issues)} issues found.")
            # Special formatting for load analysis dictionaries
            if isinstance(issues, list) and len(issues) > 0 and isinstance(issues[0], dict):
                for issue in issues:
                    print(f"   - Link {issue['link']} is {issue['status']} ({issue['utilization']}%)")
            else: # Standard formatting for lists of strings
                for issue in issues:
                    print(f"   - {issue}")
    print("--------------------------\n")

def main():
    """
    Main function to run the network analysis tool.
    """
    print("Cisco Virtual Internship - Complete Network Analysis Tool")
    print("="*60)

    # --- Step 1: Parsing ---
    print("\nStep 1: Parsing device configurations...")
    config_dir = './config'
    parser = NetworkConfigParser(config_dir)
    network_data = parser.parse_directory()
    if not network_data:
        print("❌ Parsing failed. Halting execution.")
        return
    print(f"✅ Parsed {len(network_data)} configurations successfully.")

    # --- Step 2: Topology Construction ---
    print("\nStep 2: Constructing hierarchical network topology...")
    builder = TopologyBuilder(network_data)
    graph = builder.build_graph()
    print(f"✅ Built topology: {graph.number_of_nodes()} nodes, {graph.number_of_edges()} links")
    builder.visualize_topology(output_dir='reports')

    # --- Step 3: Validation and Optimization ---
    print("\nStep 3: Running comprehensive network validation...")
    validator = NetworkValidator(network_data, graph)
    validation_results = validator.run_all_checks()
    
    print_results(validation_results)

    print("--- Next Steps ---")
    print("The network has been analyzed. The next step is the simulation engine.")


if __name__ == "__main__":
    main()

