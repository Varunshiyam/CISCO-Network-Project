# 🕸️ Step 2: Topology Construction & Visualization

> In this step, we take the parsed configuration data from **Step 1** and transform it into a **visual network topology**.  
> Using **NetworkX** + **Pyvis**, we’ll build an interactive HTML graph where routers, switches, and PCs are color-coded.

---

## 📁 1. Updated Project Directory Structure
We add a new file `topology_builder.py` inside the `src/` directory and create a `reports/` folder to store visualizations.  


``` CISCO_NETWORK_TOOL/
├── configs/ # Device configuration files
├── outputs/ # Parsed JSON outputs (Step 1)
├── reports/ # 📊 New folder for HTML visualizations
├── src/
│ ├── config_parser.py # Parser from Step 1
│ ├── topology_builder.py # 🆕 Builds & visualizes topology
│ └── main.py # Updated main script
└── README.md
```

---

## ▶️ 2. Updated Main Script (src/main.py)

Now the main.py script performs both parsing (Step 1) and visualization (Step 2).

---

## 🚀 3. How to Run the Updated Code
Make sure your environment is active, and run the following:

### 🔹 Activate Virtual Environment

#### Windows:
```
.venv\Scripts\activate
```

#### Mac/Linux:

```
source .venv/bin/activate

```


### 🔹 Install Required Packages

``` 
pip install networkx
pip install pyvis
```


### 🔹 Run the Script

``` 
python src/main.py
```

---


## 🎯 4. Expected Output:

- ✅ Terminal confirms that an HTML report has been generated

- 📊 A new file: reports/network_topology.html

- 🌐 Open it in your browser to explore the interactive graph

---

## 📸 5. Example output:

<img width="378" height="410" alt="Screenshot of output" src="https://github.com/user-attachments/assets/717281b6-d811-4c21-a37b-4c7bb52113e5" />

---

## 6.💡 Visualization details:

- 🔴 Routers → Red

- 🔵 Switches → Blue

- 🟠 PCs → Orange

You can drag, zoom, and hover on nodes to see their details.

---

