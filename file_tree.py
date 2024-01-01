"""
Writes a directory's file structure in a text file.
"""


from argparse import ArgumentParser
from pathlib import Path


_ASTERISK = "*"
_DIR_MARK = "[DIR] "
_EMPTY_STR = ""
_NEW_LINE = "\n"
_TAB = "\t"


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


def explore_dir_tree(dir_path, include_empty_dirs, name_contains=None):
	"""
	This function visits all ramifications of a directory tree structure and
	represents it with a list of FileRecord objects. If argument name_contains
	is provided, the directory tree will include only files whose name contains
	the argument.

	Args:
		dir_path (pathlib.Path): the path to the root directory
		include_empty_dirs (bool): If True, the tree will include empty
			directories.
		name_contains (str): filters the files if it is not None or an empty
			string. Defaults to None.

	Returns:
		list: FileRecord objects that make a representation of the directory
			tree structure
	"""
	if name_contains is None or name_contains == _EMPTY_STR:
		name_filter = lambda name: True
	else:
		name_filter = lambda name: name_contains in name

	file_records = list()
	_explore_dir_tree_rec(
		dir_path, file_records, include_empty_dirs, name_filter, 0)
	return file_records


def _explore_dir_tree_rec(
		dir_path, file_recs, include_empty_dirs, name_filter, depth):
	"""
	This function called by explore_dir_tree recursively visits directories to
	represent their tree structure with a list of FileRecord objects. Function
	name_filter takes each file's name as an argument and returns a Boolean. A
	file is included in the tree if and only if name_filter returns True.

	Args:
		dir_path (pathlib.Path): the path to a directory
		file_recs (list): The FileRecord objects generated throughout the
			exploration are appended to this list.
		include_empty_dirs (bool): If True, the tree will include empty
			directories.
		name_filter (function): the function that decides to include files in the
			tree depending on their name
		depth (int): the depth of dir_path in the directory tree. It should be
			set to 0 on the initial call to this function.
	"""
	file_recs.append(FileRecord(dir_path, depth))
	depth += 1

	dir_content = list(dir_path.glob(_ASTERISK))
	dir_content.sort()
	dirs = list()
	nb_files_included = 0

	for file in dir_content:
		if file.is_dir():
			dirs.append(file)

		elif name_filter(file.name):
			file_recs.append(FileRecord(file, depth))
			nb_files_included += 1

	for dir in dirs:
		inclusions = _explore_dir_tree_rec(
			dir, file_recs, include_empty_dirs, name_filter, depth)
		nb_files_included += inclusions

	if not include_empty_dirs and nb_files_included < 1:
		file_recs.pop()

	return nb_files_included


def _file_record_to_str(file_record):
	file_rec_str = _TAB * file_record.depth

	if file_record.path.is_dir():
		file_rec_str += _DIR_MARK

	file_rec_str += file_record.path.name + _NEW_LINE

	return file_rec_str


def _make_parser():
	parser = ArgumentParser(description=__doc__)

	parser.add_argument("-c", "--contains", type=str, default=None,
		help="Only include files whose name contains this argument.")

	parser.add_argument("-d", "--directory", type=Path, default=None,
		help="Path to the directory to explore")

	parser.add_argument("-e", "--exclude-empty", action="store_true",
		help="This flag excludes empty directories from the file tree.")

	parser.add_argument("-o", "--output", type=Path, default=None,
		help="Path to the .txt file that will contain the tree structure.")

	return parser


if __name__ == "__main__":
	parser = _make_parser()
	args = parser.parse_args()

	contains = args.contains

	dir_path = args.directory
	dir_path = dir_path.resolve() # Conversion to an absolute path

	include_empty_dirs = not args.exclude_empty

	output_path = args.output

	file_records = explore_dir_tree(dir_path, include_empty_dirs, contains)

	with output_path.open(mode="w", encoding="utf-8") as output_stream:
		output_stream.write(str(dir_path) + _NEW_LINE)

		for file_record in file_records[1:]:
			output_stream.write(_file_record_to_str(file_record))
