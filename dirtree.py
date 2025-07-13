"""
This application writes a directory tree's representation in a text file.
"""


from sys import exit

from src import\
	make_arg_parser,\
	write_dir_tree


if __name__ == "__main__":
	args = make_arg_parser(__doc__).parse_args()
	contains = args.contains
	exclude_empty_dirs = args.exclude_empty
	dir_path = args.directory.resolve()
	output_file = args.output

	try:
		write_dir_tree(output_file, dir_path, exclude_empty_dirs, contains)
	except (FileNotFoundError, NotADirectoryError) as error:
		print(f"{error.__class__.__name__}: {error}")
		exit(1)
