<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bee's To Speech 🐝</title>
    <link rel="stylesheet" href="style.css">
    <!-- Librería PDF.js para lectura e extracción de texto de los PDFs -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.16.105/pdf.min.js"></script>
</head>
<body>
    <div class="container">
        <header>
            <h1>🐝 Bee's To Speech</h1>
            <p class="tagline">Convierte tus PDFs y textos en voz al instante</p>
        </header>

        <section class="context-card">
            <h2>Acerca de esta plataforma</h2>
            <p>
                <strong>Bee's To Speech</strong> es una herramienta diseñada para transformar documentos PDF y textos simples en audio fluido mediante síntesis de voz. Selecciona la voz de tu preferencia, ajusta la velocidad y escucha el contenido sin necesidad de instalar software adicional.
            </p>
        </section>

        <main class="app-card">
            <!-- Carga de Archivos -->
            <div class="control-group">
                <label for="pdfInput" class="file-label">📄 Cargar archivo PDF</label>
                <input type="file" id="pdfInput" accept="application/pdf">
            </div>

            <!-- Área de Texto -->
            <div class="control-group">
                <label for="textInput">Texto a reproducir:</label>
                <textarea id="textInput" rows="8" placeholder="Sube un PDF o escribe aquí el texto que quieres escuchar..."></textarea>
            </div>

            <!-- Controles de Voz -->
            <div class="settings-grid">
                <div class="control-group">
                    <label for="voiceSelect">🗣️️ Seleccionar Voz:</label>
                    <select id="voiceSelect">
                        <option value="">Cargando voces disponibles...</option>
                    </select>
                </div>

                <div class="control-group">
                    <label for="rateInput">⚡ Velocidad: <span id="rateValue">1x</span></label>
                    <input type="range" id="rateInput" min="0.5" max="2" value="1" step="0.1">
                </div>

                <div class="control-group">
                    <label for="pitchInput">🎵 Tono: <span id="pitchValue">1</span></label>
                    <input type="range" id="pitchInput" min="0.5" max="1.5" value="1" step="0.1">
                </div>
            </div>

            <!-- Botones de Acción -->
            <div class="button-group">
                <button id="playBtn" class="btn primary">▶️ Reproducir</button>
                <button id="pauseBtn" class="btn secondary">⏸️ Pausar</button>
                <button id="stopBtn" class="btn danger">⏹️ Detener</button>
            </div>
        </main>
    </div>

    <script src="app.js"></script>
</body>
</html>
