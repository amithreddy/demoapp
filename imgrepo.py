import sqlite3
#This code is to acess a Sqlite server which holds the links to all the images in our repo.

class DB:
    def __init__(self, name):
        self.cursor=None
        self.conn=None
        self.connect(name)

    def connect(self, name):
        self.conn = sqlite3.connect(name)
        self.cursor = self.conn.cursor()
        
    def create(self):
        #Ran this code only once when first create a sql server
        #Populated the server interactively while in repel
        self.cursor.execute(
                '''
                CREATE TABLE IMAGES
                (ID INTEGER PRIMARY KEY AUTOINCREMENT, DESCRIPTION str,URL str)
                ''')
    def getall(self):
        self.cursor.execute("Select * FROM IMAGES")
        raw= self.cursor.fetchall()
        print(raw)
        table = [ {"ID": item[0], "description": item[1], "url":item[2]} for item in raw]
        return table


    def delete(self,ID):
        self.cursor.execute("DELETE FROM IMAGES WHERE ID={number}".format(number=ID))
        self.conn.commit()

    def reset(self):
        #Disconnect from database.
        #delete previous database
        #clone master database
        #connect to cloned database
        pass#copy new database and delete them

if __name__ == "__main__":
    db= DB("imgrepo.db")
    print(db.getall())
    db.conn.close()
