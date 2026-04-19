# SDN Traffic Classification & Control using POX

## Overview
This project demonstrates Software Defined Networking (SDN) using Mininet and the POX Controller.

We simulate a simple network and implement traffic control rules to:
- Allow normal communication (ICMP ping)
- Block HTTP traffic (TCP port 80)

---

## Network Topology
- 1 Switch → s1
- 2 Hosts → h1, h2
- Remote SDN Controller → POX

---

## Technologies Used
- Mininet
- POX Controller
- Open vSwitch (OVS)
- OpenFlow 1.0
- Python

---

## How to Run

### 1. Start POX Controller
pox.py forwarding.l2_learning http_block

### 2. Start Mininet
sudo mn --topo single,2 --controller remote

### 3. Test Connectivity (Allowed Traffic)
mininet> h1 ping h2

Expected: Successful ping (0% packet loss)

### 4. Test Blocked Traffic (HTTP)
mininet> h2 python3 -m http.server 80  
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
- Control Plane (POX Controller)
- Data Plane (Switch)

The POX controller installs flow rules:
- ICMP traffic → allowed (forwarded normally)
- TCP port 80 → blocked (drop rule)

---

## Demo Proof

Video Demonstration includes:
- Running Mininet
- Running POX Controller
- Successful Ping (Allowed Traffic)
- Failed HTTP Request (Blocked Traffic)

Add your video link here:
<video controls src="demo_video.mp4" title="Title"></video>

---

## Project Structure

.
├── README.md
├── http_block.py
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
- POX uses OpenFlow 1.0 by default

---

## Status
- Working
- Screenshots Included
- Demo Ready