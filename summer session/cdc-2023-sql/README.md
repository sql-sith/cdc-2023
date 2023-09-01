# SQL Server Client App in Python

We will build a tiny, toy Python application using Python. This will allow us to demonstrate why Little Bobby Tables is a bad boy, why stars are evil, and what you can do in your code to always, always, prevent SQL injection.

These are the steps I performed to prep my laptop for the 2023-08-31 class:

## SQL Server Configuration

1. Install [Microsoft ODBC Driver 18 for SQL Server](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16)
2. Install [SQL Server Developer Edition](https://www.microsoft.com/en-us/sql-server/sql-server-downloads)
3. Install [SQL Server Management Studio (SSMS)](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16&redirectedfrom=MSDN). We will use this as our query tool for SQL Server.
4. Download the AdventureWorks2022 sample OLTP database for SQL Server. To do this, go to [this page of downloads](https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver16&tabs=ssms) for SQL Server and find the download for OLTP databases that is labeled with "2022" in its name.
5. Connect to your local SQL Server using SSMS.

   - Search for **SQL Server Management Studio** in the Start Menu and select it.
   - When it presents you with a login dialog, enter the name of your computer as the **Server name**.
   - Leave the other fields as they are. In particular, you want to use Windows authentication.
   - Click the **Connect** button and you should see your SQL Server show up in the **Object Explorer** on the left-hand side of SSMS.
6. The AdventureWorks2000 file you downloaded is a database backup, so the next thing we need to do is restore the database that is contained in the backup file.

   - In SSMS, right-click your server's name in the Object Explorer and choose **New Query**. This should open a new query window.
   - In the query window, paste the following SQL. Then click on

   ```sql
   RESTORE DATABASE AdventureWorks2022 FROM DISK='C:\path\to\downloaded\file\AdventureWorks2022.bak';
   ```

   > If this command fails due to permissions, you need to move the file to a folder that is accessible to the SQL Server service. By default, if you create a root-level folder in Windows (such as 'c:\temp'), it should be readable by any user. So you can create a root-level folder, and then copy (copy, don't move) the backup file into that folder and try the restore command again, changing the file path in the command to point to the new location.
   >

## Python and PowerShell Configuration

1. Check your Python version by running `python --version`. Ensure that you are running a [supported version](https://devguide.python.org/versions/) of Python.

   > Python uses semantic versioning, where version `x.y.z` has major version `x`, minor version `y`, and patch level `z`. Major versions are increased when there are breaking changes to the product, so that not all scripts that ran on the older major version will run successully on the newer one. The minor version increases when new features are added, and the patch level changes when security remediations and bug fixes are applied.
   >
   > Python does not release major version upgrades very frequently, but minor version upgrades happen about once a year, with patch-level updates happening frequently.
   >
   > You should try to stay on a recent  releases new revisions fairly often, but you should try to stay on the You should always try to stay
   >
2. Run the following in an elevated PowerShell session to enable script execution

   The execution policy of your computer will allow you to run some of the python scripts we will need while we set up our project.

   > To start a PowerShell window with elevated permissions, click the Windows logo/Start button and search for PowerShell. When you find it, right-click it and choose _Run as administrator_.
   >

   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
   ```
3. Run the following in a normal (non-elevated) PowerShell session

```powershell
   mkdir cdc-2023-sql
   cd cdc-2023-sql

   # install required module for managing virtual environments.
   # typically you would use the venv module, but it's possible
   # for this to not be installed, and installing it is trickier
   # on some platforms. there are other products that help with
   # virtual environment management, including pyenv, poetry,
   # pipenv, pipx, asdf, and others. It's a big scary world out
   # there, so we'll just start with virtualenv.
   python -m pip install --upgrade --user virtualenv

   # create a virtual environment.
   # .venv is a common name for a virtual environment.
   python -m virtualenv .venv

   # activate the virtual environment.
   . ./.venv/Scripts/activate.ps1

   # verify that you are using the python from the virtual environment.
   Get-Command python # PowerShell

   # install module to enable use of ODBC providers from python.
   # this will allow us to connect to SQL Server, but it supports
   # connecting to other data sources also, such as mysql/mariadb.
   python -m pip install pyodbc
```

## Ready to Code!

At this point, we are ready to code. I have put a sample Python app in this folder. It is based on the script we got to work right at the end of class, but I cleaned it up a little.

## Deactivating Your Python Virtual Environment

Yeah, I forgot to tell you how to do this earlier, didn't I? To exit your virtual environment, reverting back to your default Python interpreter, just type the command `deactivate`. Virtual environments are only active inside the process that activates them, so if the command `deactivate` is unavailable, it may mean that you are not in the same PowerShell process where you activated the virtual environment.

Also, the fact that virtual environment settings are bound to a specific process means that they you have to re-activate your desired virtual environment every time you start PowerShell or any other process that uses virtual environments. The settings do not persist from one session to the next.
