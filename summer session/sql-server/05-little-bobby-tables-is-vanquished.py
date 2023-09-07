import sys
from util import *

DRIVER = "ODBC Driver 18 for SQL Server"
SERVER = "Caerdydd"
DATABASE = "AdventureWorks2022"

DEBUG = True

DEPARTMENT_GROUP_LIST = f" \
    SELECT DISTINCT d.GroupName \
    FROM HumanResources.Department AS d \
    ORDER BY d.GroupName"

DEPARTMENT_GROUP_FILTER = f" \
    SELECT d.DepartmentID, d.GroupName, d.Name \
    FROM HumanResources.Department AS d \
    WHERE d.GroupName = ? \
    ORDER BY d.GroupName \
    "


if __name__ == '__main__':
    conn = get_connection(DRIVER, SERVER, DATABASE)

    '''
        examples:
            ' UNION ALL SELECT 42, 'hi, guys!!!', 'i''m a big fan and i''m mocking YOU!!!'; RETURN --
            ' UNION ALL SELECT BusinessEntityId, FirstName + ' ' + LastName FROM Person.Person; RETURN --
            ' UNION ALL SELECT BusinessEntityId, FirstName + ' ' + LastName FROM Person.Person ORDER BY 1; RETURN --
            ' UNION ALL      SELECT d.DepartmentID, d.GroupName, d.Name     FROM HumanResources.Department AS d     WHERE d.GroupName = 'WITH XMLNAMESPACES ('http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/StoreSurvey' as awss) SELECT TOP(25) 0, LEFT(s.Name, 50) + ':' + LEFT(p.FirstName + ' ' + p.LastName, 30)  + ':' + cast(store.x.value(N'./awss:AnnualRevenue', N'int') AS varchar(max)) + ':' + store.x.value(N'awss:YearOpened', N'varchar(23)') + ':' + cast(store.x.value(N'awss:NumberEmployees', N'int') AS varchar(23)), NULL FROM sales.store AS s JOIN Person.Person AS p ON s.SalesPersonID = p.BusinessEntityID CROSS APPLY s.Demographics.nodes('(awss:StoreSurvey)[1]') AS store(x) ORDER BY 2; RETURN; --

                (or ORDER BY DepartmentID)
                (a better solution would want a subquery)
            make one more with a join to show how you can include info from multiple columns from multiple tables,
                even though there are only two columns to squish your recon info into.
            then make a parameterized version of this and talk about why that works.
    '''
    try:
        while True:
            print('\nHere is the list of department groups:')
            execute_query(conn, DEPARTMENT_GROUP_LIST)
            department_group = input("Enter one of the department group names from the list above (ENTER to exit): ")

            if not department_group:
                break
            print(f'Here are the departments within department group {department_group}:')

            execute_query_with_parameters(conn, DEPARTMENT_GROUP_FILTER, [department_group])
    except pyodbc.ProgrammingError:
        _, value, _ = sys.exc_info()
        print(f'Error running query: {value}.')
        print('Continuing to next loop iteration.')
    finally:
        conn.close()
