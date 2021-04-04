#! /bin/bash
# Azura : A cards complement build for manage package from the NCR( Nutyx Community Repository ).
# It's devel by Delta an old member of NuTyX devel team
 

function compile () {
        echo -e "Avant de poursuivre, vérifiez si votre pkgfile appelé PKGBUILD dans est seul dans un répertoire, et si le chemin vers le répertoire commence bien par : usr/ports/perso/"
        read -r -p "Si tout est bon, on vous laisse poursuivre ? O/N" reponse
        case ${reponse} in
           [oO][uU][iI]|[oO])
              echo "OK"
              read -p "Comment s'appelle votre paquet" name
              echo $name
              read -p "Donnez-nous le chemin vers le répertoire de votre pkgfile" fichier
              echo $fichier 
              cd $fichier
              pkgmk -d 
              pkgadd $name
              if [[ $? = 1 ]];then
                        cards install cards.devel
                    
              fi
              pkgmk -d 
              pkgadd $name1*
              if [[ $? = 0 ]];then
                      echo "Done"
              fi
              ;;
              esac

}



# Function main
function main () {
# Si l'user tape compile, lance la commande compile
        if [[ "$1" = "compile" ]];then
                compile
                        
        fi
}
# Le main @$ après la fermeture de la fonction sinon elle ne s'arrete pas
main "$@"

# End of Azura code.
# Thanks to all the contributors
