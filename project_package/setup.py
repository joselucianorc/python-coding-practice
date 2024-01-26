from setuptools import find_packages, setup

setup(
    name="mypackage",
    version="0.0.1",
    author_email="joselucianorc.developer@gmail.com"
    packages=find_packages(),
    url="https://github.com/joselucianorc/mypackage.git"
    license="MIT",
    description="This is my package.",
    long_description=open("README.rst").read(),
    install_requires=[]
)