from flask import Flask, render_template, request, redirect, url_for, g
import imgrepo
app = Flask(__name__)

DATABASE="imgrepo.db"
MASTER_DATABASE = "masterrepo.db"

@app.route('/', methods= ['GET','POST'])
def main():
    db = get_db()
    if request.method == "GET":
        #Get all image links in database
        items = db.getall()
        #Pass all image links into renderer
        return render_template('home.html',table=items)
    elif request.method =="POST":
        print(dir(request))
        return redirect('/')
    else:
        #Shouldn't happen. Should return a error here
        pass

def get_db():
    #g from Flask.g live in the request context, meaning its created at
    #the start of a request and killed at the end of the request.
    #So we need to connect to the database here and close the databaes
    #in close_connection
    db= getattr(g, '_database',None)
    if db is None:
        db= g._database = imgrepo.DB(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database',None)
    if db is not None:
        db.conn.close()
