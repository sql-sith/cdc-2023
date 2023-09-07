import pyodbc


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


def execute_query(connection: pyodbc.Connection, query: str):
    cursor = connection.cursor().execute(query)
    display_query_results(cursor)
    cursor.close()


def execute_query_with_parameters(connection: pyodbc.Connection, query: str, parameter_list: list[any]):
    cursor = connection.cursor().execute(query, parameter_list)
    display_query_results(cursor)
    cursor.close()

def get_connection(driver: str, server: str, database: str) -> pyodbc.Connection:
    return pyodbc.connect(
        f"Driver={{{driver}}};"
        f"Server={server};"
        f"Database={database};"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
        "Encrypt=yes"
        )
