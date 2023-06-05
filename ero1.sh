#!/bin/sh

if [ "$#" -eq 0 ] #apres rajouter quel vehicule, le nombre, solution rapide ou prix
then
    echo 'WARNING : ici vous avez lancé le drone sur tout Montréal, celui-ci dure plus de 48h, pour lancer la même chose mais avec un parcour de drone sur un quartier (ex:Outremont) faites:\n - Ctrl+C\n - ./ero1.sh -drone:Outremont -deneigeuse'
    python3 src/drone/montreal.py
    echo 'Résultat du Drone = Il faut déneiger 5 quartiers :\n — Outremont,\n — Verdun,\n — Saint-Léonard,\n — Rivière-des-prairies-pointe-aux-trembles,\n — Le Plateau-Mont-Royal.'
    #fair un fichier qui fait les 5 et afficher sur 1grqphe de Montreql
    #sinon le temps :
    python3 src/deneigeuse/machine_1/outremont_deneige.py
    python3 src/deneigeuse/machine_1/verdun_deneige.py
    python3 src/deneigeuse/machine_1/saint_leonard_deneige.py
    python3 src/deneigeuse/machine_1/riviere_deneige.py
    python3 src/deneigeuse/machine_1/plateau_deneige.py
elif [ "$1" = "-drone" ]
then
    echo 'WARNING : ici vous avez lancé le drone sur tout Montréal, celui-ci dure plus de 48h, pour lancer la même chose mais avec un parcour de drone sur un quartier (ex:Outremont) faites:\n - Ctrl+C\n - ./ero1.sh -drone:Outremont $2'
    python3 src/drone/montreal.py
    echo 'Résultat du Drone = Il faut déneiger 5 quartiers :\n — Outremont,\n — Verdun,\n — Saint-Léonard,\n — Rivière-des-prairies-pointe-aux-trembles,\n — Le Plateau-Mont-Royal.'
    if [ "$2" = "-deneigeuse1" ]
    then
        #fair un fichier qui fait les 5 et afficher sur 1grqphe de Montreql
        #sinon le temps :
        python3 src/deneigeuse/machine_1/outremont_deneige.py
        python3 src/deneigeuse/machine_1/verdun_deneige.py
        python3 src/deneigeuse/machine_1/saint_leonard_deneige.py
        python3 src/deneigeuse/machine_1/riviere_deneige.py
        python3 src/deneigeuse/machine_1/plateau_deneige.py
    elif [ "$2" = "-deneigeuse2" ]
    then
        #fair un fichier qui fait les 5 et afficher sur 1grqphe de Montreql
        #sinon le temps :
        python3 src/deneigeuse/machine_2/outremont_deneige.py
        python3 src/deneigeuse/machine_2/verdun_deneige.py
        python3 src/deneigeuse/machine_2/saint_leonard_deneige.py
        python3 src/deneigeuse/machine_2/riviere_deneige.py
        python3 src/deneigeuse/machine_2/plateau_deneige.py
    elif [ "$2" = "-deneigeuse1:Outremont" ] #fair ensuite pour chaque autre ficher
    then
        python3 src/deneigeuse/machine_1/outremont_deneige.py
    elif [ "$2" = "-deneigeuse1:Verdun" ] #fair ensuite pour chaque autre ficher
    then
        python3 src/deneigeuse/machine_1/verdun_deneige.py
    elif [ "$2" = "-deneigeuse1:Saint-Léonard" ] #fair ensuite pour chaque autre ficher
    then
        python3 src/deneigeuse/machine_1/saint_leonard_deneige.py
    elif [ "$2" = "-deneigeuse1:Rivière-des-prairies-pointe-aux-trembles" ] || [ "$2" = "-deneigeuse1:Rivière" ] #fair ensuite pour chaque autre ficher
    then
        python3 src/deneigeuse/machine_1/riviere_deneige.py
    elif [ "$2" = "-deneigeuse1:Le-Plateau-Mont-Royal" ] || [ "$2" = "-deneigeuse1:Plateau-Mont-Royal" ] || [ "$2" = "-deneigeuse1:Le_Plateau-Mont-Royal" ]#fair ensuite pour chaque autre ficher
    then
        python3 src/deneigeuse/machine_1/plateau_deneige.py
    elif [ "$2" = "-deneigeuse2:Outremont" ] #fair ensuite pour chaque autre ficher
    then
        python3 src/deneigeuse/machine_2/outremont_deneige.py
    elif [ "$2" = "-deneigeuse2:Verdun" ] #fair ensuite pour chaque autre ficher
    then
        python3 src/deneigeuse/machine_2/verdun_deneige.py
    elif [ "$2" = "-deneigeuse2:Saint-Léonard" ] #fair ensuite pour chaque autre ficher
    then
        python3 src/deneigeuse/machine_2/saint_leonard_deneige.py
    elif [ "$2" = "-deneigeuse2:Rivière-des-prairies-pointe-aux-trembles" ] || [ "$2" = "-deneigeuse2:Rivière" ] #fair ensuite pour chaque autre ficher
    then
        python3 src/deneigeuse/machine_2/riviere_deneige.py
    elif [ "$2" = "-deneigeuse2:Le-Plateau-Mont-Royal" ] || [ "$2" = "-deneigeuse2:Plateau-Mont-Royal" ] || [ "$2" = "-deneigeuse2:Le_Plateau-Mont-Royal" ]#fair ensuite pour chaque autre ficher
    then
        python3 src/deneigeuse/machine_2/plateau_deneige.py
    fi
