#!/usr/bin/python3
from fabric.api import *
from os.path import exists

env.hosts = ['54.236.44.217']

def command():
    run('mkdir yousssef')

execute(command)
