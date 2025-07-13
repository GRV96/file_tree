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

Exemple:

```
python dirtree.py -d .git -o essai.txt
```

L'aide affiche la description de tous les arguments.

```
python dirtree.py -h
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

Example:

```
python dirtree.py -d .git -o trial.txt
```

The help displays the description of all arguments.

```
python dirtree.py -h
```
