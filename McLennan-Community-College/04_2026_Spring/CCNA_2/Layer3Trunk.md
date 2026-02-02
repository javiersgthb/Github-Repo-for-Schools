
# Inter-VLAN Routing with Layer 3 Switches Configuration

## Overview

Layer 3 switches enable inter-VLAN routing by combining switching and routing capabilities, allowing VLANs to communicate without a dedicated router.

## Prerequisites

- Layer 3 switch (e.g., Cisco Catalyst 3650, 3850)
- Multiple VLANs configured
- IP routing enabled

## Configuration Steps

### 1. Enable IP Routing

ip routing

### 2. Create VLANs

vlan 10
name Sales
vlan 20
name Engineering

### 3. Create SVIs (Switched Virtual Interfaces)

interface vlan 10
ip address 192.168.10.1 255.255.255.0
no shutdown

interface vlan 20
ip address 192.168.20.1 255.255.255.0
no shutdown

### 4. Assign Ports to VLANs

interface fastethernet 0/1
switchport mode access
switchport access vlan 10

## Verification

show ip route
show vlan brief
show interface vlan 10
