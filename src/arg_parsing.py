from argparse import ArgumentParser
from pathlib import Path


def make_arg_parser() -> ArgumentParser:
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


__all__ = [make_arg_parser.__name__]
