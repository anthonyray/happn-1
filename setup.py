from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='happn',
		version='0.1',
		description='Package for interacting with the Happn API',
		url='http://github.com/rickhousley/happn',
		author='Rick Housley',
		author_email='RickyHousley+github@gmail.com',
		license='MIT',
		packages=['happn'],
		scripts=['bin/funniest-joke'],
		install_requires = ['requests', 'logging', 'json']], #urllib2 alread pre-packaged
		zip_safe=False)
