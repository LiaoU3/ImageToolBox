import setuptools

with open("README.md","r") as fh:
    long_description = fh.read()

setuptools.setup(
	name = "ImgToolBox",
	version = "1.6.0",
	author = "LiaoU3",
	author_email = "vincent932693@gmail.com",
	description = "A package about the transformations between raw, csv and numpy array",
	long_description=long_description,
	long_description_content_type = "text/markdown",
	url = "https://github.com/LiaoU3/ImageToolBox.git",
	packages = setuptools.find_packages(),
	classifiers =   ["Programming Language :: Python :: 3",
					"License :: OSI Approved :: MIT License",
					"Operating System :: OS Independent",],)
