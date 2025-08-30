# src/simulation_engine.py

import threading
import time
import logging
import random
import networkx as nx

# --- Basic Logging Setup ---
# This setup ensures that logs from different threads are clearly marked.
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(threadName)s] - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


class DeviceNode(threading.Thread):
    """
    Represents a network device (router, switch) running in its own thread.
    Simulates basic network behavior like discovering neighbors and responding to events.
    """
    def __init__(self, device_name, device_type, neighbors):
        super().__init__(name=f"Node-{device_name}")
        self.device_name = device_name
        self.device_type = device_type
        self.neighbors = neighbors
        self.arp_table = {}  # Maps IP to MAC, simplified
        self.routing_table = {} # Simplified routing table
        self.is_running = threading.Event()
        self.is_running.set()  # Set to True by default, allowing the loop to run

    def run(self):
        """The main loop for the device thread."""
        logging.info(f"{self.device_type} {self.device_name} started.")
        self._discover_neighbors()

        while True:
            if not self.is_running.is_set(): # If event is cleared, pause
                time.sleep(0.5)
                continue
            
            # In a real simulation, this is where you would process packets,
            # update routing tables periodically, etc.
            # For this simulation, we just keep it alive.
            time.sleep(random.uniform(2, 5))

    def _discover_neighbors(self):
        """Simulates ARP and OSPF neighbor discovery."""
        logging.info(f"{self.device_name} is discovering neighbors...")
        for neighbor in self.neighbors:
            # Simulate ARP request/response
            simulated_mac = f"00:1A:2B:{random.randint(10,99)}:{random.randint(10,99)}:{random.randint(10,99)}"
            self.arp_table[neighbor] = simulated_mac
        logging.info(f"{self.device_name} ARP table populated: {self.arp_table}")
        
        # Simulate establishing routing adjacencies
        self.routing_table = {n: {'cost': 1} for n in self.neighbors} # Simplified static routes
        logging.info(f"{self.device_name} initial routing table established.")

    def pause(self):
        """Pauses the device's main loop."""
        self.is_running.clear()
        logging.info(f"Node {self.device_name} paused.")

    def resume(self):
        """Resumes the device's main loop."""
        self.is_running.set()
        logging.info(f"Node {self.device_name} resumed.")

    def update_link_status(self, neighbor, status):
        """Simulates reacting to a link failure or restoration."""
        if status == 'down':
            if neighbor in self.routing_table:
                del self.routing_table[neighbor]
                logging.warning(f"{self.device_name} detected link to {neighbor} is down. Updating routing table.")
        elif status == 'up':
            if neighbor not in self.routing_table:
                self.routing_table[neighbor] = {'cost': 1}
                logging.info(f"{self.device_name} detected link to {neighbor} is restored. Updating routing table.")


class SimulationEngine:
    """
    Manages the entire network simulation, including device threads and fault injection.
    """
    def __init__(self, graph):
        self.graph = graph
        self.devices = {}

    def start_simulation(self):
        """Initializes and starts all device threads."""
        logging.info("Starting multithreaded simulation engine...")
        for node_name in self.graph.nodes():
            device_type = self.graph.nodes[node_name].get('type', 'Unknown')
            # PCs are not simulated as active nodes in this model
            if device_type in ['Router', 'Switch']:
                neighbors = list(self.graph.neighbors(node_name))
                device_thread = DeviceNode(node_name, device_type, neighbors)
                self.devices[node_name] = device_thread
                device_thread.start()
        print("\n✅ Simulation engine started with all devices running.")

    def run_day1_scenario(self, stabilization_time=5):
        """Simulates the initial network bring-up and stabilization."""
        print(f"\n--- Running Day-1 Simulation: Network Stabilization ({stabilization_time}s) ---")
        time.sleep(stabilization_time)
        print("✅ Day-1 stabilization complete. Network is operational.")

    def run_day2_fault_injection(self):
        """Simulates link failures and restorations to test network resilience."""
        print("\n--- Running Day-2 Simulation: Fault Injection ---")
        if not self.devices:
            print("No active devices to run fault injection on.")
            return
            
        # Select a random link between two active devices to fail
        active_edges = [
            (u, v) for u, v in self.graph.edges() 
            if u in self.devices and v in self.devices
        ]
        if not active_edges:
            print("No active links between simulated devices.")
            return

        u, v = random.choice(active_edges)
        
        # --- Simulate Failure ---
        print(f"\nInjecting link failure: {u} <-> {v}")
        self.devices[u].update_link_status(v, 'down')
        self.devices[v].update_link_status(u, 'down')
        
        # Check for connectivity after failure
        temp_graph = self.graph.copy()
        temp_graph.remove_edge(u, v)
        
        if nx.is_connected(temp_graph):
            logging.info(f"✅ Network maintained connectivity after {u}<->{v} failure.")
        else:
            logging.error(f"❌ Network became partitioned after {u}<->{v} failure.")
        
        time.sleep(3) # Let the network run in a failed state

        # --- Simulate Restoration ---
        print(f"Restoring link: {u} <-> {v}")
        self.devices[u].update_link_status(v, 'up')
        self.devices[v].update_link_status(u, 'up')
        logging.info(f"✅ Link {u}<->{v} restored.")
        
    def pause_and_resume(self):
        """Demonstrates pausing and resuming the entire simulation."""
        print("\n--- Demonstrating Pause/Resume Capabilities ---")
        print("Pausing simulation...")
        for device in self.devices.values():
            device.pause()
        
        time.sleep(3) # Stay paused for 3 seconds
        
        print("Resuming simulation...")
        for device in self.devices.values():
            device.resume()
        print("✅ Simulation resumed.")

    def stop_simulation(self):
        """Gracefully stops all running device threads."""
        # This is a simplified stop; a more robust solution would use signaling.
        print("\n--- Stopping Simulation ---")
        # In this implementation, the threads are daemonic, so they will exit
        # when the main thread exits. A production system would need a
        # proper shutdown signal in the thread's main loop.
        print("Simulation concluded.")
