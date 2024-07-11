#!/usr/bin/python3
"""A Fabric script that distributes an archive to web servers."""

from fabric.api import env, put, run
from os.path import exists

# Specify the IP addresses of the web servers
env.hosts = ['54.172.227.90', '100.25.192.125']


def do_deploy(archive_path):
    """Distributes an archive to web servers.
    
    Args:
        archive_path (str): The path to the archive file.
    
    Returns:
        bool: True if all operations were successful, False otherwise.
    """
    if not exists(archive_path):
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
        run(f"mkdir -p {remote_release_path}")

        # Uncompress the archive to the release directory
        run(f"tar -xzf {remote_tmp_path} -C {remote_release_path}")

        # Delete the archive from the /tmp/ directory
        run(f"rm {remote_tmp_path}")

        # Move files from web_static to the release directory
        run(f"mv {remote_release_path}/web_static/* {remote_release_path}")

        # Delete the now-empty web_static directory
        run(f"rm -rf {remote_release_path}/web_static")

        # Delete the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link to the new release
        run(f"ln -s {remote_release_path} /data/web_static/current")

        return True
    except Exception as e:
        print(f"Deployment failed: {e}")
        return False
