#! /usr/bin/python

from urllib import urlopen
from bs4 import BeautifulSoup
import pymssql
import datetime
import _mssql
import decimal
import uuid

# Copy all of the content from the provided web page
url='http://www.bvl.com.pe/mercindiceshoy.html'

webpage = urlopen(url).read()

soup = BeautifulSoup(webpage)

print soup

