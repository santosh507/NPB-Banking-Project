#!"E:\\Python36-32\\python.exe"


import cgi, cgitb
import logging
from Account import Account
import re
import sys

if (__name__ == '__main__'):

    cgitb.enable()
    
    frmLogin = cgi.FieldStorage()
    
    account_number  = frmLogin.getvalue('accountNumber')
    new_pwd         = str(frmLogin.getvalue('newPassword'))
    
   
        
    accountObj       = Account()    
    accountObj.logConfg()
    logging.info (new_pwd)
    print ("Content-Type: text/html")
    print() 
    
    if (re.search('[A-Z]',new_pwd ) is None) | (re.search('[0-9]',new_pwd ) is None) | (re.search('[0-9]',new_pwd ) is None) :
                        
          print ("""
          <html>
            <head>
                <title>NPB Payee Transaction Message</title>
            <link rel="stylesheet" type="text/css" href="Register_User.css">            
            </head>
            <body>
            <div class ="bg">
            <script>
                    alert("Invalid new_pwd ..Paswword Must Contain atleast 1 number,One Capital and a Small lettered Alphabet");
            </script>
            </body>
            </div>
        </html>
        """)             
    else:
        connectTodb      = accountObj.connectToMysqlDb()
        accountDetail    = accountObj.forgotPassword (connectTodb,account_number,new_pwd);
        connectTodb.close()
        
        logging.info(accountObj.errorFlag)
        
        if accountObj.errorFlag == '1':
            accountObj.display404Error();
        else:    
          print ("""
          <html>
            <head>
                <title>NPB Payee Transaction Message</title>
                        
            </head>
            <body>
            <script>
                    alert("Password  Reset Successfull");
            </script>
                               
            </body>
        </html>
        """)    
	
	