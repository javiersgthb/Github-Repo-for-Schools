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

!secure remote TELNET/SSH access

line vty 0 4
password *password*
login
transport input ssh telnet *(choose SSH, TELNET, or both)*
exit

!secure passwords

service password-encryption

!provide legal notification

banner motd # *\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Message \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* #



!configure interfaces IPv6

interface F0/0 or G0/0 or F0/1 or G0/1
description *what is it for?*
ip address *ipv4 subnet*
ipv6 address *ipv6address/prefix-length*
no shutdown
exit

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

vlan <i>number</i>
switchport access mode
switchport vlan <i>number</i>
exit

!save configuration

copy run start

