from setuptools import setup


setup(name='basic',
      version='0.2',
      description='Package with basic utilities for dummies',
      url='http://github.com/decordoba/basic-python',
      author='Daniel de Cordoba Gil',
      author_email='danidecordoba@gmail.com',
      license='MIT',
      packages=['basic'],
      install_requires=[
          'matplotlib'
      ],
      zip_safe=False)