from psycopg2._psycopg import connection

from entity.item import Item

class ItemRepository:
    db: connection

    def __init__(self, db: connection):
        self.db = db

    def create_item(self, item: Item):
        query = "INSERT INTO item (id, value) VALUES (%s, %s)"
        curr = self.db.cursor()

        try:
            curr.execute(query=query, vars=(item.id, item.value))
            self.db.commit()
        except Exception as err:
            self.db.rollback()
            raise err


    def get_item_by_id(self, id):
        query = "SELECT id, value FROM item WHERE id = %s"
        curr = self.db.cursor()

        try:
            curr.execute(query=query, vars=(id))
            data = curr.fetchone()
            return Item(data[0], data[1])
        except Exception as err:
            self.db.rollback()
            raise err
