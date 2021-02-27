# pylint: disable=no-name-in-module
import os
from pymongo import MongoClient
from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

cluster = MongoClient(os.environ["DB_URI"])
db = cluster['vagas_quick']

class PyObjectId(ObjectId):

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid objectid')
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')


class Vaga(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id')
    titulo: str
    atividades: str
    requisitos: str
    destaques: str
    ativo: bool = True

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }

"""
from models import db, Vaga
async def criar_vaga(vaga: Vaga):
    ret = db.vagas.insert_one(vaga.dict(by_alias=True))
        vaga.id = ret.inserted_id
"""