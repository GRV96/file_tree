from pathlib import Path


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
