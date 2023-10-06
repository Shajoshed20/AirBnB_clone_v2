#!/usr/bin/python3
# Fabfile to create and distribute an archive to a web server.
from fabric.api import env
from fabric.api import local
from fabric.api import put
from fabric.api import run
import os.path
from datetime import datetime


env.hosts = ["52.91.135.249", "52.23.244.198"]


def do_pack():
    """Pack the project into an archive."""
    dt = datetime.utcnow()
    f_name = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                           dt.month,
                                                           dt.day,
                                                           dt.hour,
                                                           dt.minute,
                                                           dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(f_name)).failed is True:
        return None
    return f_name


def do_deploy(archive_path):
    """Deploy the packed archive to a web server."""

    if os.path.isfile(archive_path) is False:
        return False
    file_path = archive_path.split("/")[-1]
    splits = file_path.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file_path)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(splits)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(splits)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file_path, splits)).failed is True:
        return False
    if run("rm /tmp/{}".format(file_path)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/"
           .format(splits, splits)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(splits)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(splits)).failed is True:
        return False
    return True


def deploy():
    """Create and distribute an archive to a web server."""
    f_name = do_pack()
    if f_name is None:
        return False
    return do_deploy(f_name)
