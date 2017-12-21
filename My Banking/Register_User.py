#!"E:\\Python36-32\\python.exe"

import sys
import cgi, cgitb
import logging
import re
from Account import Account


if (__name__ == '__main__'):

    cgitb.enable()
    frmRegister = cgi.FieldStorage()
    
    user_name    = str(frmRegister.getvalue("userName"))
    password     = str(frmRegister.getvalue("password"))
    acc_no       = frmRegister.getvalue("accNo")
    mobile_no    = frmRegister.getvalue("mobileNo")
    email_id     = str(frmRegister.getvalue("emailId"))
    
    accountObj       = Account()
    accountObj.logConfg()
    
    if (re.search('[A-Z]',password) is None) | (re.search('[0-9]',password) is None) | (re.search('[0-9]',password) is None) :
                        
          print ("""
          <html>
            <head>
                <title>NPB Payee Transaction Message</title>
            <link rel="stylesheet" type="text/css" href="Register_User.css">            
            </head>
            <body>
            <div class ="bg">
            <script>
                    alert("Invalid Password..Paswword Must Contain atleast 1 number,One Capital and a Small lettered Alphabet");
            </script>
            </body>
            </div>
        </html>
        """)             
    else:
    
        connectTodb      = accountObj.connectToMysqlDb()
        
        accountObj.registerUser(connectTodb,user_name,password,acc_no,mobile_no,email_id)        
        
        connectTodb.close()
        
        print ("Content-Type: text/html")
        print() 
        
        if accountObj.errorFlag == '1':
            accountObj.display404Error();
        else:    
          print ("""
                  <html>
                    <head>
                        <title>NPB Payee Transaction Message</title>
                    <link rel="stylesheet" type="text/css" href="Register_User.css">            
                    </head>
                    <body>
                    <div class ="bg">
                    <script>
                            alert("User Registered Successfully");
                    </script>
                    </body>
                    </div>
                </html>
                """)   

       