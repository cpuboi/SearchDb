from setuptools import setup, find_packages

setup(
    name='SearchDb',
    version='1.0.0',
    license='GPLv2',
    author='cpuboi',
    description="Python dictionary backed by SQLite, includes fast text search and more advanced data structures",
    url='https://github.com/cpuboi/SearchDb',
    keywords=['SQLite', 'dictionary', 'text search'],
    packages=find_packages(),
    classifiers=['Development Status :: 4 - Beta'],
    python_requires='>=3.9', # Older might work, have not tested
)