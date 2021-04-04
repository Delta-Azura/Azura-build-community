#!/usr/bin/env python3

# This program is devel by DELTA

import os
import time
import cowsay

def main():
  print("Hello world")
  os.system("sudo cards install cards.devel")
  os.system("sudo cards sync && sudo cards diff")
  cowsay.cow("Avant de poursuivre veuillez vérifier que votre pkgfile se trouve bien dans l'emplacement prévu à cet effet")
  print("Nous vous laissons vérifier que les conditions sont remplis")
  time.sleep(10.0)
  name = input("Donnez nous le nom de votre paquet")
  local =input("Donnez nous le chemin vers votre pkgfile")
  os.system("cd " + local)
  os.system("pkgmk -d")
  os.system("sudo pkgadd " + name)
  print("Done")
  print("Thanks to use azura, if you found a bug, please report it to us")
  
if __name__ == "__main__":
    main()
    
# End of azura code 
