__author__="collinbrooks"
__date__ ="$Sep 10, 2009 8:39:26 PM$"

from distutils.core import setup

setup(
    name='PyroSync',
    version='0.1.0',
    author='Collin D. Brooks',
    author_email='collin.brooks@gmail.com',
    packages=['pyrosync'],
    scripts=[],
    url='https://github.com/cobhimself/PyroSync',
    license='LICENSE.txt',
    description='Rsync wrapper that allows the saving of preset synchronizations.',
    long_description=open('README.txt').read(),
)

