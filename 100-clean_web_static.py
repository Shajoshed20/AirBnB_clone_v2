#!/usr/bin/python3
# Fabfile to delete out-of-date archives.
import os
from fabric.apr import *

env.hosts = ["52.91.135.249", "52.23.244.198"]


def do_clean(number=0):
    """Clean up old files."""
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
