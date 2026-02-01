
# VLAN Configuration

## Overview

VLANs (Virtual Local Area Networks) logically segment a network to improve security, performance, and management.

## Switch Configuration

### Creating VLANs

Switch(config)# vlan 10
Switch(config-vlan)# name Sales
Switch(config-vlan)# exit

### Assigning Ports to VLANs

Switch(config)# interface fastethernet 0/1
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 10

### Trunk Configuration

Switch(config)# interface fastethernet 0/24
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport trunk allowed vlan 10,20,30

## Router Configuration (Router-on-a-Stick)

### Creating Subinterfaces

Router(config)# interface fastethernet 0/0.10
Router(config-subif)# encapsulation dot1Q 10
Router(config-subif)# ip address 192.168.10.1 255.255.255.0

## Verification Commands

Switch# show vlan brief
Switch# show interfaces trunk
Router# show ip route
