import streamlit as st

st.set_page_config(
    page_title="Bee's To Speech v2.0 - Retro Y2K",
    page_icon="🐝",
    layout="wide",
    initial_sidebar_state="collapsed"
)

y2k_html_code = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🐝 Bee's To Speech v2.0 - Fix Edition 🐝</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.16.105/pdf.min.js"></script>
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
            font-size: 12px;
        }

        .y2k-btn:active {
            border-color: #808080 #ffffff #ffffff #808080;
        }

        .btn-primary { background: #ffcc00; }
        .btn-success { background: #00ff66; }
        .btn-danger { background: #ff4d4d; color: white; }

        .status-box {
            background: #fff;
            border: 2px inset #808080;
            padding: 5px;
            font-size: 11px;
            color: #333;
            margin-top: 5px;
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
    </div>

    <marquee scrollamount="5">
        *** BIENVENIDO A BEE'S TO SPEECH WEB 2.0 *** SI LAS VOCES NO APARECEN, HAZ CLIC EN 'CARGAR VOCES' ***
    </marquee>

    <div class="window-body">
        <!-- Contexto -->
        <div class="retro-card">
            <h2>ℹ SOBRE LA PLATAFORMA (SYSTEM INFO)</h2>
            <p style="font-size: 12px; margin: 5px 0;">
                <b>Bee's To Speech v2.0</b> es un sistema de síntesis de voz para archivos PDF y texto plano.
            </p>
        </div>

        <!-- Entrada de Archivo y Texto -->
        <div class="retro-card">
            <h2>📁 ENTRADA DE DATOS (PDF / TEXTO)</h2>
            <label style="font-size: 12px;"><b>1. Cargar Documento PDF:</b></label><br>
            <input type="file" id="pdfInput" accept="application/pdf"><br><br>

            <label style="font-size: 12px;"><b>2. Editor de Texto a Procesar:</b></label>
            <textarea id="textInput" rows="5" placeholder="Escribe tu texto o sube un PDF..."></textarea>
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
                    <select id="voiceSelect">
                        <option value="">Buscando voces del sistema...</option>
                    </select>
                </div>
            </div>

            <div style="margin-top: 8px;">
                <button class="y2k-btn" onclick="initVoices()">🔄 RECARGAR/FORZAR VOCES</button>
            </div>

            <div class="status-box" id="statusBox">
                Estado: Esperando interacción con el usuario...
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
    
    let synth = window.speechSynthesis;
    let allVoices = [];

    function updateStatus(msg) {
        document.getElementById('statusBox').innerText = "Estado: " + msg;
    }

    function initVoices() {
        if (!('speechSynthesis' in window)) {
            updateStatus("Tu navegador NO soporta la API de lectura de voz (SpeechSynthesis).");
            return;
        }

        allVoices = synth.getVoices();

        if (allVoices.length === 0) {
            updateStatus("Cargando voces...");
            // Reintento continuo para navegadores como Chrome/Edge
            let attempts = 0;
            let interval = setInterval(() => {
                allVoices = synth.getVoices();
                attempts++;
                if (allVoices.length > 0) {
                    clearInterval(interval);
                    filterVoices();
                    updateStatus("Se encontraron " + allVoices.length + " voces en el sistema.");
                } else if (attempts > 10) {
                    clearInterval(interval);
                    updateStatus("No se detectaron voces locales. Se usarán voces por defecto del navegador al dar clic en Reproducir.");
                    setupFallbackOptions();
                }
            }, 300);
        } else {
            filterVoices();
            updateStatus("Se encontraron " + allVoices.length + " voces en el sistema.");
        }
    }

    function setupFallbackOptions() {
        const select = document.getElementById('voiceSelect');
        select.innerHTML = '';
        const opt1 = document.createElement('option');
        opt1.value = "default_es";
        opt1.textContent = "Voz Predeterminada (Español)";
        select.appendChild(opt1);

        const opt2 = document.createElement('option');
        opt2.value = "default_en";
        opt2.textContent = "Voz Predeterminada (Inglés)";
        select.appendChild(opt2);
    }

    function filterVoices() {
        if (allVoices.length === 0) return;

        const lang = document.getElementById('langFilter').value;
        const select = document.getElementById('voiceSelect');
        select.innerHTML = '';

        const filtered = allVoices.filter(v => lang === 'all' || v.lang.startsWith(lang));
        
        if(filtered.length === 0) {
            select.innerHTML = '<option value="">No hay voces para este idioma</option>';
            return;
        }

        filtered.forEach((voice, index) => {
            const opt = document.createElement('option');
            opt.value = voice.name;
            opt.textContent = `${voice.name} (${voice.lang})`;
            select.appendChild(opt);
        });
    }

    if (speechSynthesis.onvoiceschanged !== undefined) {
        speechSynthesis.onvoiceschanged = initVoices;
    }

    window.onload = function() {
        initVoices();
    };

    // Lectura de PDF
    document.getElementById('pdfInput').addEventListener('change', async (e) => {
        const file = e.target.files[0];
        if (!file) return;
        document.getElementById('textInput').value = "Procesando el archivo PDF...";
        
        try {
            const arrayBuffer = await file.arrayBuffer();
            const pdf = await pdfjsLib.getDocument({ data: arrayBuffer }).promise;
            let fullText = '';
            for (let i = 1; i <= pdf.numPages; i++) {
                const page = await pdf.getPage(i);
                const content = await page.getTextContent();
                fullText += `--- Página ${i} ---\n` + content.items.map(item => item.str).join(' ') + '\n\n';
            }
            document.getElementById('textInput').value = fullText.trim();
            updateStatus("PDF cargado exitosamente.");
        } catch (err) {
            document.getElementById('textInput').value = "Error al leer el PDF.";
            updateStatus("Error al procesar el documento PDF.");
        }
    });

    // Reproducción
    function speakText() {
        const text = document.getElementById('textInput').value;
        if (!text.trim()) {
            alert("Escribe algo o sube un PDF para poder reproducir.");
            return;
        }

        // Si estaba pausado, reanudar
        if (synth.speaking && synth.isPaused) {
            synth.resume();
            updateStatus("Reanudando reproducción...");
            return;
        }

        synth.cancel(); // Cancelar reproducciones anteriores

        const utterance = new SpeechSynthesisUtterance(text);
        const voiceName = document.getElementById('voiceSelect').value;
        
        if (voiceName === "default_es") {
            utterance.lang = "es-ES";
        } else if (voiceName === "default_en") {
            utterance.lang = "en-US";
        } else {
            const selectedVoice = allVoices.find(v => v.name === voiceName);
            if (selectedVoice) {
                utterance.voice = selectedVoice;
            }
        }

        utterance.rate = parseFloat(document.getElementById('rateInput').value);
        utterance.pitch = parseFloat(document.getElementById('pitchInput').value);

        utterance.onstart = function() {
            updateStatus("🔊 Reproduciendo audio...");
        };

        utterance.onend = function() {
            updateStatus("Lectura finalizada.");
        };

        utterance.onerror = function(e) {
            updateStatus("Error de reproducción en el navegador. Intenta hacer clic en 'Recargar Voces'.");
            console.error(e);
        };

        synth.speak(utterance);
    }

    function pauseText() {
        if (synth.speaking && !synth.isPaused) {
            synth.pause();
            updateStatus("Reproducción pausada.");
        }
    }

    function stopText() {
        if (synth.speaking) {
            synth.cancel();
            updateStatus("Reproducción detenida.");
        }
    }

    // Descarga de Audio WAV
    function downloadWav() {
        const text = document.getElementById('textInput').value;
        if (!text.trim()) {
            alert('Por favor ingresa un texto antes de generar el audio.');
            return;
        }

        updateStatus("Generando archivo .WAV...");
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
        updateStatus("Archivo .WAV descargado.");
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

st.components.v1.html(y2k_html_code, height=920, scrolling=True)
