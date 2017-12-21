#!"E:\\Python36-32\\python.exe"

import sys
import logging
import cgi, cgitb
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
        <link rel="stylesheet" type="text/css" href="RemovePayee.css">
            </head>
            <body>
            <div class ="bg">
            <div class="Remove Payee">
                <h1><u><b>NPB-Bank Remove Payee</u></b></h1></br></br>
                <b>Account Number : """+acc_no+"""</b></br></br>    
                <b>Remove a Payee</b></br></br>
            
            <form action="PayeeTransaction.py" method="post">
                
             
            Payee Account Number: <input type="number" name="payeeAccno" required/><br/><br/>
            <input type="hidden" name="accountNumber" value=\""""+acc_no+""""/>
            <input type="hidden" name="mode" value="*DEL"/>
            Payee Bank Name:
            <select name="Payee Bank Name">
                <option value="Axis Bank">Axis Bank</option>
                <option value="HDFC Bank">HDFC Bank</option>
                <option value="Citi Bank">Citi Bank</option>
                <option value="ICICI Bank">ICICI Bank</option>
                <option value="IDFC Bank">IDFC Bank</option>
                <option value="State Bank of India">State Bank of India</option>
                <option value="Allahabad Bank">Allahabad Bank</option>
                <option value="Union Bank">Union Bank</option>
                <option value="RBL Bank">RBL Bank</option>
                <option value="Standard Chartered Bank">Standard Chartered Bank</option>
                <option value="Kotak Mahindra Bank">Kotak Mahindra Bank</option>
                <option value="UCO Bank">UCO Bank</option>
                <option value="Bank of Baroda">Bank of Baroda</option>
                <option value="Bank of India">Bank of India</option>
                <option value="Bandhan Bank">Bandhan Bank</option>
                <option value="Canara Bank">Canara Bank</option>
                <option value="City Union Bank">City Union Bank</option>
                <option value="United Bank of India">United Bank of India</option>
            </select><br/><br/>
            
            <input type="submit" value="Remove" /></br><br/>
        
        </form>
        </div>
        </div>
        </body>
        </html>""")