elif [ "$1" = "-drone:Outremont" ]  #fair ensuite pour chaque autre ficher
then
    python3 src/drone/outremont.py
    echo 'Résultat du Drone = Il faut déneiger Outremont.'
    if [ "$2" = "-deneigeuse1" ]
    then
        #que outremont car seul verifier
        python3 src/deneigeuse/machine_1/outremont_deneige.py
    elif [ "$2" = "-deneigeuse1:Outremont" ]
    then
        python3 src/deneigeuse/machine_1/outremont_deneige.py
    elif [ "$2" = "-deneigeuse2" ]
    then
        #que outremont car seul verifier
        python3 src/deneigeuse/machine_2/outremont_deneige.py
    elif [ "$2" = "-deneigeuse2:Outremont" ]
    then
        python3 src/deneigeuse/machine_2/outremont_deneige.py
    fi
elif [ "$1" = "-drone:Verdun" ]
then
    python3 src/drone/verdun_drone.py
    echo 'Résultat du Drone = Il faut déneiger Verdun.'
    if [ "$2" = "-deneigeuse1" ]
    then
        python3 src/deneigeuse/machine_1/verdun_deneige.py
    elif [ "$2" = "-deneigeuse1:Verdun" ]
    then
        python3 src/deneigeuse/machine_1/verdun_deneige.py
    elif [ "$2" = "-deneigeuse2" ]
    then
        python3 src/deneigeuse/machine_2/verdun_deneige.py
    elif [ "$2" = "-deneigeuse2:Verdun" ]
    then
        python3 src/deneigeuse/machine_2/verdun_deneige.py
    fi
elif [ "$1" = "-drone:Saint-Léonard" ]
then
    python3 src/drone/saint_leonard_drone.py
    echo 'Résultat du Drone = Il faut déneiger Saint-Léonard.'
    if [ "$2" = "-deneigeuse1" ]
    then
        python3 src/deneigeuse/machine_1/saint_leonard_deneige.py
    elif [ "$2" = "-deneigeuse1:Saint-Léonard" ]
    then
        python3 src/deneigeuse/machine_1/saint_leonard_deneige.py
    elif [ "$2" = "-deneigeuse2" ]
    then
        python3 src/deneigeuse/machine_2/saint_leonard_deneige.py
    elif [ "$2" = "-deneigeuse2:Saint-Léonard" ]
    then
        python3 src/deneigeuse/machine_2/saint_leonard_deneige.py
    fi
elif [ "$1" = "-drone:Rivière-des-prairies-pointe-aux-trembles" ] || [ "$1" = "-drone:Rivière" ]
then
    python3 src/drone/riviere_drone.py
    echo 'Résultat du Drone = Il faut déneiger Rivière-des-prairies-pointe-aux-trembles.'
    if [ "$2" = "-deneigeuse1" ]
    then
        python3 src/deneigeuse/machine_1/riviere_deneige.py
    elif [ "$2" = "-deneigeuse1:Rivière-des-prairies-pointe-aux-trembles" ] || [ "$2" = "-deneigeuse1:Rivière" ]
    then
        python3 src/deneigeuse/machine_1/riviere_deneige.py
    elif [ "$2" = "-deneigeuse2" ]
    then
        python3 src/deneigeuse/machine_2/riviere_deneige.py
    elif [ "$2" = "-deneigeuse2:Rivière-des-prairies-pointe-aux-trembles" ] || [ "$2" = "-deneigeuse2:Rivière" ]
    then
        python3 src/deneigeuse/machine_2/riviere_deneige.py
    fi
