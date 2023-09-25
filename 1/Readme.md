# Brief Pandas - Analyse de données 

---

Lecture essentielle : https://pandas.pydata.org/docs/user_guide/10min.html

Tout au long de ce brief prenez des notes, afin de présenter une veille + demo/résultats, en fin de journée, pour un cross-call avec Marseille/Nice ;)

**Entrainement:**

Avec numpy vous avez découvert les array (np.ndarray?) qui est LE principal type d'objet avec lequel on travaille avec numpy.
Pandas va nous apporter deux nouveaux types (qui encapsule les array numpy, en nous offrant de nombreuses fonctionnalités et utilitaires au array):
- pd.DataFrame?
- pd.Series?

Voici un façon de créer une DataFrame à partir d'un dictionnaire python:
```
df = pd.DataFrame({
    "colonne a": [1, 2, 3],
    "colonne b": [6, 7, 8],
    "colonne c": [0, 0, 1]
})
```


Tester cet objet, accéder au colonne. Itérer l'objet. Afficher le. Récupérer le tableau numpy. Rajouter une nouvelle colonne. Renommer toutes les colonnes en mettant les initiales en majuscules (str.title?)

---

Un agent de la DGSI vous contacte pour réaliser une mission urgente pour le gouvernement. Vous avez un 24h !

Ils ont besoin d'experts en science de la donnée pour analyser des données du Covid.

Les données sont sur le site du gouvernement sur le lien suivant : https://www.data.gouv.fr/en/datasets/donnees-hospitalieres-relatives-a-lepidemie-de-covid-19/?undefined#/resources

Pour vous faciliter la vie, ils ont réduit les données dans un premier tableau que vous pouvez analyser et qui comprend des données du covid en France, et par sexe.
(cf `reduced_covid_sexe.csv` + `metadata_covid_sexe.csv`)

> use the paramaters `encoding="latin-1"` to solve the encoding error you can have when loading the metadata file !


Les données "sexe" sont encodées comme suit:

```
0: femmes + hommes
1: hommes
2: femmes
```

A partir des données fournie, vous devez faire un analyse et synthèse des données. Pour chacun de vos résultats, le code associé doit être fourni (pour prouver votre réponse/analyse).
Voici ce qu'ils cherchent à savoir :
- Afficher les 15 premières lignes du tableau covid_sexe.csv. (df.head?)
- Afficher les 15 dernières lignes du tableau covid_sexe.csv. (df.tail?)
- Afficher les dataframe du metadata_sexe ? a quoi sert t'il ?
- Quelle est la période temporelle sur laquelle s'étendent les données ?
- Sur combien de jours s'étale les données ? années ?
- Dessiner un Heatmap des corrélations des caractéristiques qui vous semblent pertinentes d'observer ? Discuter les résultats
- Tracer l'evolution sur un même graphique des hospitalisations et des réanimations, pour les Femmes et pour les hommes. Discuter les résultats
- Tracer sut le même graphique le nombre de décès cumulés pour les hommes et pour les femmes, mais sur une échelle verticale différente/sépare (plt.twinx?)
- Quelle est la probabilité pour un Français (vs) une Française de mourir du Covid au début de la période disponible ? à la fin de la période disponible ?


Bonus (à ajuster en fonction de votre vitesse d'exécution ;) :

1. Retrouver le tableau de donnée "reduced_covid_sexe.csv" à partir des données csv officielle disponible sur le site de data.gouv.fr (pd.groupby?, et pd.unstack?)
    - data - par sexe https://www.data.gouv.fr/fr/datasets/r/63352e38-d353-4b54-bfd1-f1b3ee1cabd7
    - metadata : https://www.data.gouv.fr/fr/datasets/r/3f0f1885-25f4-4102-bbab-edec5a58e34a

2. Tracer un histogramme permettant de visualiser quelles sont les régions ou la probabilité de mourir du covid en France est la plus élevé ?

3. Quelles sont les 3 régions les plus dangereuses ? les 3 les moins dangereuses ?

4. Tracer les probabilités d'hospitalisation/réanimation/décès du covid par tranche d'âge
    - data - par age (and +): https://www.data.gouv.fr/fr/datasets/r/e3d83ab3-dc52-4c99-abaf-8a38050cc68c)
