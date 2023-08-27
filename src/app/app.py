from psycopg2._psycopg import connection
from redis import Redis

from adapters.store.item.item_repo import ItemRepository
from adapters.cache.item.item_cache import ItemCache

from app.item.command.create_item import CreateItem
from app.item.query.get_item_by_id import GetItemByID

class Command:
    create_item: CreateItem

    def __init__(self, cache, repo):
        self.create_item = CreateItem(cache=cache, repo=repo)


class Query:
    get_item_by_id: GetItemByID

    def __init__(self, cache, repo):
        self.get_item_by_id = GetItemByID(cache=cache, repo=repo)

class Application:
    command: Command
    query: Query

    def __init__(self, cache: Redis, db: connection):
        item_repo = ItemRepository(db=db)
        item_cache = ItemCache(cache=cache)

        self.command = Command(cache=item_cache, repo=item_repo)
        self.query = Query(cache=item_cache, repo=item_repo)