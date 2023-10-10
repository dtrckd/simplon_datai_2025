# Clustering with K-means


## Description

Découvrir l'apprentissage non-supervisé au travers de l'algorithme K-means.

## Contexte

L'apprentissage non-supervisé se présente comme une approche de l'apprentissage automatique qui permet de découvrir la structure sous-jacente des données en l'absence d'étiquetage, c'est à dire sans catégorie ou classe connues en avance.


Afin de se familiariser avec cette approche et mieux l'appréhender pour l'utiliser dans des scénario plus complexes, les objectifs sont les suivants : 
* Nous souhaitons comprendre le principe de cette technique et les scénarios d'utilisation.
* Comprendre, expérimenter et évaluer un algorithme de cette classe de problème d'apprentissage : les  K-moyennes (ou K-means) sur un jeu de données simple.
* Comprendre et comparer les métrique d'évaluation en jeux.
* Tester sur des jeux précédemment utilisé de classification, la capacité de l'algorithme à retrouver les catégories de prédiction.


Question de veilles:

* Qu'est ce que le clustering ?
* Est ce un problème difficile  ? pourquoi ? Donnez la complexité en temps et mémoire 
* Quelle sont les métriques utilisés pour le clustering ?
* Écrivez en une phrase votre compréhension pour 3 métrique avec ground truth (dont MNI) 3 sans ground truth (dont silhouette)
	* donner en une phrase l'intuition derrière ces mesures.
    * différence entre NMI et AMI et silhouette ?

## Explore 

- Run a clustering algorithm on the digits/mnist dataset to cluster the numbers.
- Compute the different metrics for unsupervised learning and comment on them.
- Visualize the clustering in a 2D dimensional space using dimensionality reduction techniques.

## Dive

- Load and understand the **20 news groups** dataset.
- Use clustering to find out the group of the document, but this time use train test split method to evaluate the results.
- compare the results with two diffrerent vectorization approach : CountVectorizer and TfIDFVectorizer.
- Compare the results of with another clusetring model called LDA ? https://scikit-learn.org/stable/modules/decomposition.html#latentdirichletallocation
- Compare your clustering prédiction with a classic classification approach. Which one works better ? why ?


## Ressources

* (fr) https://mrmint.fr/algorithme-k-means
* https://scikit-learn.org/stable/modules/clustering.html#clustering
* https://scikit-learn.org/stable/modules/clustering.html#clustering-evaluation



## Livrable

Un git par apprenant avec les éléments suivants:
1. Un notebook, résumant le travail

## Modalité pédagogique

durée: 2 jours
groupe: individuel

