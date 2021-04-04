#!/usr/bin/env python3

# This program is devel by DELTA

import os
import time

def main():
  print("Hello world")
  os.system("sudo cards install cards.devel")
  os.system("sudo cards sync && sudo cards diff")
  print("Avant de poursuivre veuillez vérifier que votre pkgfile se trouve bien dans l'emplacement prévu à cet effet")
  print("Nous vous laissons vérifier que les conditions sont remplis")
  time.sleep(10.0)
  name=input("donnez nous le paquet de votre paquet : ")
  os.chdir("/usr/ports/perso/" + name)
  os.system("sudo pkgmk -d")
  os.system("sudo pkgadd " + name + "1*")
  print("Done")
  print("Thanks to use azura, if you found a bug, please report it to us")
  
if __name__ == "__main__":
    main()
    
# End of azura code 
