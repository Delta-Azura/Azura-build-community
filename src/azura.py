#!/usr/bin/env python3

import os
import sys  

# Fonction principale, build le pkgfile
def compile():
  print("Hello world")
  os.system("sudo cards install cards.devel && sudo cards sync && sudo cards upgrade")
  name =input("Donnez nous le nom de votre paquet : ")
  # Vérification de la présence du chemin
  try:
      os.chdir("/usr/ports/perso/" + name)
  except:
      print("Veuillez vérifier que votre PKGFILE se situe dans un réperoire commençant par : /usr/ports/perso/")
      exit()

  os.system("sudo pkgmk -d")
  os.system("sudo pkgadd " +name+ "1*")
  print("Done")
  print("If you have found a bug, please report it")

# Fonction install, permet d'installer un paquet, comming soon
def install():
    print("Nous syncronisons les dépôts de votre os ... please wait ") 
    os.system("sudo cards sync")
    package =input("Donnez nous du package à installer : ")
    os.system("sudo cards install " + package)
    print("Nous procédons à un nettoyage des archives binaires")
    os.system("sudo cards purge")
    print("Done")
    exit()

def update():
    print("Nous mettons votre système à jour")
    os.system("sudo cards sync")
    print("Nous nettoyons les archives binaires")
    os.system("sudo cards upgrade")
    print("Done")

# Comming soon
def remove ():
    rem =input("Quel paquet voulez vous supprimer : ")
    os.system("sudo cards remove " + rem )
    os.system("sudo cards purge")

#  Les arguments
if sys.argv[1] == "update":
    update()

if sys.argv[1] == "compile":
    compile()

if sys.argv[1] == "install":
    install()

if sys.argv[1] == "remove":
    remove()


# Les arguments
if sys.argv[1] == "compile":
    compile()
if sys.argv[1] == "install":
    install()
