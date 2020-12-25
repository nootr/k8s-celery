from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='myapp',
    version='0.1',
    description='A trivial Celery app',
    long_description=long_description,
    author='Joris Hartog',
    author_email='jorishartog@hotmail.com',
    long_description_content_type='text/markdown',
    packages=find_packages(),
    scripts=['run_myapp.py'],
    install_requires=[
        'flask',
        'celery',
    ],
)

