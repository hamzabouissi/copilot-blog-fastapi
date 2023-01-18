import fastapi

app = fastapi.FastAPI()


@app.get("/foobar")
async def foobar():
    return {"message": "hello world"}

@app.get("/")
async def home():
    return {"message": "Welcome home son"}