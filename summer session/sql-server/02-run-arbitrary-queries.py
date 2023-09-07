from util import *

DRIVER = "ODBC Driver 18 for SQL Server"
SERVER = "Caerdydd"
DATABASE = "AdventureWorks2022"

VERY_PLAIN_MANUFACTURING_QUERY = " \
    SELECT d.DepartmentID, d.Name \
    FROM HumanResources.Department AS d \
    WHERE d.GroupName = 'Manufacturing' \
    ORDER BY d.DepartmentId \
    "

SEMI_CRAZY_SALES_QUERY = " \
    WITH XMLNAMESPACES ('http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/StoreSurvey' as awss) \
    SELECT TOP(25) \
        LEFT(s.Name, 50) AS Store \
        , LEFT(p.FirstName + ' ' + p.LastName, 30) AS Salesperson \
        , store.x.value(N'./awss:AnnualRevenue', N'int') AS AnnualRevenue \
        , store.x.value(N'awss:YearOpened', N'varchar(8)') AS YearOpened \
        , store.x.value(N'awss:NumberEmployees', N'int') AS Employees \
    FROM sales.store AS s \
    JOIN Person.Person AS p \
        ON s.SalesPersonID = p.BusinessEntityID \
    CROSS APPLY s.Demographics.nodes('(awss:StoreSurvey)[1]') AS store(x) \
    ORDER BY Store \
    "


if __name__ == '__main__':
    conn = get_connection(DRIVER, SERVER, DATABASE)
    execute_query(conn, VERY_PLAIN_MANUFACTURING_QUERY)
    execute_query(conn, SEMI_CRAZY_SALES_QUERY)
    conn.close()
