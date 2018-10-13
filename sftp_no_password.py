#!/usr/bin/env python3

import paramiko

privatekeyfile = "/Users/damien/.ssh/id_rsa"
host = "172.30.30.5"
port = 22
username = "damien"

mykey = paramiko.RSAKey.from_private_key_file(privatekeyfile)
print(type(mykey))

transport = paramiko.Transport((host, port))
transport.connect("damien", pkey=mykey)

sftp = paramiko.SFTPClient.from_transport(transport)
