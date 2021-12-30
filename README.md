# File Tree

## Français

L'application File Tree écrit dans un fichier texte l'arborescence des fichiers
contenus dans un dossier racine. L'indentation indique quels éléments sont
inclus dans d'autres.

Il faut lancer File Tree en ligne de commande avec les arguments suivants.

* `-d`/`--directory`: le chemin du dossier à explorer
* `-o`/`--output`: le chemin du fichier contenant l'arborescence écrite de `-d`

Exemple:

```
python file_tree.py -d .git -o essai.txt
```

L'argument `-h` affiche la description des autres arguments.

```
python file_tree.py -h
```

## English

Application File Tree writes the tree structure of a root directory's files in
a text file. The indentation indicates which elements are contained in other
ones.

File Tree must be executed in command line with the following arguments.

* `-d`/`--directory`: the path to the folder to explore
* `-o`/`--output`: the path to the file meant to contain the written tree structure of `-d`

Example:

```
python file_tree.py -d .git -o trial.txt
```

Argument `-h` displays the other arguments' description.

```
python file_tree.py -h
```
