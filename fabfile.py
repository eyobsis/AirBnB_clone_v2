from fabric import task
from datetime import datetime

@task
def do_pack(c):
    try:
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        c.local("mkdir -p versions")
        filename = f"versions/web_static_{now}.tgz"
        c.local("tar -cvzf {filename} web_static".format(filename=filename))
        return filename
    except Exception as e:
        return None

