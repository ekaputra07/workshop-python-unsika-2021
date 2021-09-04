import uuid
from datetime import datetime

items = []


def all_items():
    """
    Return semua items, urutkan berdasarkan waktu dibuat.
    """
    return sorted(items, key=lambda x: x['created'], reverse=True)


def new_item(name):
    """
    Buat item baru, kita hanya perlu parameter nama, sisanya kita generate sebelum menyimpan.
    """
    item = {
        'id': str(uuid.uuid4()),
        'done': False,
        'name': name,
        'created': datetime.now()
    }
    items.append(item)
    return item


def update_item(id):
    """
    Update status item, apabila status awal True maka akan jadi False, begitu juga sebaliknya.
    """
    for item in items:
        if item['id'] == id:
            item['done'] = not item['done']


def delete_item(id):
    """
    Hapus item dari daftar berdasarkan id yang diberikan.
    """
    global items
    items = list(filter(lambda x: x['id'] != id, items))
