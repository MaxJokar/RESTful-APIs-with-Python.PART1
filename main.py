from fastapi import FastAPI, HTTPException
from models import User, Gender, Role
from typing import List
from uuid import UUID, uuid4

app = FastAPI()

db: list[User] = [
    User(
        # id=uuid4(),
        id=UUID("d2e206af-3b91-4f1c-a94f-f81a9f234026"),  # we get Fixed ids
        first_name="Maxim",
        last_name="jokar",
        gender=Gender.male,
        roles=[Role.admin],
    ),
    User(
        # id=uuid4(),
        id=UUID("2c1b7557-a9cf-4e4e-b6aa-d00226d18142"),
        first_name="Philip",
        last_name="jokar",
        gender=Gender.male,
        roles=[Role.student],
    ),
]


@app.get("/")
def root():
    return {"Hello FastAPI "}


@app.get("/api/v1/users")
async def fetch_user():
    return db


@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user.id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404, detail=" user with id :{user.id} does not exist"
    )
