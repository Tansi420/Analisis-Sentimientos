from textblob import TextBlob
import pandas as pd
import streamlit as st
from PIL import Image
from googletrans import Translator

st.title('🌈 Espejo de Emociones')
image = Image.open('portada.jpg')
st.image(image)
st.subheader("✨ Cuéntame cómo te sientes hoy y te responderé desde el corazón")

translator = Translator()

with st.sidebar:
               st.subheader("🧭 Cómo leo tus emociones")
               ("""
                💗 Polaridad: Es la brújula de tu ánimo. Va de -1 (un día muy pesado)
                a 1 (un día radiante), y el 0 marca un estado de calma o neutralidad.

                🎭 Subjetividad: Me dice cuánto de tu frase nace de tus emociones y
                opiniones (cerca de 1) y cuánto de hechos concretos (cerca de 0).

                 """
               ) 

with st.expander('📓 Abrir mi diario emocional'):
    text = st.text_input('Escribe lo que sientes en este momento: ')
    if text:

        translation = translator.translate(text, src="es", dest="en")
        trans_text = translation.text
        blob = TextBlob(trans_text)
        st.write('💗 Nivel de ánimo (polaridad): ', round(blob.sentiment.polarity,2))
        st.write('🎭 Carga emocional (subjetividad): ', round(blob.sentiment.subjectivity,2))
        x=round(blob.sentiment.polarity,2)
        if x > 0.0 and x <=1.0:
            st.write('😊 Tu energía es Positiva')
            st.write('🌟 ¡Qué bonito leerte así! Guarda este momento: es combustible para los días difíciles. Compártelo con alguien que quieras.')
        elif x < 0.0 and x >= -1.0:
            st.write('😔 Tu energía es Negativa')
            st.write('🫂 Gracias por confiar en mí. Respira profundo, tómate un vaso de agua y recuerda que los días pesados también pasan. Habla con alguien de confianza si lo necesitas.')
        else:
            st.write('😐 Tu energía es Neutral')
            st.write('🍃 Un día en calma. Buen momento para hacer una pausa, escuchar tu música favorita o planear algo que te ilusione.')
