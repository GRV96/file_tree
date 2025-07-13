# DirTree

## FRANÇAIS

L'application DirTree écrit l'arborescence d'un dossier racine dans un fichier
texte. Les niveaux d'indentation indiquent quels éléments sont inclus dans
chaque dossier. La marque `[DR]` indique qu'un élément est un dossier.

Il faut lancer DirTree en ligne de commande. Les arguments suivants sont
obligatoires.

* `-d`/`--directory`: le chemin du dossier racine.
* `-o`/`--output`: le chemin du fichier qui contiendra l'arborescence du
dossier spécifié par `-d`.

L'aide affiche la description de tous les arguments.

```
python dirtree -h
```

Exemple d'exécution:

```
python dirtree -d /un/dossier -o essai.txt
```

Il est possible d'exécuter DirTree depuis le dépôt local.

```
python . -d .git -o essai.txt
```

## ENGLISH

Application DirTree writes a root directory's tree structure in a text file.
The indentation levels indicate which items are contained in each directory.
Mark `[DR]` indicates that an item is a directory.

DirTree must be executed in command line. The following arguments are
mandatory.

* `-d`/`--directory`: the path to the root directory.
* `-o`/`--output`: the path to the file meant to contain the tree structure of
the directory specified with `-d`.

The help displays the description of all arguments.

```
python dirtree -h
```

Execution example:

```
python dirtree -d /a/directory -o trial.txt
```

It is possible to execute DirTree from the local repository.

```
python . -d .git -o trial.txt
```
