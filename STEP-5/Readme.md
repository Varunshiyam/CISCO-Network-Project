# 🚀 Step 5: Report Generator Integration

In this final step, we will add a **report generator module** to compile all simulation results and parsed network data into a single structured JSON file. This completes the CISCO_NETWORK_TOOL application.

---

## 📁 1. Final Project Directory Structure

We now add the `reporter.py` file to the `src` directory.  
Your final structure will look like this:

```
CISCO_NETWORK_TOOL/
│── reports/
│ └── network_graph.html
│── src/
│ ├── init.py
│ ├── parser.py
│ ├── topology_builder.py
│ ├── simulation_engine.py
│ ├── reporter.py <-- ✅ NEW FILE
│ └── main.py
│── requirements.txt
│── README.md
```

<img width="387" height="263" alt="Final Directory Structure" src="https://github.com/user-attachments/assets/30a7ed97-1cd0-4dbb-a0f2-6c944cc15127" />

---

## 📄 2. Code for Report Generator (`src/reporter.py`)

---

## ▶️ 3. Updated Main Script (src/main.py)

We now update the main.py script to include the Reporter class.
At the end of the workflow, the system will generate a final_report.json.

---

## 4. Expected Output

### After running the script:

- An interactive HTML graph (reports/network_graph.html)

- A final structured JSON report (reports/final_report.json)

### Example JSON structure:

```
{
    "parsed_data": { ... },
    "topology_data": { ... },
    "simulation_data": { ... }
}
```


---

## 💻 5. Terminal Commands:

### Activate Virtual Environment:

- Windows:

```
.venv\Scripts\Activate
```

- Mac/Linux:

```
source .venv/bin/activate
```

### Install Dependencies:

```
pip install networkx pyvis
```

### Run Final Application:

```
python src/main.py
```

---

> *✅ At this stage, your project is fully functional — it can parse configs, build topologies, simulate network behavior, and generate a complete JSON report. 🎉*
