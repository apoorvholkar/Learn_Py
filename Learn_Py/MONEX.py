#! /usr/bin/python

from urllib import urlopen
from bs4 import BeautifulSoup
import pymssql
import datetime
import _mssql
import decimal
import uuid

# Copy all of the content from the provided web page
url='http://www.mnse.me/code/navigate.asp?Id=59'

webpage = urlopen(url).read()

soup = BeautifulSoup(webpage)

tableData = soup.findAll("div",{"class":"float_block"})
for i in tableData:
    soup1 = BeautifulSoup(str(i))
    indexData1 = soup1.findAll("h1")
    for j in indexData1:
        if j.get_text() == "Index MONEX":
            for k in i.find_all("td")[0]:
                tradeDate = k.get_text()
            for k in i.find_all("td")[2]:
                indexValue = k.get_text()

tradeDate1 =  tradeDate[-10:]
indexValue1 = float(indexValue.replace(".","dot").replace(",","comma").replace("dot","").replace("comma","."))            


conn = pymssql.connect(host='unicorn3', user='sa', password='Passw0rd', database='df1')

cur = conn.cursor()

cur.execute('select top 1 CONVERT(VARCHAR(10),date,103) from df1.dbo.Bloomberg_market_dat where variable_number= 1502 order by date desc')

row = cur.fetchone()

while row:
    DBdate =  (row[0])
    row = cur.fetchone()

cur.execute("select max(revision) from df1.dbo.revision_set where open_remarks like 'df1.dbo.Bloomberg_market_dat, df1.dbo.Bloomberg_market_ent'")

row = cur.fetchone()

while row:
    revisionNo =  (row[0])
    row = cur.fetchone()
    
'''
print "DBdate " ,DBdate
print "Trade Date ",tradeDate1
print "Index Value ", indexValue1
print "Revision", revisionNo
'''
revisionNo1= int(revisionNo)
tradeDate2 = datetime.datetime.strptime(tradeDate1,'%d/%m/%Y')

if DBdate != tradeDate1:
    sql_command = "insert into df1.dbo.Bloomberg_market_dat values(%d,%s,%d,%d,%d)"
    cur.execute(sql_command,(1502,tradeDate2,indexValue1,1,revisionNo1))
else:
    print "data already present"
conn.commit()    
conn.close()
   
