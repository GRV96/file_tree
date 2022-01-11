from pathlib import Path
from sys import exit

from jazal import\
	MissingPathArgWarner,\
	make_altered_name


_ERROR_INTRO = "ERROR! "


def check_dir_path(arg_name, dir_path):
	missing_path_warner = MissingPathArgWarner(arg_name, "")

	if dir_path is None:
		print(_ERROR_INTRO + missing_path_warner.make_missing_arg_msg())
		exit(1)

	try:
		path_checker = missing_path_warner.make_reactive_path_checker(dir_path)
		path_checker.check_path_exists()
		path_checker.check_path_is_dir()
		path_checker.check_extension_correct()

	except Exception as e:
		print(_ERROR_INTRO + str(e))
		exit(1)


def check_output_path(arg_name, output_path, extension, dir_path):
	missing_path_warner = MissingPathArgWarner(arg_name, extension)

	if output_path is None:
		output_path = Path.cwd()/make_altered_name(dir_path,
			after_stem=" file tree", extension=missing_path_warner.extension)

	else:
		path_checker =\
			missing_path_warner.make_reactive_path_checker(output_path)

		if path_checker.path_is_dir():
			output_path = output_path/make_altered_name(
				dir_path, after_stem=" file tree",
				extension=missing_path_warner.extension)

		else:
			try:
				path_checker.check_extension_correct()

			except ValueError as e:
				print(_ERROR_INTRO + str(e))
				exit(1)

	return output_path
