-> Pour pouvoir essayer notre projet, il faut installer OSMnx : 

pip install osmnx


-> Pour essayer notre programme il faut utiliser le script ./ero1 comme ceci (Outremont est un exemple autres quartiers possibles):
    ./ero1.sh                                           => lance le drone sur toute la ville et deneige les 5 quartiers (ATTENTION: drone sur la ville +48h) avec la machine1 de base
    ./ero1.sh -drone                                    => lance seulement le drone sur toute la ville
    ./ero1.sh -drone:Outremont                          => lance le drone seulement sur le quartier d'Outremont (sinon: Verdun, Saint-Léonard, Rivière, Plateau-Mont-Royal)
    ./ero1.sh -deneigeuse1                              => lance la deneigeuse sur les 5 quartiers avec la première machine
    ./ero1.sh -deneigeuse2                              => lance la deneigeuse sur les 5 quartiers avec la deuxième machine
    ./ero1.sh -deneigeuse1:Outremont                    => lance la deneigeuse seulement sur Outremont(autres quartiers aussi, et autre machine aussi)
    ./ero1.sh -drone -deneigeuse1:Outremont             => lance le drone sur toute la ville et deneigeuse sur Outremont
    ./ero1.sh -drone:Outremont -deneigeuse1:Outremont   => lance drone et deneigeuse sur Outremont
    ./ero1.sh -drone:Outremont -deneigeuse1             => lance drone et deneigeuse sur Outremont


ARCHITECTURE : 
.
├── AUTHORS.txt
├── ero1.sh
├── Hierholzer.py
├── info_sujet.txt
├── README.txt
└── src
    ├── deneigeuse
    │   ├── machine_1
    │   │   ├── outremont_deneige.py
    │   │   ├── plateau_deneige.py
    │   │   ├── riviere_deneige.py
    │   │   ├── saint_leonard_deneige.py
    │   │   └── verdun_deneige.py
    │   └── machine_2
    │       ├── outremont_deneige.py
    │       ├── plateau_deneige.py
    │       ├── riviere_deneige.py
    │       ├── saint_leonard_deneige.py
    │       └── verdun_deneige.py
    └── drone
        ├── montreal.py
        ├── outremont.py
        ├── plateau_drone.py
        ├── riviere_drone.py
        ├── saint_leonard_drone.py
        └── verdun_drone.py

Utilisation OSMnx:
Boeing, G. 2017. OSMnx: New Methods for Acquiring, Constructing, Analyzing, and Visualizing Complex Street Networks. Computers, Environment and Urban Systems 65, 126-139. doi:10.1016/j.compenvurbsys.2017.05.004
