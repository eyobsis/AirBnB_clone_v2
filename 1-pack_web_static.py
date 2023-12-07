#!/usr/bin/python3
"""
Creates a compressed archive of the web_static folder
"""

from fabric.api import local
from datetime import datetime

def do_pack():
    try:
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        filename = "versions/web_static_{}.tgz".format(now)
        local("tar -cvzf {} web_static".format(filename))
        return filename
    except Exception as e:
        return None

