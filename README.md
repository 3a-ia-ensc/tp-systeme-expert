# Système expert - AkiNN

#  ![Supported Python Versions](https://img.shields.io/badge/Python->=3.8-blue.svg?logo=python&logoColor=white) ![Made withJupyter](https://img.shields.io/badge/Jupyter-6.1.5-orange.svg?logo=jupyter&logoColor=white) ![GitHub license](https://img.shields.io/badge/License-DTFW-green.svg?logo=GitHub Sponsors&logoColor=white) 

_Auteurs:_ [Simon Audrix](mailto:saudrix@ensc.fr) & [Gabriel Nativel-Fontaine](mailto:gnativ910e@ensc.fr)

Ce dépôt contient un système expert, spécialisé dans le conseil lors de la création d'architectures de réseaux de neurones. Il s'agit du système **AkiNN**.

Il a été réalisé dans le cadre du module **Connaissances et Représentations** du parcours **Intelligence Artificielle** inscrit dans la 3ème année du cursus d'ingénieur au sein de l'[Ecole Nationale Supérieure de Cognitique](http://www.ensc.fr). Il utilise comme base un système de chainage réalisé par [Laurent Simon](https://www.labri.fr/perso/lsimon/). 

## Architecture

### Les faits

Le système utilise une base de faits qui se regroupent en quatre grande catégories:

- Qu'elles données l'utilisateur veut traiter
- L'objectif de son traitement
- La possibilité de faire un apprentissage supervisé ou non
- L'ensemble des architectures possibles

Ici l'ensemble des faits décrivant une architecture sont considérés comme terminaux, à l'inverse des trois autres catégories ou tout les faits peuvent être utilisés comme des faits initiaux.

### Les règles

Chacun de ces faits peut être utilisé en entré ou en sortie de règles. L'utilisateur peut questionner le système en lui donnant en entrée un ou plusieurs faits initiaux ou terminaux. Les règles utilisent ensuite deux techniques de chaînage pour naviguer dans la base de fait et inférer des conclusion.

#### Chainage avant

Les règles utilisent un système de chainage avant à partir de faits initiaux, cela lui permet de naviguer de règle en règle en fonction des faits reçu lors de la requête de l'utilisateur. Si une règle est incomplète, c'est à dire que le système ne dispose pas de connaissance sur l'ensemble des faits nécessaire pour l'appliquée, alors **AkiNN** peut demander à l'utilisateur de compléter ces règles en statuant sur les faits manquants. Partant de faits initiaux le système peut donc inférer un architecture de réseaux adaptée au problème proposé par l'utilisateur.

### Chaînage arrière

De même, un utilisateur peut donner en entré un fait terminal. Dans ce cas, le système utilise une technique de chaînage arrière afin de conclure sur les entrée possible du réseaux demandé. __AkiNN__ peut donc vous dire quelles données utiliser dans votre architecture.

## Interface





<p align="center">
    <img src='https://ensc.bordeaux-inp.fr/sites/default/files/upload/page-edito/inp/img/logos/logo.ensc-bxinp.jpg' width=200px height=150px />
</p>
