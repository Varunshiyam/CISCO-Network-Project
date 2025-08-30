# ⚙️ Cisco Network Tool – Setup & Execution Guide  

---

## 🖼️ Project Setup Overview  
<img width="650" height="311" alt="Project Setup Screenshot" src="https://github.com/user-attachments/assets/0f867618-91b0-475d-9ab5-3342baca6cd7" />

---

# 🛠️ 2. Environment Setup  

Open your terminal or command prompt, navigate to the **`CISCO_NETWORK_TOOL`** directory, and run these commands to set up your Python environment.  

---

## 🔹 Create a Virtual Environment  


`python -m venv .venv `

## 🔹 Activate the Environment

- On Windows (PowerShell):
  

`.\.venv\Scripts\Activate.ps1`

- On macOS/Linux: 

`source .venv/bin/activate`

✅ Your terminal prompt should now show (.venv)

---

## 🔹 Install Necessary Libraries:

`pip install networkx pyvis matplotlib`

##  How to Run the Code

Make sure your terminal is in the root directory:

`CISCO_NETWORK_TOOL/`

Run the main script:

`python src/main.py`
