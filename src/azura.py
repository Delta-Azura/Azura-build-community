#!/usr/bin/env python3

# Les imports 
import os
import sys  
import parser 
yes = "yes"
from lxml import etree

# Fonction d'aide : 
def help():
    print("Hi")
    print("Pour mettre à jour votre os : sudo azura update ")
    print("Pour installer un paquet : sudo azura install ")
    print("Pour désistaller des paquets : sudo azura remove ")
    print("Pour compile un pkgfile : sudo azura compile ")
def explore ():
    print("Peut être que vous souhaitez apprendre de nouvelle chose à propos de azura, pour cela, nous vous conseillons de vous rendre sur le github de azura build community où vous trouverez un moyen de nous contacter pour contribuer ainsi que le résumé de l'histoire de azura")


# Fonction install, permet d'installer un paquet, comming soon
def install():
    print("Nous syncronisons les dépôts de votre os ... please wait ") 
    os.system("sudo cards sync")
    package =input("Donnez nous du package à installer : ")
    flatpak =input("Ces paquets sont-ils des flatpaks ? [yes ou no] : ")
    if flatpak == yes :
        os.system("flatpak update")
        os.system("flatpak install " + package )
    if flatpak != yes :
        os.system("sudo cards install " + package )
    print("Nous procédons à un nettoyage des archives binaires")
    os.system("sudo cards purge")
    print("Done")
    exit()

def update():
    print("Nous mettons votre système à jour")
    os.system("sudo cards sync")
    os.system("sudo cards upgrade")
    ask =input("Des mises à jour de flatpak sont peut-être dispo, voulez-vous les effectuer ? [yes ou no] : ")
    if ask == yes :
        os.system("flatpak update")
    if ask != yes:
        print("Done")
        exit()

    print("Nous nettoyons les archives binaires")
    os.system("sudo cards purge")
    print("Done")

# Comming soon
def remove ():
    os.chdir("/var/azura/lib/pkg/DB")


def compile():
    principal_vrai=input("Indiquer nous l'URL vers le code source du paquet à compiler ? : ")
    os.system("wget -c " +principal_vrai )
    instructions-de-build=input("Donnez nous les instructions de build : ")

    exit()


#  Les arguments
if sys.argv[1] == "update":
    update()

if sys.argv[1] == "compile":
    compile()

if sys.argv[1] == "install":
    install()

if sys.argv[1] == "remove":
    remove()

if sys.argv[1] == "help":
    help()

if sys.argv[1] == "explore":
    explore()


