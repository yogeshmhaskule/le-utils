from setuptools import setup


with open('README.md') as file:
    long_description = file.read()


setup(
    name="le-utils",
    packages=["le_utils"],
    version="0.0.3",
    description="LE Utils and constants shared across Kolibri, Ricecooker and the Content Curation Server.",
    long_description=long_description,
    license="MIT",
    url="https://github.com/learningequality/le-utils",
    download_url="https://github.com/learningequality/le-utils/tarball/0.0.3",
    keywords="le-utils le_utils le utils kolibri ricecooker content curation",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Topic :: Utilities",
    ],
    author="Jordan Yoshihara",
    author_email="jordan@learningequality.org",
)
