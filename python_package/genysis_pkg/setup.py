
#BUILD AND INSTALL (run these two lines form the CMD line)
#python setup.py sdist bdist_wheel --universal
#twine upload dist/*

from setuptools import setup
setup(name='genysis',
      version='0.1.1',
      description='generative design lattive design',
      url='https://github.com/francisbitontistudio/genysis_pythonPKG.git',
      author='F. Bitonti',
      author_email='francis@studiobitonti.com',
      license='MIT',
      packages=['genysis'],
      install_requires=['requests>=2.18.4',
                        'json>=2.0.9',
                        'ast>=82160']
      )
