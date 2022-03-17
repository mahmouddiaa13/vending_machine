from fastapi import FastAPI
import uvicorn

from infrastructure.db_conn.pg_sql_alchemy import engine, Base
from routers import users_routers, auth_routers

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Vending Machine")

app.include_router(users_routers.router)
app.include_router(auth_routers.router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)
