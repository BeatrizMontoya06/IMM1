import streamlit as st
from gtts import gTTS
import pypdf
import base64
import io

# Configuración de la página
st.set_page_config(
    page_title="Bee's To Speech v2.0 - Retro Y2K",
    page_icon="🐝",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inicializar estados de sesión
if "audio_b64" not in st.session_state:
    st.session_state.audio_b64 = None
if "audio_bytes" not in st.session_state:
    st.session_state.audio_bytes = None
if "pdf_text" not in st.session_state:
    st.session_state.pdf_text = ""

# Cabecera Retro Y2K
y2k_html_header = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=VT323&display=swap');

        body {
            background-color: #008080;
            background-image: 
                radial-gradient(#40e0d0 15%, transparent 16%),
                radial-gradient(#004040 15%, transparent 16%);
            background-size: 16px 16px;
            font-family: Tahoma, 'MS Sans Serif', sans-serif;
            margin: 0;
            padding: 0;
            color: #000;
        }

        .y2k-container {
            background: #c0c0c0;
            border: 3px solid;
            border-color: #ffffff #808080 #808080 #ffffff;
            padding: 8px;
            box-shadow: 5px 5px 15px rgba(0,0,0,0.5);
        }

        .title-bar {
            background: linear-gradient(90deg, #000080, #1084d0);
            color: white;
            padding: 4px 8px;
            font-weight: bold;
            font-size: 14px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        marquee {
            background: #000;
            color: #00ff00;
            font-family: 'VT323', monospace;
            font-size: 18px;
            padding: 4px;
            border: 2px inset #808080;
            margin: 8px 0;
        }

        .retro-card {
            border: 2px inset #ffffff;
            background: #e0e0e0;
            padding: 10px;
            margin-bottom: 12px;
        }

        .retro-card h2 {
            margin-top: 0;
            font-size: 14px;
            background: #000080;
            color: #fff;
            padding: 3px 6px;
        }
    </style>
</head>
<body>
<div class="y2k-container">
    <div class="title-bar">
        <span>🐝 C:\\BEES_TO_SPEECH\\v2.0\\APP.EXE</span>
    </div>

    <marquee scrollamount="5">
        *** BIENVENIDO A BEE'S TO SPEECH WEB 2.0 *** CARGA TU ARCHIVO PDF O ESCRIBE TEXTO Y ESCÚCHALO AL INSTANTE ***
    </marquee>

    <div class="retro-card">
        <h2>ℹ SOBRE LA PLATAFORMA (SYSTEM INFO)</h2>
        <p style="font-size: 12px; margin: 3px 0;">
            <b>Bee's To Speech v2.0</b> convierte tus documentos PDF y textos a voz con reproducción automática directa en tu navegador.
        </p>
    </div>
</div>
</body>
</html>
"""
st.components.v1.html(y2k_html_header, height=190)

# Sección 1: Cargar PDF (Fuera del formulario para procesarlo al instante)
st.markdown("### 📄 1. Cargar Archivo PDF:")
uploaded_file = st.file_uploader(
    "Selecciona un archivo PDF desde tu equipo", 
    type=["pdf"], 
    key="pdf_uploader"
)

if uploaded_file is not None:
    try:
        reader = pypdf.PdfReader(uploaded_file)
        text_acc = ""
        for i, page in enumerate(reader.pages):
            extracted = page.extract_text()
            if extracted:
                text_acc += f"--- Página {i+1} ---\n{extracted}\n\n"
        st.session_state.pdf_text = text_acc
        st.success("✅ Texto extraído del PDF con éxito.")
    except Exception as e:
        st.error(f"Error al leer el PDF: {e}")

# Formulario principal de texto y voz
with st.form(key="tts_form"):
    st.markdown("### 📝 2. Editor de Texto / Contenido:")
    user_text = st.text_area(
        label="Texto a reproducir",
        value=st.session_state.pdf_text,
        height=180,
        placeholder="Escribe tu texto aquí o sube un PDF arriba para extraer su contenido...",
        label_visibility="collapsed"
    )

    st.markdown("### 🎙️ 3. Selecciona la Voz / Idioma:")
    voice_option = st.selectbox(
        "Voz",
        options=[
            ("🇪🇸 Español (Latinoamérica)", "es", "com.mx"),
            ("🇪🇸 Español (España)", "es", "es"),
            ("🇺🇸 Inglés (EE.UU.)", "en", "com"),
            ("🇬🇧 Inglés (Reino Unido)", "en", "co.uk"),
            ("🇫🇷 Francés", "fr", "fr"),
            ("🇮🇹 Italiano", "it", "it")
        ],
        format_func=lambda x: x[0],
        label_visibility="collapsed"
    )

    submit_button = st.form_submit_button("▶️ REPRODUCIR AUDIO EN LA PÁGINA")

# Generar síntesis de voz al hacer clic
if submit_button:
    if not user_text.strip():
        st.warning("⚠️ Escribe un texto o sube un PDF antes de presionar Reproducir.")
    else:
        with st.spinner("Generando audio..."):
            try:
                lang_code = voice_option[1]
                tld_code = voice_option[2]

                tts = gTTS(text=user_text, lang=lang_code, tld=tld_code, slow=False)
                
                fp = io.BytesIO()
                tts.write_to_fp(fp)
                fp.seek(0)
                
                audio_bytes = fp.read()
                st.session_state.audio_bytes = audio_bytes
                
                # Base64 para reproducción con autoplay
                b64 = base64.b64encode(audio_bytes).decode()
                st.session_state.audio_b64 = b64

            except Exception as err:
                st.error(f"Error al generar el audio: {err}")

# Reproductor automático HTML5 + Descarga
if st.session_state.audio_b64 is not None:
    player_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            .player-card {{
                background: #e0e0e0;
                border: 2px inset #ffffff;
                padding: 15px;
                text-align: center;
                font-family: Tahoma, sans-serif;
                margin-top: 10px;
            }}
            audio {{
                width: 100%;
                margin-top: 10px;
            }}
            .status {{
                color: #008000;
                font-weight: bold;
                font-size: 13px;
                margin-bottom: 8px;
            }}
        </style>
    </head>
    <body>
        <div class="player-card">
            <div class="status">🔊 REPRODUCIENDO AUDIO AUTOMÁTICAMENTE...</div>
            <audio controls autoplay>
                <source src="data:audio/mp3;base64,{st.session_state.audio_b64}" type="audio/mp3">
                Tu navegador no soporta el reproductor de audio.
            </audio>
        </div>
    </body>
    </html>
    """
    st.components.v1.html(player_html, height=120)

    st.download_button(
        label="💾 DESCARGAR AUDIO (.MP3)",
        data=st.session_state.audio_bytes,
        file_name="bees_to_speech.mp3",
        mime="audio/mp3"
    )
