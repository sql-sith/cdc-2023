import pyodbc 
import sys

DRIVER = "ODBC Driver 18 for SQL Server"
SERVER = "Caerdydd"
DATABASE = "AdventureWorks2022"

QUERY_REPLACE_TOKEN = '[REPLACEME]'


DEPARTMENT_GROUP_LIST = f" \
    SELECT DISTINCT d.GroupName \
    FROM HumanResources.Department AS d \
    ORDER BY d.GroupName"

DEPARTMENT_GROUP_FILTER = f" \
    SELECT d.DepartmentID, d.Name \
    FROM HumanResources.Department AS d \
    WHERE d.GroupName = '{QUERY_REPLACE_TOKEN}' \
    ORDER BY d.GroupName \
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
    cur = connection.cursor().execute(query)
    display_query_results(cur)
    cur.close()


if __name__ == '__main__':
    conn = get_connection(DRIVER, SERVER, DATABASE)

    '''
        examples:
            ' UNION ALL SELECT 1, 'hi, guys!!!'; RETURN --
            ' UNION ALL SELECT BusinessEntityId, FirstName + ' ' + LastName FROM Person.Person; RETURN --
            ' UNION ALL SELECT BusinessEntityId, FirstName + ' ' + LastName FROM Person.Person ORDER BY 1; RETURN --
                (or ORDER BY DepartmentID)
                (a better solution would want a subquery)
            make one more with a join to show how you can include info from multiple columns from multiple tables,
                even though there are only two columns to squish your recon info into.
            then make a parameterized version of this and talk about why that works.
    '''
    try:
        while True:
            print('\nHere is the list of department groups:\n')
            execute_query(conn, DEPARTMENT_GROUP_LIST)
            print('')

            department_group = input("Enter one of the department group names from the list above (ENTER to exit): ")
            if not department_group:
                break

            query = DEPARTMENT_GROUP_FILTER.replace(QUERY_REPLACE_TOKEN, department_group)
            # print(f"Executing query {query}...")
            execute_query(conn, query)
    except pyodbc.ProgrammingError:
        _, value, _ = sys.exc_info()
        print(f'Error running query: {value.strerror}.')
        print('Continuing to next loop iteration.')
    finally:
        conn.close()
