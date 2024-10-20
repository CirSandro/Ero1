# README

## Installation

Pour essayer notre projet, il faut installer OSMnx :

```bash
pip install osmnx
```

## Utilisation du Programme

Pour utiliser notre programme, exécutez le script `./ero1.sh` de la manière suivante (Outremont est un exemple, d'autres quartiers sont possibles) :

- `./ero1.sh`  
  Lance le drone sur toute la ville et déneige les 5 quartiers (ATTENTION : drone sur la ville pendant +48h) avec la machine 1 de base.

- `./ero1.sh -drone`  
  Lance seulement le drone sur toute la ville.

- `./ero1.sh -drone:Outremont`  
  Lance le drone seulement sur le quartier d'Outremont (autres quartiers possibles : Verdun, Saint-Léonard, Rivière, Plateau-Mont-Royal).

- `./ero1.sh -deneigeuse1`  
  Lance la déneigeuse sur les 5 quartiers avec la première machine.

- `./ero1.sh -deneigeuse2`  
  Lance la déneigeuse sur les 5 quartiers avec la deuxième machine.

- `./ero1.sh -deneigeuse1:Outremont`  
  Lance la déneigeuse seulement sur Outremont (autres quartiers et autres machines possibles).

- `./ero1.sh -drone -deneigeuse1:Outremont`  
  Lance le drone sur toute la ville et la déneigeuse sur Outremont.

- `./ero1.sh -drone:Outremont -deneigeuse1:Outremont`  
  Lance le drone et la déneigeuse sur Outremont.

- `./ero1.sh -drone:Outremont -deneigeuse1`  
  Lance le drone et la déneigeuse sur Outremont.

**Note** : Nous n'avons pas eu le temps de prévoir une option pour plusieurs déneigeuses ou d'autres quartiers. Les valeurs doivent être modifiées manuellement dans le fichier suivant :

```bash
python3 src/deneigeuse/plusieurs_machines/outremont.py
```

Cela lancera `n` déneigeuses de type 1 sur le quartier d'Outremont.

## Architecture du Projet

```
.
├── doc
│   ├── AUTHORS.txt
│   ├── ERO1.pdf
│   └── presentation_ERO1.pdf
├── ero1.sh
├── README.txt
└── src
    ├── deneigeuse
    │   ├── machine_1
    │   │   ├── outremont_deneige.py
    │   │   ├── plateau_deneige.py
    │   │   ├── riviere_deneige.py
    │   │   ├── saint_leonard_deneige.py
    │   │   └── verdun_deneige.py
    │   ├── machine_2
    │   │   ├── outremont_deneige.py
    │   │   ├── plateau_deneige.py
    │   │   ├── riviere_deneige.py
    │   │   ├── saint_leonard_deneige.py
    │   │   └── verdun_deneige.py
    │   └── plusieurs_machines
    │       └── outremont.py
    └── drone
        ├── montreal.py
        ├── outremont.py
        ├── plateau_drone.py
        ├── riviere_drone.py
        ├── saint_leonard_drone.py
        └── verdun_drone.py

```

### Ressources supplémentaires

- Aide Python Graph : [NetworkX Documentation](https://networkx.org/documentation/stable/tutorial.html)

## Contexte

### Déneigement à Montréal

- Période : Octobre à avril (7 mois)
- Effectif : 3000 employés
- Matériel : 2000 appareils
- Sel de déneigement : 200 000 tonnes (300 000 chargements par an)
- Réseau : 228 km de routes, 449 km de réseau piéton
- Budget : 165 M$

### Objectif

L'objectif est de réduire au maximum le coût du déneigement lors d'une journée type en minimisant les trajets tout en garantissant que la zone soit traitée.

### Mission

- Déterminer le trajet minimal du drone lors du survol en effectuant une analyse fine.
- Déterminer l'itinéraire des véhicules.
- Proposer un modèle de coût pour l'opération de l'ensemble de la ville en fonction des véhicules disponibles.

### Contraintes

- **Auteurs** : Liste des auteurs
- **README** : Instructions d'installation et d'exécution + descriptif de la structure du rendu.
- **Fichier PDF** : 4 pages de synthèse (données utilisées + hypothèses/modèle + solutions + limites).
- **Script** : Exécution de la démonstration de notre solution.
- Sous-arborescence pour l'étude du vol du drone.
- Sous-arborescence sur le déneigement de 5 lieux.

### Coûts

**Drone**  
- Coût : 100 € / jour  
- Coût par km : 0,01 € / km  

**Véhicules**  
- **Type 1**  
  - Coût : 500 € / jour  
  - Coût par km : 1,1 € / km  
  - Coût par heure : 1,1 € (premières 8 heures), 1,3 € après  
  - Vitesse moyenne : 10 km/h  

- **Type 2**  
  - Coût : 800 € / jour  
  - Coût par km : 1,3 € / km  
  - Coût par heure : 1,3 € (premières 8 heures), 1,5 € après  
  - Vitesse moyenne : 20 km/h  

## Références

Utilisation d'OSMnx :  
Boeing, G. (2017). OSMnx: New Methods for Acquiring, Constructing, Analyzing, and Visualizing Complex Street Networks. *Computers, Environment and Urban Systems*, 65, 126-139. doi:10.1016/j.compenvurbsys.2017.05.004
