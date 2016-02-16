"""
dataserviceclient setup installation script
@author: benjaminneely
"""
from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='dataserviceclient',
      version='0.1',
      description='Data Service at Duke Client',
      url='https://github.com/Duke-Translational-Bioinformatics/duke-data-service-pythonClient',
      author='Benjamin Neely',
      author_email='nigelneely@gmail.com',
      license='GNU General Public License v3 (GPLv3)',
      packages=['dataserviceclient'],
      install_requires=[         
      ],
      entry_points = {
        'console_scripts': ['dataserviceclient=dataserviceclient.command_line:main'],
      },
      zip_safe=False)

