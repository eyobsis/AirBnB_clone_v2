#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives
"""
from fabric.api import env, run, local, lcd, cd
import os

env.hosts = ['34.229.66.177', '34.204.101.218']
env.user = 'ubuntu'
env.key_filename = '/root/.ssh/school/id_rsa'


def do_clean(number=0):
    number = max(1, int(number))

    with lcd('versions'):
        archives = sorted(os.listdir('.'))
        archives_to_keep = archives[-number:]
        arc = archives_to_keep
        local("rm -f $(ls -1 | grep -vE '{}')".format('|'.join(arc)))

    with cd('/data/web_static/releases'):
        releases = run("ls -1").split()
        releases_to_delete = sorted(releases)[:-number]

        if releases_to_delete:
            run("rm -rf {}".format(' '.join(releases_to_delete)))
