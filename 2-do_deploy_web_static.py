#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""

from datetime import datetime
from fabric.api import env, local, put, run, sudo
from fabric.context_managers import settings
import os

# IP address of web-01 and web-02
env.hosts = ["54.172.227.90", "100.25.192.125"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"  # Update this with the correct path to your SSH key if necessary


def do_pack():
    """
    Return the archive path if archive has generated correctly.
    """
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archived_f_path = "versions/web_static_{}.tgz".format(date)
    t_gzip_archive = local("tar -cvzf {} web_static".format(archived_f_path))

    if t_gzip_archive.succeeded:
        return archived_f_path
    else:
        return None


def do_deploy(archive_path):
    """
    Distribute archive to web servers.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Extract the filename and file basename
        filename = archive_path.split('/')[-1]
        basename = filename.split('.')[0]

        # Define remote paths
        remote_tmp_path = f"/tmp/{filename}"
        remote_release_path = f"/data/web_static/releases/{basename}"

        # Upload the archive to the /tmp/ directory on the web server
        put(archive_path, remote_tmp_path)

        # Create the release directory on the web server
        sudo(f"mkdir -p {remote_release_path}")

        # Uncompress the archive to the release directory
        sudo(f"tar -xzf {remote_tmp_path} -C {remote_release_path}")

        # Delete the archive from the /tmp/ directory
        sudo(f"rm {remote_tmp_path}")

        # Move files from web_static to the release directory
        sudo(f"mv {remote_release_path}/web_static/* {remote_release_path}")

        # Delete the now-empty web_static directory
        sudo(f"rm -rf {remote_release_path}/web_static")

        # Delete the current symbolic link
        sudo("rm -rf /data/web_static/current")

        # Create a new symbolic link to the new release
        sudo(f"ln -s {remote_release_path} /data/web_static/current")

        print("New version deployed!")
        return True
    except Exception as e:
        print(f"Deployment failed: {e}")
        return False

