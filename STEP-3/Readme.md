# 🔍 Step 3: Validation & Optimization Analysis

> In this step, we add **intelligence** to the project — validating configurations, detecting issues, and analyzing performance bottlenecks.  
> The system now checks for **errors, duplications, mismatches, loops, and load distribution** to make the network more reliable.

---

## 📁 1. Updated Project Directory Structure
We add a new file `validator.py` to handle **config validation** and **optimization analysis**.  

```
CISCO_NETWORK_TOOL/
├── configs/ # Device configuration files
├── outputs/ # Parsed JSON outputs (Step 1)
├── reports/ # HTML visualizations
├── src/
│ ├── config_parser.py # Step 1 - Parsing
│ ├── topology_builder.py # Step 2 - Visualization
│ ├── validator.py # 🆕 Step 3 - Validation & Analysis
│ └── main.py # Updated main script
└── README.md
```

---

## 📸 Example structure:  
<img width="203" height="548" alt="Directory Screenshot" src="https://github.com/user-attachments/assets/422ab7d9-5eeb-42fe-9ea9-05f83e786451" />

---

## 🧾 2. Updated Code for Validator (`src/validator.py`)
The `Validator` class runs multiple checks and reports issues.  

---

## 3. Updated Main Script (src/main.py)

Now main.py performs Step 1 → Step 2 → Step 3.

---

## 🚀 4. How to Run Step-3
Make sure your virtual environment is active (see Step-1 & Step-2 setup).

---

### 🔹 Run the Main Script
```
python src/main.py
```

---

## 🎯 5. Expected Output

### ✅ Terminal Output:

A printed Validation & Analysis Report listing issues (duplicates, loops, missing devices, etc.)

```
🔍 Validation & Analysis Report:
🚨 Duplicate IP found: 192.168.1.1 on R1 and R2
🔁 Potential loop detected: [['R1', 'R2', 'R3']]
```

---

### 📊 6. File Output:
reports/network_topology.html (same as Step 2 visualization)

Future enhancement: Save validation results in JSON for audit

---

