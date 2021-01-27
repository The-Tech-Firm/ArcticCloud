import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name = "ArcticCloud",
    version = "1.0.1",
    author = "Apurba Ghosh",
    author_email = "new.to.world2003@gmail.com",
    description = "A Library containing modules for Daily tasks",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Stark-Corp/ArcticCloud/",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        
    ],
    python_requires = ">= 3.6",
)