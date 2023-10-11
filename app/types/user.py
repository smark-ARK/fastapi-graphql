from strawberry import type, field, mutation
from typing import List, Optional
from app.helpers.user import get_user, get_users, add_user, update_user, delete_user


@type
class User:
    id: int
    name: str
    email: str
    password: str


@type
class Query:
    @field
    def user(self, info, id: int) -> User:
        return get_user(id)

    @field
    def users(self) -> List[User]:
        return get_users()


@type
class Mutation:
    @mutation
    def create_user(self, name: str, email: str, password: str) -> User:
        return add_user(name, email, password)

    @mutation
    def delete_user(self, id: int) -> bool:
        return delete_user(id)

    @mutation
    def update_user(
        self,
        id: int,
        name: Optional[str] = None,
        email: Optional[str] = None,
        password: Optional[str] = None,
    ) -> User:
        updated = {}
        if name:
            updated.update({"name": name})
        if email:
            updated.update({"email": email})
        if password:
            updated.update({"password": password})
        return update_user(id, updated)
