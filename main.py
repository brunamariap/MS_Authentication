from fastapi import FastAPI
from prisma import Prisma
from controllers import user

app = FastAPI()
app.include_router(user.router)

prisma = Prisma(auto_register=True)

@app.on_event("startup")
async def startup():
    await prisma.connect()

@app.on_event("shutdown")
async def shutdown():
    await prisma.disconnect()