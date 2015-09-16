import pyodbc
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=unicorn4;DATABASE=Test;Trusted_Connection=yes')
cursor = cnxn.cursor()
cursor.execute("select top 10 ID_BB_COMPANY,COMPANY_ID from TEST.dbo.security_information")
rows = cursor.fetchall()
for row in rows:
    print row.ID_BB_COMPANY, row.COMPANY_ID


