#!/usr/bin/env python3

import os
import os.path

folder_path = "usr/ports/perso/"

def main():
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

if __name__ == "__main__":
  main()

