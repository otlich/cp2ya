#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, glob, sys, time, logging, ConfigParser
from datetime import datetime

#https://github.com/TyVik/YaDiskClient
try:
    from YaDiskClient.YaDiskClient import YaDisk
except:
    print """Not found module YaDiskClient.\r\npip install YaDiskClient or easy_install YaDiskClient or download from https://github.com/TyVik/YaDiskClient """
    sys.exit()

def getUserInfo(param):
    conf = ConfigParser.RawConfigParser()
    conf.read(os.path.expanduser('~/.cp2ya'))
    try:
        result = conf.get('auth',param)
    except:
        print "Can't' read config %s" %(os.path.expanduser('~/.cp2ya'))
        sys.exit()
    return result


def auth():
    login = getUserInfo('login')
    password = getUserInfo('password')
    disk = YaDisk(login, password)
    return disk


def copy_dir(ffolder, to):
    try:
        listfir = os.listdir(ffolder)
    except OSError:
        print 'Pass file or folder %s' %ffolder
        return True
    
    for f in os.listdir(ffolder):
        if os.path.isfile(os.path.join(ffolder,f)):
            upload(os.path.join(ffolder,f),os.path.join(to,f))
        else:
            copy_dir(os.path.join(ffolder,f), os.path.join(to,f))
    return True

def mkdir(path):
    try:
        auth().mkdir(path)
    except:
        mkdir(os.path.split(path)[0])
    print "Create dir on YaDisk %s" %path
    return True

def upload(filepath,to):
    print 'Copy %s to %s' %(filepath,to)
    try:
        auth().upload(filepath, to)
    except Exception as e:
        if str(e).split('.')[0] == "409":
            path, filename = os.path.split(to)
            mkdir(path)
            upload(filepath,to)
        else:
            print e
            
if __name__ == '__main__':
    arg = sys.argv

    try:
        from_file  = arg[1]
    except:
        print "Error. Need srcFile. Usage: cpya srcFile dstFile"
        sys.exit()
    path, filename = os.path.split(from_file)

    try:
        to_file = arg[2]
    except:
        to_file = '/%s' %filename

    if os.path.exists(from_file):
        if os.path.isfile(from_file):
            upload(from_file, to_file)
        elif os.path.isdir(from_file):
            copy_dir(from_file, to_file)
    else:
        print 'File or Folder not found'
