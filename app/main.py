import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

# from app import models
# from app.database import engine
from app.routers import user

# models.Base.metadata.create_all(bind=engine)


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"


schema = strawberry.Schema(Query)


graphql_app = GraphQLRouter(schema)


app = FastAPI()
app.include_router(user.router)
