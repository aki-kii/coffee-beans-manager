from fastapi import FastAPI

from app.routers import mybeans, use, roast, grind

app = FastAPI()


app = FastAPI()
app.include_router(mybeans.router)
app.include_router(use.router)
app.include_router(roast.router)
app.include_router(grind.router)
