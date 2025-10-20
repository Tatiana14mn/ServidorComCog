from mcp.server.fastmcp import FastMCP
import sqlite3
from database import init_db
init_db()
mcp = FastMCP("InventarioDB")
DB = "inventory.db"
@mcp.tool()
def crear_producto(nombre: str, categoria: str, cantidad: int, precio: float) -> str: 
   conn = sqlite3.connect(DB)
   cursor = conn.cursor()
   cursor.execute("INSERT INTO productos (nombre, categoria, cantidad,precio) VALUES (?, ?, ?, ?)", 
                  (nombre, categoria, cantidad, precio)) 
   conn.commit()
   conn.close()
   return "Producto creado exitosamente"
@mcp.tool()
def consultar_producto(id: int) -> dict: 
   conn = sqlite3.connect(DB)
   cursor = conn.cursor()
   cursor.execute("SELECT * FROM productos WHERE id = ?", (id,))
   row = cursor.fetchone()
   conn.close() 
   if row:
      return {"id": row[0], "nombre": row[1], "categoria": row[2], "cantidad": row[3], "precio": row[4]}
   return {"error": "Producto no encontrado"}
@mcp.tool()
def actualizar_producto(id: int, cantidad: int) -> str:
 conn = sqlite3.connect(DB)
 cursor = conn.cursor()
 cursor.execute("UPDATE productos SET cantidad = ? WHERE id = ?", (cantidad, id))
 conn.commit()
 conn.close()
 return "Producto actualizado correctamente"
@mcp.tool()
def eliminar_producto(id: int) -> str:
   conn = sqlite3.connect(DB)
   cursor = conn.cursor()
   cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
   conn.commit()
   conn.close()
   return "Producto eliminado correctamente"
@mcp.resource("productos://listado")
def listar_productos() -> dict:
   conn = sqlite3.connect(DB)
   cursor = conn.cursor()
   cursor.execute("SELECT * FROM productos")
   rows = cursor.fetchall()
   conn.close()
   return { row[0]: {"nombre": row[1], "categoria": row[2], "cantidad": row[3], "precio": row[4]} for row in rows}
if __name__ == "__main__":
   mcp.run()