import pyodbc


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


def display_query_results(cursor: pyodbc.Cursor):
    print('\n', end='')

    coldefs = cursor.description
    colmeta = {}
    for colidx in range(len(coldefs)):
        col = coldefs[colidx]
        colmeta[colidx] = {
            "name": col[0],
            "width": col[4] if col[4] > len(col[0]) else len(col[0])
            }

    for id in colmeta.keys():
        meta = colmeta[id]
        print(f'{meta["name"]:<{meta["width"]}} ', end='')
    print('\n', end='')

    for id in colmeta.keys():
        meta = colmeta[id]
        print("-" * meta["width"] + ' ', end='')
    print('\n', end='')

    for row in cursor:
        for id in colmeta.keys():
            print(f"{str(row[id]):<{colmeta[id]['width']}} ", end='')
        print('\n', end='')

    print('\n', end='')


def get_connection(driver: str, server: str, database: str) -> pyodbc.Connection:
    return pyodbc.connect(
        f"Driver={{{driver}}};"
        f"Server={server};"
        f"Database={database};"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
        "Encrypt=yes"
        )


def execute_query(connection: pyodbc.Connection, query: str):
    cursor = connection.cursor().execute(query)
    display_query_results(cursor)
    cursor.close()


if __name__ == '__main__':
    conn = get_connection(DRIVER, SERVER, DATABASE)
    execute_query(conn, VERY_PLAIN_MANUFACTURING_QUERY)
    execute_query(conn, SEMI_CRAZY_SALES_QUERY)
    conn.close()
