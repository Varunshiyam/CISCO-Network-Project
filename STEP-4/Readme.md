# ⚙️ Step 4: Multithreaded Simulation Engine

> In this step, we move beyond static validation into **dynamic simulation**.  
> Each network device becomes a **threaded node**, simulating startup, neighbor discovery, and fault handling.  
> The engine coordinates **Day-1 (normal startup)** and **Day-2 (fault injection)** events.

---

## 📁 1. Updated Project Directory Structure
We add the `simulation_engine.py` module inside `src/` for managing device simulations.

```
CISCO_NETWORK_TOOL/
├── configs/
├── outputs/
├── reports/
├── src/
│ ├── config_parser.py # Step 1 - Parsing
│ ├── topology_builder.py # Step 2 - Visualization
│ ├── validator.py # Step 3 - Validation
│ ├── simulation_engine.py # 🆕 Step 4 - Multithreaded Simulation
│ └── main.py # Updated main script
└── README.md
```


## 📸 Example structure:  

<img width="383" height="236" alt="Directory Screenshot" src="https://github.com/user-attachments/assets/473d0d9c-19a2-4dc6-94fd-1d05c7ba7831" />

---

## 📄 2. Code for Simulation Engine (`src/simulation_engine.py`)

This module introduces:

- **`DeviceNode`** → Represents a router/switch/PC, each running in its own thread  
- **`SimulationEngine`** → Manages startup, neighbor discovery, link failures, and recovery  

```
# src/simulation_engine.py
```
## ▶️ 3. Updated Main Script (src/main.py)

Now, Step-4 integrates with Steps 1–3.

## 🚀 4. How to Run the Simulation

Ensure your virtual environment is active and required packages are installed (Steps 1–2).

Run the simulation:
```
python src/main.py
```


## 🎯 5. Expected Output
✅ Terminal Logs
Device startup messages

Neighbor discoveries

Simulated link failure & restoration

Shutdown confirmation

``` 
🚀 Starting Simulation Engine...

[10:01:05] 🔌 R1 starting up...
[10:01:06] 🤝 R1 discovered neighbor R2
[10:01:06] 🤝 R2 discovered neighbor R1
⚡ Injecting link failure between R1 and R2...
[10:01:11] R1 Link to R2 is DOWN ❌
[10:01:11] R2 Link to R1 is DOWN ❌
🔧 Restoring link between R1 and R2...
[10:01:14] R1 Link to R2 is UP ✅
[10:01:14] R2 Link to R1 is UP ✅
🛑 Stopping Simulation Engine...

```

