# DirTree

## FRANÇAIS

Le paquet DirTree permet de créer une représentation de l'arborescence d'un
dossier racine et de l'écrire dans un fichier texte. Une arborescence est
constituée de deux types d'éléments: des dossiers et des fichiers.

### Représentation textuelle d'une arborescence

Lorsqu'une arborescence est représentée dans un fichier texte, chaque ligne
correspond à un élément. La marque `[DR]` indique qu'un élément est un dossier.
Les dossiers contiennent les éléments dont le niveau d'indentation est
supérieur au leur.

### Contenu

La classe `DirTreeItem` représente un élément d'une arborescence de dossiers.

La fonction `explore_dir_tree` visite toutes les ramifications d'une
arborescence de dossiers et la représente par des instances de `DirTreeItem`.

La fonction `write_dir_tree` écrit la représentation textuelle d'une
arborescence de dossiers dans un fichier texte.

### Application en ligne de commande

Lorsqu'on exécute le paquet DirTree en ligne de commande, il écrit
l'arborescence d'un dossier racine dans un fichier texte. Les arguments
suivants sont obligatoires.

* `-d`/`--directory`: le chemin du dossier racine.
* `-o`/`--output`: le chemin du fichier qui représentera l'arborescence du
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

Package DirTree allows to make a representation of a directory tree and write
it in a text file. A directory tree contains items of two types: directories
and files.

### Text representation of a directory tree

When a directory tree is represented in a text file, each line corresponds to
a tree item. Mark `[DR]` indicates that an item is a directory. Directories
contain the items whose indentation level is greater than theirs.

### Content

Class `DirTreeItem` represents an item in a directory tree.

Function `explore_dir_tree` visits all ramifications of a directory tree and
represents it with `DirTreeItem` instances.

Function `write_dir_tree` writes the text representation of a directory tree in
a text file.

### Command line application

When package DirTree is executed in command line, it writes a root directory's
tree in a text file. The following arguments are mandatory.

* `-d`/`--directory`: the path to the root directory.
* `-o`/`--output`: the path to the file meant to represent the tree structure
of the directory specified with `-d`.

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
