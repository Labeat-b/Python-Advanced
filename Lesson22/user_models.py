from pydantic import BaseModel, conint, constr

class User(BaseModel):
    id: int
    name: str
    age: int
    email: str

user = User(id=1, name='John Doe', age=30, email='johndoe@example.com')
print(user)

class AnotherUser(BaseModel):
    id: conint(gt=50)
    name: constr(min_length=3, max_length=50)

user1 = AnotherUser(id=51, name='Alice')
print(user1)