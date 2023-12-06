#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives
"""
from fabric.api import env, run, local
from datetime import datetime
import os

env.hosts = ['34.229.66.177', '34.204.101.218']  # Add your server IPs here
env.user = 'ubuntu'  # Replace with your username
env.key_filename = '/root/.ssh/school/id_rsa '  # Replace with your SSH private key path


def do_clean(number=0):
    number = int(number)
    if number < 2:
        number = 1

    archives = sorted(os.listdir('versions'))
    archives_to_keep = archives[-number:]

    local("cd versions; rm $(ls -1 | grep -vE '{}')".format('|'.join(archives_to_keep)))

    releases = run("ls -1 /data/web_static/releases").split()
    releases_to_delete = sorted(releases)[:-number]

    if len(releases_to_delete) > 0:
        run("cd /data/web_static/releases; rm -rf {}".format(' '.join(releases_to_delete)))

