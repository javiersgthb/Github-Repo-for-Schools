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
exec-timeout *minutes* *seconds*
login

!secure passwords
service password-encryption
security passwords min-length *length*
login block-for *seconds* attempts *number* within *seconds*

!Set Domain, RSA, and username
ip domain-name cisco.com
crypto key generate rsa
username *username* secret *password*

!Configure SSH/Telnet
line vty 0 15
exec-timeout *minutes* *seconds*
transport input ssh
login (local)
exit
ip ssh version 2
exit

!provide legal notification
banner motd # *\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Message \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* #

!configure interfaces
interface *interface number*
description *what is it for?*
ip address *ipv4 subnet*
ipv6 address *ipv6address/prefix-length*
ipv6 address *ip-address* link local
no shutdown
exit

ip default-gateway *ipv4*

!configure loopback
interface loopback *number*
ip address *ip-address* *subnet-mask*
ipv6 address *ip-address*
exit

!setting the clock
clock set hh:mm:ss day month year

!switching VLANs
vlan *number*
switchport access mode
switchport vlan *number*
exit

!save configuration
write mem (copy running-config startup-config)
