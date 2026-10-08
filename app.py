from textblob import TextBlob
import pandas as pd
import streamlit as st
from PIL import Image
from googletrans import Translator

# ---------- ESTÉTICA (la fuente no se toca: se usa la de Streamlit) ----------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(160deg, #1b1f3b 0%, #2d2a55 55%, #3b3270 100%);
        color: #f3efff;
    }
    h1, h2, h3, p, label, span, div { color: #f3efff; }
    h1 {
        text-align: center;
        letter-spacing: 1px;
        text-shadow: 0 0 18px rgba(255, 214, 102, 0.55);
    }
    [data-testid="stSidebar"] {
        background: #14172e;
        border-right: 2px solid #ffd666;
    }
    [data-testid="stExpander"] {
        background: rgba(255, 255, 255, 0.07);
        border: 1px solid #ffd666;
        border-radius: 18px;
    }
    .stTextInput input {
        background: #fffaf0;
        color: #1b1f3b;
        border-radius: 12px;
        border: 2px solid #ffd666;
    }
    img { border-radius: 24px; box-shadow: 0 0 25px rgba(255, 214, 102, 0.35); }
    .tarjeta {
        border-radius: 18px;
        padding: 16px 20px;
        margin-top: 12px;
        background: rgba(255, 255, 255, 0.10);
        border-left: 8px solid #ffd666;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title('🧭 Brújula Emocional')
image = Image.open('emoticones.jpg')
st.image(image)
st.subheader("Cuéntale a la brújula cómo te sientes hoy y ella te dirá hacia dónde apunta tu ánimo")

translator = Translator()

with st.sidebar:
               st.subheader("Cómo leer tu brújula")
               ("""
                Polaridad: Es el norte de tu brújula. Indica si lo que escribiste suena positivo, negativo o neutral.
                Su valor oscila entre -1 (ánimo muy bajo) y 1 (ánimo muy alto), con 0 representando un día en calma.
                
               Subjetividad: Mide cuánto de tu frase nace de tus emociones y opiniones frente a lo que son hechos.
               Va de 0 a 1, donde 0 es un relato completamente objetivo y 1 es una confesión totalmente personal.

                 """
               ) 

with st.expander('Escribe en tu diario emocional'):
    text = st.text_input('¿Cómo te sientes? Escribe una frase de tu día: ')
    if text:

        translation = translator.translate(text, src="es", dest="en")
        trans_text = translation.text
        blob = TextBlob(trans_text)
        st.write('Polarity: ', round(blob.sentiment.polarity,2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity,2))
        x=round(blob.sentiment.polarity,2)
        if x > 0.0 and x <=1.0:
            st.write( 'Es un sentimiento Positivo 😊')
            color = "#2fbf71"
            fondo = "linear-gradient(160deg, #1d4d3a 0%, #2f7a56 55%, #4aa37a 100%)"
            mensaje = ("🌞 La brújula apunta al norte soleado. Tu día suena brillante: "
                       "guarda esta frase, será tu recordatorio para los días grises.")
        elif x >= -1 and x < 0:
            st.write( 'Es un sentimiento Negativo 😔')
            color = "#5b8def"
            fondo = "linear-gradient(160deg, #1a2447 0%, #2a3a73 55%, #3c4f94 100%)"
            mensaje = ("🌧️ La brújula marca tormenta, pero las tormentas pasan. "
                       "Respira hondo, toma agua y haz una pausa: lo que sientes es válido.")
        else:
            st.write( 'Es un sentimiento Neutral 😐')
            color = "#ffd666"
            fondo = "linear-gradient(160deg, #3a3a3a 0%, #55527a 55%, #6d6a96 100%)"
            mensaje = ("🌤️ La aguja está quieta: un día en calma. "
                       "Quizá es buen momento para hacer algo nuevo y mover la brújula.")

        # Interacción: el fondo de la página y la tarjeta cambian según tu sentimiento
        st.markdown(
            f"""
            <style>
            .stApp {{ background: {fondo}; }}
            .tarjeta {{ border-left-color: {color}; }}
            </style>
            <div class="tarjeta">{mensaje}</div>
            """,
            unsafe_allow_html=True,
        )            st.write('😊 Tu energía es Positiva')
            st.write('🌟 ¡Qué bonito leerte así! Guarda este momento: es combustible para los días difíciles. Compártelo con alguien que quieras.')
        elif x < 0.0 and x >= -1.0:
            st.write('😔 Tu energía es Negativa')
            st.write('🫂 Gracias por confiar en mí. Respira profundo, tómate un vaso de agua y recuerda que los días pesados también pasan. Habla con alguien de confianza si lo necesitas.')
        else:
            st.write('😐 Tu energía es Neutral')
            st.write('🍃 Un día en calma. Buen momento para hacer una pausa, escuchar tu música favorita o planear algo que te ilusione.')
