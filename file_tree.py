from argparse import ArgumentParser
from pathlib import Path


def _make_parser():
	parser = ArgumentParser()

	parser.add_argument("-d", "--directory", type=Path, default=None,
		help="Path to the directory to explore")

	parser.add_argument("-o", "--output", type=Path, default=None,
		help="Path to the .txt file that will contain the tree structure.")

	return parser


if __name__ == "__main__":
	parser = _make_parser()
	args = parser.parse_args()

	directory = args.directory
	output_path = args.output

	print(type(directory), directory)
	print(type(output_path), output_path)
