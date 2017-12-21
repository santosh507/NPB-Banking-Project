#!"E:\\Python36-32\\python.exe"

import cgi, cgitb
import logging
from Account import Account

if (__name__ == '__main__'):
    cgitb.enable()
    frmLogin = cgi.FieldStorage()
    
    userName = str(frmLogin.getvalue('userId'))
    password = str(frmLogin.getvalue('password'))
    
    accountObj       = Account()
    accountObj.logConfg()
    connectTodb      = accountObj.connectToMysqlDb()
    accountDetail    = accountObj.getAccountDetails(connectTodb,userName,password)
    
    connectTodb.close()
    
    print ("Content-Type: text/html")
    print()
        
    
    if accountDetail:
    #If row found then display Dashboard html page
        logging.info("User Logged in successfully")
        for accno,accnam,accbal in accountDetail:
            account_no = accno
            account_name = str(accnam,'utf-8')
            account_balance = accbal
        print ("""
         <html>
            <head>
                <title>NPB Dashboard</title>
            <link rel="stylesheet" type="text/css" href="UserLogin.css">            
            </head>
            <body>
            <div class ="bg">
                <div class ="Logout">
                    <button onclick="window.location.href='Login.html'">Logout</button>
                </div>
                
                <div class = "Account Details">
                     <h1><u><b>NPB Dashboard</u></b></h1></br></br>
                     
                        <h2><u>Account Details</u></h2></br></br>
                        <b>AccountNumber : </b>"""+account_no+"""</br></br>
                        <b>AccountName   : </b>"""+account_name+"""</br></br>
                        <b>Balance       : </b>"""+account_balance+"""</br></br>
                        
                        <u>Choose from a list of services offered from our Dashboard</u><br/><br/>
                        
                        <b>Select your choice:</b></br></br>
                    
                        <form method="post">   
                            <input type="hidden" name="accountNumber" value=\""""+account_no+""""/>
                            <input type="submit" formaction="AddPayee.py" value="Add Payee"/ ></br></br>
                            <input type="submit" formaction="RemovePayee.py" value="Remove Payee" /><br/></br>
                            <input type="submit" formaction="TransferMoney.py" value="Money Transfer" /><br/><br/>    
                            <input type="submit" formaction="DepositMoney.py" value="Deposit" /><br/></br>
                        </form>
                </div>      
              </div>  
            </body>
        </html>
        """)   
    else:  
        if accountObj.errorFlag == '1':
            accountObj.display404Error();
            sys.exit()
        
        logging.error("Invalid User id or Password") 
        print ("""
          <html>
            <head>
                <title>NPB Login Failure</title>
                        
            </head>
            <body>
            <script>
                    alert("Error : Invalid userName or password...Please try again..");
            </script>
                 <center><u><b>Invalid userName or password...Please try again...</u></b></center></br>
                  
            </body>
        </html>
        """)
















