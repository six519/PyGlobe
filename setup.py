import pyglobe

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

setup(
	name='PyGlobe',
	version=pyglobe.__version__,
	description='Python interface for Globe Labs API',
	author='Ferdinand Silva',
	author_email='ferdinandsilva@ferdinandsilva.com',
	packages=['pyglobe'],
	install_requires=['suds'],
	url='https://github.com/six519/PyGlobe',
)
	
