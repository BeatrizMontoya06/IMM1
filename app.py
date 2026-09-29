import streamlit as st
from gTTS import gTTS
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

# Inicializar estados en la sesión de Streamlit
if "audio_b64" not in st.session_state:
    st.session_state.audio_b64 = None
if "audio_bytes" not in st.session_state:
    st.session_state.audio_bytes = None
if "pdf_text" not in st.session_state:
    st.session_state.pdf_text = ""

# Procesar carga de archivo PDF
uploaded_file = st.file_uploader("Cargar PDF (opcional)", type=["pdf"], key="pdf_uploader", label_visibility="collapsed")

if uploaded_file is not None:
    try:
        reader = pypdf.PdfReader(uploaded_file)
        text_acc = ""
        for i, page in enumerate(reader.pages):
            extracted = page.extract_text()
            if extracted:
                text_acc += f"--- Página {i+1} ---\n{extracted}\n\n"
        st.session_state.pdf_text = text_acc
    except Exception as e:
        st.error(f"Error leyendo el PDF: {e}")

# Captura de datos vía Formulario de Streamlit para sincronizar botones e inputs
with st.form(key="tts_form"):
    # Interfaz Y2K
    y2k_html_header = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <style>
            @import url('https://fonts.googleapis.com/css2?family=VT323&display=swap');

            body {{
                background-color: #008080;
                background-image: 
                    radial-gradient(#40e0d0 15%, transparent 16%),
                    radial-gradient(#004040 15%, transparent 16%);
                background-size: 16px 16px;
                font-family: Tahoma, 'MS Sans Serif', sans-serif;
                margin: 0;
                padding: 0;
                color: #000;
            }}

            .y2k-container {{
                background: #c0c0c0;
                border: 3px solid;
                border-color: #ffffff #808080 #808080 #ffffff;
                padding: 8px;
                box-shadow: 5px 5px 15px rgba(0,0,0,0.5);
            }}

            .title-bar {{
                background: linear-gradient(90deg, #000080, #1084d0);
                color: white;
                padding: 4px 8px;
                font-weight: bold;
                font-size: 14px;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }}

            marquee {{
                background: #000;
                color: #00ff00;
                font-family: 'VT323', monospace;
                font-size: 18px;
                padding: 4px;
                border: 2px inset #808080;
                margin: 8px 0;
            }}

            .retro-card {{
                border: 2px inset #ffffff;
                background: #e0e0e0;
                padding: 10px;
                margin-bottom: 12px;
            }}

            .retro-card h2 {{
                margin-top: 0;
                font-size: 14px;
                background: #000080;
                color: #fff;
                padding: 3px 6px;
            }}
        </style>
    </head>
    <body>
    <div class="y2k-container">
        <div class="title-bar">
            <span>🐝 C:\\BEES_TO_SPEECH\\v2.0\\APP.EXE</span>
        </div>

        <marquee scrollamount="5">
            *** BIENVENIDO A BEE'S TO SPEECH WEB 2.0 *** TUS PDFS Y TEXTOS SONARÁN DIRECTAMENTE EN TU NAVEGADOR ***
        </marquee>

        <div class="retro-card">
            <h2>ℹ SOBRE LA PLATAFORMA (SYSTEM INFO)</h2>
            <p style="font-size: 12px; margin: 3px 0;">
                <b>Bee's To Speech v2.0</b> convierte documentos PDF y texto en audio fluido de alta calidad que se reproduce automáticamente dentro de la página.
            </p>
        </div>
    </div>
    </body>
    </html>
    """
    st.components.v1.html(y2k_html_header, height=190)

    st.markdown("### 📁 1. Editor de Texto / Contenido del PDF:")
    user_text = st.text_area(
        label="Texto a procesar",
        value=st.session_state.pdf_text,
        height=180,
        placeholder="Escribe tu texto aquí o sube un PDF arriba...",
        label_visibility="collapsed"
    )

    st.markdown("### 🎙️ 2. Selecciona la Voz / Idioma:")
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

# Procesar generación de audio al enviar el formulario
if submit_button:
    if not user_text.strip():
        st.warning("⚠️ Escribe un texto o sube un PDF antes de presionar Reproducir.")
    else:
        with st.spinner("Generando sintetizador de audio..."):
            try:
                lang_code = voice_option[1]
                tld_code = voice_option[2]

                # Síntesis TTS con gTTS
                tts = gTTS(text=user_text, lang=lang_code, tld=tld_code, slow=False)
                
                fp = io.BytesIO()
                tts.write_to_fp(fp)
                fp.seek(0)
                
                audio_bytes = fp.read()
                st.session_state.audio_bytes = audio_bytes
                
                # Convertir a Base64 para reproducción automática vía HTML5
                b64 = base64.b64encode(audio_bytes).decode()
                st.session_state.audio_b64 = b64

            except Exception as err:
                st.error(f"Error generando el audio: {err}")

# Renderizar reproductor de audio Y2K con Autoplay + Botón de Descarga
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

    # Botón de Descarga
    st.download_button(
        label="💾 DESCARGAR AUDIO (.MP3)",
        data=st.session_state.audio_bytes,
        file_name="bees_to_speech.mp3",
        mime="audio/mp3"
    )
