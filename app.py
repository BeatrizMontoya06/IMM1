import streamlit as st
import os
import time
import glob
import base64
from gtts import gTTS
from PIL import Image

# ---------------------------------------------------------
# CONFIGURACIÓN DE PÁGINA
# ---------------------------------------------------------
st.set_page_config(
    page_title="AudibleDesk v2.4 | Professional Text-to-Speech Suite",
    page_icon="🎙️",
    layout="wide"
)

# ---------------------------------------------------------
# ESTILO VISUAL: WEB 2000s CORPORATIVA / SERIA (SYSTEM SOFTWARE)
# ---------------------------------------------------------
corporate_y2k_css = """
<style>
    /* Fondo estilo escritorio/portal profesional de los 2000s */
    .stApp {
        background-color: #d4ecee;
        background-image: linear-gradient(180deg, #b8dbe0 0%, #e8f4f5 100%);
        color: #102a43;
        font-family: 'Tahoma', 'Verdana', 'Segoe UI', sans-serif;
    }

    /* Encabezados estilo Windows / Web Enterprise */
    h1 {
        color: #0b3c5d !important;
        font-family: 'Georgia', 'Times New Roman', serif;
        border-bottom: 3px double #0b3c5d;
        padding-bottom: 8px;
        font-weight: bold;
    }
    h2, h3, h4 {
        color: #1d2731 !important;
        font-family: 'Tahoma', sans-serif;
    }

    /* Contenedores con aspecto de ventana de software / biselado 3D */
    .software-card {
        background-color: #ffffff;
        border: 2px solid #829ab1;
        box-shadow: 3px 3px 0px #627d98;
        padding: 16px;
        margin-bottom: 18px;
        border-radius: 2px;
    }

    .window-header {
        background: linear-gradient(90deg, #10375c 0%, #008080 100%);
        color: #ffffff;
        padding: 6px 12px;
        font-weight: bold;
        font-size: 14px;
        margin: -16px -16px 14px -16px;
        border-bottom: 2px solid #0b3c5d;
    }

    /* Botones de acción retro tipo ejecutable */
    .stButton>button {
        background: linear-gradient(180deg, #f0f4f8 0%, #bcccdc 100%);
        color: #102a43 !important;
        border: 2px solid #486581 !important;
        box-shadow: 2px 2px 0px #243b53;
        font-weight: bold;
        font-family: 'Tahoma', sans-serif;
        border-radius: 3px !important;
        text-transform: uppercase;
        padding: 6px 16px;
    }
    .stButton>button:hover {
        background: linear-gradient(180deg, #334e68 0%, #102a43 100%);
        color: #ffffff !important;
        border-color: #102a43 !important;
    }

    /* Banner informativo superior */
    .top-banner {
        background-color: #008080;
        color: #ffffff;
        padding: 6px 12px;
        font-size: 12px;
        font-weight: bold;
        border: 1px solid #004d4d;
        margin-bottom: 15px;
    }
</style>
"""
st.markdown(corporate_y2k_css, unsafe_allow_html=True)

# Crear directorio temporal de trabajo
if not os.path.exists("temp"):
    os.makedirs("temp")

# ---------------------------------------------------------
# BARRA SUPERIOR E IDENTIDAD DE LA HERRAMIENTA
# ---------------------------------------------------------
st.markdown('<div class="top-banner">SYSTEM STATUS: ONLINE ■ AUDIBLE DESK SUITE v2.4 ■ SPEECH SYNTHESIS ENGINE</div>', unsafe_allow_html=True)

col_logo, col_title = st.columns([1, 4])

with col_logo:
    if os.path.exists('images.jpeg'):
        image = Image.open('images.jpeg')
        st.image(image, width=180)
    else:
        st.info("🖼️ [AudibleDesk System Logo]")

with col_title:
    st.title("AudibleDesk™ Pro")
    st.markdown("**Sistema Institucional de Conversión de Texto a Voz & Accesibilidad Académica**")
    st.write("Plataforma web diseñada para la síntesis de voz, lectura asistida de libros, artículos de investigación, accesibilidad audiovisual y optimización del tiempo de estudio.")

st.write("---")

# ---------------------------------------------------------
# BARRA LATERAL (SIDEBAR) - CONTEXTO Y CASOS DE USO
# ---------------------------------------------------------
with st.sidebar:
    st.subheader("🖥️ AudibleDesk Workstation")
    st.caption("Versión 2.4 - Build 2006")
    
    st.write("---")
    st.markdown("### 🎯 ¿A quién está dirigida?")
    st.markdown("""
    * **Estudiantes e Investigadores:** Escucha papers, tesis y libros mientras realizas otras tareas.
    * **Accesibilidad e Inclusión:** Herramienta de apoyo para personas con discapacidad visual, baja visión o dislexia.
    * **Docentes y Creadores:** Generación rápida de guiones narrados y material educativo auditivo.
    * **Aprendizaje de Idiomas:** Práctica de pronunciación y comprensión auditiva multilingüe.
    """)
    
    st.write("---")
    st.markdown("### 🔒 Seguridad & Privacidad")
    st.caption("• Sin Malware | Archivos generados en memoria temporal con auto-eliminación periódica.")

# ---------------------------------------------------------
# OPCIONES DE IDIOMA, REGIÓN Y CONFIGURACIÓN DE VOZ
# ---------------------------------------------------------
st.markdown('<div class="software-card"><div class="window-header">⚙️ CONFIGURACIÓN DEL MOTOR DE VOZ (SPEECH ENGINE)</div>', unsafe_allow_html=True)

col_lang, col_accent, col_speed = st.columns(3)

