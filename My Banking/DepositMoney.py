#!"E:\\Python36-32\\python.exe"

import cgi, cgitb
import sys
import logging
from Account import Account

if (__name__ == '__main__'):
    
    frmUsrLogin = cgi.FieldStorage()
    accountObj  = Account()
    accountObj.logConfg()
    acc_no      = frmUsrLogin.getvalue('accountNumber')
    
    if accountObj.errorFlag == '1':
        accountObj.display404Error();
    else:    
        print ("Content-Type: text/html")
        print()
        print ("""
                <html>
            <head>
                <title>NPB BANK</title>
                <link rel="stylesheet" type="text/css" href="DepositMoney.css">
            </head>
            <body>
            <div class ="bg">
            <div class="Deposit Money">
                <h1><u><b>NPB-Deposit Money</u></b></h1></br></br>
                <b>Account Number : """+acc_no+"""</b></br></br>    
                <b>Deposit Money</b></br></br>
            
            <form action="PayeeTransaction.py" method="post">
                
            Deposit Money: <input type="number" name="depositMoney" required/><br/><br/>
            <input type="hidden" name="accountNumber" value=\""""+acc_no+""""/>
            <input type="hidden" name="mode" value="*DEP"/>
          
            
            <input type="submit" value="Deposit" /></br><br/>
        
        </form>
        </div>
        </div>
        </body>
        </html>""")