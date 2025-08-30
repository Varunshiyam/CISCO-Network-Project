# src/main.py

import json
from parser import NetworkConfigParser

def main():
    """
    Main function to run the network analysis tool.
    """
    print("Cisco Virtual Internship - Complete Network Analysis Tool")
    print("="*60)

    # --- Step 1: Parsing and Validation ---
    print("Step 1: Parsing device configurations with comprehensive validation...")
    
    config_dir = './config'  # Relative path to your config files
    parser = NetworkConfigParser(config_dir)
    network_data = parser.parse_directory()

    if network_data:
        num_configs = len(network_data)
        print(f"✅ Parsed {num_configs} configurations successfully.\n")

        # Pretty-print the parsed data to verify correctness
        print("--- Parsed Network Data ---")
        print(json.dumps(network_data, indent=2))
        print("---------------------------\n")

        # This `network_data` object will be the input for the next steps.
        # e.g., build_topology(network_data)
    else:
        print("❌ Parsing failed. Please check the directory path and file contents.")


if __name__ == "__main__":
    main()
