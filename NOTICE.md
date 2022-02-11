Le projet se divise en 2 parties, un jeu puissance 4 et un notebook (.ipynb) afin de visualiser les données des parties.

Le jeu se lance à partir de l'exécutable dans le répertoire /dist "puissance4.exe". (windows sur et normalement Linux). 

On peut également lancer le projet à partir des fichiers sources pour Linux si l'exécutable ne fonctionne pas sur cet OS.

Une fois la partie terminée, les données sont enregistrées dans un .csv dans le répertoire racine "previous_games.csv".

Dans ce même répertoire figure le notebook "dataviz_panda.ipynb" permettant de visualiser les données du .csv généré.

Notez que nous avons également ajouté un .csv "previous_games_statique.csv" permettant d'avoir un csv déja rempli, si pour la correction vous ne souhaitez pas lancer x fois le programme.

Il faudra juste modifier dans le notebook la commande data=pd.read_csv("previous_games.csv") afin de charger le bon csv.

/!\ Nous avons globalement réglé toutes les éventuelles erreurs du programme exceptée une dernière. Si jamais vous ouvrez le "previous_games.csv" avec excel et/ou avec d'autres
logiciel de même nature, le programme ne pourra plus écrire dans ce fichier et il plantera. Si vous souhaitez lancer le programme, veuillez à ne pas ouvrir le csv avec un autre logiciel.

Bon jeu ! :)