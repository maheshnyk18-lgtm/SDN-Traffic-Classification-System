# SDN Traffic Classification & Control using Ryu

## Overview
This project demonstrates Software Defined Networking (SDN) using Mininet and the Ryu Controller.

We simulate a simple network and implement traffic control rules to:
- Allow normal communication (ICMP ping)
- Block HTTP traffic (port 80)

---

## Network Topology
- 1 Switch → s1
- 2 Hosts → h1, h2
- Remote SDN Controller → Ryu

---

## Technologies Used
- Mininet
- Ryu Controller
- Open vSwitch (OVS)
- Python

---

## How to Run

### 1. Start Ryu Controller
ryu-manager traffic_controller.py

### 2. Start Mininet
sudo mn --topo single,2 --controller remote --switch ovsk

### 3. Test Connectivity (Allowed Traffic)
mininet> h1 ping h2

Expected: Successful ping (0% packet loss)

### 4. Test Blocked Traffic (HTTP)
mininet> h1 curl http://10.0.0.2

Expected: Connection timeout (HTTP blocked)

### 5. View Flow Rules
sudo ovs-ofctl dump-flows s1

---

## Screenshots

### Mininet Topology
![Topology](screenshots/topology.jpeg)

### Ping (Allowed Traffic)
![Ping](screenshots/ping.jpeg)

### HTTP Blocked
![HTTP Block](screenshots/http_block.jpeg)

### Flow Table
![Flow Table](screenshots/flow_table.jpeg)

### Controller Logs
![Controller](screenshots/controller.jpeg)

---

## Key Concept

SDN separates:
- Control Plane (Ryu Controller)
- Data Plane (Switches)

The controller dynamically installs rules:
- Allows ICMP traffic
- Blocks HTTP traffic

---

## Demo Proof
Video Demonstration includes:
- Running Mininet
- Running Ryu Controller
- Successful Ping (Allowed Traffic)
- Failed HTTP Request (Blocked Traffic)

Add your video link here:
<PASTE_YOUR_LINK>

---

## Project Structure

.
├── README.md
├── traffic_controller.py
└── screenshots/
    ├── topology.jpeg
    ├── ping.jpeg
    ├── http_block.jpeg
    ├── flow_table.jpeg
    └── controller.jpeg

---

## Notes
- Controller must be started before Mininet
- Uses remote controller mode
- Works on Ubuntu (VM / Native)

---


## Status
- Working
- Screenshots Included
- Demo Ready