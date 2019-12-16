
Développeur python junior, vous venez d'intégrer une start-up novatrice qui prévoit de
révolutionner le jeu de plateau. Son objectif ? Proposer une version informatisée du célèbre jeu
Donjons et Dragons qui connaît un succès grandissant.
Vous avez été embauché afin de développer une première mouture implantant les mécaniques de
base du jeu avant que votre équipe ne soit renforcée par de nouveaux développeurs et que vous
puissiez produire un POC.
Attention cependant, vous êtes jeune et avez tout l'avenir devant vous, vous ne savez donc pas si
vous resterez longtemps dans l'entreprise surtout avec le nombre d'offres d'emploi sur le marché.
Vous devrez donc produire un code clair et maintenable qu'un éventuel remplaçant sera capable de
reprendre sans difficultés. Vous l'aurez compris votre application sera développée en respectant les
bonnes pratiques de Python et plus précisément de la POO.
Spécifications fonctionnelles :
. Le joueur peut choisir le type de personnage qu'il souhaite incarner
- Trois classes sont disponibles pour le joueur (guerrier, archer, magicien)
- Le joueur peut nommer son personnage comme il le désire au début du jeu
- Trois classes sont disponibles pour les ennemis (orc, loup, zombie)
- Les personnages ont tous au minimum les caractéristiques suivantes (vie, attaque, défense, agilité,
nom)
- Le magicien dispose en plus de mana représentant sa force magique
- Un personnage peut en attaquer un autre, la cible perd alors de la vie en proportion de sa valeur de
défense et de la valeur d'attaque de l'assaillant
- Le magicien peut se soigner. Ce sort consomme du mana mais lui redonne de la vie. S'il n'a pas
assez de mana, il ne peut pas le lancer
- Un combat est simulé entre le personnage du joueur et un ennemi de votre choix jusqu'à ce que
l'un ou l'autre des personnages soit mort. Assurez-vous de tester que la méthode soin du magicien
soit fonctionnelle
Spécifications techniques :
- Langage Python 3
- Organisation du code en modules et packages
- Usage de la programmation orientée objet
- Respect du principe DRY
- Essayer de respecter certains des principes SOLID
- Programme exécutable par le lancement d'un fichier main.py
