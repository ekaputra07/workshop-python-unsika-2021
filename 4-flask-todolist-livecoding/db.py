import uuid
from datetime import datetime

items = []

'''
items = [
{
    'id': 'sdajhd',
    'status': False,
    'created': 'dsada',
    'name': 'Abc'
},
{
    'id': 'sdajhd',
    'status': False,
    'created': 'dsada',
    'name': 'Abc'
}
]
'''

def get_items():
    return items


def add_item(name):
    item = {
        'id': str(uuid.uuid4()),
        'name': name,
        'status': False,
        'created': datetime.now()
    }
    items.append(item)


def update_item(id):
    for item in items:
        if item['id'] == id:
            item['status'] = not item['status']


def delete_item(id):
    global items

    # items_new = []
    # for item in items:
    #     if item['id'] != id:
    #         items_new.append(item)
    # items = items_new

    items = list(filter(lambda item: item['id'] != id, items))