#! /bin/bash

 function compile () {
        echo -e "Avant de poursuivre, vérifiez si votre pkgfile appelé PKGBUILD dans est seul dans un répertoire, et si le chemin vers le répertoire commence bien par : usr/ports/perso/"
        read -r -p "Si tout est bon, on vous laisse poursuivre ? O/N : " reponse
        case ${reponse} in
           [oO][uU][iI]|[oO])
              echo "OK"
              echo $1
              cd /usr/ports/perso/$name
              pkgmk -d 
              pkgadd $name
              if [[ $? = 1 ]];then
                      cards install cards.devel
                      pkgmk -d
                      pkgadd ${1}1*
              fi
              if [[ $? = 1 ]];then
                      echo "votre pkgfile ne porte pas le nom de pkgfile ou bien il ne se trouve pas dans le bon répertoire "
                      exit
              fi
              ;;
              esac

}

function install () {
        if [[ $2 ]];then
              sudo cards upgrade
              sudo cards install $2
              read -p "Souaitez vous installer des flatpaks, si oui veuillez spécifié lesquels ? : " ask_1
              if [[ $ask_1 = non ]];then
                    echo "ok"
              else 
                    flatpak update && flatpak install $ask_1
                    sudo cards purge 
              fi
}
              
# Function main
function main () {
# Si l'user tape compile, lance la commande compile
        if [[ $1 ]];then
                compile
}
# Le main @$ après la fermeture de la fonction sinon elle ne s'arrete pas
main "$@"

# End of Azura code.
# Thanks to all the contributors
