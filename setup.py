from setuptools import find_packages,setup


setup(

    name='ML_project',
    version='0.1',
    author='Areeba',
    author_email='areebaofficials@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
)