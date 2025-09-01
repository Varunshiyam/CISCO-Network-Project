# ⚙️ Cisco Network Tool – Setup & Execution Guide  

---

## 🖼️ Project Setup Overview  
<img width="650" height="311" alt="Project Setup Screenshot" src="https://github.com/user-attachments/assets/0f867618-91b0-475d-9ab5-3342baca6cd7" />

---

# ⚙️ Step 1: Project Setup & Foundational Parser

> 🛠️ *In this step, we prepare the development environment and build the **core parser** that reads Cisco configuration files and transforms them into structured data.*

---

## 🎯 Objectives
- 🖥️ **Set up the Python development environment**  
- 📂 **Parse router/switch/PC configuration files**  
- 🏷️ **Extract key details** such as hostnames, interfaces, IPs, VLANs, and protocols  
- 🧩 **Prepare structured objects** (Python dicts / JSON) for use in later steps  

---

## 🛠️ Environment Setup
To ensure smooth execution, follow these steps:

---

### 1. Create a Virtual Environment

```bash

python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows   


```


---


### 2. Install Dependencies

```bash

pip install networkx matplotlib pyvis
```


---


### 3. Libraries Used:


<img width="500" height="500" alt="Screenshot 2025-09-01 at 9 29 03 AM" src="https://github.com/user-attachments/assets/4f8eac4d-3d91-4df2-9d5e-0cbc0889bc02" />


#### 📂 Input Files:

Provide router/switch/PC configuration files in the configs/ folder. Example:

``` configs/
 ├── R1.txt
 ├── S1.txt
 ├── PC1.txt
 └── ...
```

#### 🔍 Parser Functionality:

The parser module reads .txt configuration files and extracts details:

- 🏷️ Device Hostname → (e.g., R1, S1)

- 🌐 Interface Details → Names, IPs, Subnet Masks

- 📡 Routing Protocols → OSPF, BGP configs

- 🗂️ VLAN Configurations → VLAN IDs & assignments

- ⚡ Bandwidth/MTU → Captured for links


---


### 📝 Example Workflow:

#### Input (R1.txt):

```
hostname R1
!
interface GigabitEthernet0/0
 ip address 192.168.1.1 255.255.255.0
 bandwidth 100000
!
router ospf 1
 network 192.168.1.0 0.0.0.255 area 0
```

#### Parser Output (JSON):

```
{
  "hostname": "R1",
  "interfaces": [
    {
      "name": "GigabitEthernet0/0",
      "ip": "192.168.1.1",
      "subnet": "255.255.255.0",
      "bandwidth": "100000"
    }
  ],
  "protocols": {
    "OSPF": ["192.168.1.0/24"]
  }
}
```


---
