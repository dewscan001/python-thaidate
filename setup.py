from setuptools import setup, find_packages

def readme():
    with open('README.md', 'r', encoding='utf8', ) as f:
        return f.read()

setup(name='thaidate',
    version='0.1.0',
    description='python-thaidate',
    author='DewBloodmetal',
    author_email='dewscan001@gmail.com',
    license='DewBloodmetal',
    install_requires=[''],
    keywords='python thaidate python-thaidate',
    long_description=readme(),
    long_description_content_type='text/markdown'
)