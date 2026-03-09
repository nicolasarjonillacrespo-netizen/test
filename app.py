import streamlit as st

# 1. EL ARCHIVADOR (Nuestra base de datos de preguntas)
# Cada bloque entre { } es una pregunta distinta. Cada pregunta es un diccionario de 3 entradas (texto, opciones, correcta).
# Creamos la lista de preguntas:
preguntas = [
    {
        "texto": "¿En que equipos NO ha jugado CR7?",
        "opciones": ["Real Madrid", "Juventus", "Benfica", "Manchester United"],
        "correcta": "Benfica"
    },
    {
        "texto": "¿En que fecha gano Messi su ultima Champions?",
        "opciones": ["2021", "2015", "2019"],
        "correcta": "2015"
    },
    {
        "texto": "¿Cuantos goles tiene Julian Alvarez actualmente?",
        "opciones": ["144", "145", "143"],
        "correcta": "144"
    },
    {    "texto": "¿Primer dorsal de Vini JR en el Madrid?",
        "opciones": ["17", "25", "28", "20"],
        "correcta": "28"
    },
    {
        "texto": "¿Por que Poul Pogba no podia jugar al futbol hasta ahora?",
        "opciones": ["Dierna", "Lesion", "Dopaje"],
        "correcta": "Dopaje"
    },
    {
        "texto": "¿En que equipo juega aztualmente Dybala?",
        "opciones": ["Milan", "La Roma", "Galatasaray"],
        "correcta": "La Roma"
    },
    {
        "texto": "¿Con cuantos años gano Mbappe el mundial?",
        "opciones": ["21", "18", "19"],
        "correcta": "19"
    },
    {
        "texto": "¿Como se llama el actual presidente del Malaga FC?",
        "opciones": ["Illojuan", "José María Muñoz", "El patica"],
        "correcta": "José María Muñoz"
    },
    {    "texto": "¿Quien gano la primera Eurocopa?",
        "opciones": ["Union Sovietica", "España", "Italia", "Rumania"],
        "correcta": "Union Sovietica"
    },
    {
        "texto": "¿cual fue el jugador que en su momento costo 222 millones de euros?",
        "opciones": ["Haaland", "Neymar", "Benzema"],
        "correcta": "Neymar"
    }
]

# Configuración visual de la página
st.title("Test durisimo de Futbol")
st.write("Veamos cuantas aciertas ")

# 2. EL FORMULARIO (Agrupamos todo para que no se recargue la web a cada clic)
# Eso se consigue con el comando with

with st.form("quiz_form"):

    # Aquí guardaremos las respuestas que elija el alumno. Será una lista.
    respuestas_usuario = []
   
    # Recorremos el archivador usando un bucle 'for' para crear las preguntas
    for pregunta in preguntas:
        st.subheader(pregunta["texto"]) # Ponemos el texto de la pregunta

        # Creamos los botones de opción (radio)
        eleccion = st.radio("Elige una opción:", pregunta["opciones"], key=pregunta["texto"])

        # Guardamos la elección en nuestra lista usando append ()
        respuestas_usuario.append(eleccion)
        st.write("---") # Una línea para separar preguntas

    # Botón obligatorio para cerrar el formulario
    boton_enviar = st.form_submit_button("Entregar Examen")

# 3. LA CORRECCIÓN (Solo ocurre cuando pulsamos el botón)
if boton_enviar:
    aciertos = 0
    # Total es número de preguntas (usa el método len)
    total = len(preguntas)

    # Comparamos las respuestas del usuario con las 'correctas' del archivador
    for i in range(total):
        if respuestas_usuario[i] == preguntas[i]["correcta"]:
            aciertos = aciertos + 1

    # Calculamos la nota sobre 10
    nota = (aciertos / total) * 10

    # Mostramos el resultado con colores
    st.divider()
    st.header(f"Resultado final: {nota} / 10")

    if nota >= 5:
        st.success(f"¡Felicidades! Has aprobado con {aciertos} aciertos.")
        st.balloons() # ¡Efecto de globos!
    else:
        st.error(f"Has sacado un {nota}. ¡Toca estudiar un poco más!")
