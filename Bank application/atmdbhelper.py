import mysql.connector

class atmdb:


    def __init__(self):
        # conncet to database
        try:
            self.conn = mysql.connector.connect(host="127.0.0.1", user="root", password="", database="atm")
            self.mycursor = self.conn.cursor()
        except:
            print('cant connect')
            exit()



    def check_login(self,accountID,pincode):

        # perform login

        self.mycursor.execute(
            "SELECT * FROM users WHERE accountID LIKE {} AND pincode LIKE {}".format(accountID, pincode))
        data = self.mycursor.fetchall()

        return data


    def fetch_userdata(self,user_id):

        self.mycursor.execute("SELECT * FROM users WHERE user_id LIKE {}".format(user_id))
        data = self.mycursor.fetchall()


        return data


    def register(self,accountID,name,pincode):

        try:
            self.mycursor.execute("""
            
            INSERT INTO users (user_id,accountID,name,pincode,account)
            VALUES
            (NULL,{},'{}',{},0)

            """.format(accountID, name, pincode))
            self.conn.commit()
            return 1

        except:
            return 0


    def update(self,ok,user_id):

        try:
            self.mycursor.execute("UPDATE users SET account= {} WHERE user_id= {}".format(ok, user_id))
            self.conn.commit()
            return 1

        except:
            return 0










