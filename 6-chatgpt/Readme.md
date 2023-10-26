# NLC : The Natural Language Transcompiler

L'histoire de l'informatique est marquée par les compilateurs qui permettent de traduire un programme (code source) en un code machine (assembleur), ce dernier permettant l'exécution physique sur des ordinateurs.

Grâce aux poussées de l'IA générative moderne, et notamment les LLMs (Large Language Model), nous allons construire le premier compilateur permettant de directement traduire du langage humain en code source, avec pour objectif de fournir un outils de prototypage d'une grande simplicité et facilitant la productivité et découverte d'un langage informatique ou d'un librairie. La traduction de code vers un autre code source est appelé transcompilateur (ou transpileur).

Le projet se décompose en deux partie majeures, qui pourront encore être découpées en sous-tâches : 

- Frontend : Le frontend sera une page simple offrant une zone de texte principale permettant de rentrer la description d'un programme informatique. Un sélecteur de choix, optionnelle permettra de préciser le langage de programmation qui doit être utilisé pour la génération. Voici un scénario utilisateur décrivant le fonctionnement :
    1. L'utilisateur rentre la description du programme (l'explication de ce qu'il est censé faire)
    2. [opt] Il précise éventuellement un langage de programmation
    3. Après la soumission des données, le frontend devra afficher deux blocs, sous le bloc de texte de la description initiale: Le premier dans lequel le programme généré devra s'afficher, et un buttons "execute" présent dans un coin. Le deuxième, initialement vide permettant d'afficher les résultats (la sortie standard/output) de l'exécution du programme.
    4. Le bloc avec le code généré devrait pouvoir être éditable pour éventuellement apporter des modifications avant ré-execution.

- Backend : Le backend est constitué de trois parties
    - Connection à l'api d'OpenAi pour la génération (utilisation du modèle gpt-3.5-turbo avec "Chat completion API")
        - [opt] Ingénierie de prompt pour améliorer les performances de la génération
    - Stockage de chaque session dans une base de données (i.e, en premier lieu, la description + la génération)
    - La partie "execution" code et retour de la sortie standard du programme.



Le projet peux être découpé en quatres phases :

1. Faire tourner "simplement" la génération du programme et l'afficher à l'écran.
2. Designer votre DB pour pouvoir enregistrer chaque sessions.
3. rajouter un menu ou un onglet, selon ce qui vous parait le plus pertinent, pour voir la liste des sessions, et pouvoir soit les effacer, ou les réanimer.
4. Faire la partie exécution du programme (on commence avec python uniquement) avec affichage de la sortie (En cas d'erreur d'exécution, l"afficher  en rouge dans le bloc d'exécution du frontend)


### Veille

LLM & OpenAi API



### Organization

Travaillez en mode agile, en faisant des itérations simples et courtes, afin d'observer (et débugger plus facilement) le résultats de ce que vous développez. Les tâches [opt] typiquement peuvent être considérées en seconde itération (ou plus).  

Redécouper les taches pour quelle soient claires pour vous et votre équipe (quitte à les clarifier avec le PO) et vous répartir la charge de travaille.   

Faite des réunions de groupe pour présenter chacune de vos avancées/découvertes. Ne restez pas bloqué, a la place partager votre problématique à votre groupe, on trouve plus rapidement de solutions en intelligence collective, qu'en tournant en rond.  
 


## Livrable

Un git par équipe. Devra contenir : 
- le code propre
- Un readme documentant comment installer et executer le programme.
- Un lien vers votre kanban/project agile

## Modalité pédagogique

durée: 3 jours.
groupe: 3 à 4.
rendus: un repo par groupe.
