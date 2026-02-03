
# VLAN Trunking Configuration

## Overview

VLAN trunking allows multiple VLANs to traverse a single physical link between network devices using encapsulation protocols.

## Encapsulation Methods

### 802.1Q (Dot1Q)

Industry standard, open protocol.

### ISL (Inter-Switch Link)

Cisco proprietary protocol (legacy).

## Configuration Steps

### Enable Trunking on Interface

## Enter interface configuration mode

configure terminal
interface GigabitEthernet0/1

## Set encapsulation protocol

encapsulation dot1q 1

## Enable trunking mode

switchport mode trunk

## Set static trunking mode

switchport trunk encapsulation dot1q

## Optional: Specify allowed VLANs

switchport trunk allowed vlan 1,10,20,30

## Exit and save

exit
write memory

## Verify Configuration

show interfaces trunk
show interfaces GigabitEthernet0/1 switchport

## Best Practices

- Use 802.1Q for interoperability
- Explicitly define allowed VLANs
- Assign native VLAN explicitly
- Monitor trunk status regularly

## Troubleshooting Commands

### Verify Trunk Status

show interfaces trunk
show interfaces GigabitEthernet0/1 trunk

### Check VLAN Configuration

show vlan brief
show vlan id 10

### Diagnose Encapsulation Issues

do show interfaces GigabitEthernet0/1 switchport
do show interfaces trunk
do show vlan summary

### Monitor Trunk Errors

show interfaces GigabitEthernet0/1 counters errors
show interfaces GigabitEthernet0/1 status

### Common Issues

- **Mismatched encapsulation**: Verify both sides use same protocol
- **VLAN not allowed**: Check `switchport trunk allowed vlan`
- **Native VLAN mismatch**: Can cause spanning tree issues
- **Port in access mode**: Confirm `switchport mode trunk` is set
