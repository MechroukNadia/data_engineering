# data_engineering
l'idée de l'exercice c'est d'extraire des informations dans un site ( dans notre cas on extrait les informations météorologiques pour plusieurs villes de l'Algérie) , 
puis on les a transformer en données pertinentes ( par exemple on a supprimé les duplications des mémes tuples...) et on les a enregestré dans un fichiers (.csv) à la sortie,
à la fin on les a affiché sur une carte (pour bien représenté les données qu'on a extrait).

le but de cet exercice c'est de créer un fichier Docker qui contient un cron job ( qui vas nous permettre d'exécuter le fichiers "etl.py" chaque 10 minutes ç'est à dire dire
automatisée le processus d'(extraction _trasformation _ chargement : etl).

les 3 fichiers (extract.py / transform.py et load.py ) contient respectivement les codes qui nous permet d'extraire, transformer et charger les données pertinentes.
le fichier "trasformed.csv " contient les résultats aprés le nettoyage des données extraites.
le fichier " cities.json" contient les cités Algériens por lesquelles on a travailler.
le fichier "Dockerfile" contient les élements nécessaire pour la création de l'image docker ainsi que la définitions de cron job (sa configuration ).
le fichier " cron_sc.bat" contient le fichier qui contient le processus qui doit etre exécuter chaque 10 minutes. 

--> le travail demandé n'est pas terminé à 100%, j'ai builder l'image docker et j'ai exécuter, j'ai rencontré un probléme, c'est pour cela que j'ai modifier le code et j'ai mets
que chaque 1 minute, il va faire le update ça marche, mais malheureusement y'a un probléme à chaque une minute il m'affiche cette erreur "2023-06-09 10:12:02 /cron_script.sh: 1: python: not",
j'ai charché sur le net et j'ai trouvé que c'est à cause de l'interpréteur python, j'ai essayé plusiurs solutions proposée par chatgpt mais j'aarive pas à trouver la bonne solution.
