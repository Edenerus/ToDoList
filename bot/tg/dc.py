from marshmallow import EXCLUDE
from pydantic import BaseModel, Field


class MessageFrom(BaseModel):
    id: int
    is_bot: bool
    first_name: str
    last_name: str | None = None
    language_code: str | None = None


class Chat(BaseModel):
    id: int
    first_name: str
    last_name: str | None = None
    type: str | None = None


class Entity(BaseModel):
    offset: int
    length: int
    type: str | None = None


class Message(BaseModel):
    message_id:  int
    chat: Chat
    from_: MessageFrom = Field(..., alias='from')
    date: int
    text: str
    entities: list[Entity] = []


class UpdateObj(BaseModel):
    update_id: int
    message: Message


class GetUpdatesResponse(BaseModel):
    ok: bool
    result: list[UpdateObj] = []

    class Meta:
        unknown = EXCLUDE


class SendMessageResponse(BaseModel):
    ok: bool
    result: Message = ''

    class Meta:
        unknown = EXCLUDE
