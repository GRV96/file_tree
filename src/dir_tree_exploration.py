from pathlib import Path
from types import FunctionType

from .dir_tree_item import DirTreeItem


_ASTERISK: str = "*"
_EMPTY_STR: str = ""


def explore_dir_tree(
		dir_path: Path,
		exclude_empty_dirs: bool,
		name_contains: str = None
		) -> list[DirTreeItem]:
	"""
	This function visits all ramifications of a directory tree and represents
	it with a list of DirTreeItem instances. These objects can be used to write
	the tree's representation in a text file.

	Empty directories can be excluded from the tree representation. A directory
	is considered empty if it contains nothing or if it contains only
	subdirectories that do not contain files.

	If argument name_contains is provided, this function will consider only the
	files whose name contains the argument. The search for name_contains in the
	files' name is case-insensitive.

	Args:
		dir_path: the path to a directory.
		exclude_empty_dirs: If True, the tree will exclude empty directories.
		name_contains: enables filtering the files if it is not None nor an
			empty string. Defaults to None.

	Returns:
		list: DirTreeItem instances representing directories and files in a
			directory tree.

	Raises:
		FileNotFoundError: if dir_path does not exist.
		NotADirectoryError: if dir_path exists, but is not a directory.
	"""
	if not dir_path.exists():
		raise FileNotFoundError(f"{dir_path} does not exist.")

	if not dir_path.is_dir():
		raise NotADirectoryError(f"{dir_path} is not a directory.")

	if name_contains is None or name_contains == _EMPTY_STR:
		name_filter = lambda name: True
	else:
		name_contains_lower = name_contains.lower()
		name_filter = lambda name: name_contains_lower in name.lower()

	dir_tree_items = _explore_dir_tree_rec(
		dir_path, exclude_empty_dirs, name_filter, 0)

	return dir_tree_items


def _explore_dir_tree_rec(
		dir_path: Path,
		exclude_empty_dirs: bool,
		name_filter: FunctionType,
		depth: int
		) -> list[DirTreeItem]:
	"""
	This function called by explore_dir_tree recursively visits directories to
	represent their tree structure with a list of DirTreeItem objects.

	Argument name_filter is a function that takes a file's name as an argument
	and returns a Boolean. A file is included in the tree if and only if
	name_filter returns True.

	Args:
		dir_path: the path to a directory.
		exclude_empty_dirs: If True, the tree will exclude empty directories.
		name_filter: the function that decides to include files in the tree
			depending on their name.
		depth: the depth of dir_path in the directory tree. It should be set to
			0 when this function is first called.

	Returns:
		list: DirTreeItem objects representing dir_path's tree structure.
	"""
	dir_tree_items: list[DirTreeItem] = list()
	directories: list[Path] = list()

	depth += 1

	for item in dir_path.glob(_ASTERISK):
		if item.is_dir():
			directories.append(item)

		# The item is a file.
		elif name_filter(item.name):
			dir_tree_items.append(DirTreeItem(item, depth))

	for directory in directories:
		sub_dir_tree_items = _explore_dir_tree_rec(
			directory, exclude_empty_dirs, name_filter, depth)
		dir_tree_items.extend(sub_dir_tree_items)

	if not exclude_empty_dirs or len(dir_tree_items) > 0:
		dir_tree_items.insert(0, DirTreeItem(dir_path, depth-1))

	return dir_tree_items


__all__ = [explore_dir_tree.__name__]
