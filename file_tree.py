"""
This script writes a directory tree's representation in a text file.
"""


from sys import exit

from src import\
	explore_dir_tree,\
	make_arg_parser


_NEW_LINE: str = "\n"


if __name__ == "__main__":
	args = make_arg_parser().parse_args()
	contains = args.contains
	exclude_empty_dirs = args.exclude_empty
	dir_path = args.directory.resolve()
	output_path = args.output

	try:
		dir_tree_items = explore_dir_tree(dir_path, exclude_empty_dirs, contains)
	except (FileNotFoundError, NotADirectoryError) as error:
		print(f"{error.__class__.__name__}: {error}")
		exit(1)

	with output_path.open(mode="w", encoding="utf-8") as output_stream:
		output_stream.write(str(dir_path) + _NEW_LINE)

		for dir_tree_item in dir_tree_items[1:]:
			item_as_str = str(dir_tree_item) + _NEW_LINE
			output_stream.write(item_as_str)
