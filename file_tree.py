"""
This script writes a directory tree's representation in a text file.
"""


from argparse import ArgumentParser
from pathlib import Path
from types import FunctionType


_ASTERISK: str = "*"
_DIRECTORY_MARK: str = "[DR] "
_EMPTY_STR: str = ""
_NEW_LINE: str = "\n"
_TAB: str = "\t"


class DirTreeItem:
	"""
	A directory tree item is a directory or a file.
	"""

	def __init__(self, path: Path, depth: int):
		"""
		The constructor needs the item's path and its depth in the directory
		tree. The root's depth should be 0.

		Args:
			path: the item's path.
			depth: the item's depth in the directory tree.
		"""
		self._path = path
		self._depth = depth

	@property
	def depth(self) -> int:
		"""
		int: this item's depth in the directory tree.
		"""
		return self._depth

	@property
	def path(self) -> Path:
		"""
		pathlib.Path: this item's path.
		"""
		return self._path


def explore_dir_tree(
		dir_path: Path,
		exclude_empty_dirs: bool,
		name_contains: str = None
		) -> list[DirTreeItem]:
	"""
	This function visits all ramifications of a directory tree and represents
	it with a list of DirTreeItem instances. These objects can be used to write
	the tree's representation in a text file.

	If argument name_contains is provided, this function will consider only the
	files whose name contains the argument. The search for name_contains in the
	files' name is case-insensitive.

	Args:
		dir_path: the path to the root directory.
		exclude_empty_dirs: If True, the tree will exclude empty directories.
		name_contains: enables filtering the files if it is not None or
			an empty string. Defaults to None.

	Returns:
		list: DirTreeItem instances representing directories and files in a
			directory tree.
	"""
	if name_contains is None or name_contains == _EMPTY_STR:
		name_filter = lambda name: True
	else:
		name_contains_lower = name_contains.lower()
		name_filter = lambda name: name_contains_lower in name.lower()

	dir_tree_items = list()
	_explore_dir_tree_rec(
		dir_path, dir_tree_items, exclude_empty_dirs, name_filter, 0)

	return dir_tree_items


def _explore_dir_tree_rec(
		dir_path: Path,
		dir_tree_items: list[DirTreeItem],
		exclude_empty_dirs: bool,
		name_filter: FunctionType,
		depth: int
		) -> int:
	"""
	This function called by explore_dir_tree recursively visits directories to
	represent their tree structure with a list of DirTreeItem objects.

	Argument name_filter is a function that takes a file's name as an argument
	and returns a Boolean. A file is included in the tree if and only if
	name_filter returns True.

	Args:
		dir_path: the path to a directory.
		dir_tree_items: This list will contain the DirTreeItem objects
			instantiated throughout the directory tree's exploration. It should
			be empty when this function is first called.
		exclude_empty_dirs: If True, the tree will exclude empty directories.
		name_filter: the function that decides to include files in the tree
			depending on their name.
		depth: the depth of dir_path in the directory tree. It should be set to
			0 when this function is first called.
	
	Returns:
		int: the number of files from dir_path and its subdirectories that this
			function included in the directory tree.
	"""
	dir_tree_items.append(DirTreeItem(dir_path, depth))
	depth += 1

	directories: list[Path] = list()
	nb_files_included = 0

	for item in dir_path.glob(_ASTERISK):
		if item.is_dir():
			directories.append(item)

		# The item is a file.
		elif name_filter(item.name):
			dir_tree_items.append(DirTreeItem(item, depth))

	for directory in directories:
		nb_files_sub_dir = _explore_dir_tree_rec(
			directory, dir_tree_items, exclude_empty_dirs, name_filter, depth)
		nb_files_included += nb_files_sub_dir

	if exclude_empty_dirs and nb_files_included < 1:
		dir_tree_items.pop()

	return nb_files_included


def _dir_tree_item_to_str(dir_tree_item: DirTreeItem) -> str:
	item_str = _TAB * dir_tree_item.depth

	if dir_tree_item.path.is_dir():
		item_str += _DIRECTORY_MARK

	item_str += dir_tree_item.path.name

	return item_str


def _make_parser() -> ArgumentParser:
	parser = ArgumentParser(description=__doc__)

	parser.add_argument("-c", "--contains",
		type=str, default=None,
		help="Only include files whose name contains this argument.")

	parser.add_argument("-d", "--directory",
		type=Path, default=None, required=True,
		help="Path to the directory tree structure's root.")

	parser.add_argument("-e", "--exclude-empty", action="store_true",
		help="This flag excludes empty directories from the directory tree.")

	parser.add_argument("-o", "--output",
		type=Path, default=None, required=True,
		help="Path to the text file that will represent the directory tree.")

	return parser


if __name__ == "__main__":
	args = _make_parser().parse_args()
	contains = args.contains
	exclude_empty_dirs = args.exclude_empty
	dir_path = args.directory.resolve()
	output_path = args.output

	dir_tree_items = explore_dir_tree(dir_path, exclude_empty_dirs, contains)

	with output_path.open(mode="w", encoding="utf-8") as output_stream:
		output_stream.write(str(dir_path) + _NEW_LINE)

		for dir_tree_item in dir_tree_items[1:]:
			output_stream.write(
				_dir_tree_item_to_str(dir_tree_item) + _NEW_LINE)
