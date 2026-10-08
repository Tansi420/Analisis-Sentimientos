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
        background-color: #fff6e9;
        background-image: radial-gradient(#f3d9b8 1.5px, transparent 1.5px);
        background-size: 26px 26px;
        color: #3b2f4a;
    }
    h1, h2, h3, p, label, span, div, li { color: #3b2f4a; }
    h1 {
        text-align: center;
        padding: 18px 10px;
        border-radius: 28px;
        color: #ffffff;
        background: linear-gradient(90deg, #ff7e67 0%, #ffb347 50%, #ffd166 100%);
        box-shadow: 0 8px 0 #e4684f;
    }
    h3 { text-align: center; }
    [data-testid="stSidebar"] {
        background: #ffe3d3;
        border-right: 6px dashed #ff7e67;
    }
    [data-testid="stExpander"] {
        background: #ffffff;
        border: 3px solid #3b2f4a;
        border-radius: 26px;
        box-shadow: 8px 8px 0 #3b2f4a;
    }
    .stTextInput input {
        background: #fff6e9;
        color: #3b2f4a;
        border-radius: 999px;
        border: 3px solid #ff7e67;
        padding: 10px 18px;
    }
    img {
        display: block;
        margin: 0 auto;
        border-radius: 50%;
        border: 6px solid #ffffff;
        box-shadow: 0 0 0 5px #ff7e67, 0 10px 25px rgba(59, 47, 74, 0.3);
    }
    .tarjeta {
        border-radius: 22px;
        padding: 18px 22px;
        margin-top: 14px;
        background: #ffffff;
        border: 3px solid #3b2f4a;
        box-shadow: 6px 6px 0 #ff7e67;
        font-size: 1.05rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title('🧭 Brújula Emocional')
image = Image.open('emoticones.jpg')
st.image(image, width=260)
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
            acento = "#2fbf71"
            fondo = "#e6f9ec"
            punto = "#b9ebc9"
            mensaje = ("🌞 La brújula apunta al norte soleado. Tu día suena brillante: "
                       "guarda esta frase, será tu recordatorio para los días grises.")
        elif x >= -1 and x < 0:
            st.write( 'Es un sentimiento Negativo 😔')
            acento = "#5b8def"
            fondo = "#e8efff"
            punto = "#c3d4fb"
            mensaje = ("🌧️ La brújula marca tormenta, pero las tormentas pasan. "
                       "Respira hondo, toma agua y haz una pausa: lo que sientes es válido.")
        else:
            st.write( 'Es un sentimiento Neutral 😐')
            acento = "#b08ad9"
            fondo = "#f3ecfb"
            punto = "#dccbef"
            mensaje = ("🌤️ La aguja está quieta: un día en calma. "
                       "Quizá es buen momento para hacer algo nuevo y mover la brújula.")

        # Interacción: el fondo, los puntos y los bordes cambian según tu sentimiento
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-color: {fondo};
                background-image: radial-gradient({punto} 1.5px, transparent 1.5px);
            }}
            h1 {{ background: {acento}; box-shadow: 0 8px 0 #3b2f4a; }}
            img {{ box-shadow: 0 0 0 5px {acento}, 0 10px 25px rgba(59, 47, 74, 0.3); }}
            .tarjeta {{ box-shadow: 6px 6px 0 {acento}; }}
            .stTextInput input {{ border-color: {acento}; }}
            </style>
            <div class="tarjeta">{mensaje}</div>
            """,
            unsafe_allow_html=True,
        )