# Mapeo completo de idiomas y acentos (TLD)
VOICE_CONFIG = {
    "Español (Latinoamérica)": {"lg": "es", "tld": "com.mx"},
    "Español (España)": {"lg": "es", "tld": "es"},
    "Español (Estados Unidos)": {"lg": "es", "tld": "com"},
    "English (United States)": {"lg": "en", "tld": "com"},
    "English (United Kingdom)": {"lg": "en", "tld": "co.uk"},
    "English (Australia)": {"lg": "en", "tld": "com.au"},
    "English (India)": {"lg": "en", "tld": "co.in"},
    "Français (France)": {"lg": "fr", "tld": "fr"},
    "Français (Canada)": {"lg": "fr", "tld": "ca"},
    "Deutsch (Alemania)": {"lg": "de", "tld": "de"},
    "Italiano (Italia)": {"lg": "it", "tld": "it"},
    "Português (Brasil)": {"lg": "pt", "tld": "com.br"},
    "日本語 (Japonés)": {"lg": "ja", "tld": "co.jp"},
    "中文 (Chino Mandarín)": {"lg": "zh-CN", "tld": "com"}
}

with col_lang:
    opcion_seleccionada = st.selectbox("Seleccione Idioma / Región:", list(VOICE_CONFIG.keys()))

with col_accent:
    slow_speed = st.checkbox("🐢 Modo Lectura Lenta (Pausado)")

with col_speed:
    st.caption("Modo de Procesamiento:")
    st.code("gTTS Core v2.x [Active]", language="text")

st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# ÁREA DE ENTRADA DE TEXTO
# ---------------------------------------------------------
st.markdown('<div class="software-card"><div class="window-header">📄 EDITOR DE TEXTO PARA SÍNTESIS</div>', unsafe_allow_html=True)

text_input = st.text_area("Pegue o escriba aquí el fragmento del libro, artículo o documento:", height=200, placeholder="Ingrese el contenido en texto plano aquí...")

st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# FUNCIÓN Y GENERACIÓN DE AUDIO
# ---------------------------------------------------------
def text_to_speech_engine(text, lang, tld, slow):
    clean_name = f"audio_{int(time.time())}"
    file_path = f"temp/{clean_name}.mp3"
    tts = gTTS(text=text, lang=lang, tld=tld, slow=slow)
    tts.save(file_path)
    return file_path

if st.button("🎙️ SINTETIZAR Y GENERAR AUDIO"):
    if text_input.strip() == "":
        st.warning("⚠️ El campo de texto está vacío. Ingrese texto para continuar.")
    else:
        with st.spinner("Procesando síntesis de voz mediante el motor de síntesis..."):
            try:
                config = VOICE_CONFIG[opcion_seleccionada]
                file_path = text_to_speech_engine(
                    text=text_input, 
                    lang=config["lg"], 
                    tld=config["tld"], 
                    slow=slow_speed
                )
                
                st.success("✅ ¡Síntesis completada con éxito!")
                
                # Reproductor
                with open(file_path, "rb") as f:
                    audio_bytes = f.read()
                    
                st.markdown("### 🔊 Salida de Audio Generada:")
                st.audio(audio_bytes, format="audio/mp3")
                
                # Botón de descarga
                b64 = base64.b64encode(audio_bytes).decode()
                href = f'<a href="data:audio/mp3;base64,{b64}" download="audibledesk_transcripcion.mp3" style="background-color: #008080; color: white; padding: 10px 18px; text-decoration: none; font-weight: bold; border: 2px solid #004d4d; border-radius: 3px; display: inline-block;">💾 Descargar Archivo MP3</a>'
                st.markdown(href, unsafe_allow_html=True)

            except Exception as e:
                st.error(f"❌ Ocurrió un error en el motor de lectura: {e}")

st.write("---")

# ---------------------------------------------------------
# INFORMACIÓN INSTITUCIONAL Y FEEDBACK
# ---------------------------------------------------------
col_info1, col_info2, col_info3 = st.columns(3)

with col_info1:
    st.markdown('<div class="software-card"><div class="window-header">ℹ️ SOBRE LA PLATAFORMA</div>', unsafe_allow_html=True)
    st.write("AudibleDesk es una iniciativa desarrollada para optimizar el acceso al conocimiento escrito mediante tecnologías de conversión de texto a voz multilingües.")
    st.markdown('</div>', unsafe_allow_html=True)

with col_info2:
    st.markdown('<div class="software-card"><div class="window-header">❓ PREGUNTAS FRECUENTES</div>', unsafe_allow_html=True)
    st.markdown("""
    * **¿Es gratuito?** Sí, de uso libre para fines educativos y personales.
    * **¿Compatibilidad?** Funciona en ordenadores, tablets y móviles.
    * **¿Límite de caracteres?** Soporta párrafos extensos y fragmentos de libros.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with col_info3:
    st.markdown('<div class="software-card"><div class="window-header">💬 EVALUACIÓN DE SERVICIO</div>', unsafe_allow_html=True)
    modo = st.radio("¿Cómo evalúa la calidad de la síntesis?", ('Excelente', 'Aceptable', 'Requiere Mejoras'))
    if modo:
        st.caption("Agradecemos su retroalimentación para la mejora del sistema.")
    st.markdown('</div>', unsafe_allow_html=True)

# Mantenimiento de archivos antiguos en servidor
def remove_old_files(days=1):
    mp3_files = glob.glob("temp/*.mp3")
    now = time.time()
    cutoff = days * 86400
    for f in mp3_files:
        if os.stat(f).st_mtime < now - cutoff:
            try:
                os.remove(f)
            except Exception:
                pass

remove_old_files(1)
