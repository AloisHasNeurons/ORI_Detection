# Détection de l'ORI

  Notre projet consiste à la création d’un programme pour détectés de l’origine de réplication dans une séquence d’ADN donnée.

  L’origine de réplication (ORI) est une séquence d’ADN spécifique, riche en Adénine et Thymine, et par conséquent, pauvre en Guanine et Cytosine, reconnue par la protéine dnaA, permettant d’indiquer où la réplication de l’ADN s’amorce.

  Dans ce projet nous allons donc créer un programme ayant pour but de trouver l’origine de réplication d’une séquence d’ADN donnée. L’origine de réplication est facilement identifiable en utilisant sa richesse en Adénine et en Thymine. En effet, si l’on fait un graphique représentant le taux de GC moyen tout au long de la séquence, on peut trouver l’origine de réplication qui se matérialise par un changement isolé et important du taux de GC en un point.

  Par ailleurs, nous pouvons également nous appuyer sur le calcul (G-C)/(G+C), en faisant un graphique de ce calcul en fonction des paires de bases nous pouvons clairement voir apparaître l’ORI car on observe un changement de signe du résultat à partir de l’origine de réplication. 

  Par ailleurs, le but de cet exercice va être de réussir à trouver l’ORI sur un génome complet, en l’occurrence celui de Borrelia Burgdorferi. Nous disposons donc d’un fichier contenant le génome complet en format FASTA, et nous allons devoir le traiter à l’aide d’un programme afin de faire apparaître l’ORI avec les méthodes présentées ci-dessus. 

  L’organisme dont nous allons étudier le génome est donc une bactérie du nom de Borrelia Burgdorferi qui engendre la maladie de Lyme.

  Ce projet nous permettra d’approfondir nos connaissances en programmation Python en les appliquant à un problème biologique concret. De plus, il nous permettra d’apprendre à utiliser le langage R afin de traiter les données récoltées grâce à Python et d’en faire des graphiques exploitables et pouvoir les analysés pour pouvoir trouver l’ORI.
