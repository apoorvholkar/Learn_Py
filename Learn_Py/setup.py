from distutils.core import setup
import py2exe
import _mssql
from urllib import urlopen
from bs4 import BeautifulSoup
import pymssql
import decimal
import uuid


setup(console=['MONEX.py'])