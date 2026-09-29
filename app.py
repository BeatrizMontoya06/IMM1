import streamlit as st
from gtts import gTTS
import pypdf
import base64
import io

# Configuración de la página
st.set_page_config(
    page_title="Bee's To Speech v2.0 - Retro Y2K Edition",
    page_icon="🐝",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inicializar estados en sesión
if "audio_b64" not in st.session_state:
    st.session_state.audio_b64 = None
if "audio_bytes" not in st.session_state:
    st.session_state.audio_bytes = None
if "pdf_text" not in st.session_state:
    st.session_state.pdf_text = ""

# Inyección CSS Global para transformar toda la app a estilo Web de los 2000
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=VT323&display=swap');

    /* Fondo Turquesa Pixelado */
    .stApp {
        background-color: #008080 !important;
        background-image: 
            radial-gradient(#40e0d0 15%, transparent 16%),
            radial-gradient(#004040 15%, transparent 16%) !important;
        background-size: 16px 16px !important;
        font-family: 'MS Sans Serif', Tahoma, sans-serif !important;
    }

    /* Estilo de Contenedores y Bloques en Relieve Metalizado (Windows 98) */
    div[data-testid="stVerticalBlock"] > div {
        background: #c0c0c0;
        border: 3px solid;
        border-color: #ffffff #808080 #808080 #ffffff;
        padding: 12px;
        box-shadow: 4px 4px 10px rgba(0,0,0,0.5);
    }

    /* Etiquetas e Identificadores Retro */
    label, p, h1, h2, h3, span {
        color: #000000 !important;
        font-family: 'MS Sans Serif', Tahoma, sans-serif !important;
    }

    /* Campos de Entrada / Carga de Archivo */
    div[data-baseweb="file-uploader"], textarea, select, div[data-baseweb="select"] {
        background-color: #ffffff !important;
        border: 2px inset #808080 !important;
        font-family: monospace !important;
        color: #000000 !important;
    }

    /* Botones estilo Y2K en 3D */
    .stButton > button, div[data-testid="stDownloadButton"] > button {
        background: #c0c0c0 !important;
        color: #000000 !important;
        border: 2px solid !important;
        border-color: #ffffff #808080 #808080 #ffffff !important;
        font-weight: bold !important;
        font-size: 13px !important;
        border-radius: 0px !important;
        cursor: pointer !important;
        box-shadow: 2px 2px 0px #000000 !important;
    }

    .stButton > button:active, div[data-testid="stDownloadButton"] > button:active {
        border-color: #808080 #ffffff #ffffff #808080 !important;
        box-shadow: inset 1px 1px 0px #000000 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Encabezado Retro Y2K (Barra de Título + Marquesina + Información)
y2k_header = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=VT323&display=swap');

        body {
            font-family: Tahoma, 'MS Sans Serif', sans-serif;
            margin: 0;
            padding: 0;
            background: transparent;
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

        .title-buttons {
            display: flex;
            gap: 2px;
        }

        .win-btn {
            width: 16px;
            height: 14px;
            background: #c0c0c0;
            border: 1px solid;
            border-color: #ffffff #808080 #808080 #ffffff;
            font-size: 9px;
            line-height: 10px;
            text-align: center;
            font-weight: bold;
            color: #000;
        }

        marquee {
            background: #000;
            color: #00ff00;
            font-family: 'VT323', monospace;
            font-size: 20px;
            padding: 4px;
            border: 2px inset #808080;
            margin: 8px 0;
        }

        .retro-info {
            border: 2px inset #ffffff;
            background: #e0e0e0;
            padding: 8px;
            margin-bottom: 8px;
        }

        .retro-info h2 {
            margin: 0 0 4px 0;
            font-size: 13px;
            background: #000080;
            color: #fff;
            padding: 2px 6px;
        }
    </style>
</head>
<body>
    <div class="title-bar">
        <span>🐝 C:\\BEES_TO_SPEECH\\v2.0\\APP.EXE</span>
        <div class="title-buttons">
            <div class="win-btn">_</div>
            <div class="win-btn">□</div>
            <div class="win-btn">✕</div>
        </div>
    </div>

    <marquee scrollamount="5">
        *** BIENVENIDO A BEE'S TO SPEECH WEB 2.0 *** LA EXPERIENCIA COMPLETA DE TEXTO Y PDF A VOZ ***
    </marquee>

    <div class="retro-info">
        <h2>ℹ SOBRE LA PLATAFORMA (SYSTEM INFO)</h2>
        <p style="font-size: 12px; margin: 2px 0; color: #000;">
            <b>Bee's To Speech v2.0</b> extrae el texto de tus archivos PDF y los convierte en audio mp3 sintetizado listo para sonar en tu navegador.
        </p>
    </div>
</body>
</html>
"""
st.components.v1.html(y2k_header, height=185)

# Sección 1: Cargar PDF (Ventana Retro)
st.markdown("### 📁 1. Cargar Archivo PDF")
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
        st.error(f"Error al procesar el archivo PDF: {e}")

# Sección 2 y 3: Formulario para Texto, Voz y Reproducción
with st.form(key="tts_form"):
    st.markdown("### 📝 2. Editor de Texto / Contenido")
    user_text = st.text_area(
        label="Texto a reproducir",
        value=st.session_state.pdf_text,
        height=160,
        placeholder="Escribe tu texto aquí o sube un PDF arriba para extraer su contenido...",
        label_visibility="collapsed"
    )

    st.markdown("### 🎙️ 3. Seleccionar Voz e Idioma")
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

# Procesamiento de voz en backend
if submit_button:
    if not user_text.strip():
        st.warning("⚠️ Ingresa texto o sube un PDF antes de presionar Reproducir.")
    else:
        with st.spinner("Sintetizando voz..."):
            try:
                lang_code = voice_option[1]
                tld_code = voice_option[2]

                tts = gTTS(text=user_text, lang=lang_code, tld=tld_code, slow=False)
                
                fp = io.BytesIO()
                tts.write_to_fp(fp)
                fp.seek(0)
                
                audio_bytes = fp.read()
                st.session_state.audio_bytes = audio_bytes
                
                # Codificación base64 para el reproductor en HTML5
                b64 = base64.b64encode(audio_bytes).decode()
                st.session_state.audio_b64 = b64

            except Exception as err:
                st.error(f"Error al generar el audio: {err}")

# Reproductor Automático HTML5 con estilo Y2K + Botón para Descargar
if st.session_state.audio_b64 is not None:
    player_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            .player-card {{
                background: #e0e0e0;
                border: 2px inset #ffffff;
                padding: 12px;
                text-align: center;
                font-family: Tahoma, sans-serif;
                margin-top: 10px;
            }}
            audio {{
                width: 100%;
                margin-top: 8px;
            }}
            .status {{
                color: #008000;
                font-weight: bold;
                font-size: 13px;
                background: #000;
                padding: 4px;
                border: 1px inset #808080;
            }}
        </style>
    </head>
    <body>
        <div class="player-card">
            <div class="status">🔊 REPRODUCIENDO AUDIO AUTOMÁTICAMENTE...</div>
            <audio controls autoplay>
                <source src="data:audio/mp3;base64,{st.session_state.audio_b64}" type="audio/mp3">
                Tu navegador no soporta la reproducción de audio.
            </audio>
        </div>
    </body>
    </html>
    """
    st.components.v1.html(player_html, height=120)

    st.download_button(
        label="💾 DESCARGAR ARCHIVO MP3",
        data=st.session_state.audio_bytes,
        file_name="bees_to_speech.mp3",
        mime="audio/mp3"
    )