elif [ "$1" = "-drone:Le-Plateau-Mont-Royal" ] || [ "$1" = "-drone:Plateau-Mont-Royal" ] || [ "$1" = "-drone:Le_Plateau-Mont-Royal" ]
then
    python3 src/drone/plateau_drone.py
    echo 'Résultat du Drone = Il faut déneiger Le Plateau-Mont-Royal.'
    if [ "$2" = "-deneigeuse1" ]
    then
        python3 src/deneigeuse/machine_1/plateau_deneige.py
    elif [ "$2" = "-deneigeuse1:Le-Plateau-Mont-Royal" ] || [ "$2" = "-deneigeuse1:Plateau-Mont-Royal" ] || [ "$2" = "-deneigeuse1:Le_Plateau-Mont-Royal" ]
    then
        python3 src/deneigeuse/machine_1/plateau_deneige.py
    elif [ "$2" = "-deneigeuse2" ]
    then
        python3 src/deneigeuse/machine_2/plateau_deneige.py
    elif [ "$2" = "-deneigeuse2:Le-Plateau-Mont-Royal" ] || [ "$2" = "-deneigeuse2:Plateau-Mont-Royal" ] || [ "$2" = "-deneigeuse2:Le_Plateau-Mont-Royal" ]
    then
        python3 src/deneigeuse/machine_2/plateau_deneige.py
    fi
elif [ "$1" = "-deneigeuse1" ]
then
    #fair un fichier qui fait les 5 et afficher sur 1grqphe de Montreql
    #sinon le temps :
    python3 src/deneigeuse/machine_1/outremont_deneige.py
    python3 src/deneigeuse/machine_1/verdun_deneige.py
    python3 src/deneigeuse/machine_1/saint_leonard_deneige.py
    python3 src/deneigeuse/machine_1/riviere_deneige.py
    python3 src/deneigeuse/machine_1/plateau_deneige.py
elif [ "$1" = "-deneigeuse1:Outremont" ] #fair ensuite pour chaque autre ficher
then
    python3 src/deneigeuse/machine_1/outremont_deneige.py
elif [ "$1" = "-deneigeuse1:Verdun" ] #fair ensuite pour chaque autre ficher
then
    python3 src/deneigeuse/machine_1/verdun_deneige.py
elif [ "$1" = "-deneigeuse1:Saint-Léonard" ] #fair ensuite pour chaque autre ficher
then
    python3 src/deneigeuse/machine_1/saint_leonard_deneige.py
elif [ "$1" = "-deneigeuse1:Rivière-des-prairies-pointe-aux-trembles" ] || [ "$1" = "-deneigeuse1:Rivière" ]
then
    python3 src/deneigeuse/machine_1/riviere_deneige.py
elif [ "$1" = "-deneigeuse1:Le-Plateau-Mont-Royal" ] || [ "$1" = "-deneigeuse1:Plateau-Mont-Royal" ] || [ "$1" = "-deneigeuse1:Le_Plateau-Mont-Royal" ]
then
    python3 src/deneigeuse/machine_1/plateau_deneige.py
elif [ "$1" = "-deneigeuse2" ]
then
    #fair un fichier qui fait les 5 et afficher sur 1grqphe de Montreql
    #sinon le temps :
    python3 src/deneigeuse/machine_2/outremont_deneige.py
    python3 src/deneigeuse/machine_2/verdun_deneige.py
    python3 src/deneigeuse/machine_2/saint_leonard_deneige.py
    python3 src/deneigeuse/machine_2/riviere_deneige.py
    python3 src/deneigeuse/machine_2/plateau_deneige.py
elif [ "$1" = "-deneigeuse2:Outremont" ] #fair ensuite pour chaque autre ficher
then
    python3 src/deneigeuse/machine_2/outremont_deneige.py
elif [ "$1" = "-deneigeuse2:Verdun" ] #fair ensuite pour chaque autre ficher
then
    python3 src/deneigeuse/machine_2/verdun_deneige.py
elif [ "$1" = "-deneigeuse2:Saint-Léonard" ] #fair ensuite pour chaque autre ficher
then
    python3 src/deneigeuse/machine_2/saint_leonard_deneige.py
elif [ "$1" = "-deneigeuse2:Rivière-des-prairies-pointe-aux-trembles" ] || [ "$2" = "-deneigeuse2:Rivière" ]
then
    python3 src/deneigeuse/machine_2/riviere_deneige.py
elif [ "$1" = "-deneigeuse2:Le-Plateau-Mont-Royal" ] || [ "$1" = "-deneigeuse2:Plateau-Mont-Royal" ] || [ "$1" = "-deneigeuse2:Le_Plateau-Mont-Royal" ]
then
    python3 src/deneigeuse/machine_2/plateau_deneige.py
else
    echo 'Pour lancer le code (voir README.txt) : ./ero1.sh [-drone] || [-drone:${nom_quartier}] [-deneigeuse[12]] || [-deneigeuse[12]:${nom_quartier}]'
fi