📁 1. Updated Project Directory Structure
First, we'll add a new file, topology_builder.py, to your src directory and create a reports folder for the output.


<img width="400" height="310" alt="Screenshot 2025-08-30 at 12 40 22 PM" src="https://github.com/user-attachments/assets/79b21673-50bd-4c2a-98ec-1374d95a8462" />



 2. Code for Topology Builder (src/topology_builder.py)
This new module takes the parsed data from Step 1, builds a network graph using NetworkX, and then creates an interactive HTML visualization with Pyvis.


▶️ 3. Updated Main Script (src/main.py)
Now, we update the main.py script to import and use the new TopologyBuilder class. It will now perform both Step 1 and Step 2.



🚀 4. How to Run the Updated Code
Make sure your project is set up as described and your virtual environment is active.

Run the main.py script from your root directory (CISCO_NETWORK_TOOL/):


Expected Output:

<img width="378" height="410" alt="Screenshot 2025-08-30 at 12 40 07 PM" src="https://github.com/user-attachments/assets/717281b6-d811-4c21-a37b-4c7bb52113e5" />



File Output:
Opening the newly created .html file in your reports folder will show you an interactive graph of your network, which you can drag, zoom, and explore. Routers will be red, switches blue, and PCs orange.


## TERMINAL CODE:

----------

##### Windows:
.venv\Scripts\Activate


----------

#### MAC:

source .venv/bin/activate

----------

### 3. Install networkx

pip install networkx


----------

### Install Pyvis:

pip install pyvis

----------


## FINALLY TO RUN AFTER ALL PROCESS:

python src/main.py

