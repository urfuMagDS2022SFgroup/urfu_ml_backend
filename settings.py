import os

PORT = int(os.environ.get('PORT', 8001))
DB_USER = os.environ['POSTGRES_USER']
DB_PASSWORD = os.environ['POSTGRES_PASSWORD']
DB_SERVER = os.environ['POSTGRES_HOST']
DB_PORT = int(os.environ['POSTGRES_PORT'])
DB_NAME = os.environ['POSTGRES_DB_NAME']
CONN_TEMPLATE = (
    'postgresql+asyncpg://{user}:{password}@{host}:{port}/{name}'
)
MIGRATIONS_CONN_TEMPLATE = (
    'postgresql://{user}:{password}@{host}:{port}/{name}'
)
DEFAULT_LIMIT = 100