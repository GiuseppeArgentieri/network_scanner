# network_scanner

## I have created this program that allows you to scan all the clients connected to your local network. It works on Linux-based operating systems and can be executed using a command similar to the following:

```console
python main.py -i 192.168.86.1/24
```
or
```console
python main.py --ip 192.168.86.1/24
```
Where:
- ip (or i) specifies the ip address you want to scan. In the example above, I added '/24' at the end to encompass all the IP addresses within the subnet.
