from pathlib import Path


_DIRECTORY_MARK: str = "[DR] "
_TAB: str = "\t"


class DirTreeItem:
	"""
	A directory tree item is a directory or a file.
	"""

	def __init__(self, path: Path, depth: int) -> None:
		"""
		The initializer needs the item's path and its depth in the directory
		tree. The root's depth should be 0.

		Args:
			path: the item's path.
			depth: the item's depth in the directory tree.
		"""
		self._path = path
		self._depth = depth

	def __str__(self) -> str:
		"""
		This method creates a string meant to be part of a directory tree
		representation in a text file. The string will consist of a number of
		tabulations equivalent to this item's depth in the tree and this item's
		name. If this item is a directory, mark [DR] will precede its name.

		Returns:
			str: this directory tree item's string representation.
		"""
		item_path = self._path
		item_str = _TAB * self._depth

		if item_path.is_dir():
			item_str += _DIRECTORY_MARK

		item_str += item_path.name

		return item_str

	@property
	def depth(self) -> int:
		"""
		This item's depth in the directory tree.
		"""
		return self._depth

	@property
	def path(self) -> Path:
		"""
		This item's path.
		"""
		return self._path


__all__ = [DirTreeItem.__name__]
