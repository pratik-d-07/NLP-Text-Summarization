import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "NLP-Text-Summarization"
AUTHOR_USER_NAME = "pratik-d-07"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "pvdahale7@gmail.com"

setuptools.setup (
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    email = AUTHOR_EMAIL,
    description = "A small Python Package",
    long_description = long_description,
    long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where = "src")    
)


