import pymssql



cur = conn.cursor()

'''
cur.execute('CREATE TABLE persons(id INT, name VARCHAR(100))')
cur.executemany("INSERT INTO persons VALUES(%d, %s)", \
    [ (1, 'John Doe'), (2, 'Jane Doe') ])
conn.commit()  # you must call commit() to persist your data if you don't set autocommit to True
'''


cur.execute('select top 1 * from df1.dbo.Bloomberg_market_dat where variable_number= 1502 order by date desc')

row = cur.fetchone()

while row:
    DBdate =  (row[1])
    row = cur.fetchone()
    
    
cur.execute("insert into df1.dbo.Bloomberg_market_dat(variable) values ('pyodbc', 'awesome library')")
conn.commit()

    
conn.close()


print DBdate