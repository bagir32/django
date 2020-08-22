# Django
Learn django framwork

## Installing xampp: 
https://blog.templatetoaster.com/install-xampp-on-windows/

## Start XAMPP on linux
```
sudo /opt/lampp/lampp status
```
## mysql database as backend database using xmapp:
http://localhost/phpmyadmin

## When using power shell make sure to set Execution Policy as:
```
Set-ExecutionPolicy AllSigned -Scope CurrentUser -Force
Set-ExecutionPolicy Bypass -Scope CurrentUser -Force
Set-ExecutionPolicy Default -Scope CurrentUser -Force
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
Set-ExecutionPolicy Restricted -Scope CurrentUser -Force
Set-ExecutionPolicy Undefined -Scope CurrentUser -Force
Set-ExecutionPolicy Unrestricted -Scope CurrentUser -Force
```

<br />
link: https://www.tenforums.com/tutorials/54585-change-powershell-script-execution-policy-windows-10-a.html

## To Start new project in Django use this command:
```
django-admin startproject project-name
```

## To test your Django project run the test server using this command:
```
python3 manage.py runserver
```

The output shoud show you the URL of Project's homepage and listening port like:
<br />
http://localhost:8000

## How I fixed the problem of failing to install mysqlclient

I tried to install mySQL to use it for this Django project but I failed to install mysqlclient, that might be due to an incompatibility issue(my processor is win 64-bit and my Python version is for win 32-bit). Below, I want to document the steps that helped to fix this issue:
I used the following command :
```
pip install mysqlclient
```
Which gave me the following error :<br>
_mysql.c(29): fatal error C1083: Cannot open include file: 'mysql.h': No such file or directory <br>
The steps that I followed to solve the problem were:<br>
+ I downloaded a wheel file from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient) 
+ I’ve chosen the file with the name : mysqlclient-1.4.6-cp38-cp38-win32
Which is compatible with my Python version(3.8.2 for Windows 32-bit) as shown in the -cp38 and -win32 parts of the file name. Note: as l mentioned before my Windows is 64-bit but I downloaded a Python for 32-bit.

+ To know the appropriate. whl file for your Windows run the Python shell and you will find its version and for which Windows processor type it is. 
+ Then I opened a terminal and navigated to the directory where the wheel file is downloaded and installed it using pip, e.g;

```
pip install mysqlclient- 1.4.6-cp38-cp38-win32.whl
```
This should solve the problem but it wasn’t enough to fix it for me :angry:
<br> So after a search I tried this and it worked, finally:satisfied::
```
Pip install pymysql
```
+ Then to the \__init\__.py file of the project directory I added this:
```
import pymysql 
pymysql.install_as_MySQLdb()
```
