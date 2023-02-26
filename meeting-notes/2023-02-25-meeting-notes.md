# February 25, 2023 Meeting

## Agenda

1. Look at a suspicious email
2. Review what we really need to do at the competition with DNS
3. Look back at the **How the Internet Works** diagram
   1. We just covered DNS
   2. We are going to talk about firewalls today
   3. We will configure a local firewall on our VMs
   4. Use `nc` to test them

## All the rest of the notes

Go to [the GitHub page where I occasionally post updates](https://github.com/sql-sith/cdc-2023).

resolvectl dns enp0s3 192.168.128.1
make it persistent
or disable the service

systemctl status named-resolvconf.service 
systemctl disable named-resolvconf.service 

listener nc
