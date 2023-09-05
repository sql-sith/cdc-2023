import pyodbc

import pyodbc
DRIVER = "ODBC Driver 18 for SQL Server"
SERVER = "Caerdydd"
DATABASE = "AdventureWorks2022"

conn = pyodbc.connect(
    "Driver={ODBC Driver 18 for SQL Server};Server=Caerdydd;Database=AdventureWorks2022;" +
    "Trusted_Connection=yes;TrustServerCertificate=yes;Encrypt=yes"
)

cursor = conn.execute('SELECT * FROM HumanResources.Department ORDER BY name');

for row in cursor:
    print('row = %r' % (row,))

cursor.close()
conn.close()
