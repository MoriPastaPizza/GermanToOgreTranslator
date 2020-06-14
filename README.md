

<h1 align=center>Deutsch zu Oger / MeddlFränkisch Übersetzer</h1>
<p align=center>Ein Reddit-Bot welcher deutsche Sätze in "Ogersprache" übersetzt</p>

<p align=center>
	<img src="images/ruinerbot.png" alt="Logo" width="45%" height="45%">
</p>

## Inhalt

* [Über](#über)
* [How-To](#how-to)
* [Fehlermeldungen](#fehlermeldungen)
	* [Fehlermeldung erzwingen](#fehlermeldung-erzwingen)
* [Du willst mithelfen? Oder das Wörterbuch erweitern?](#du-willst-mithelfen-oder-das-wörterbuch-erweitern)
	* [Wörterbuch erweitern](#wörterbuch-erweitern)
	* [Normale Menschen](#du-kennst-dich-etzadla-mitm-bezeh-net-so-gut-aus)
	* [Nerds](#du-hast-scho-amoal-in-gimb-was-neigspeicherd)
* [Danksagungen](#danksagung)

## Über
Inspiriert von diesem [Post](https://www.reddit.com/r/Drachenlord/comments/gyiaiv/es_muss_gesagt_werden/) .

Da einige Posts im [Drachenlord Subreddit](https://www.reddit.com/r/Drachenlord/) in "normalen" Hochdeutsch verfasst werden, oder es einfach zu viel hadde Abbeid ist einen langen Text ins Meddlfrängische zu übersetzten, wurde dieser Bot erschaffen.

Obwohl der Wortschatz von diesem Bot einen ziemlich hohen Ikuh hat, hat er doch noch viel Verbesserungsbedarf. Und **DU** kannst dabei helfen, schau einfach [hier](#du-willst-mithelfen-oder-das-wörterbuch-erweitern)!

Das Drachengame hat mir viele Lacher und Momente beschert. Ich wollte auch mal meinen kleinen Beitrag leisten. Ich hoffe dieser Bot wird viel benutzt, bringt euch ein paar Lacher und wird von vielen Wahnsinnichen [verbessert](#du-willst-mithelfen-oder-das-wörterbuch-erweitern).

> PS: Dieser Bot funktioniert in allen Subreddits, also meddelt den auch in anderen deutschprachigen Subs raus!

## How-To
Dich nervt ein Post / Kommentar der im "Hochdeutschen" geschrieben wurde? Erwähne einfach den [DeutschZuOgerBot](https://www.reddit.com/user/DeutschZuOgerBot/) in einem Kommentar!

    u/DeutschZuOgerBot
   
   Er sollte so schnell wie möglich zurückmeddln und den orginal Text übersetzten!

![Beispiel](https://github.com/MoriPastaPizza/GermanToOgreTranslator/blob/master/images/screenshot.jpg?raw=true)

## Fehlermeldungen

Ab und an kann es zu Fehlern kommen, aber nicht wegen mir.

> Ich bin das höchste Wesne, ich mach keine Fehler. Des waren wieder die Gagg Haider die schon bei GidHub abeiden und meinen Code manubulieren!!

*SOLLTE* es zu Fehlern kommen meddelt sich der bot mit einer zufälligen Fehlermeddlung:

![Fehlermeddlung](https://github.com/MoriPastaPizza/GermanToOgreTranslator/blob/master/images/screenshot_error.jpg?raw=true)

#### Fehlermeldung erzwingen

Um eine Fehlermeldung zu erzwingen musst du einfach den Parameter "--error" hinter den Aufruf schreiben:

    /u/DeutschZuOgerBot --error
  
## Du willst mithelfen? Oder das Wörterbuch erweitern?
### Wörterbuch erweitern
Im [dict](https://github.com/MoriPastaPizza/GermanToOgreTranslator/tree/master/dict "dict") Ordner sind 3 Dateien

 1. [dictionary_default.json](https://github.com/MoriPastaPizza/GermanToOgreTranslator/blob/master/dict/dictionary_default.json "dictionary_default.json")
 2. [dictionary_error_messages.json](https://github.com/MoriPastaPizza/GermanToOgreTranslator/blob/master/dict/dictionary_error_messages.json "dictionary_error_messages.json")
 3. [dictionary_header.json](https://github.com/MoriPastaPizza/GermanToOgreTranslator/blob/master/dict/dictionary_header.json "dictionary_header.json")
 
 Die erste ist das eigentlich Wörterbuch.  
 Das zweite ist für die zufälligen Fehlermeldungen.  
 Das dritte ist für die zufälligen Header beim Posten (hauptsächlich Zitate vom [Oger](https://github.com/MoriPastaPizza/GermanToOgreTranslator/blob/master/images/ruiner.jpeg)).
 
  Die Wörter vor dem : sind die Wörter nach welchen gesucht werden soll. Die Wörter in den eckigen Klammern [] sind die, welche die gefundenen ersetzten.... Sollten mehrere Wörter in den Klammern stehen, wird eins zufällig davon ausgewählt.
#### Du kennst dich etzadla mitm Bezeh net so gut aus?
Kein Problem! Schick [mir](https://www.reddit.com/user/MoriPastaPizza) einfach deine Wörterbuch Vorschläge so! Egal ob für das eigentliche Wörterbuch oder die Fehlermeddlungen oder die Header! Ich versuche diese dann mit einzubinden.

#### Du hast scho amoal in Gimb was neigspeicherd?
Du kannst mir gerne helfen diesen Bot zu verbessern! Einfach einen Pullrequest machen!
Jeder Vorschlag / Verbesserung am Source-Code oder an den Dictionaries ist herzlich wilkommen.

 

## Danksagung

* [VredditDownloader](https://github.com/JohannesPertl/vreddit-download-bot)
* [Altschauerbergwiki](https://altschauerberg.com/index.php/Winklersche_Rechtschreibreform)
* [Praw](https://praw.readthedocs.io/en/latest)
* [Readme Template](https://github.com/othneildrew/Best-README-Template/blob/master/README.md)
