import streamlit as st
import os
import time
import glob
import base64
import re
from gTTS import gTTS
from pypdf import PdfReader

# -----------------------------------------------------------------------------
# CONFIGURACIÓN DE PÁGINA
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="AudioDoc Pro 2000 - Conversión de Documentos a Voz",
    page_icon="💾",
    layout="wide"
)

# -----------------------------------------------------------------------------
# ESTILO VISUAL RETRO AÑO 2000 (Y2K / WINDOWS 98 / CLASSIC WEB)
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    /* Tipografía clásica de los 2000 */
    html, body, [class*="css"] {
        font-family: "Tahoma", "Verdana", "Arial", sans-serif !important;
        background-color: #008080 !important; /* Color teal clásico */
        color: #000000;
    }
    
    /* Contenedor principal con diseño de ventana clásica */
    .stApp {
        background-color: #008080 !important;
    }
    
    .main .block-container {
        background-color: #c0c0c0 !important;
        border: 3px solid;
        border-color: #ffffff #808080 #808080 #ffffff;
        padding: 20px !important;
        box-shadow: 4px 4px 10px rgba(0,0,0,0.5);
        margin-top: 20px;
        margin-bottom: 20px;
    }

    /* Barra de título retro estilo ventana */
    .retro-header {
        background: linear-gradient(90deg, #000080, #1084d0);
        color: white;
        padding: 6px 12px;
        font-weight: bold;
        font-size: 16px;
        letter-spacing: 1px;
        margin-bottom: 15px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border: 1px solid #000;
    }

    /* Cajas corporativas e informativas */
    .retro-box {
        background-color: #ffffff;
        border: 2px inset #808080;
        padding: 12px;
        margin-bottom: 15px;
        font-size: 13px;
    }

    /* Botones estilo Windows 98 / 2000 */
    .stButton>button {
        background-color: #c0c0c0 !important;
        color: #000000 !important;
        border-top: 2px solid #ffffff !important;
        border-left: 2px solid #ffffff !important;
        border-right: 2px solid #000000 !important;
        border-bottom: 2px solid #000000 !important;
        font-weight: bold !important;
        font-family: "Tahoma", sans-serif !important;
        border-radius: 0px !important;
        padding: 6px 15px !important;
        box-shadow: none !important;
    }

    .stButton>button:active {
        border-top: 2px solid #000000 !important;
        border-left: 2px solid #000000 !important;
        border-right: 2px solid #ffffff !important;
        border-bottom: 2px solid #ffffff !important;
    }

    /* Sidebar retro */
    section[data-testid="stSidebar"] {
        background-color: #c0c0c0 !important;
        border-right: 3px solid #808080;
    }

    /* Banner con parpadeo suave tipo web antigua */
    .blink {
        animation: blinker 1.5s linear infinite;
        color: #000080;
        font-weight: bold;
    }
    @keyframes blinker {
        50% { opacity: 0; }
    }
    
    /* Separador retro */
    hr {
        border: 0;
        height: 2px;
        border-top: 2px solid #808080;
        border-bottom: 2px solid #ffffff;
        margin: 15px 0;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# INICIALIZACIÓN DE DIRECTORIO TEMPORAL
# -----------------------------------------------------------------------------
if not os.path.exists("temp"):
    os.makedirs("temp")

def clean_old_files(days=7):
    mp3_files = glob.glob("temp/*.mp3")
    now = time.time()
    cutoff = days * 86400
    for f in mp3_files:
        if os.stat(f).st_mtime < (now - cutoff):
            try:
                os.remove(f)
            except Exception:
                pass

clean_old_files(7)

# -----------------------------------------------------------------------------
# ENCABEZADO TIPO VENTANA Y2K
# -----------------------------------------------------------------------------
st.markdown("""
<div class="retro-header">
    <span>📟 AudioDoc_Pro_v2.01.exe - [Servicio Institucional de Lectura]</span>
    <span>[ _ ] [ 📄 ] [ X ]</span>
</div>
""", unsafe_allow_html=True)

st.title("🖨️ Sistema de Conversión Documental PDF a Voz")
st.markdown("<span class='blink'>● SERVIDOR EN LÍNEA - CONEXIÓN SEGURA 56K / ADSL</span>", unsafe_allow_html=True)

st.markdown("---")

# -----------------------------------------------------------------------------
# BARRA LATERAL: INFORMACIÓN INSTITUCIONAL ("SOMOS...")
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("### 🏢 Sobre Nuestra Empresa")
    st.markdown("""
    <div class="retro-box">
    <b>AudioDoc Technologies S.A.</b><br><br>
    Somos un centro corporativo especializado en soluciones de accesibilidad e ingeniería de procesamiento del lenguaje.
    <br><br>
    <b>Nuestra Misión:</b><br>
    Nos dedicamos a transformar documentación escrita y archivos en formato PDF en flujos de audio de alta fidelidad, promoviendo la inclusión digital, la optimización del tiempo institucional y la accesibilidad universal para empresas e instituciones educativas.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### ⚙️ Centro de Soporte")
    st.caption("Compatibilidad verificada con Netscape Navigator, Internet Explorer 5.5+ y Mozilla Firefox.")
    st.caption("© 2000 - 2026 AudioDoc Technologies Inc. Todos los derechos reservados.")

# -----------------------------------------------------------------------------
# SECCIÓN PRINCIPAL: CARGA Y LECTURA DE PDF
# -----------------------------------------------------------------------------
col_left, col_right = st.columns([1, 1])

with col_left:
    st.markdown("### 📂 1. Selección de Archivo PDF")
    uploaded_file = st.file_uploader("Cargue su archivo PDF para procesamiento:", type=["pdf"])

    extracted_text = ""
    if uploaded_file is not None:
        try:
            reader = PdfReader(uploaded_file)
            num_pages = len(reader.pages)
            
            st.success(f"Archivo cargado correctamente: {uploaded_file.name} ({num_pages} páginas)")
            
            # Selector de rango de páginas para PDFs extensos
            if num_pages > 1:
                page_range = st.slider("Seleccionar rango de páginas a procesar:", 1, num_pages, (1, min(num_pages, 5)))
                start_p, end_p = page_range[0] - 1, page_range[1]
            else:
                start_p, end_p = 0, 1

            for page_num in range(start_p, end_p):
                page = reader.pages[page_num]
                extracted_text += page.extract_text() or ""

            # Limpiar saltos de línea excesivos
            extracted_text = re.sub(r'\n+', '\n', extracted_text).strip()

        except Exception as e:
            st.error(f"Error al leer el archivo PDF: {e}")

    # Permite editar o ingresar texto manualmente
    st.markdown("### 📝 2. Contenido extraído / Texto a sintetizar")
    final_text = st.text_area(
        "Verifique o ingrese el texto que desea convertir a audio:",
        value=extracted_text,
        height=220,
        placeholder="Cargue un archivo PDF o escriba directamente su texto aquí..."
    )

with col_right:
    st.markdown("### 🎙️ 3. Configuración de Voz y Acents")
    
    # Mapeo de voces/acentos combinando código de idioma (lang) y TLD de gTTS
    voice_options = {
        "Español - España (Voz Estándar)": {"lang": "es", "tld": "es"},
        "Español - México (Voz Latinoamericana 1)": {"lang": "es", "tld": "com.mx"},
        "Español - Estados Unidos (Voz Latinoamericana 2)": {"lang": "es", "tld": "us"},
        "Español - Colombia / Internacional": {"lang": "es", "tld": "co"},
        "Inglés - Estados Unidos": {"lang": "en", "tld": "com"},
        "Inglés - Reino Unido": {"lang": "en", "tld": "co.uk"},
        "Inglés - Australia": {"lang": "en", "tld": "com.au"},
        "Francés - Francia": {"lang": "fr", "tld": "fr"},
        "Alemán - Alemania": {"lang": "de", "tld": "de"}
    }
    
    selected_voice_label = st.selectbox(
        "Seleccione el perfil de voz deseado:",
        list(voice_options.keys())
    )
    
    selected_voice = voice_options[selected_voice_label]

    st.markdown("---")
    st.markdown("### ⚡ 4. Procesamiento")
    
    if st.button("💾 GENERAR ARCHIVO DE AUDIO (.MP3)"):
        if not final_text.strip():
            st.warning("⚠️ No hay texto disponible para generar audio. Por favor ingrese texto o cargue un PDF.")
        else:
            with st.spinner("Procesando síntesis de voz en el servidor... Por favor espere."):
                try:
                    # Generar audio con gTTS
                    tts = gTTS(
                        text=final_text,
                        lang=selected_voice["lang"],
                        tld=selected_voice["tld"],
                        slow=False
                    )
                    
                    file_timestamp = int(time.time())
                    filename = f"audiodoc_{file_timestamp}.mp3"
                    filepath = os.path.join("temp", filename)
                    tts.save(filepath)

                    st.markdown("---")
                    st.markdown("### 🔊 Resultado de la Conversión")
                    
                    # Reproducción de audio
                    with open(filepath, "rb") as f:
                        audio_bytes = f.read()
                    st.audio(audio_bytes, format="audio/mp3")

                    # Botón de descarga con codificación base64
                    b64 = base64.b64encode(audio_bytes).decode()
                    href = f'''
                    <a href="data:file/mp3;base64,{b64}" download="{filename}" style="text-decoration: none;">
                        <button style="
                            background-color: #c0c0c0;
                            color: #000000;
                            border-top: 2px solid #ffffff;
                            border-left: 2px solid #ffffff;
                            border-right: 2px solid #000000;
                            border-bottom: 2px solid #000000;
                            font-weight: bold;
                            padding: 8px 16px;
                            cursor: pointer;
                        ">
                            💾 DESCARGAR ARCHIVO MP3
                        </button>
                    </a>
                    '''
                    st.markdown(href, unsafe_allow_html=True)
                    st.success("¡Síntesis finalizada con éxito!")

                except Exception as e:
                    st.error(f"Error durante el proceso de síntesis: {e}")

# -----------------------------------------------------------------------------
# PIE DE PÁGINA RETRO
# -----------------------------------------------------------------------------
st.markdown("---")
st.markdown("""
<div style="text-align: center; font-size: 11px; color: #404040;">
    <b>[ AudioDoc Pro Enterprise Edition ]</b> — Optimizado para resolución 1024x768.<br>
    Visitas: <img src="https://hitwebcounter.com/counter/counter.php?page=12345678&style=0006&nbdigits=5&type=page&initCount=1042" title="Contador de Visitas" Alt="web counter"   border="0" style="vertical-align: middle;">
</div>
""", unsafe_allow_html=True)
