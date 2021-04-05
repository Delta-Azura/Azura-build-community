#!/usr/bin/env python3

import os
import sys  

compile = sys.argv[1]
install = sys.argv[1]
purge = sys.argv[1]

def compile():
  print("Hello world")
  os.system("sudo cards install cards.devel && sudo cards sync && sudo cards upgrade")
  name =input("Donnez nous le nom de votre paquet : ")
  try:
      os.chdir("/usr/ports/perso/" + name)
  except:
      print("Veuillez vérifier que votre PKGFILE se situe dans un réperoire commençant par : /usr/ports/perso/")
      exit()

  os.system("sudo pkgmk -d")
  os.system("sudo pkgadd " +name+ "1*")
  print("Done")
  print("If you have found a bug, please report it")


def install():
    print("Nous syncronisons les dépôts de votre os ... please wait ") 
    os.system("sudo cards sync")
    package =input("Donnez nous du package à installer : ")
    os.system("sudo cards install " + package)
    print("Nous procédons à un nettoyage des archives binaires")
    os.system("sudo cards purge")
    print("Done")
    exit()



# Les arguments
if sys.argv[1] == "compile":
    compile()
if sys.argv[1] == "install":
    install()
