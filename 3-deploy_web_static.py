#!/usr/bin/python3
"""This module soport the deploy function"""
from datetime import datetime
from fabric.api import local, run, put, env
import os

env.hosts = ['35.237.104.173', '34.138.139.5']


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
        run('mkdir -p ' + dir + '/')
        run('tar -xzf /tmp/' + filename + ' -C ' + dir + '/')
        # delete the archive from the web server.
        run('rm /tmp/' + filename)
        # This apear in the intranet sample.
        run('mv /data/web_static/releases/' + file + '/web_static/*\
             /data/web_static/releases/' + file + '/')
        # This appear in the intranet too.
        run('rm -rf /data/web_static/releases/' + file + '/web_static')
        # delete the current symbolic link.
        run('rm -rf /data/web_static/current')
        # Create a new symbolic link.
        run('ln -s ' + dir + '/ /data/web_static/current')
        print('New version deployed!')
        return True
    except Exception:
        return False


def deploy():
    """This function call the do_pack funct."""
    path = do_pack()
    if not path:
        return False
    return do_deploy(path)
