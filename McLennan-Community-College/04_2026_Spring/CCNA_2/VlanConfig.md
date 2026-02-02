
# VLAN Configuration with Router-on-a-Stick

## Overview

Router-on-a-Stick is a routing method that uses a single router interface to route traffic between multiple VLANs on a switch.

## Prerequisites

- Switch with VLAN support
- Router with subinterface capability
- Trunk link between switch and router

## Configuration Steps

### Switch Configuration

vlan 10
name VLAN10
vlan 20
name VLAN20

interface fa0/1
switchport mode trunk
switchport trunk allowed vlan 10,20

### Router Configuration

interface fa0/0.10
encapsulation dot1Q 10
Rip address 192.168.10.1 255.255.255.0

interface fa0/0.20
encapsulation dot1Q 20
ip address 192.168.20.1 255.255.255.0

interface fa0/0
no shutdown

## Verification

show vlan brief
show interfaces trunk
show ip route
