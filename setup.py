import setuptools


_ENCODING_UTF8 = "utf-8"
_MODE_R = "r"


def _make_descriptions():
	with open("README.md", _MODE_R, encoding=_ENCODING_UTF8) as readme_file:
		readme_content = readme_file.read()

	title_fr = "## FRANÇAIS"
	title_en = "## ENGLISH"

	index_fr = readme_content.index(title_fr)
	index_end_fr = readme_content.index("Il est possible")

	index_en = readme_content.index(title_en)
	index_desc_en = index_en + len(title_en)
	index_desc_end_en = readme_content.index(
		"A directory tree contains", index_desc_en)
	index_end_en = readme_content.index("It is possible", index_desc_end_en)

	short_description = readme_content[index_desc_en: index_desc_end_en]
	short_description = short_description.replace("\n", " ")
	short_description = short_description.replace("`", "")
	short_description = short_description.strip()

	long_description = readme_content[index_fr: index_end_fr]\
		+ readme_content[index_en:index_end_en].strip()

	return short_description, long_description


if __name__ == "__main__":
	short_desc, long_desc = _make_descriptions()

	setuptools.setup(
		name = "dirtree",
		version = "0.0.0",
		author = "Guyllaume Rousseau",
		description = short_desc,
		long_description = long_desc,
		long_description_content_type = "text/markdown",
		url = "https://github.com/GRV96/dirtree",
		classifiers = [
			"Development Status :: 5 - Production/Stable",
			"Intended Audience :: Developers",
			"Intended Audience :: End Users/Desktop",
			"License :: OSI Approved :: MIT License",
			"Operating System :: OS Independent",
			"Programming Language :: Python :: 3",
			"Topic :: System :: Filesystems",
			"Topic :: Utilities"
		],
		#packages = setuptools.find_packages(),
		license = "MIT",
		license_files = ("LICENSE",))
