from adapters.store.item.item_repo import ItemRepository
from adapters.cache.item.item_cache import ItemCache
from entity.item import Item

class CreateItem:
    repo: ItemRepository
    cache: ItemCache

    def __init__(self, cache: ItemCache, repo: ItemRepository):
        self.repo = repo
        self.cache = cache

    def handle(self, item: Item):
        try:
            self.cache.set_item(item=item)
            self.repo.create_item(item=item)
        except Exception as err:
            raise err