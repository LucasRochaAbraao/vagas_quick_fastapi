from fastapi import FastAPI

from models import db, Vaga

app = FastAPI()

@app.get('/vagas')
async def todas_vagas():
    vagas = []
    for vaga in db.vagas.find():
        vagas.append(Vaga(**vaga))
   
    return {'vagas': vagas}


@app.post('/vagas')
async def criar_vaga(vaga: Vaga):
    print(type(vaga), vaga)
    return {type(vaga): vaga}
    if hasattr(vaga, 'id'):
        delattr(vaga, 'id')
    ret = db.vagas.insert_one(vaga.dict(by_alias=True))
    vaga.id = ret.inserted_id

    return {'vaga': vaga}
