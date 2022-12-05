import functools as fn
import typing as tp

import databases
import settings
import strawberry
import uvicorn
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from strawberry.schema.config import StrawberryConfig


@strawberry.type
class Query:
    """Query."""

    @strawberry.field
    def hello(self) -> str:
        return 'world'


schema = strawberry.Schema(
    query=Query,
    config=StrawberryConfig(auto_camel_case=True),
)


async def startup_db(db: databases.Database):
    await db.connect()


async def shutdown_db(db: databases.Database):
    await db.disconnect()


HOOK_TYPE = tp.Optional[
    tp.Sequence[tp.Callable[[], tp.Any]]
]


def get_app(
    db: databases.Database,
    on_startup: HOOK_TYPE = None,
    on_shutdown: HOOK_TYPE = None,
) -> FastAPI:
    app = FastAPI(
        on_startup=[fn.partial(startup_db, db)]
        if on_startup is None else on_startup,
        on_shutdown=[fn.partial(shutdown_db, db)]
        if on_shutdown is None else on_shutdown,
    )
    graphql_app = GraphQLRouter(
        schema,
    )
    app.include_router(graphql_app, prefix='/graphql')
    return app


def main() -> None:
    database = databases.Database(
        settings.CONN_TEMPLATE.format(
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
            port=settings.DB_PORT,
            host=settings.DB_SERVER,
            name=settings.DB_NAME,
        ),
    )
    app = get_app(database)
    uvicorn.run(
        app,
        host='0.0.0.0',
        port=settings.PORT,
    )


if __name__ == '__main__':
    main()