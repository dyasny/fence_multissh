#!/bin/env python

import yaml
import paramiko


def load_config:
    with open('config.yaml','r') as f:
        conf = yaml.load(f)
    return conf

def update_config(location, repotype):
    #TODO: git clone/pull configs, download from http, etc
    pass

def validate_config:
    #TODO: verify no similar IPs exist in config.yaml and other syntax
    pass


def gather_host_details(data, conf):    
# data can be any input, need to see whether it's hostname or ip, 
#and if so, return the full list of IPs and hostnames from config
    hostnames = []
    ips = []
    key = ''
    rootpass = ''
    for h in conf:
        if data in h['host']['hostname'] or data in h['host']['ip']:
            hostnames = h['host']['hostname'].split()
            ips = h['host']['ip'].split()
            key = h['host']['key']
            rootpass = h['host']['rootpass']
            sshport = h['host']['sshport']
            
    return hostnames, ips, key, rootpass
    
def fence_test(host, port):
    pass


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('example.com', port=22, username='root', password='password')
stdin, stdout, stderr = ssh.exec_command('cat /etc/redhat-release')
print stdout.read()

