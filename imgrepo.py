import sqlite3
import os
import shutil
#This code is to acess a Sqlite server which holds the links to all the images in our repo.

class DB:
    def __init__(self):
        self.cursor=None
        self.conn=None
        self.masterdb='masterrepo.db'
        self.dbfile='imgrepo.db'
        self.connect()

    def connect(self):
        self.conn = sqlite3.connect(self.dbfile)
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
        table = [ {"ID": item[0], "description": item[1], "url":item[2]} for item in raw]
        return table

    def delete(self,ID):
        self.cursor.execute("DELETE FROM IMAGES WHERE ID={number}".format(number=ID))
        self.conn.commit()

    def reset(self):
        #Disconnect from database.
        self.conn.close()
        #delet previous database
        os.remove(self.dbfile)
        #clone master database
        shutil.copyfile(self.masterdb, self.dbfile)
        #connect to cloned database
        self.connect()


if __name__ == "__main__":
    db= DB()
    print(db.getall())
