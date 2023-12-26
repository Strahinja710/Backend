from fastapi import FastAPI 
from database import engine
import models, routers
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

# cors policy
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://192.168.104.101:8000",
    "http://127.0.0.1:5500",
]

# Kreiranje tabele u bazi, ako ne postoji
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# cors policy
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Uključivanje rutera u aplikaciju
app.include_router(routers.router)


# Dodavanje logike za pokretanje Uvicorn servera
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
