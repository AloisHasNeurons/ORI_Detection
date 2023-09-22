# Détection de l'ORI
## Introduction

  ### L’origine de réplication (ORI) est une séquence d’ADN spécifique, riche en Adénine et Thymine (AT), donc pauvre en Guanine et Cytosine (GC). Elle est reconnue par la protéine dnaA et permet d’indiquer où la réplication de l’ADN s’amorce.

L’origine de réplication est facilement identifiable en utilisant sa richesse en Adénine et en Thymine. En effet, si l’on fait un graphique représentant le taux de GC moyen tout au long de la séquence, on peut trouver l’origine de réplication qui se matérialise par un changement isolé et important du taux de GC en un point.

De plus, nous pouvons nous appuyer sur le calcul (G-C)/(G+C), en faisant un graphique de ce calcul en fonction des paires de bases nous pouvons clairement voir apparaître l’ORI car on observe un changement de signe du résultat à partir de l’origine de réplication. 

L’organisme dont nous allons étudier le génome est une bactérie du nom de Borrelia Burgdorferi qui engendre la maladie de Lyme.

## Objectif du projet
L'objectif principal de ce projet est de créer un programme capable de détecter l'origine de réplication (ORI) dans une séquence d'ADN donnée. L'ORI est une séquence spécifique d'ADN qui joue un rôle crucial dans le processus de réplication de l'ADN. En développant ce programme, nous visons à automatiser la détection de l'ORI, ce qui peut être une tâche complexe et fastidieuse si réalisée manuellement.

## Méthodes de Détection de l'ORI
Dans ce projet, nous utilisons deux principales méthodes pour détecter l'ORI dans une séquence d'ADN :

1. Analyse du Taux de GC Moyen: Nous calculons le taux de GC (Guanine-Cytosine) moyen le long de la séquence d'ADN. L'ORI se caractérise par une brusque diminution de ce taux. En traçant un graphique du taux de GC en fonction de la position, nous pouvons identifier l'emplacement de l'ORI.
2. Calcul de (G-C)/(G+C) : Cette méthode consiste à calculer la valeur de (G-C)/(G+C) pour chaque position le long de la séquence d'ADN. Lorsque nous représentons ces valeurs sous forme de graphique en fonction des paires de bases, nous observons un changement de signe distinct à l'emplacement de l'ORI.

## Données Utilisées

Pour ce projet, nous avons utilisé le génome complet de Borrelia Burgdorferi, l'organisme responsable de la maladie de Lyme. Les données du génome sont fournies sous forme de fichier au format FASTA. Notre programme traite ces données pour détecter l'ORI. Il est tout à fait envisageable d'utiliser ce programme pour détecter l'ORI chez un autre organisme, il faudrait pour cela une séquence au format FASTA dans le dossier Sequence, et il faudrait modifier le main.py pour donner le bon fichier en entrée. Nous n'avons pas prévu d'interface permettant la sélection d'un fichier dans cette version.

## Langages de Programmation Utilisés

Nous avons développé ce projet en utilisant principalement Python pour l'analyse de données et le traitement du génome. De plus, nous avons utilisé le langage R pour générer des graphiques à partir des données extraites par Python, facilitant ainsi l'analyse de l'emplacement de l'ORI.

## Résulats
### Aperçu des résultats obtenus avec l'exemple du génome de Borrelia Burgdorferi
![GC Skew](https://github.com/AloisVINCENT/Demarche-Scientifique-ORI/assets/78328371/20d3c9df-99c0-45e7-8364-a32ac8978403)

![Sans titre](https://github.com/AloisVINCENT/Demarche-Scientifique-ORI/assets/78328371/c70b8dbc-41ea-4fd6-a633-3227d9d75e18)

## Auteurs
- Aloïs VINCENT
- Erwann GALLOIS

# Conclusion & Expériences personnelles
Ce projet de détection de l'ORI dans une séquence d'ADN nous a permis d'appliquer nos compétences en programmation à un problème biologique complexe. Il nous a également fait explorer l'utilisation de Python et R dans le domaine de la bioinformatique. Nous espérons que ce programme sera utile pour d'autres chercheurs et biologistes dans leurs travaux de recherche sur l'ADN.
