aide python graph : https://networkx.org/documentation/stable/tutorial.html


Déneiger Montréal de octobre à avril = 7mois
 => 3000 employés, 2000 appareils, 200 000 tonnes de sel de deblaiment ou chargement (300 000 chargements par an)suivant l'importance
 => 228km de route, 449km de réseau pédestre
 => budget 165M$

ON S'INTERESSE AU DEBLAIEMENT face chute de neige de => 2,5 à 15cm
obj : reduire le plus possible le cout sur une journée type = minimiser trajet en garantissant que la zone soit traité

Le niveau de neige il n'est parfois pas la peine de déneiger des routes=effectuer analyse aérienne par drone

MISSION:
 - determiner trajet minimal du drone lors du survol en effectuant analyse fine
 - determiner itinéraire des vehicules
 - propose modèle de cout pour opération de l'ensemble de la ville en fct des véhicule à disposition

CONTRAINTE:
 - AUTHORS : liste des auteurs ********FAIT********
 - README : instruction installation et execution + descriptif structure du rendu
 - fichier pdf :4p synthèse reflexion (=donné utiliser+hypothese/modele+solution+limite) =>VOIR SUJET
 - script executant demonstration de notre solution
 - sous-arborescence de l'étude du vol du drone
 - sous-arborescence sur deneigement de 5lieux VOIR SUJET

DRONE:
 - 100€ /jour
 - 0,01€ /km

VEHICULE:
 - type 1 : -> 500€ /jour
   	    -> 1,1€ /km
	    -> 1,1€ /h les 8premieres heures puis 1,3€ /h
	    -> vitesse moyenne : 10km/h
 - type 2 : -> 800€ /jour
   	    -> 1,3€ /km
	    -> 1,3€ /h les 8premieres heures puis 1,5€ /h
	    -> vitesse moyenne : 20km/h

Utilisation OSMnx:
Boeing, G. 2017. OSMnx: New Methods for Acquiring, Constructing, Analyzing, and Visualizing Complex Street Networks. Computers, Environment and Urban Systems 65, 126-139. doi:10.1016/j.compenvurbsys.2017.05.004
