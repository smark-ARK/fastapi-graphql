from fastapi import APIRouter

from app.types.user import Query, Mutation
from strawberry import Schema
from strawberry.asgi import GraphQL


schema = Schema(query=Query, mutation=Mutation)
router = APIRouter(prefix="/user", tags=["Users"])
graphql_app = GraphQL(schema=schema)

router.add_route("/", graphql_app)
