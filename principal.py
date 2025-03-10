import streamlit as st

def validar_producto(nombre, precio, categorias_seleccionadas, en_venta):
    categorias_validas = {"Chocolates", "Caramelos", "Mashmelos", "Galletas", "Salados", "Gomas de mascar"}
    
    # Validaciones
    if not nombre.strip():
        return "El nombre del producto no puede estar vacío."
    
    if len(nombre) > 20:
        return "El nombre del producto no debe superar los 20 caracteres."
    
    try:
        precio = float(precio)
        if precio <= 0 or precio >= 999:
            return "El precio debe ser mayor a 0 y menor a 999 soles."
    except ValueError:
        return "Por favor verifique el campo del precio."
    
    for categoria in categorias_seleccionadas:
        if categoria not in categorias_validas:
            return "Una o más categorías no son válidas."
    
    if en_venta not in ["Sí", "No"]:
        return "El estado de venta no es válido."
    
    return "Felicidades su producto se agregó."

# Streamlit UI
st.title("Formulario de Producto - Dulcino")

# Inicializar almacenamiento de productos en sesión
if "productos" not in st.session_state:
    st.session_state.productos = []

nombre = st.text_input("Nombre del Producto")
precio = st.text_input("Precio del Producto (separador decimal es .)")

categorias_validas = ["Chocolates", "Caramelos", "Mashmelos", "Galletas", "Salados", "Gomas de mascar"]
categorias_seleccionadas = st.multiselect("Categorías del Producto (puede elegir uno más)", categorias_validas)

en_venta = st.radio("¿El producto está en venta?", ["Sí", "No"])

if st.button("Agregar Producto"):
    resultado = validar_producto(nombre, precio, categorias_seleccionadas, en_venta)
    if resultado == "Felicidades su producto se agregó.":
        # Guardar el producto en la sesión
        st.session_state.productos.append({
            "Nombre": nombre,
            "Precio": precio,
            "Categorías": ", ".join(categorias_seleccionadas),
            "En Venta": en_venta
        })
        st.success(resultado)
    else:
        st.error("Lo sentimos, no pudo crear este producto.")
        st.error(resultado)

# Mostrar productos agregados
st.subheader("Productos Agregados")
if st.session_state.productos:
    for producto in st.session_state.productos:
        st.write(f"**Nombre:** {producto['Nombre']}")
        st.write(f"**Precio:** {producto['Precio']} soles")
        st.write(f"**Categorías:** {producto['Categorías']}")
        st.write(f"**En Venta:** {producto['En Venta']}")
        st.markdown("---")
else:
    st.info("Aún no se han agregado productos.")