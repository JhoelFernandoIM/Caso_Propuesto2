import streamlit as st

def validar_producto(nombre, precio, categorias_seleccionadas, en_venta):
    categorias_validas = {"Chocolates", "Caramelos", "Mashmelos", "Galletas", "Salados", "Gomas de mascar"}
    
    # Validaciones
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

nombre = st.text_input("Nombre del Producto")
precio = st.text_input("Precio del Producto")

categorias_validas = ["Chocolates", "Caramelos", "Mashmelos", "Galletas", "Salados", "Gomas de mascar"]
categorias_seleccionadas = st.multiselect("Categorías del Producto", categorias_validas)

en_venta = st.radio("¿El producto está en venta?", ["Sí", "No"])

if st.button("Agregar Producto"):
    resultado = validar_producto(nombre, precio, categorias_seleccionadas, en_venta)
    if resultado == "Felicidades su producto se agregó.":
        st.success(resultado)
    else:
        st.error(resultado)
