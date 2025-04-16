# File Tree

## FRANÇAIS

L'application File Tree écrit l'arborescence d'un dossier racine dans un
fichier texte. Les niveaux d'indentation indiquent quels éléments sont inclus
dans chaque dossier.

Il faut lancer File Tree en ligne de commande avec les arguments suivants.

* `-d`/`--directory`: le chemin du dossier racine.
* `-o`/`--output`: le chemin du fichier qui contiendra l'arborescence du
dossier spécifié par `-d`.

Exemple:

```
python file_tree.py -d .git -o essai.txt
```

L'argument `-h` affiche l'aide.

```
python file_tree.py -h
```

## ENGLISH

Application File Tree writes a root directory's tree structure in a text file.
The indentation levels indicate which items are contained in each directory.

File Tree must be executed in command line with the following arguments.

* `-d`/`--directory`: the path to the root directory.
* `-o`/`--output`: the path to the file meant to contain the tree structure of
the directory specified with `-d`.

Example:

```
python file_tree.py -d .git -o trial.txt
```

Flag `-h` displays the help.

```
python file_tree.py -h
```
