#!/usr/bin/python3
""" Fabric script (based on the file 1-pack_web_static.py) that distributes an
    archive to your web servers, using the function do_deploy"""

from fabric.operations import local
from datetime import datetime


def do_pack(archive_path):
    """Deploy archive"""
    try:
        local("mkdir -p versions")
        l = local("tar -cvzf versions/web_static_{}.tgz web_static/"
                  .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
        return l
    except Exception:
        return None
