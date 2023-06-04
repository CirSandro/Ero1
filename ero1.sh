#!/bin/sh

if [ "$#" -eq 0 ] #apres rajouter quel vehicule, le nombre, solution rapide ou prix
then
    echo 'WARNING : ici vous avez lancé le drone sur tout Montréal, celui-ci dure plus de 48h, pour lancer la même chose mais avec un parcour de drone sur un quartier (ex:Outremont) faites:\n - Ctrl+C\n - ./ero1.sh -drone:Outremont -deneigeuse'
    python3 src/drone/montreal.py
    echo 'Résultat du Drone = Il faut déneiger 5 quartiers :\n — Outremont,\n — Verdun,\n — Saint-Léonard,\n — Rivière-des-prairies-pointe-aux-trembles,\n — Le Plateau-Mont-Royal.'
    #fair un fichier qui fait les 5 et afficher sur 1grqphe de Montreql
    #sinon le temps :
    python3 src/deneigeuse/outremont_deneige.py
    python3 src/deneigeuse/verdun_deneige.py
    python3 src/deneigeuse/saint_leonard_deneige.py
    python3 src/deneigeuse/riviere_deneige.py
    python3 src/deneigeuse/plateau_deneige.py
elif [ "$1" = "-drone" ]
then
    echo 'WARNING : ici vous avez lancé le drone sur tout Montréal, celui-ci dure plus de 48h, pour lancer la même chose mais avec un parcour de drone sur un quartier (ex:Outremont) faites:\n - Ctrl+C\n - ./ero1.sh -drone:Outremont $2'
    python3 src/drone/montreal.py
    echo 'Résultat du Drone = Il faut déneiger 5 quartiers :\n — Outremont,\n — Verdun,\n — Saint-Léonard,\n — Rivière-des-prairies-pointe-aux-trembles,\n — Le Plateau-Mont-Royal.'
    if [ "$2" = "-deneigeuse" ]
    then
        #fair un fichier qui fait les 5 et afficher sur 1grqphe de Montreql
        #sinon le temps :
        python3 src/deneigeuse/outremont_deneige.py
        python3 src/deneigeuse/verdun_deneige.py
        python3 src/deneigeuse/saint_leonard_deneige.py
        python3 src/deneigeuse/riviere_deneige.py
        python3 src/deneigeuse/plateau_deneige.py
    elif [ "$2" = "-deneigeuse:Outremont" ] #fair ensuite pour chaque autre ficher
    then
        python3 src/deneigeuse/outremont_deneige.py
    elif [ "$2" = "-deneigeuse:Verdun" ] #fair ensuite pour chaque autre ficher
    then
        python3 src/deneigeuse/verdun_deneige.py
    elif [ "$2" = "-deneigeuse:Saint-Léonard" ] #fair ensuite pour chaque autre ficher
    then
        python3 src/deneigeuse/saint_leonard_deneige.py
    elif [ "$2" = "-deneigeuse:Rivière-des-prairies-pointe-aux-trembles" ] || [ "$2" = "-deneigeuse:Rivière" ] #fair ensuite pour chaque autre ficher
    then
        python3 src/deneigeuse/riviere_deneige.py
    elif [ "$2" = "-deneigeuse:Le-Plateau-Mont-Royal" ] || [ "$2" = "-deneigeuse:Plateau-Mont-Royal" ] || [ "$2" = "-deneigeuse:Le_Plateau-Mont-Royal" ]#fair ensuite pour chaque autre ficher
    then
        python3 src/deneigeuse/plateau_deneige.py
    fi
elif [ "$1" = "-drone:Outremont" ]  #fair ensuite pour chaque autre ficher
then
    python3 src/drone/outremont.py
    echo 'Résultat du Drone = Il faut déneiger Outremont.'
    if [ "$2" = "-deneigeuse" ]
    then
        #que outremont car seul verifier
        python3 src/deneigeuse/outremont_deneige.py
    elif [ "$2" = "-deneigeuse:Outremont" ]
    then
        python3 src/deneigeuse/outremont_deneige.py
    fi
