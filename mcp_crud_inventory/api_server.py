from fastapi import FastAPI, HTTPException
import sqlite3
from database import init_db

app = FastAPI(title="InventarioDB API")

DB = "inventory.db"
init_db()

@app.post("/productos/")
def crear_producto(nombre: str, categoria: str, cantidad: int, precio: float):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO productos (nombre, categoria, cantidad, precio) VALUES (?, ?, ?, ?)",
        (nombre, categoria, cantidad, precio),
    )
    conn.commit()
    conn.close()
    return {"mensaje": "Producto creado exitosamente"}

@app.get("/productos/{id}")
def consultar_producto(id: int):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?", (id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {
            "id": row[0],
            "nombre": row[1],
            "categoria": row[2],
            "cantidad": row[3],
            "precio": row[4],
        }
    raise HTTPException(status_code=404, detail="Producto no encontrado")

@app.put("/productos/{id}")
def actualizar_producto(id: int, cantidad: int):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("UPDATE productos SET cantidad = ? WHERE id = ?", (cantidad, id))
    conn.commit()
    conn.close()
    return {"mensaje": "Producto actualizado correctamente"}

@app.delete("/productos/{id}")
def eliminar_producto(id: int):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return {"mensaje": "Producto eliminado correctamente"}

@app.get("/productos/")
def listar_productos():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    rows = cursor.fetchall()
    conn.close()
    return [
        {
            "id": row[0],
            "nombre": row[1],
            "categoria": row[2],
            "cantidad": row[3],
            "precio": row[4],
        }
        for row in rows
    ]