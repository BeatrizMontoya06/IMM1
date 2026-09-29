import streamlit as st
import pypdf

st.set_page_config(page_title="Bee's To Speech 🐝", page_icon="🐝", layout="centered")

# Estilos personalizados (Temática Bee's)
st.markdown("""
    <style>
    .main { background-color: #fdfbf7; }
    h1 { color: #1a1a1a; }
    .stButton>button { background-color: #ffcc00; color: #1a1a1a; font-weight: bold; border-radius: 8px; border: none; }
    .stButton>button:hover { background-color: #e6b800; }
    </style>
""", unsafe_allow_html=True)

st.title("🐝 Bee's To Speech")
st.caption("Convierte tus PDFs y textos en voz al instante")

# Contexto de la página
with st.expander("ℹ️ Acerca de esta plataforma", expanded=True):
    st.write("""
        **Bee's To Speech** es una herramienta diseñada para transformar documentos PDF 
        y textos simples en audio fluido mediante síntesis de voz en el navegador.
    """)

# Carga de archivo PDF
uploaded_file = st.file_uploader("📄 Cargar archivo PDF", type=["pdf"])

pdf_text = ""
if uploaded_file is not None:
    try:
        reader = pypdf.PdfReader(uploaded_file)
        for i, page in enumerate(reader.pages):
            extracted = page.extract_text()
            if extracted:
                pdf_text += f"--- Página {i+1} ---\n{extracted}\n\n"
    except Exception as e:
        st.error(f"Error al leer el PDF: {e}")

# Área de texto
text_to_read = st.text_area(
    "Texto a reproducir:", 
    value=pdf_text, 
    height=200, 
    placeholder="Sube un PDF o escribe aquí el texto..."
)

# Controles de audio web mediante Web Speech API
if text_to_read.strip():
    # Inyectamos el reproductor de voz con JS
    js_code = f"""
    <script>
    function speak() {{
        const text = `{text_to_read.replace('`', '')}`;
        const utterance = new SpeechSynthesisUtterance(text);
        window.speechSynthesis.cancel();
        window.speechSynthesis.speak(utterance);
    }}
    </script>
    <button onclick="speak()" style="background-color: #ffcc00; border: none; padding: 10px 20px; font-weight: bold; border-radius: 8px; cursor: pointer;">
        ▶️ Escuchar Texto
    </button>
    """
    st.components.v1.html(js_code, height=60)
