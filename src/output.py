from pathlib import Path

from .dir_tree_exploration import explore_dir_tree
from .dir_tree_item import DirTreeItem


_ENCODING_UTF8 = "utf-8"
_MODE_W = "w"

_DIRECTORY_MARK: str = "[DR] "
_NEW_LINE: str = "\n"
_TAB: str = "\t"


def _dir_tree_item_to_str(dir_tree_item: DirTreeItem) -> str:
	item_path = dir_tree_item.path
	item_str = _TAB * dir_tree_item.depth

	if item_path.is_dir():
		item_str += _DIRECTORY_MARK

	item_str += item_path.name

	return item_str


def write_dir_tree(
		output_file: Path,
		dir_path: Path,
		exclude_empty_dirs: bool,
		name_contains: str = None) -> None:
	"""
	This function writes the text representation of a directory tree in a text
	file. The indentation levels indicate which items are contained in each
	directory. Mark [DR] indicates that an item is a directory.

	Empty directories can be excluded from the tree representation. A directory
	is considered empty if it contains nothing or if it contains only
	subdirectories that do not contain files.

	If argument name_contains is provided, this function will consider only the
	files whose name contains the argument. The search for name_contains in the
	files' name is case-insensitive.

	Args:
		output_file: the text file that will contain the directory tree's
			representation.
		dir_path: the path to a directory.
		exclude_empty_dirs: If True, the tree will exclude empty directories.
		name_contains: enables filtering the files if it is not None nor an
			empty string. Defaults to None.

	Raises:
		FileNotFoundError: if dir_path does not exist.
		NotADirectoryError: if dir_path exists, but is not a directory.
	"""
	# Can raise an exception.
	dir_tree_items = explore_dir_tree(
		dir_path, exclude_empty_dirs, name_contains)

	with output_file.open(
			mode=_MODE_W, encoding=_ENCODING_UTF8) as output_stream:
		output_stream.write(str(dir_path) + _NEW_LINE)

		for dir_tree_item in dir_tree_items[1:]:
			item_as_str = _dir_tree_item_to_str(dir_tree_item) + _NEW_LINE
			output_stream.write(item_as_str)


__all__ = [write_dir_tree.__name__]
