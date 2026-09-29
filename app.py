import streamlit as st
from gtts import gTTS
import pypdf
import io

# Configuración de página
st.set_page_config(
    page_title="Bee's To Speech v2.0 - Retro Y2K",
    page_icon="🐝",
    layout="centered"
)

# Estilos Web de los años 2000 (Y2K)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=VT323&display=swap');
    
    .stApp {
        background-color: #008080;
        background-image: 
            radial-gradient(#40e0d0 15%, transparent 16%),
            radial-gradient(#004040 15%, transparent 16%);
        background-size: 16px 16px;
        font-family: Tahoma, 'MS Sans Serif', sans-serif;
    }
    
    div[data-testid="stVerticalBlock"] > div {
        background: #c0c0c0;
        border: 3px solid;
        border-color: #ffffff #808080 #808080 #ffffff;
        padding: 10px;
        box-shadow: 4px 4px 10px rgba(0,0,0,0.5);
    }

    h1, h2, h3 {
        color: #000080;
        font-family: Tahoma, sans-serif;
    }

    .marquee-text {
        background: #000;
        color: #00ff00;
        font-family: 'VT323', monospace;
        font-size: 20px;
        padding: 6px;
        border: 2px inset #808080;
        margin-bottom: 15px;
    }

    /* Estilo de botones retro Y2K */
    .stButton>button {
        background: #c0c0c0 !important;
        color: #000 !important;
        border: 2px solid !important;
        border-color: #ffffff #808080 #808080 #ffffff !important;
        font-weight: bold !important;
        border-radius: 0px !important;
    }

    .stButton>button:active {
        border-color: #808080 #ffffff #ffffff #808080 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Título y Marquesina
st.title("🐝 Bee's To Speech v2.0")
st.markdown('<div class="marquee-text"><marquee scrollamount="6">*** BIENVENIDO A BEE\'S TO SPEECH *** TRANSFORMA TUS PDFS Y TEXTO EN AUDIO REAL ***</marquee></div>', unsafe_allow_html=True)

# Información del sistema
with st.expander("ℹ️ SOBRE LA PLATAFORMA (SYSTEM INFO)", expanded=True):
    st.write("Convierte archivos PDF o textos directos en voz utilizando el motor de audio en la nube.")

# Carga de archivo PDF
uploaded_file = st.file_uploader("📄 1. Cargar Documento PDF:", type=["pdf"])

pdf_extracted_text = ""
if uploaded_file is not None:
    try:
        reader = pypdf.PdfReader(uploaded_file)
        for page in reader.pages:
            text = page.extract_text()
            if text:
                pdf_extracted_text += text + "\n"
        st.success("PDF leído correctamente.")
    except Exception as e:
        st.error(f"Error al leer el PDF: {e}")

# Campo de Texto
user_text = st.text_area("📝 2. Editor de Texto a Procesar:", value=pdf_extracted_text, height=150, placeholder="Escribe tu texto o sube un PDF...")

# Selección de Voz / Idioma
st.subheader("🎙️ CONFIGURACIÓN DE VOZ")
voice_option = st.selectbox(
    "Selecciona la voz / idioma:",
    options=[
        ("Español (Latinoamérica)", "es", "com.mx"),
        ("Español (España)", "es", "es"),
        ("Inglés (EE.UU.)", "en", "com"),
        ("Inglés (Reino Unido)", "en", "co.uk"),
        ("Francés", "fr", "fr"),
        ("Italiano", "it", "it")
    ],
    format_func=lambda x: x[0]
)

# Generación y Reproducción de Audio
if st.button("▶️ GENERAR Y REPRODUCIR AUDIO"):
    if not user_text.strip():
        st.warning("Ingresa un texto o sube un PDF antes de continuar.")
    else:
        with st.spinner("Generando audio..."):
            try:
                lang_code = voice_option[1]
                tld_code = voice_option[2]

                # Generar el audio real MP3 con gTTS
                tts = gTTS(text=user_text, lang=lang_code, tld=tld_code, slow=False)
                
                # Guardar en memoria
                fp = io.BytesIO()
                tts.write_to_fp(fp)
                fp.seek(0)
                
                audio_bytes = fp.read()

                # Reproductor de Streamlit
                st.audio(audio_bytes, format="audio/mp3", start_time=0)

                # Botón de Descarga
                st.download_button(
                    label="💾 DESCARGAR AUDIO (.MP3)",
                    data=audio_bytes,
                    file_name="bees_to_speech.mp3",
                    mime="audio/mp3"
                )
                st.success("¡Audio generado con éxito!")

            except Exception as err:
                st.error(f"Error al generar el audio: {err}")
