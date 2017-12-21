#!"E:\\Python36-32\\python.exe"

import cgi, cgitb
import logging
from Account import Account
import sys

if (__name__ == '__main__'):

    cgitb.enable()
    
    FrmPayee = cgi.FieldStorage()
    
    payee_acc_no    = FrmPayee.getvalue('payeeAccno')
    account_number  = FrmPayee.getvalue('accountNumber') 
    payee_mode      = str(FrmPayee.getvalue('mode')) 
    payee_bank_name = str(FrmPayee.getvalue('Payee Bank Name'))
    
    accountObj       = Account()    
    accountObj.logConfg()
    connectTodb      = accountObj.connectToMysqlDb()    
    
    if payee_mode   == '*ADD': 
        payee_acc_name  = str(FrmPayee.getvalue('payeeAccName'))
        accountDetail    = accountObj.addPayee(connectTodb,account_number,payee_acc_no,payee_acc_name,payee_bank_name);
    
    if payee_mode   == '*DEL': 
        accountDetail    = accountObj.removePayee(connectTodb,account_number,payee_acc_no,payee_bank_name);
    
    if payee_mode   == '*TRNSFRMONY': 
        transfer_amount  = FrmPayee.getvalue('transferAmount')
        accountDetail    = accountObj.transferAmount(connectTodb,account_number,payee_acc_no,payee_bank_name,transfer_amount);
    
    if payee_mode   == '*DEP': 
       deposit_money    = FrmPayee.getvalue('depositMoney')
       accountDetail    = accountObj.depositMoney(connectTodb,account_number,deposit_money);
    
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
        <link rel="stylesheet" type="text/css" href="PayeeTransaction.css">            
        </head>
        <body>
        <div class ="bg">
            <div class="Payee Transaction">

        <script>    
                alert("Payee Transaction Successfull");
        </script>
        </div>
        </div>
        </body>
    </html>
    """)    