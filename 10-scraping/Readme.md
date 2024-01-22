# Scrapy Quotes
compétence: C1, C4, C5, C17, 

## Building a scraper with scrapy


Objectif : Nous avons besoin de votre expertise pour une mission délicate et exigeante : collecter des citations éparpillées sur le site [http://quotes.toscrape.com](http://quotes.toscrape.com). Votre objectif sera de maîtriser l'art subtil du scraping avec Scrapy, de stocker ces trésors de sagesse dans une base MongoDB et enfin, de créer un serveur Flask qui dévoilera une citation aléatoire à chaque visite, tel un oracle moderne.

- Phase 1 - Étude approfondie de Scrapy : En tant qu'experts en développement et intelligence artificielle, vous devez être des connaisseurs avertis des dernières technologies. Commencez donc par une analyse exhaustive de Scrapy, l'instrument raffiné pour le scraping de données. Découvrez ses fonctionnalités, ses forces et ses faiblesses, et soyez prêts à les exploiter pour mener à bien votre mission avec brio. Voici quelque liens incontournable:
    - https://scrapy.org/
    - Le scrapy tuto: https://python.gotrained.com/scrapy-tutorial-web-scraping-craigslist/
    - ihow to send "item" to mongodb : https://docs.scrapy.org/en/latest/topics/item-pipeline.html?highlight=screenshot#write-items-to-mongodb
- Phase 2 - Élaboration du Spider : Une fois votre formation sur Scrapy achevée, il est temps de mettre en pratique vos nouvelles compétences. Infiltrez le site [http://quotes.toscrape.com](http://quotes.toscrape.com) et construisez un Spider élégant qui saura extraire les citations et leurs auteurs avec finesse et discrétion.
- Phase 3 - Conservation des données dans MongoDB : Maintenant que vous avez récupéré ces précieuses informations, vous devez les préserver avec soin. Pour cela, utilisez MongoDB pour stocker les quotes. Veillez à ce que vos données soient bien organisées et faciles à récupérer.
- Phase 4 - Création d'un serveur Flask : Enfin, pour partager vos découvertes avec le monde, vous devez créer un serveur Flask qui affichera une citation aléatoire à chaque visite. Impressionnez vos pairs en créant une interface simple, élégante et sophistiquée qui mettra en valeur vos talents d'expert en renseignement du web.
- Phase 5 - Synchronisation/Stabilisation: faites en sorte qu'a chaque fois que vous relancer votre crawler, les données soit mise à jours en base de donnée. En cas d'erreur (objet non trouvé, url fausse, logger cette information dans un table de votre base. Cette information pourra être utile pour des questions de monitoring automatique (C20).


Questions / Bonuses:
- Pourquoi et comment créer des index dans mongodb ?
- comment et pourquoi set le useragent avec scrapy
- Deployer votre webapp sur l'internet. Deux solution possible, gratuite : https://www.pythonanywhere.com ou https://ngrok.com  (si pb avec mongodb, dumper la bdd dans un fichier que vous chargerai en python. Solution possible car peu de données...)
- Mettre en 
- Besoin d'executer du Javascript. Jetez un oeil à Splash: https://github.com/scrapy-plugins/scrapy-splash

