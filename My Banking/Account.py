import _mysql
import sys
import re
import logging
from fileinput import close


class Account():
    errorFlag='0'
    
    def self__init__():
        errorFlag = '0'
     
    def connectToMysqlDb(self):
        try:
            conn=_mysql.connect("localhost","root","","banking_mindtree")
            logging.info("Connection to db successfull")
        except Exception as e:
            logging.error("Connection couldn't be established ->\r\nError details : "+str(e))
            self.errorFlag = '1'
        return conn
            
    def getAccountDetails(self,conn,userName,password):
        sql     =("SELECT acc_no,acc_name,acc_balance FROM ACCOUNTDETAILS WHERE USER_ID="
        + "'" +userName+ "'" 
        +" AND PASSWORD ="
        + "'" +password + "'")
        try:
            conn.query(sql)
        except Exception as e:    
            logging.error("Error : "+e)
            self.errorFlag = '1'
            conn,close()
            
        result  = conn.store_result()
        row     = result.fetch_row()
        return row
    
    def registerUser(self,conn,user_name,password,acc_no,mobile_no,email_id):
        sql=("UPDATE accountdetails set user_id="+ "'"
        +user_name+ "'" +",password="+ "'" +password + "'"
        +",phone_number="
        +mobile_no+",email_id ="+ "'" 
        +email_id+ "'" +"  where acc_no="+acc_no)
      #  logging.info(sql)
        try:
            conn.query(sql)
            conn.commit()
        except Exception as e:
            logging.error("failed to update values : "+e)
            self.errorFlag = '1'
            conn.close()
            
    def addPayee(self,conn,account_number,payee_acc_no,payee_acc_name,payee_bank_name):
        sql="INSERT INTO payeedetails values("+account_number+','+payee_acc_no+','+"'"+payee_acc_name+"'"+','+"'"+payee_bank_name+"'"+")"  
        
        logging.info(sql)
        try:
            conn.query(sql)
            conn.commit()
        except Exception as e:
            logging.error("failed to insert values to DB : " + e)
            self.errorFlag = '1'
            conn.close()
    
    def removePayee(self,conn,account_number,payee_acc_no,payee_bank_name):
        sql="DELETE FROM payeedetails WHERE acc_no="+account_number+" AND payee_accno="+payee_acc_no+" AND payee_bankname="+"'"+payee_bank_name+"'"  
        
        logging.info(sql)
        try:
            conn.query(sql)
            conn.commit()
        except Exception as e:
            logging.error("failed to remove values from DB : "+ e)
            self.errorFlag = '1'
            conn.close()
    
    def transferAmount(self,conn,account_number,payee_acc_no,payee_bank_name,transfer_amount):
        sql="UPDATE accountdetails SET acc_balance = acc_balance-"+transfer_amount + " WHERE acc_no="+account_number # AND payee_accno="+payee_acc_no+" AND payee_bankname="+"'"+payee_bank_name+"'"
          
        logging.info(sql)
        try:
            conn.query(sql)
            conn.commit()
        except Exception as e:
            logging.error("failed to Transfer Money to DB : "+ e)
            self.errorFlag = '1'
            conn.close() 
    
    def depositMoney(self,conn,account_number,deposit_money):
        sql="UPDATE accountdetails SET acc_balance=acc_balance+"+deposit_money+" WHERE acc_no="+account_number  
        
        logging.info(sql)
        try:
            conn.query(sql)
            conn.commit()
        except Exception as e:
            logging.error("failed to remove values from DB "+ e)
            self.errorFlag = '1'
            conn.close()
            
    def forgotPassword(self,conn,account_number,new_pwd):
        sql="UPDATE accountdetails SET password="+"'"+new_pwd+"'"+" WHERE acc_no="+account_number  
        
        logging.info(sql)
        try:
            conn.query(sql)
            conn.commit()
        except Exception as e:
            logging.error("failed to update password:  "+ e)
            self.errorFlag = '1'
            conn.close()
            
    def logConfg(self,mode='a'):
            # Configure the log file
            log_fname = "my_account_app.log"
            logging.basicConfig(filename    =   log_fname,
                                filemode    =   mode,
                                level       =   logging.INFO,
                                format      =   '%(asctime)s : %(levelname)s => %(message)s',
                                datefmt     =   '%Y-%m-%d %H:%M:%S')

    def display404Error(self):
        
        print ("""
                  <html>
                    <head>
                        <title>404 Error</title>
                    <link rel="stylesheet" type="text/css" href="404.css">            
                    </head>
                    <body>
                    <div class ="bg">
                    </div>
                    </body>
                </html>
              """)











