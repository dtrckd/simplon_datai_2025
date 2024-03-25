# Création d'un Bot Discord avec Fonctionnalité de Recherche Augmentée (RAG)

Dans ce projet, nous allons développer un bot Discord capable de communiquer en langage naturel, de soutenir une conversation interactive et d'accéder à des sources d'information récentes sur le web.

Pour vous donner une idée de ce à quoi pourrait ressembler un RAG moderne et vous inspirer pour la conception de l'affichage des sources et de l'expérience utilisateur (UX), consultez le site suivant : [Perplexity AI](https://www.perplexity.ai/).

Notre bot sera basé sur le concept d'un RAG. Cependant, plutôt que de s'appuyer sur une base de connaissances vectorielles pour enrichir le contexte, il utilisera les résultats de l'API de recherche de Brave. Il est donc important d'étudier cette API pour maximiser ses avantages : [API de recherche Brave](https://api.search.brave.com/).

### Récit utilisateur 1 - RAG Simple

- L'utilisateur peut interroger le bot pour obtenir des informations sourcées et actualisées.
- L'utilisateur peut engager une conversation avec le bot.
- Le bot doit afficher un message tel que "xxx est en train d'écrire" dans Discord pour informer l'utilisateur qu'une réponse est en cours de préparation.

### Récit utilisateur 2 - RAG Vision

- L'utilisateur peut envoyer un document dans le chat accompagné d'un message.
- Le bot détecte si le document est un texte (code, markdown, etc.) ou une image.
    - Si c'est une image, le bot utilise le modèle GPT-Vision pour analyser l'image. Pour plus d'informations, consultez : [Guide GPT-Vision](https://platform.openai.com/docs/guides/vision).
    - Si c'est une image, le bot utilise également le modèle GPT-Vision pour traiter l'image(s).
    - Dans les autres cas, le bot revient au mode RAG initial.

### Technologies

- LangChain et Llama-Index sont deux importantes bibliothèques facilitant l'interaction avec de nombreuses API pour la création de RAG et d'autres techniques de CoT (Chain of Thought). Elles peuvent être utiles pour découvrir de nouveaux outils ou concepts, mais leur utilisation n'est pas obligatoire. Vous pouvez recréer les composants en Python, ce qui est souvent simple et pourrait vous éviter des dépendances tout en simplifiant la compréhension de leur logique.
- L'utilisation d'un client API est très utile. Apprenez à en utiliser un ici : [Bruno](https://www.usebruno.com/).
- Un client Discord pour développer des bots est disponible ici : [Documentation Discord.py](https://discordpy.readthedocs.io/en/latest/).
- utilisation de `.env` et `load_dotenv` pour isoler les clés et secret du projet proprement : https://stackoverflow.com/questions/41546883/what-is-the-use-of-python-dotenv

### Modalités Pédagogiques

- Travail en équipe (divisé en 3 groupes).
- Partagez un dépôt Git sur Simplonline.
- durée: 2 à 5 jours.
