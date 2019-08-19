#!/usr/bin/python3
"""Write a Fabric script (based on the file 2-do_deploy_web_static.py) that
   creates and distributes an archive to your web servers, using the
   function deploy"""

from fabric.operations import local
from datetime import datetime
import os
from fabric.api import *


env.hosts = ['35.229.72.201', '35.237.176.253']


def do_pack():
    """Compress before sending"""
    local("mkdir -p versions")
    name = "versions/web_static_{}.tgz".format(datetime.now().strftime
                                               ("%Y%m%d%H%M%S"))
    l = local("tar -cvzf {} web_static".format(name))
    if l.failed:
        return None
    return name


def do_deploy(archive_path):
    """ Deploy archive!"""
    if not os.path.exists(archive_path):
        return False
    a_ver = archive_path.split("/")[1]
    a_file = a_ver.split(".")[0]
    exe = put(archive_path, "/tmp/{}".format(a_ver))
    if exe.failed:
        return False
    exe = run("mkdir -p /data/web_static/releases/{}".format(a_file))
    if exe.failed:
        return False
    exe = run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
              .format(a_ver, a_file))
    if exe.failed:
        return False
    exe = run("rm /tmp/{}".format(a_ver))
    if exe.failed:
        return False
    exe = run("mv /data/web_static/releases/{}/web_static/*\
              /data/web_static/releases/{}/".format(a_file, a_file))
    if exe.failed:
        return False
    exe = run("rm -rf /data/web_static/releases/{}/web_static".format(a_file))
    if exe.failed:
        return False
    exe = run("rm -rf /data/web_static/current")
    if exe.failed:
        return False
    exe = run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
              .format(a_file))
    if exe.failed:
        return False
    print('New version deployed!')
    return True


def deploy():
    """ Full deployment"""
    path = do_pack()
    if path is None:
        return False
    a_path = do_deploy(path)
    return a_path
