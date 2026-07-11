from fastapi import FastAPI
from src.routes.todorouter import todoRouter
from src.utils.base import Base,engine
from contextlib import asynccontextmanager

# //This is where model is tied up to engine
@asynccontextmanager
async def onStart(app):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Table creation Done")
    yield 
    await engine.dispose()


app = FastAPI(lifespan=onStart)

@app.get("/")
def getBasic():
    return {"message": "Hello Fast API Rupesh make it successful do hardwork"}

app.include_router(todoRouter)
