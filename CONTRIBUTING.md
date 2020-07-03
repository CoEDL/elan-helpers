# Contribution guide

1. Create a new folder in the top level
	- Use lower case, hyphen-separated words, e.g. `header-extractor`

2. Place your script(s) in the that folder, e.g. `header-extractor/extract.py`

3. Add all dependencies into a `dist` folder, e.g. `header-extractor/dist/some-dependency.py`

4. Include a `README.md` in the root of your script folder, e.g. `header-extractor/README.md`, specifying
	1. the usage environment (e.g. Python 3.6 + numpy + Libxml2)
	2. usage instructions (e.g. `python extract.py infile.cha outfile.csv`)

5. Ideally, also include dummy or sample files to show a minimal working example of script.
