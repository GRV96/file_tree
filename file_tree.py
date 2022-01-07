"""
Writes a directory's file structure in a text file.
"""


from argparse import ArgumentParser
from pathlib import Path


class FileRecord:
	"""
	This class represents a file found in a directory tree structure.
	"""

	def __init__(self, path, depth):
		"""
		The constructor needs the file's path and its depth in the tree
		structure. The root's depth is 0.

		Args:
			path (pathlib.Path): the file's path
			depth (int): the file's depth in the directory tree structure
		"""
		self._path = path
		self._depth = depth

	@property
	def depth(self):
		"""
		int: this file's depth in the directory tree structure
		"""
		return self._depth

	@property
	def path(self):
		"""
		pathlib.Path: this file's path
		"""
		return self._path


def explore_dir_tree(dir_path):
	"""
	This function visits all ramifications of a directory tree structure and
	represents it with a list of FileRecord objects.

	Args:
		dir_path (pathlib.Path): the path to the root directory

	Returns:
		list: FileRecord objects that make a representation of the directory
			tree structure
	"""
	file_records = list()
	_explore_dir_tree_rec(dir_path, file_records, 0)
	return file_records


def _explore_dir_tree_rec(dir_path, file_recs, depth):
	"""
	This function called by explore_dir_tree recursively visits directories to
	represent their tree structure with a list of FileRecord objects.

	Args:
		dir_path (pathlib.Path): the path to the root directory
		file_recs (list): The FileRecord objects generated throughout the
			exploration are appended to this list.
		depth (int): the depth of dir_path in the directory tree. It should be
			set to 0 on the initial call to this function.
	"""
	file_recs.append(FileRecord(dir_path, depth))
	depth += 1

	files = list(dir_path.glob("*"))
	files.sort()

	for file in files:
		if file.is_dir():
			_explore_dir_tree_rec(file, file_recs, depth)

		else:
			file_recs.append(FileRecord(file, depth))


def _make_parser():
	parser = ArgumentParser(description=__doc__)

	parser.add_argument("-d", "--directory", type=Path, default=None,
		help="Path to the directory to explore")

	parser.add_argument("-o", "--output", type=Path, default=None,
		help="Path to the .txt file that will contain the tree structure.")

	return parser


if __name__ == "__main__":
	_NEW_LINE = "\n"
	_TAB = "\t"

	parser = _make_parser()
	args = parser.parse_args()

	dir_path = args.directory
	dir_path = dir_path.resolve() # Conversion to an absolute path

	output_path = args.output

	file_records = explore_dir_tree(dir_path)

	with output_path.open(mode="w", encoding="utf-8") as output_stream:
		output_stream.write(str(dir_path) + _NEW_LINE)

		for file_record in file_records[1:]:
			output_stream.write(
				_TAB * file_record.depth + file_record.path.name + _NEW_LINE)
