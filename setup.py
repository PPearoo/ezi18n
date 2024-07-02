from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.4'
DESCRIPTION = 'A custom i18n implementation that is built to be easily used.'

# Setting up
setup(
    name="ezi18n",
    version=VERSION,
    author="Pearoo",
    author_email="<contact@pearoo.hu>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'i18n', 'translation', 'localisation', 'localization'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)