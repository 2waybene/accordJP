from setuptools import setup, find_packages
from codecs import open
from os import path

__version__ = '0.0.1'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# get the dependencies and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if x.startswith('git+')]

setup(
    name='accordJP',
    version=__version__,
    description='This project is to help Dr. Motsinger-Reif for her accord clinical trial project pipeline automation.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/2waybene/accordJP',
    download_url='https://github.com/2waybene/accordJP/tarball/' + __version__,
    license='BSD',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
    ],
    keywords='',
    #packages=find_packages(exclude=['docs', 'tests*']),
    packages=find_packages(include=['docs', 'tests*', 'accordJP']),
    include_package_data=True,
    author='Jianying Li',


    install_requires=install_requires,
    dependency_links=dependency_links,
    author_email='jianying.li@gmail.com',



    entry_points='''
        [console_scripts]
        accordJP=accordJP.cli:main
    ''',


)
