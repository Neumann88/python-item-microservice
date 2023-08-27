from adapters.store.item.item_repo import ItemRepository
from adapters.cache.item.item_cache import ItemCache

class GetItemByID:
    repo: ItemRepository
    cache: ItemCache

    def __init__(self, cache: ItemCache, repo: ItemRepository):
        self.repo = repo
        self.cache = cache

    def handle(self, id: int):
        try:
            data = self.cache.get_item_by_id(id=id)
            if data is not None:
                return data

            item = self.repo.get_item_by_id(id)
            self.cache.set_item(item=item)
            return item
        except Exception as err:
            raise err