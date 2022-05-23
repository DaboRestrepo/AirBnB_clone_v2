#!/usr/bin/python3
"""Compress a archive before sending."""
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """Generate a .tgz file from the web static contents."""
    if not os.path.exists('versions'):
        local('mkdir versions')
    try:
        time = datetime.now().strftime('%Y%m%d%H%M%S')
        file_name = 'versions/web_static_' + time + '.tgz'
        local('tar -cvzf ' + file_name + ' web_static')
        return file_name
    except Exception:
        return None
