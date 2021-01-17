from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    adict = { 
            'name':"zebra",
           'thumbnail':"/img",
           'url':"/img2",
           'ID':1
            }
    items = [adict, adict]
    return render_template('home.html',table=items)


