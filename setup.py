from setuptools import setup, find_packages
from os import path

working_directory = path.abspath(path.dirname(__file__))

with open(path.join(working_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='main_report_Alex_Drob',
    version='0.0.1',
    # url='https://git.foxminded.ua/foxstudent107281/monaco_racing_report',
    author='Alex Drob',
    author_email='lackingabrain@gmail.com',
    description='My own package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[]
)
url = 'https://git.foxminded.ua/foxstudent107281/monaco_racing_report'
