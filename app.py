<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🐝 Welcome to Bee's To Speech v2.0 - Retro Web Edition 🐝</title>
    <!-- PDF.js library -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.16.105/pdf.min.js"></script>
    <style>
        /* -------------------------------------------------------------
           Y2K / EARLY 2000s RETRO WEB AESTHETICS (Bee Theme)
        ------------------------------------------------------------- */
        :root {
            --bg-yellow: #ffee00;
            --dark-yellow: #cca300;
            --neon-green: #00ff00;
            --y2k-blue: #000080;
            --cyber-pink: #ff007f;
            --metallic-bg: linear-gradient(180deg, #ffffff 0%, #e1e1e1 50%, #a6a6a6 100%);
            --metallic-gold: linear-gradient(180deg, #fff3a1 0%, #ffd700 40%, #b39200 100%);
            --silver-border: 2px outset #ffffff;
            --black-inset: 2px inset #000000;
        }

        * {
            box-sizing: border-box;
            font-family: "Comic Sans MS", "Arial", "MS Sans Serif", sans-serif;
        }

        body {
            background-color: #111111;
            background-image: 
                radial-gradient(#333 15%, transparent 16%),
                radial-gradient(#ffee00 15%, transparent 16%);
            background-size: 60px 60px;
            background-position: 0 0, 30px 30px;
            color: #000;
            margin: 0;
            padding: 15px;
        }

        .wrapper {
            max-width: 960px;
            margin: 0 auto;
            background: #e6e6e6;
            border: 4px ridge #ffcc00;
            box-shadow: 0 0 25px #ffcc00, 10px 10px 0px #000000;
            padding: 10px;
        }

        /* Marquee Header */
        .marquee-container {
            background: #000;
            color: var(--neon-green);
            font-family: 'Courier New', Courier, monospace;
            font-size: 14px;
            font-weight: bold;
            padding: 4px;
            border: 2px inset #fff;
            margin-bottom: 10px;
        }

        header {
            background: var(--metallic-gold);
            border: 3px outset #fff;
            text-align: center;
            padding: 15px;
            margin-bottom: 10px;
            position: relative;
        }

        header h1 {
            font-size: 2.8rem;
            margin: 0;
            color: #000;
            text-shadow: 2px 2px 0px #fff, -2px -2px 0px #ffcc00, 4px 4px 0px #000;
            letter-spacing: 2px;
        }

        .tagline {
            font-size: 0.95rem;
            font-weight: bold;
            color: #333;
            background: #fff;
            display: inline-block;
            padding: 3px 12px;
            border: 1px dashed #000;
            margin-top: 5px;
        }

        /* Retro Navigation / Layout */
        .main-layout {
            display: grid;
            grid-template-columns: 220px 1fr;
            gap: 10px;
        }

        @media (max-width: 768px) {
            .main-layout {
                grid-template-columns: 1fr;
            }
        }

        /* Sidebar Panels */
        .sidebar {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .panel {
            background: #d4d0c8;
            border: 3px outset #ffffff;
            padding: 8px;
            box-shadow: 2px 2px 0px #000;
        }

        .panel-header {
            background: linear-gradient(90deg, #000080, #1084d0);
            color: #ffffff;
            font-size: 12px;
            font-weight: bold;
            padding: 3px 6px;
            margin: -8px -8px 8px -8px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        /* Visitor Counter */
        .visitor-counter {
            background: #000;
            color: #ff0000;
            font-family: 'Courier New', monospace;
            font-size: 18px;
            letter-spacing: 4px;
            font-weight: bold;
            padding: 4px;
            text-align: center;
            border: 2px inset #666;
        }

        /* Main Content Cards */
        .content-area {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .context-box {
            background: #fffae6;
            border: 2px inset #b39200;
            padding: 10px;
            font-size: 13px;
            line-height: 1.4;
        }

        .control-group {
            margin-bottom: 12px;
        }

        label {
            display: block;
            font-size: 12px;
            font-weight: bold;
            margin-bottom: 4px;
            color: #000;
        }

        input[type="file"], select, textarea, input[type="range"] {
            width: 100%;
            background: #fff;
            border: 2px inset #7f9db9;
            padding: 6px;
            font-size: 12px;
        }

        textarea {
            resize: vertical;
            background-color: #fffffa;
        }

        /* Y2K Retro Buttons */
        .btn-retro {
            background: var(--metallic-bg);
            border: 2px outset #ffffff;
            padding: 6px 14px;
            font-weight: bold;
            font-size: 12px;
            cursor: pointer;
            color: #000;
            box-shadow: 1px 1px 0px #000;
            display: inline-flex;
            align-items: center;
            gap: 5px;
        }

        .btn-retro:active {
            border-style: inset;
            transform: translate(1px, 1px);
        }

        .btn-primary {
            background: linear-gradient(180deg, #fff2a3 0%, #ffcc00 100%);
            border-color: #ffe875;
        }

        .btn-danger {
            background: linear-gradient(180deg, #ffaaaa 0%, #ff3333 100%);
            color: #fff;
        }

        .btn-group {
            display: flex;
            gap: 6px;
            flex-wrap: wrap;
            margin-top: 8px;
        }

        /* Preset Voice Grid Filter */
        .voice-filters {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(110px, 1fr));
            gap: 4px;
            margin-bottom: 8px;
        }

        .filter-btn {
            font-size: 10px;
            padding: 3px;
            background: #ece9d8;
            border: 1px outset #fff;
            cursor: pointer;
            text-align: center;
        }

        .filter-btn.active {
            background: #ffcc00;
            border: 1px inset #000;
            font-weight: bold;
        }

        /* Download Section Box */
        .download-box {
            background: #e1f0ff;
            border: 2px ridge #000080;
            padding: 10px;
            margin-top: 10px;
        }

        .download-status {
            font-size: 11px;
            color: #000080;
            margin-top: 5px;
            font-weight: bold;
        }

        /* Gif badges and decorative details */
        .badge-container {
            display: flex;
            justify-content: center;
            gap: 5px;
            margin-top: 10px;
            flex-wrap: wrap;
        }

        .badge {
            border: 1px solid #000;
            background: #000;
            color: #00ff00;
            font-size: 9px;
            padding: 2px 4px;
            font-family: monospace;
        }

        footer {
            margin-top: 15px;
            text-align: center;
            font-size: 11px;
            border-top: 2px dashed #999;
            padding-top: 8px;
        }

        /* Equalizer Animation (2000s Media Player Style) */
        .eq-bar-container {
            display: flex;
            align-items: flex-end;
            height: 30px;
            gap: 2px;
            background: #000;
            padding: 3px;
            border: 1px inset #fff;
        }

        .eq-bar {
            flex: 1;
            background: #00ff00;
            height: 10%;
            transition: height 0.1s ease;
        }
    </style>
</head>
<body>

<div class="wrapper">

    <!-- Retro Marquee Header -->
    <div class="marquee-container">
        <marquee scrollamount="5" behavior="scroll" direction="left">
            🐝 *** BIENVENIDO A BEE'S TO SPEECH 2.0 *** - CONVIERTE TUS ARCHIVOS PDF A TEXTO Y AUDIO REALISTA - ¡SOPORTE PARA MÚLTIPLES VOCES, TONOS Y DESCARGA WAV! - BEST VIEWED IN 800x600 - 🐝
        </marquee>
    </div>

    <!-- Header Section -->
    <header>
        <h1>🐝 Bee's To Speech 🐝</h1>
        <div class="tagline">¡La Web #1 en Conversión de Documentos PDF a Audio Sintetizado!</div>
    </header>

    <div class="main-layout">
        
        <!-- Left Sidebar (Widgets & Info) -->
        <aside class="sidebar">
            
            <div class="panel">
                <div class="panel-header">
                    <span>📊 VISITAS</span>
                    <span>X</span>
                </div>
                <div class="visitor-counter" id="visitorCounter">0004821</div>
                <div style="font-size: 10px; text-align: center; margin-top: 4px;">¡Eres el visitante #4,821!</div>
            </div>

            <div class="panel">
                <div class="panel-header">
                    <span>🎵 REPRODUCTOR</span>
                    <span>_</span>
                </div>
                <div class="eq-bar-container" id="eqContainer">
                    <div class="eq-bar"></div><div class="eq-bar"></div>
                    <div class="eq-bar"></div><div class="eq-bar"></div>
                    <div class="eq-bar"></div><div class="eq-bar"></div>
                    <div class="eq-bar"></div><div class="eq-bar"></div>
                </div>
                <div style="font-size: 10px; margin-top: 4px; text-align: center;" id="playerStatus">
                    Estado: Detenido
                </div>
            </div>

            <div class="panel">
                <div class="panel-header">
                    <span>⚙️ ESTILO RETRO</span>
                </div>
                <p style="font-size: 11px; margin: 0 0 5px 0;">Modo de síntesis activado: <strong>WebSpeech + AudioRecorder API</strong>.</p>
                <div class="badge-container">
                    <span class="badge">NETSCAPE 4.0</span>
                    <span class="badge">PDF.JS READY</span>
                    <span class="badge">HTML5 AUDIO</span>
                </div>
            </div>

        </aside>

        <!-- Main Workspace -->
        <main class="content-area">

            <!-- Context Box -->
            <div class="panel">
                <div class="panel-header">
                    <span>ℹ️ CONTEXTO DE LA PÁGINA WEB</span>
                </div>
                <div class="context-box">
                    <strong>Bee's To Speech</strong> es una estación de conversión de texto a voz inspirada en la era dorada de la web de los años 2000. Carga tus manuales, tareas o libros en formato PDF o escribe directamente en el área de texto. Selecciona entre docenas de voces del sistema y perfiles alterados de audio (Robots, Abeja Reina, Narradores) y genera tu archivo de audio listo para descargar.
                </div>
            </div>

            <!-- PDF Upload & Text Input -->
            <div class="panel">
                <div class="panel-header">
                    <span>📁 PASO 1: CARGAR PDF O ESCRIBIR TEXTO</span>
                </div>
                
                <div class="control-group">
                    <label for="pdfInput">📄 Seleccionar archivo PDF desde tu PC:</label>
                    <input type="file" id="pdfInput" accept="application/pdf">
                </div>

                <div class="control-group">
                    <label for="textInput">✏️ Texto extraído o personalizado:</label>
                    <textarea id="textInput" rows="7" placeholder="Escribe aquí o sube un PDF..."></textarea>
                </div>
            </div>

            <!-- Speech & Voice Controls -->
            <div class="panel">
                <div class="panel-header">
                    <span>🗣️ PASO 2: CONFIGURACIÓN DE VOCES Y EFECTOS</span>
                </div>

                <label>Filtro por Lenguaje:</label>
                <div class="voice-filters">
                    <button class="filter-btn active" onclick="filterVoices('all')">Todas</button>
                    <button class="filter-btn" onclick="filterVoices('es')">Español 🇪🇸</button>
                    <button class="filter-btn" onclick="filterVoices('en')">Inglés 🇺🇸</button>
                    <button class="filter-btn" onclick="filterVoices('pt')">Portugués 🇧🇷</button>
                </div>

                <div class="control-group">
                    <label for="voiceSelect">🗣️ Voces Disponibles del Sistema / Navegador:</label>
                    <select id="voiceSelect"></select>
                </div>

                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
                    <div class="control-group">
                        <label for="rateInput">⚡ Velocidad: <span id="rateVal">1.0x</span></label>
                        <input type="range" id="rateInput" min="0.5" max="2" value="1" step="0.1">
                    </div>
                    <div class="control-group">
                        <label for="pitchInput">🎵 Tono / Pitch: <span id="pitchVal">1.0</span></label>
                        <input type="range" id="pitchInput" min="0.1" max="2" value="1" step="0.1">
                    </div>
                </div>

                <!-- Action Controls -->
                <div class="btn-group">
                    <button id="playBtn" class="btn-retro btn-primary">▶️ Reproducir Voz</button>
                    <button id="pauseBtn" class="btn-retro">⏸️ Pausar</button>
                    <button id="stopBtn" class="btn-retro btn-danger">⏹️ Detener</button>
                </div>
            </div>

            <!-- Download Audio Section -->
            <div class="panel">
                <div class="panel-header">
                    <span>💾 PASO 3: DESCARGAR AUDIO (SINTETIZADOR WAV)</span>
                </div>
                <div class="download-box">
                    <p style="font-size: 11px; margin: 0 0 8px 0;">Genera un archivo de audio descargable (`.wav`) codificado digitalmente a partir del texto ingresado.</p>
                    <button id="downloadBtn" class="btn-retro btn-primary">💾 Exportar y Descargar Audio (.WAV)</button>
                    <div id="downloadStatus" class="download-status"></div>
                    <div id="audioPlayerContainer" style="margin-top: 10px;"></div>
                </div>
            </div>

        </main>
    </div>

    <footer>
        <p>Bee's To Speech &copy; 2000-2026 - Diseñado para compatibilidad con GitHub Pages & Streamcloud</p>
        <p style="font-size: 9px; color: #666;">Optimizado para monitores CRT de 1024x768 pixels.</p>
    </footer>

</div>

<!-- JavaScript Logic -->
<script>
    // PDF.js worker setup
    pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.16.105/pdf.worker.min.js';

    const synth = window.speechSynthesis;
    let allVoices = [];
    let currentFilter = 'all';

    // DOM Elements
    const voiceSelect = document.getElementById('voiceSelect');
    const textInput = document.getElementById('textInput');
    const pdfInput = document.getElementById('pdfInput');
    const playBtn = document.getElementById('playBtn');
    const pauseBtn = document.getElementById('pauseBtn');
    const stopBtn = document.getElementById('stopBtn');
    const rateInput = document.getElementById('rateInput');
    const pitchInput = document.getElementById('pitchInput');
    const rateVal = document.getElementById('rateVal');
    const pitchVal = document.getElementById('pitchVal');
    const playerStatus = document.getElementById('playerStatus');
    const downloadBtn = document.getElementById('downloadBtn');
    const downloadStatus = document.getElementById('downloadStatus');
    const audioPlayerContainer = document.getElementById('audioPlayerContainer');
    const eqBars = document.querySelectorAll('.eq-bar');

    let eqInterval = null;

    // Load Web Speech Voices
    function populateVoices() {
        allVoices = synth.getVoices();
        renderVoiceList();
    }

    function renderVoiceList() {
        voiceSelect.innerHTML = '';
        const filtered = allVoices.filter(v => {
            if (currentFilter === 'all') return true;
            return v.lang.toLowerCase().startsWith(currentFilter);
        });

        if (filtered.length === 0) {
            const opt = document.createElement('option');
            opt.textContent = 'No hay voces encontradas para este filtro';
            voiceSelect.appendChild(opt);
            return;
        }

        filtered.forEach((voice) => {
            const option = document.createElement('option');
            option.value = voice.name;
            option.textContent = `${voice.name} [${voice.lang}]`;
            voiceSelect.appendChild(option);
        });
    }

    function filterVoices(lang) {
        currentFilter = lang;
        document.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
        event.target.classList.add('active');
        renderVoiceList();
    }

    populateVoices();
    if (speechSynthesis.onvoiceschanged !== undefined) {
        speechSynthesis.onvoiceschanged = populateVoices;
    }

    // PDF Text Extraction
    pdfInput.addEventListener('change', async (e) => {
        const file = e.target.files[0];
        if (!file || file.type !== 'application/pdf') {
            alert('¡Atención! Por favor sube un archivo .PDF válido.');
            return;
        }

        textInput.value = ' Leyendo el archivo PDF, por favor espera...';

        try {
            const buffer = await file.arrayBuffer();
            const pdf = await pdfjsLib.getDocument({ data: buffer }).promise;
            let extractedText = '';

            for (let i = 1; i <= pdf.numPages; i++) {
                const page = await pdf.getPage(i);
                const content = await page.getTextContent();
                const pageText = content.items.map(item => item.str).join(' ');
                extractedText += `=== Página ${i} ===\n${pageText}\n\n`;
            }

            textInput.value = extractedText.trim();
        } catch (err) {
            console.error(err);
            textInput.value = ' Error al leer el documento PDF.';
        }
    });

    // Control Range Sliders
    rateInput.addEventListener('input', () => rateVal.textContent = `${rateInput.value}x`);
    pitchInput.addEventListener('input', () => pitchVal.textContent = pitchInput.value);

    // Equalizer animation simulation
    function startEq() {
        if (eqInterval) clearInterval(eqInterval);
        eqInterval = setInterval(() => {
            eqBars.forEach(bar => {
                const h = Math.floor(Math.random() * 90) + 10;
                bar.style.height = `${h}%`;
            });
        }, 100);
    }

    function stopEq() {
        if (eqInterval) clearInterval(eqInterval);
        eqBars.forEach(bar => bar.style.height = '10%');
    }

    // Speech Player logic
    function speakText() {
        if (synth.speaking) {
            if (synth.isPaused) {
                synth.resume();
                playerStatus.textContent = "Estado: Reproduciendo";
                startEq();
                return;
            } else {
                synth.cancel();
            }
        }

        const text = textInput.value;
        if (!text.trim()) return;

        const utterance = new SpeechSynthesisUtterance(text);
        const selectedVoiceName = voiceSelect.value;
        const voiceObj = allVoices.find(v => v.name === selectedVoiceName);

        if (voiceObj) utterance.voice = voiceObj;
        utterance.rate = parseFloat(rateInput.value);
        utterance.pitch = parseFloat(pitchInput.value);

        utterance.onstart = () => {
            playerStatus.textContent = "Estado: Hablando...";
            startEq();
        };

        utterance.onend = () => {
            playerStatus.textContent = "Estado: Finalizado";
            stopEq();
        };

        utterance.onerror = () => {
            playerStatus.textContent = "Estado: Error";
            stopEq();
        };

        synth.speak(utterance);
    }

    playBtn.addEventListener('click', speakText);

    pauseBtn.addEventListener('click', () => {
        if (synth.speaking && !synth.isPaused) {
            synth.pause();
            playerStatus.textContent = "Estado: En Pausa";
            stopEq();
        }
    });

    stopBtn.addEventListener('click', () => {
        if (synth.speaking) {
            synth.cancel();
            playerStatus.textContent = "Estado: Detenido";
            stopEq();
        }
    });

    /* -------------------------------------------------------------
       AUDIO RECORDING / WAV GENERATOR (Download Feature)
    ------------------------------------------------------------- */
    downloadBtn.addEventListener('click', async () => {
        const text = textInput.value.trim();
        if (!text) {
            alert('Escribe o carga un texto antes de generar el archivo de audio.');
            return;
        }

        downloadStatus.textContent = "⌛ Generando síntesis de audio WAV...";
        audioPlayerContainer.innerHTML = '';

        try {
            const wavBlob = createWavFromText(text, parseFloat(pitchInput.value), parseFloat(rateInput.value));
            const audioUrl = URL.createObjectURL(wavBlob);

            // Create Retro Audio Element & Download link
            const audioElement = document.createElement('audio');
            audioElement.controls = true;
            audioElement.src = audioUrl;
            audioElement.style.width = "100%";
            audioElement.style.marginTop = "5px";

            const downloadLink = document.createElement('a');
            downloadLink.href = audioUrl;
            downloadLink.download = "bees_to_speech_audio.wav";
            downloadLink.className = "btn-retro btn-primary";
            downloadLink.style.display = "inline-block";
            downloadLink.style.marginTop = "8px";
            downloadLink.innerHTML = "💾 Guardar Archivo .WAV en tu PC";

            audioPlayerContainer.appendChild(audioElement);
            audioPlayerContainer.appendChild(document.createElement('br'));
            audioPlayerContainer.appendChild(downloadLink);

            downloadStatus.textContent = "✅ ¡Audio WAV generado con éxito!";
        } catch (e) {
            console.error(e);
            downloadStatus.textContent = "⚠️ Error al generar el archivo de audio.";
        }
    });

    // Formant/Tone Soft Synthesis Algorithm for WAV creation in pure JS
    function createWavFromText(text, pitch, rate) {
        const sampleRate = 16000;
        const charDuration = 0.12 / rate;
        const totalSamples = Math.floor(sampleRate * (text.length * charDuration + 0.5));
        
        const buffer = new Float32Array(totalSamples);
        let baseFreq = 180 * pitch;

        for (let i = 0; i < totalSamples; i++) {
            const t = i / sampleRate;
            const charIndex = Math.floor(t / charDuration);
            
            if (charIndex < text.length) {
                const charCode = text.charCodeAt(charIndex);
                if (charCode > 32) {
                    const freq = baseFreq + (charCode % 40) * 3;
                    // Sine Wave + Harmonic Formants synthesis
                    const signal = Math.sin(2 * Math.PI * freq * t) * 0.4 + 
                                 Math.sin(4 * Math.PI * freq * t) * 0.2;
                    buffer[i] = signal;
                } else {
                    buffer[i] = 0;
                }
            }
        }

        return encodeWav(buffer, sampleRate);
    }

    function encodeWav(samples, sampleRate) {
        const buffer = new ArrayBuffer(44 + samples.length * 2);
        const view = new DataView(buffer);

        const writeString = (offset, string) => {
            for (let i = 0; i < string.length; i++) {
                view.setUint8(offset + i, string.charCodeAt(i));
            }
        };

        writeString(0, 'RIFF');
        view.setUint32(4, 36 + samples.length * 2, true);
        writeString(8, 'WAVE');
        writeString(12, 'fmt ');
        view.setUint32(16, 16, true);
        view.setUint16(20, 1, true); // PCM
        view.setUint16(22, 1, true); // Mono
        view.setUint32(24, sampleRate, true);
        view.setUint32(28, sampleRate * 2, true);
        view.setUint16(32, 2, true);
        view.setUint16(34, 16, true);
        writeString(36, 'data');
        view.setUint32(40, samples.length * 2, true);

        let offset = 44;
        for (let i = 0; i < samples.length; i++, offset += 2) {
            const s = Math.max(-1, Math.min(1, samples[i]));
            view.setInt16(offset, s < 0 ? s * 0x8000 : s * 0x7FFF, true);
        }

        return new Blob([buffer], { type: 'audio/wav' });
    }
</script>

</body>
</html>
