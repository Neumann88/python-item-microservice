import uvicorn
from fastapi import FastAPI
from redis import Redis
import psycopg2

from transport.http.v1.item.item_handler import ItemHttpHandler
from app.app import Application

redis_conn = None
postgresql_conn = None

if __name__ == "__main__":
    try:
        redis_conn = Redis(host="localhost", port="6379", decode_responses=True)
        postgresql_conn = psycopg2.connect(user="test", password="test", host="localhost", port="5432", database="test")

        app = Application(redis_conn, postgresql_conn)
        item_http_handler = ItemHttpHandler(app)

        app = FastAPI()
        app.add_api_route("/items/{item_id}", item_http_handler.get_item, methods=["GET"])
        app.add_api_route("/items", item_http_handler.create_item, methods=["POST"])

        uvicorn.run(app, host="localhost", port=8080)
    except Exception as err:
        print(err)
    finally:
        redis_conn.close()
        postgresql_conn.close()
