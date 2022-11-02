# Pré CQI 2023 - Intelligence Artificielle (10 points)

## Mise en situation

Le PDG du Potato Cloud Fest dire qu'il veut trouver une façon d'occuper son enfant lorsqu'il l'amènera au travail pendant les semaines menant au festival. Il vous dit que son enfant est un grand fan du jeu de société **BATTLESHIP**. Vous n'êtes pas très à l'aise avec les enfants et vous n'aimez pas jouer à **BATTLESHIP**, mais vous adorez programmer. 

Pour lui rendre un service tout en démontrant vos capacités de programmation, vous décidez de préparer une intelligence artificielle pour jouer contre son enfant. Il est très important d'avoir une intelligence artificielle capable de gagner rapidement sinon l'enfant découvrira la supercherie et son père devra à nouveau trouver une façon de l'occuper!

## Logiciel Requis
- Python 3.7+

## Règlement - Battleship pour les nuls

Il aura **5 navires de largeur 1 et de longueur variable**. Ils seront disposés secrètement sur **une grille de taille 10x10**. À chaque tour, vous devez énoncer une case où vous soupçonnez la présence d'une partie d'un navire quelconque. Vous saurez immédiatement s'il s'agit d'un tir réussi (*HIT*), d'un tir manqué (*MISS*) ou d'un tir fatal (*SUNK*).

Vous gagnez si vous faites couler tous les navires adverses.

```Veuillez noter qu'il s'agit d'une version à un joueur de Battleship. Votre but est d'écrire une IA qui minimise le nombre de tour requis pour faire couler les navires.```

## Instructions

**Ne pas modifier autre chose que `Bot.py`**

* Vous devez implanter la méthode `do_turn` de `Bot.py`;
* Cette dernière doit retourner une paire (tuple) ayant:
    * Première composante: la lettre de la colonne désirée (A à J)
    * Deuxième composante: l'index de la rangée désirée (\[0, 9\])
* Vous pouvez ajouter des attributs à la classe `Bot` comme vous voulez

## Évaluation

Vous serez évalués en fonction de la moyenne du nombre de tours requis pour couler tous les navires.

```Si votre bot prend plus que 90 tours à faire couler tous les navires, l'exécution est stoppée ✂✂✂```

## Remise

Vous devez remettre le fichier `Bot.py`, tout simplement.

## Exécuter
Pour exécuter le programme vous pouvez rouler la commande ci-dessous. Vous pouvez également rajouter un argument qui indique le nombre de partie à jouer et calculer la moyenne à par rapport 
```
$ python3 Main.py <nombre de partie>
```

## Points

L'équipe avec la moyenne la plus petite aura directement `10 points`. Le reste des équipes auront un pointage pondéré à la meilleure équipe.

Le total sur 10 points est calculé ainsi :

$$ Total = {NbrTourMoyen_{meilleur équipe} \over NbrTourMoyen_{équipe}} * 10 $$


