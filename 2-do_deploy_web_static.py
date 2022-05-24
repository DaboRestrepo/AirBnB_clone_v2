#!/usr/bin/python3
"""This module soport the do_deploy function."""
import os
from fabric.api import put, run, env

env.hosts = ['35.237.104.173', '34.138.139.5']


def do_deploy(archive_path):
    """Distribute an archive to the web servers."""
    if not os.path.exists(archive_path):  # archive_path: blabla/blabla
        return False
    try:
        # Split the filename to have only the webserver part.
        filename = archive_path.split('/')
        filename = filename[-1]  # web_static_20220523164957.tgz
        file = filename.split('.')
        file = file[0]  # without ext.
        dir = '/data/web_static/releases/' + file  # Folder name
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/')
        # Uncompress the file.
        run('mkdir -p ' + dir)
        run('tar -xzf /tmp/' + filename + ' -C ' + dir)
        # delete the archive from the web server.
        run('rm -rf /tmp/' + filename)
        # delete the current symbolic link.
        run('rm -rf /data/web_static/current')
        # Create a new symbolic link.
        run('ln -s ' + dir + ' /data/web_static/current')
        print('New version deployed!')
        return True
    except Exception:
        return False
