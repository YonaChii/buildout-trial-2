from setuptools import setup, find_packages
 
setup(
  name='test',
  version= "1.0",
  description='trying 2nd tutorial',
  author='Yona',
  packages= find_packages('src'),
  package_dir={ '' : 'src' },
  install_requires = ['django == 1.5.5'],
)
