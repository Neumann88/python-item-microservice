import json
from redis import Redis

from entity.item import Item

def to_json(data: Item):
    return json.dumps(data, default=lambda o: o.__dict__, indent=4)

def from_json(data: str):
        return json.loads(data, object_hook=lambda d: Item(**d))

class ItemCache:
    cache: Redis

    def __init__(self, cache: Redis):
        self.cache = cache

    def get_item_by_id(self, id: int):
        try:
            res = self.cache.get(name=f"item.{id}")
            if res is None:
                return None

            return from_json(data=res)
        except Exception as err:
            raise err

    def set_item(self, item: Item):
        try:
            return self.cache.set(name=f"item.{item.id}", value=to_json(data=item))
        except Exception as err:
            raise err