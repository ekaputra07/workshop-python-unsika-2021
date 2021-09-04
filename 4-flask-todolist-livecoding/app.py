from flask import Flask, render_template, request, redirect

import db

app = Flask(__name__)

@app.route('/')
def home():
    items = db.get_items()
    return render_template('index.html', items=items)

@app.route('/new', methods=['POST'])
def new():
    item_name = request.form['item_name']
    db.add_item(item_name)
    return redirect('/')

@app.route('/update', methods=['POST'])
def update():
    item_id = request.form['item_id']
    db.update_item(item_id)
    return 'ok'

@app.route('/delete', methods=['POST'])
def delete():
    item_id = request.form['item_id']
    db.delete_item(item_id)
    return 'ok'


