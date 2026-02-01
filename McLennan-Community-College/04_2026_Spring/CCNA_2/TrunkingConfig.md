
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

```bash
# Enter interface configuration mode
configure terminal
interface GigabitEthernet0/1

# Set encapsulation protocol
encapsulation dot1q 1

# Enable trunking mode
switchport mode trunk

# Optional: Specify allowed VLANs
switchport trunk allowed vlan 1,10,20,30

# Exit and save
exit
write memory
```

### Verify Configuration

```bash
show interfaces trunk
show interfaces GigabitEthernet0/1 switchport
```

## Best Practices

- Use 802.1Q for interoperability
- Explicitly define allowed VLANs
- Assign native VLAN explicitly
- Monitor trunk status regularly
