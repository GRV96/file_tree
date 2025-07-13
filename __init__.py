"""
This package allows to make a representation of a directory tree and write it
in a text file.
"""


from .src import\
	DirTreeItem,\
	explore_dir_tree,\
	write_dir_tree


__all__ = [
	DirTreeItem.__name__,
	explore_dir_tree.__name__,
	write_dir_tree.__name__
]
