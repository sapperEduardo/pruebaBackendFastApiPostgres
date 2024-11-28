from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.user_connection import UserConnection
from schemas.user_schema import UserSchema


app = FastAPI()
userConn = UserConnection()


# Lista de orígenes permitidos
origins = [
    "http://127.0.0.1:5500",  # Permite tu origen de desarrollo
    "http://localhost:5500",  # Alternativa por si usas localhost
    # Añade otros orígenes si los necesitas
]

# Configura el middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],            # Permitir los orígenes especificados
    allow_credentials=True,            # Permitir el uso de cookies
    allow_methods=["*"],               # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],               # Permitir todos los encabezados
)

@app.get("/")
def get():
    return {
        "estado":"¡Todo bien!",
        "estado2":"¡Todo correcto!",
        "estado3":"¡Y yo que me alegro!"
    } 


# CREATE
@app.post("/api/insert")
def user_insert(user_data: UserSchema):
    data = user_data.dict()
    data.pop("id")
    print(data)
    userConn.write(data)
    return {"estado":"correcto"}


# READ
@app.get("/api/users")
def get_all_users()-> list[UserSchema]:
    data = userConn.read_all()

    mapa = [{"id":i,"name":n, "phone":p } for i,n,p in data]

    return mapa

# READ
@app.get("/api/user/{id}")
def get_one_user(
    id:str
)-> UserSchema:
    data = userConn.read_one(id=id)
    id,name,phone = data

    mapa = {"id":id,"name":name,"phone":phone}  

    return mapa


# UPDATE
@app.put("/api/user/{id}")
def update_one(user_data:UserSchema, id:str):
    data = {"id":id,"name":user_data.name,"phone":user_data.phone}
    print(data)
    userConn.update_one(data)
    return {"estado":"correcto"}    



# DELETE
@app.delete("/api/user/delete/{id}")
def delete_one(id:str):
    userConn.delete_one(id)
    return {"estado":"correcto"}