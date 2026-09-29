import streamlit as st

# Configuración de página de Streamlit
st.set_page_config(
    page_title="Bee's To Speech v2.0 - Retro Y2K",
    page_icon="🐝",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Renderizado de la aplicación HTML/JS/CSS Y2K completa
y2k_html_code = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🐝 Bee's To Speech v2.0 - Retro Web Edition 🐝</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.16.105/pdf.min.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=VT323&family=MS+Sans+Serif&display=swap');

        body {
            background-color: #008080;
            background-image: 
                radial-gradient(#40e0d0 15%, transparent 16%),
                radial-gradient(#004040 15%, transparent 16%);
            background-size: 16px 16px;
            font-family: 'MS Sans Serif', Tahoma, sans-serif;
            margin: 0;
            padding: 10px;
            color: #000;
        }

        .y2k-container {
            max-width: 900px;
            margin: 0 auto;
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

        .title-bar-buttons button {
            width: 16px;
            height: 14px;
            font-size: 9px;
            line-height: 10px;
            padding: 0;
            margin-left: 2px;
            background: #c0c0c0;
            border: 1px solid;
            border-color: #ffffff #808080 #808080 #ffffff;
            cursor: pointer;
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

        .window-body {
            padding: 10px;
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

        textarea, select, input[type="file"], input[type="range"] {
            width: 100%;
            box-sizing: border-box;
            background: #fff;
            border: 2px inset #808080;
            font-family: monospace;
            padding: 4px;
        }

        .btn-group {
            display: flex;
            gap: 8px;
            margin-top: 10px;
            flex-wrap: wrap;
        }

        .y2k-btn {
            background: #c0c0c0;
            border: 2px solid;
            border-color: #ffffff #808080 #808080 #ffffff;
            padding: 6px 12px;
            font-weight: bold;
            cursor: pointer;
            font-family: sans-serif;
            font-size: 12px;
        }

        .y2k-btn:active {
            border-color: #808080 #ffffff #ffffff #808080;
        }

        .btn-primary { background: #ffcc00; }
        .btn-success { background: #00ff66; }
        .btn-danger { background: #ff4d4d; color: white; }

        .counter-box {
            background: #000;
            color: #ff0000;
            font-family: 'VT323', monospace;
            font-size: 20px;
            padding: 2px 8px;
            display: inline-block;
            border: 2px inset #808080;
        }

        .grid-2 {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
        }

        @media (max-width: 600px) {
            .grid-2 { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>

<div class="y2k-container">
    <div class="title-bar">
        <span>🐝 C:\\BEES_TO_SPEECH\\v2.0\\APP.EXE</span>
        <div class="title-bar-buttons">
            <button>_</button>
            <button>□</button>
            <button>✕</button>
        </div>
    </div>

    <marquee scrollamount="5">
        *** BIENVENIDO A BEE'S TO SPEECH WEB 2.0 *** LA MEJOR EXPERIENCIA DE TEXTO A VOZ DEL MILENIO *** CONVIERTE TUS PDFS A AUDIO AL INSTANTE ***
    </marquee>

    <div class="window-body">
        <!-- Contexto Y2K -->
        <div class="retro-card">
            <h2>ℹ️️ SOBRE LA PLATAFORMA (SYSTEM INFO)</h2>
            <p style="font-size: 12px; margin: 5px 0;">
                <b>Bee's To Speech v2.0</b> es un sistema avanzado de síntesis de voz diseñado para procesar archivos PDF y texto plano directamente desde tu navegador. Ajusta el tono, selecciona entre múltiples frecuencias/voces y descarga el archivo de audio simulado.
            </p>
            <p style="font-size: 11px;">
                Visitas totales: <span class="counter-box">004289</span> | Estado del servidor: <span style="color: green; font-weight: bold;">ONLINE</span>
            </p>
        </div>

        <!-- Entrada de Archivo y Texto -->
        <div class="retro-card">
            <h2>📁 ENTRADA DE DATOS (PDF / TEXTO)</h2>
            <label style="font-size: 12px;"><b>1. Cargar Documento PDF:</b></label><br>
            <input type="file" id="pdfInput" accept="application/pdf"><br><br>

            <label style="font-size: 12px;"><b>2. Editor de Texto a Procesar:</b></label>
            <textarea id="textInput" rows="6" placeholder="Escribe tu texto o sube un PDF..."></textarea>
        </div>

        <!-- Controles de Voz -->
        <div class="retro-card">
            <h2>🎙️ CONFIGURACIÓN DEL SINTETIZADOR DE VOZ</h2>
            
            <div class="grid-2">
                <div>
                    <label style="font-size: 11px;"><b>Filtrar Idioma:</b></label>
                    <select id="langFilter" onchange="filterVoices()">
                        <option value="all">Todas las voces</option>
                        <option value="es">Español (es)</option>
                        <option value="en">Inglés (en)</option>
                    </select>
                </div>

                <div>
                    <label style="font-size: 11px;"><b>Seleccionar Voz:</b></label>
                    <select id="voiceSelect"><option>Cargando voces del sistema...</option></select>
                </div>
            </div>

            <br>

            <div class="grid-2">
                <div>
                    <label style="font-size: 11px;"><b>Velocidad: <span id="rateVal">1.0x</span></b></label>
                    <input type="range" id="rateInput" min="0.5" max="2" value="1" step="0.1" oninput="document.getElementById('rateVal').innerText=this.value+'x'">
                </div>

                <div>
                    <label style="font-size: 11px;"><b>Tono (Pitch): <span id="pitchVal">1.0</span></b></label>
                    <input type="range" id="pitchInput" min="0.5" max="1.5" value="1" step="0.1" oninput="document.getElementById('pitchVal').innerText=this.value">
                </div>
            </div>
        </div>

        <!-- Controles de Acción -->
        <div class="retro-card" style="text-align: center;">
            <div class="btn-group" style="justify-content: center;">
                <button class="y2k-btn btn-primary" onclick="speakText()">▶️ REPRODUCIR</button>
                <button class="y2k-btn" onclick="pauseText()">⏸️ PAUSAR</button>
                <button class="y2k-btn btn-danger" onclick="stopText()">⏹️ DETENER</button>
                <button class="y2k-btn btn-success" onclick="downloadWav()">💾 DESCARGAR AUDIO (.WAV)</button>
            </div>
        </div>
    </div>
</div>

<script>
    pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.16.105/pdf.worker.min.js';
    const synth = window.speechSynthesis;
    let allVoices = [];

    function populateVoices() {
        allVoices = synth.getVoices();
        filterVoices();
    }

    function filterVoices() {
        const lang = document.getElementById('langFilter').value;
        const select = document.getElementById('voiceSelect');
        select.innerHTML = '';

        const filtered = allVoices.filter(v => lang === 'all' || v.lang.startsWith(lang));
        
        if(filtered.length === 0) {
            select.innerHTML = '<option>No se encontraron voces para este idioma</option>';
            return;
        }

        filtered.forEach((voice) => {
            const opt = document.createElement('option');
            opt.value = voice.name;
            opt.textContent = `${voice.name} (${voice.lang})`;
            select.appendChild(opt);
        });
    }

    populateVoices();
    if (speechSynthesis.onvoiceschanged !== undefined) {
        speechSynthesis.onvoiceschanged = populateVoices;
    }

    // Extracción PDF
    document.getElementById('pdfInput').addEventListener('change', async (e) => {
        const file = e.target.files[0];
        if (!file) return;
        document.getElementById('textInput').value = "Leyendo archivo PDF...";
        
        try {
            const arrayBuffer = await file.arrayBuffer();
            const pdf = await pdfjsLib.getDocument({ data: arrayBuffer }).promise;
            let fullText = '';
            for (let i = 1; i <= pdf.numPages; i++) {
                const page = await pdf.getPage(i);
                const content = await page.getTextContent();
                fullText += `--- Página ${i} ---\n` + content.items.map(item => item.str).join(' ') + '\n\n';
            }
            document.getElementById('textInput').value = fullText;
        } catch (err) {
            document.getElementById('textInput').value = "Error al procesar el PDF.";
        }
    });

    // Reproducción TTS
    function speakText() {
        if (synth.speaking && synth.isPaused) {
            synth.resume();
            return;
        }
        synth.cancel();

        const text = document.getElementById('textInput').value;
        if (!text.trim()) return;

        const utterance = new SpeechSynthesisUtterance(text);
        const voiceName = document.getElementById('voiceSelect').value;
        const selectedVoice = allVoices.find(v => v.name === voiceName);
        
        if (selectedVoice) utterance.voice = selectedVoice;
        utterance.rate = parseFloat(document.getElementById('rateInput').value);
        utterance.pitch = parseFloat(document.getElementById('pitchInput').value);

        synth.speak(utterance);
    }

    function pauseText() {
        if (synth.speaking) synth.pause();
    }

    function stopText() {
        if (synth.speaking) synth.cancel();
    }

    // Descarga de Audio WAV Generado
    function downloadWav() {
        const text = document.getElementById('textInput').value;
        if (!text.trim()) {
            alert('Por favor ingresa un texto antes de generar el audio.');
            return;
        }

        const sampleRate = 22050;
        const pitch = parseFloat(document.getElementById('pitchInput').value);
        const durationSec = Math.max(2, text.length * 0.08);
        const numSamples = Math.floor(sampleRate * durationSec);
        
        const buffer = new Int16Array(numSamples);
        const baseFreq = 180 * pitch;

        for (let i = 0; i < numSamples; i++) {
            const t = i / sampleRate;
            const envelope = Math.sin((i / numSamples) * Math.PI);
            const val = Math.sin(2 * Math.PI * baseFreq * t) * 0.3 +
                        Math.sin(2 * Math.PI * (baseFreq * 1.5) * t) * 0.2;
            buffer[i] = val * 32767 * envelope;
        }

        const wavHeader = createWavHeader(numSamples * 2, sampleRate);
        const blob = new Blob([wavHeader, buffer], { type: 'audio/wav' });
        const url = URL.createObjectURL(blob);

        const a = document.createElement('a');
        a.href = url;
        a.download = 'bees_to_speech_audio.wav';
        a.click();
        URL.revokeObjectURL(url);
    }

    function createWavHeader(dataSize, sampleRate) {
        const buffer = new ArrayBuffer(44);
        const view = new DataView(buffer);

        function writeString(offset, string) {
            for (let i = 0; i < string.length; i++) {
                view.setUint8(offset + i, string.charCodeAt(i));
            }
        }

        writeString(0, 'RIFF');
        view.setUint32(4, 36 + dataSize, true);
        writeString(8, 'WAVE');
        writeString(12, 'fmt ');
        view.setUint32(16, 16, true);
        view.setUint16(20, 1, true);
        view.setUint16(22, 1, true);
        view.setUint32(24, sampleRate, true);
        view.setUint32(28, sampleRate * 2, true);
        view.setUint16(32, 2, true);
        view.setUint16(34, 16, true);
        writeString(36, 'data');
        view.setUint32(40, dataSize, true);

        return buffer;
    }
</script>

</body>
</html>
"""

# Renderizado dentro del contenedor de Streamlit
st.components.v1.html(y2k_html_code, height=900, scrolling=True)
