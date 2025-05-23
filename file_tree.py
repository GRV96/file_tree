"""
This script writes a directory tree's representation in a text file.
"""


from argparse import ArgumentParser
from pathlib import Path


_ASTERISK = "*"
_DIRECTORY_MARK = "[DR] "
_EMPTY_STR = ""
_NEW_LINE = "\n"
_TAB = "\t"


class DirTreeItem:
	"""
	A directory tree item is a directory or a file.
	"""

	def __init__(self, path, depth):
		"""
		The constructor needs the item's path and its depth in the directory
		tree. The root's depth should be 0.

		Args:
			path (pathlib.Path): the item's path.
			depth (int): the item's depth in the directory tree.
		"""
		self._path = path
		self._depth = depth

	@property
	def depth(self):
		"""
		int: this item's depth in the directory tree.
		"""
		return self._depth

	@property
	def path(self):
		"""
		pathlib.Path: this item's path.
		"""
		return self._path


def explore_dir_tree(dir_path, name_contains=None):
	"""
	This generator visits all ramifications of a directory tree and represents
	it with DirTreeItem instances. These objects can be used to write the
	tree's representation in a text file.

	If argument name_contains is provided, this generator yields DirTreeItem
	instances only for the files whose name contains the argument. The search
	for name_contains in the files' name is case-insensitive.

	Args:
		dir_path (pathlib.Path): the path to the root directory.
		name_contains (str): enables filtering the files if it is not None or
			an empty string. Defaults to None.

	Yields:
		DirTreeItem: It represents a directory or a file in a directory tree.
	"""
	if name_contains is None or name_contains == _EMPTY_STR:
		name_filter = lambda name: True
	else:
		name_contains_lower = name_contains.lower()
		name_filter = lambda name: name_contains_lower in name.lower()

	yield from _explore_dir_tree_rec(dir_path, name_filter, 0)


def _explore_dir_tree_rec(dir_path, name_filter, depth):
	"""
	This generator called by explore_dir_tree recursively visits directories to
	represent their tree structure with DirTreeItem objects.

	Argument name_filter is a function that takes a file's name as an argument
	and returns a Boolean. This generator yields a DirTreeItem instance for a
	given file if and only if name_filter returns True.

	Args:
		dir_path (pathlib.Path): the path to a directory.
		name_filter (function): the function that decides to include files in
			the tree depending on their name.
		depth (int): the depth of dir_path in the directory tree. It should be
			set to 0 when this generator is first called.

	Yields:
		DirTreeItem: It represents a directory or a file in a directory tree.
	"""
	yield DirTreeItem(dir_path, depth)
	depth += 1
	directories = list()

	for item in dir_path.glob(_ASTERISK):
		if item.is_dir():
			directories.append(item)

		# The item is a file.
		elif name_filter(item.name):
			yield DirTreeItem(item, depth)

	for directory in directories:
		yield from _explore_dir_tree_rec(directory, name_filter, depth)


def _dir_tree_item_to_str(dir_tree_item):
	item_str = _TAB * dir_tree_item.depth

	if dir_tree_item.path.is_dir():
		item_str += _DIRECTORY_MARK

	item_str += dir_tree_item.path.name

	return item_str


def _make_parser():
	parser = ArgumentParser(description=__doc__)

	parser.add_argument("-c", "--contains", type=str, default=None,
		help="Only include files whose name contains this argument.")

	parser.add_argument("-d", "--directory",
		type=Path, default=None, required=True,
		help="Path to the directory tree structure's root.")

	parser.add_argument("-o", "--output",
		type=Path, default=None, required=True,
		help="Path to the text file that will represent the directory tree.")

	return parser


if __name__ == "__main__":
	args = _make_parser().parse_args()
	contains = args.contains
	dir_path = args.directory.resolve()
	output_path = args.output

	dir_tree_item_gen = explore_dir_tree(dir_path, contains)
	next(dir_tree_item_gen) # Skip the root directory's name.

	with output_path.open(mode="w", encoding="utf-8") as output_stream:
		output_stream.write(str(dir_path) + _NEW_LINE)

		for dir_tree_item in dir_tree_item_gen:
			output_stream.write(
				_dir_tree_item_to_str(dir_tree_item) + _NEW_LINE)
