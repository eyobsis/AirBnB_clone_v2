#!/usr/bin/python3
# A Fabfile to generates a .tgz archive from the contents of web_static.
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """To  Create a tar gzipped archive of the directory web_static."""
    js = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(js.year,
                                                         js.month,
                                                         js.day,
                                                         js.hour,
                                                         js.minute,
                                                         js.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