elif [ "$1" = "-drone:Verdun" ]
then
    python3 src/drone/verdun_drone.py
    echo 'Résultat du Drone = Il faut déneiger Verdun.'
    if [ "$2" = "-deneigeuse" ]
    then
        python3 src/deneigeuse/verdun_deneige.py
    elif [ "$2" = "-deneigeuse:Verdun" ]
    then
        python3 src/deneigeuse/verdun_deneige.py
    fi
elif [ "$1" = "-drone:Saint-Léonard" ]
then
    python3 src/drone/saint_leonard_drone.py
    echo 'Résultat du Drone = Il faut déneiger Saint-Léonard.'
    if [ "$2" = "-deneigeuse" ]
    then
        python3 src/deneigeuse/saint_leonard_deneige.py
    elif [ "$2" = "-deneigeuse:Saint-Léonard" ]
    then
        python3 src/deneigeuse/saint_leonard_deneige.py
    fi
elif [ "$1" = "-drone:Rivière-des-prairies-pointe-aux-trembles" ] || [ "$1" = "-drone:Rivière" ]
then
    python3 src/drone/riviere_drone.py
    echo 'Résultat du Drone = Il faut déneiger Rivière-des-prairies-pointe-aux-trembles.'
    if [ "$2" = "-deneigeuse" ]
    then
        python3 src/deneigeuse/riviere_deneige.py
    elif [ "$2" = "-deneigeuse:Rivière-des-prairies-pointe-aux-trembles" ] || [ "$2" = "-deneigeuse:Rivière" ]
    then
        python3 src/deneigeuse/riviere_deneige.py
    fi
elif [ "$1" = "-drone:Le-Plateau-Mont-Royal" ] || [ "$1" = "-drone:Plateau-Mont-Royal" ] || [ "$1" = "-drone:Le_Plateau-Mont-Royal" ]
then
    python3 src/drone/plateau_drone.py
    echo 'Résultat du Drone = Il faut déneiger Le Plateau-Mont-Royal.'
    if [ "$2" = "-deneigeuse" ]
    then
        python3 src/deneigeuse/plateau_deneige.py
    elif [ "$2" = "-deneigeuse:Le-Plateau-Mont-Royal" ] || [ "$2" = "-deneigeuse:Plateau-Mont-Royal" ] || [ "$2" = "-deneigeuse:Le_Plateau-Mont-Royal" ]
    then
        python3 src/deneigeuse/plateau_deneige.py
    fi
elif [ "$1" = "-deneigeuse" ]
then
    #fair un fichier qui fait les 5 et afficher sur 1grqphe de Montreql
    #sinon le temps :
    python3 src/deneigeuse/outremont_deneige.py
    python3 src/deneigeuse/verdun_deneige.py
    python3 src/deneigeuse/saint_leonard_deneige.py
    python3 src/deneigeuse/riviere_deneige.py
    python3 src/deneigeuse/plateau_deneige.py
elif [ "$1" = "-deneigeuse:Outremont" ] #fair ensuite pour chaque autre ficher
then
    python3 src/deneigeuse/outremont_deneige.py
elif [ "$1" = "-deneigeuse:Verdun" ] #fair ensuite pour chaque autre ficher
then
    python3 src/deneigeuse/verdun_deneige.py
elif [ "$1" = "-deneigeuse:Saint-Léonard" ] #fair ensuite pour chaque autre ficher
then
    python3 src/deneigeuse/saint_leonard_deneige.py
elif [ "$1" = "-deneigeuse:Rivière-des-prairies-pointe-aux-trembles" ] || [ "$2" = "-deneigeuse:Rivière" ]
then
    python3 src/deneigeuse/riviere_deneige.py
elif [ "$1" = "-deneigeuse:Le-Plateau-Mont-Royal" ] || [ "$1" = "-deneigeuse:Plateau-Mont-Royal" ] || [ "$1" = "-deneigeuse:Le_Plateau-Mont-Royal" ]
then
    python3 src/deneigeuse/plateau_deneige.py
else
    echo 'Pour lancer le code (voir README.txt) : ./ero1.sh [-drone] || [-drone:${nom_quartier}] [-deneigeuse] || [-deneigeuse:${nom_quartier}]'
fi