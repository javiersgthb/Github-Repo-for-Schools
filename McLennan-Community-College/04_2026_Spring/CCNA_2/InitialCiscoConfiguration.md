# Initial Cisco Configuration

!enable privileged exec
en

!enter configuration
conf t

!configure device name
hostname *hostname*

!secure privileged exec
enable secret *password*

!secure user exec
line console 0
password *password*
login

!secure passwords
service password-encryption

!secure remote TELNET/SSH access
ip domain-name cisco.com
crypto key generate rsa
username *username* secret *password*
line vty 0 15
transport input ssh
login (local)
exit
ip ssh version 2
exit

!provide legal notification
banner motd # *\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Message \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* #

!configure interfaces IPv6
interface F0/0 or G0/0 or F0/1 or G0/1
description *what is it for?*
ip address *ipv4 subnet*
ipv6 address *ipv6address/prefix-length*
no shutdown
exit

!configure loopback
interface loopback *number*
ip address *ip-address* *subnet-mask*

!turn on IPv6 routing
ipv6 unicast-routing

!configure interfaces link-local
interface gigabitethernet 0/0/0
ipv6 address *address (fe80 link-local)*
no shutdown
exit

interface serial 0/1/0
ipv6 address *address (fe80 link-local)*
no shutdown
exit

!Configure IPv4
interface vlan1
ip address *ipv4 subnet*
no shutdown
exit

ip default-gateway *ipv4*

!switching VLANs
vlan *number*
switchport access mode
switchport vlan *number*
exit

!save configuration
write mem (copy running-config startup-config)
