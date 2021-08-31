
from flask import Flask, redirect, url_for, render_template, request

from db import all_items, delete_item, new_item, update_item

# buat Flask app
app = Flask(__name__)


@app.route('/')
def home():
    """
    Halaman utama.
    """
    return render_template('index.html', todos=all_items())


@app.route('/new', methods=['POST'])
def new():
    """
    Untuk membuat todo baru, hanya menerima request bertipe POST.
    """
    new_item(request.form.get('todo'))
    return redirect(url_for('home'))


@app.route('/update', methods=['POST'])
def update():
    """
    Untuk memperbarui status todo, hanya menerima request bertipe POST.
    """
    id = request.form.get('id')
    update_item(id)
    return 'ok'


@app.route('/delete', methods=['POST'])
def delete():
    """
    Untuk menghapus todo, hanya menerima request bertipe POST.
    """
    id = request.form.get('id')
    delete_item(id)
    return 'ok'
