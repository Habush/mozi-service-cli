__author__ = 'Abdulrahman Semrie<hsamireh@gmail.com>'

from setuptools import setup

setup(
    name="Mozi Service CLI",
    version="1.0",
    author="Abdulrahman Semrie",
    author_email="hsamireh@gmail.com",
    descirption="A cli tool that will prepare a json file which can be used to call the MOSES SNET Service",
    py_modules=["mozi_cli"],
    install_requires=[
        "Click",
    ],
    entry_points="""
        [console_scripts]
        mozi-cli=mozi_cli:cli
    """
)