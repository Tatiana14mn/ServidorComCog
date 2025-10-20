import asyncio
from fastmcp.client import Client

async def main():
    # Conexión explícita al servidor MCP local
    async with Client("mcp://localhost:8000") as client:
        print("\n🧪 Creando producto...")
        result = await client.call_tool(
            "crear_producto",
            nombre="Auriculares",
            categoria="Electrónica",
            cantidad=10,
            precio=59.99,
        )
        print(result)

        print("\n📦 Listando productos...")
        listado = await client.call_resource("productos://listado")
        print(listado)

        print("\n🔍 Consultando producto con ID=1...")
        consulta = await client.call_tool("consultar_producto", id=1)
        print(consulta)

        print("\n🔧 Actualizando cantidad del producto ID=1...")
        actualizacion = await client.call_tool("actualizar_producto", id=1, cantidad=20)
        print(actualizacion)

        print("\n🗑️ Eliminando producto ID=1...")
        eliminacion = await client.call_tool("eliminar_producto", id=1)
        print(eliminacion)

asyncio.run(main())

