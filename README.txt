-> Pour pouvoir essayer notre projet, il faut installer OSMnx : 

pip install osmnx


-> Pour essayer notre programme il faut utiliser le script ./ero1 comme ceci (Outremont est un exemple autres quartiers possibles):
    ./ero1.sh                                          => lance le drone sur toute la ville et deneige les 5 quartiers (ATTENTION: drone sur la ville +48h)
    ./ero1.sh -drone                                   => lance seulement le drone sur toute la ville
    ./ero1.sh -drone:Outremont                         => lance le drone seulement sur le quartier d'Outremont (sinon: Verdun, Saint-Léonard, Rivière, Plateau-Mont-Royal)
    ./ero1.sh -deneigeuse                              => lance la deneigeuse sur les 5 quartiers
    ./ero1.sh -deneigeuse:Outremont                    => lance la deneigeuse seulement sur Outremont(autres quartiers aussi)
    ./ero1.sh -drone -deneigeuse:Outremont             => lance le drone sur toute la ville et deneigeuse sur Outremont
    ./ero1.sh -drone:Outremont -deneigeuse:Outremont   => lance drone et deneigeuse sur Outremont
    ./ero1.sh -drone:Outremont -deneigeuse             => lance drone et deneigeuse sur Outremont


ARCHITECTURE : 
.
├── AUTHORS.txt
├── ero1.sh
├── Hierholzer.py
├── info_sujet.txt
├── README.txt
└── src
    ├── deneigeuse
    │   ├── outremont_deneige.py
    │   ├── plateau_deneige.py
    │   ├── riviere_deneige.py
    │   ├── saint_leonard_deneige.py
    │   └── verdun_deneige.py
    └── drone
        ├── montreal.py
        ├── outremont.py
        ├── plateau_drone.py
        ├── riviere_drone.py
        ├── saint_leonard_drone.py
        └── verdun_drone.py
