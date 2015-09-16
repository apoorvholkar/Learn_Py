import pyodbc
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=unicorn4;DATABASE=TIER2;Trusted_Connection=yes')
cursor = cnxn.cursor()
cursor.execute("EXECUTE TIER2.PROD.SP_USDSWAP_retrieval")
rows = cursor.fetchall()
#for row in rows:
print rows[0].DATA_DATE,rows[0].USSW1_Curncy,rows[0].USSW2_Curncy,rows[0].USSW3_Curncy,rows[0].USSW4_Curncy,rows[0].USSW5_Curncy,rows[0].USSW6_Curncy


