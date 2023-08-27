from fastapi import Response, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from entity.item import Item
from app.app import Application

class ItemRequest(BaseModel):
    id: int
    value: int

class ItemHttpHandler:
    app: Application

    def __init__(self, app: Application):
        self.app = app

    def get_item(self, item_id):
        try:
            return self.app.query.get_item_by_id.handle(item_id)
        except Exception as err:
            return JSONResponse(
                content={"message": str(err)},
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def create_item(self, in_item: ItemRequest):
        try:
            item = Item(id=in_item.id, value=in_item.value)
            self.app.command.create_item.handle(item=item)
            return Response()
        except Exception as err:
            return JSONResponse(
                content={"message": str(err)},
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
