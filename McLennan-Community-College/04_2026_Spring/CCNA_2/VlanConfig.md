
# VLAN Configuration with Router-on-a-Stick

## Overview
Router-on-a-Stick is a routing method that uses a single router interface to route traffic between multiple VLANs on a switch.

## Prerequisites
- Switch with VLAN support
- Router with subinterface capability
- Trunk link between switch and router

## Configuration Steps

### Switch Configuration
```
Switch(config)# vlan 10
Switch(config-vlan)# name VLAN10
Switch(config-vlan)# vlan 20
Switch(config-vlan)# name VLAN20

Switch(config)# interface fa0/1
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport trunk allowed vlan 10,20
```

### Router Configuration
```
Router(config)# interface fa0/0.10
Router(config-subif)# encapsulation dot1Q 10
Router(config-subif)# ip address 192.168.10.1 255.255.255.0

Router(config)# interface fa0/0.20
Router(config-subif)# encapsulation dot1Q 20
Router(config-subif)# ip address 192.168.20.1 255.255.255.0

Router(config)# interface fa0/0
Router(config-if)# no shutdown
```

## Verification
```
show vlan brief
show interfaces trunk
show ip route
```
