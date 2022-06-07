from fastapi import FastAPI

from app.routers import beans, mybeans

app = FastAPI()


# routing
app.include_router(beans.router)
app.include_router(mybeans.router)