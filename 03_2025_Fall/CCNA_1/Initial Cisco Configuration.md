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



!secure passwords

exit

service password-encryption



!provide legal notification

banner motd #*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Message \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\**#



!configure interfaces

interface F0/0 or G0/0 or F0/1 or G0/1

description *what is it for?*

ip address *ipv4 subnet*

ipv6 address *ipv6address/prefix-length*

no shutdown



ipv6 unicast-routing



interface gigabitethernet 0/0/0

ipv6 address *address (fe80 link-local)*

no shutdown

exit

interface gigabitethernet 0/0/1

ipv6 address *address (fe80 link-local)*

no shutdown

exit

interface serial 0/1/0

ipv6 address *address (fe80 link-local)*

no shutdown

exit



!ip default gateway

interface vlan1

ip address *ipv4 subnet*

no shutdown

exit

ip default-gateway *ipv4*



!save configuration

copy run start

