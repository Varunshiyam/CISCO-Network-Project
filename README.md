<img width="2121" height="338" alt="Banner-cisco" src="https://github.com/user-attachments/assets/7bec4724-efd5-4bf0-b974-358d086dcece" />


---

# 🛜 Project: End-to-End Network Analysis & Simulation Framework


## 🔗 Cisco Network Tool — Parser, Visualizer & Simulator

> This project is a **Python-based networking Automation** that walks you through the entire lifecycle of a Cisco networking project — from **parsing router configs** to **visualizing topologies**, running a **multithreaded simulation**, and generating **JSON reports**.  
It is designed for learners ranging from **CCNA beginners** to **CCNP/CCIE aspirants**, making it a hands-on companion for real-world networking challenges.

---

## 🧑🏻‍💻 Code Execution - HTML/JSON File Generated:

https://github.com/user-attachments/assets/890df98c-2f94-4306-87a6-a6e9102530dd

---

## 🗺️ Topology Output:

https://github.com/user-attachments/assets/e273f2b6-0fa0-444b-8e6f-4a51e7975bda

---

## 📌 Features
✨ This tool provides end-to-end functionality:

- 📂 **Parse router configuration files** (`R1.txt`, `R2.txt`, `R3.txt`, etc.)
- 🖥️ **Extract device details**:
  - 🏷️ Router hostname  
  - 🌐 Interfaces, IP addresses, and subnet masks  
  - 📡 OSPF advertised networks  
- 🔍 **Discover direct links** between routers
- 🗺️ **Build and visualize** the network graph (NetworkX + Matplotlib)
- ⚡ **Multithreaded simulation engine**  
  - Device nodes run in parallel  
  - Simulates neighbor discovery & link failures  
- 📝 **Structured JSON Reports**  
  - Captures parsed data, discovered links, simulation logs, and results

---

## 🛠️ Installation & Setup
Follow these steps to set up the environment:

1. 📥 **Clone the repository**
   ```bash
   git clone https://github.com/your-username/cisco-network-tool.git
   cd cisco-network-tool

2. 🐍 **Create virtual environment & install dependencies**
```
python -m venv .venv
source .venv/bin/activate   # On Mac/Linux
.venv\Scripts\activate      # On Windows

pip install -r requirements.txt
```
3. ▶️ **Run the tool**

```
python src/main.py
```

---


## 📂 Project Directory Structure
After completing all steps (1 → 5), your project structure will look like this:

graphql
```
cisco-network-tool/
│── configs/                # Sample router configs (R1.txt, R2.txt, etc.)
│── output/                 # Generated reports & visualization outputs
│── src/
│   ├── parser.py           # Step 1: Parse router configs
│   ├── topology_builder.py # Step 2: Build network topology
│   ├── visualizer.py       # Step 3: Visualize with NetworkX + Matplotlib
│   ├── simulation_engine.py# Step 4: Multithreaded simulation engine
│   ├── reporter.py         # Step 5: Report generator (JSON)
│   └── main.py             # Entry point to run the tool
│── requirements.txt
│── README.md
```


---

## 📖 Step-by-Step Guide

### ✅ Step 1: Parser
- Extract hostnames, interfaces, IPs, and OSPF networks from Cisco router configs.

### ✅ Step 2: Topology Builder
- Build a graph of devices and links using NetworkX.

### ✅ Step 3: Visualization
- Plot the network graph with Matplotlib, displaying nodes (routers) and edges (links).

### ✅ Step 4: Simulation Engine

- Launch multithreaded device nodes simulating:

- Neighbor discovery:

- Link failures & recovery

- Each device runs as an independent thread.

### ✅ Step 5: Reporter

- Compile everything into a structured JSON file:

- Device info

- Link discovery results

- Simulation logs

---


## 📊 Example Output:

- Topology Graph
Generated via Matplotlib, showing routers and links.

- Simulation Logs
```
[R1] Discovered neighbor R2
[R2] Discovered neighbor R3
[Engine] Link between R1 and R2 failed
[R1] Lost neighbor R2
```
- Final JSON Report (output/report.json)
```
{
  "devices": {...},
  "links": [...],
  "simulation": {
    "events": [
      "R1 discovered R2",
      "R2 discovered R3",
      "Link between R1 and R2 failed"
    ]
  }
}
```

---


> ### 🎯 Who Is This For?:

> - 🟢 Beginners (CCNA) → Learn parsing & simple topologies

> - 🟡 Intermediate (CCNP) → Study OSPF/EIGRP behavior, simulate failures

> - 🔴 Advanced (CCIE Prep) → Extend the engine, test automation workflows

---


### 📌 Future Enhancements:

- 🔧 Support for BGP parsing

- 📡 Real-time traffic flow simulation

- 📑 Report export in PDF/HTML

- 🤖 Integration with n8n / Ansible for automation

---



### 📝 License:

This project is open-source under the MIT License.
Feel free to fork, contribute, and experiment with new features!

---

<img width="1470" height="213" alt="Screenshot 2025-09-01 at 6 28 26 PM" src="https://github.com/user-attachments/assets/344e9ff3-a789-49d8-ad70-cea7ea2e1233" />


---
