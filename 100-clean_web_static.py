#!/usr/bin/python3
# Fabfile to delete out-of-date archives.
import os
from fabric.api import env
from fabric.api import local
from fabric.apr import *

env.hosts = ["52.91.135.249", "52.23.244.198"]


def do_clean(number=0):
    """Clean up old files."""
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]
