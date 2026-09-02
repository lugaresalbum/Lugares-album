import os

# Create HTML content
index_html = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LUGARES — Mateo Fuertes</title>
    <!-- Google Fonts for Editorial Typography -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <main class="paper-container">
        <!-- Cabecera discreta superior -->
        <header class="header-meta">
            <span class="album-title">LUGARES</span>
            <span class="year">2026</span>
        </header>

        <hr class="divider-top">

        <!-- Contenido principal del manifiesto -->
        <article class="manifesto-content">
            <h1 class="manifesto-title">Manifiesto de los lugares</h1>

            <p>La identidad construye su sentido en los lugares. Toma cuerpo cuando existe un espacio donde puede circular y permanecer.</p>
            
            <p>Un lugar es un territorio -físico o metafísico-, en el que una persona, y más aún un grupo de personas, ponen en práctica su identidad. Un marco donde el ser se despliega, se constituye y, fundamentalmente, se relaciona con el ser trascendente de la comunidad.</p>
            
            <p>Un lugar es tal en la medida en que nos reconocemos ahí, y a la vez podemos ser reconocidos por otros. Donde no somos indiferentes al entorno, ni el entorno nos es indiferente.</p>
            
            <p>Podemos pensar los lugares, también, de forma relacional, en tensión con el concepto de los no-lugares: espacios donde la experiencia se reduce al tránsito, donde la relación con el entorno es meramente protocolar, donde no se exige ni se produce memoria. Aeropuertos, autopistas, shoppings, estaciones de servicio, hoteles, peajes.</p>

            <div class="section-separator">-</div>

            <p>Asistimos hoy al reinado de los no-lugares. En el bolsillo llevamos siempre un ejemplar. Ahí nuestra presencia es constante, pero despojada de sentido. No hay esencia, es el terreno de la pura circunstancia. La interacción se fragmenta, pierde el marco que la articula.</p>
            
            <p>Este disco vuelve la mirada hacia los lugares, el arraigo, la tradición en su sentido más amplio, la posibilidad de reconocerse en un espacio que permita, a la vez, reconocerse en un otro. Es, ante todo, una reivindicación de la pertenencia.</p>
            
            <p>La música es muchas veces, (claro está, no siempre), un lugar. Lo es porque funciona como anclaje de la emocionalidad colectiva; como punto de unión; como forma de inscripción en un grupo.</p>
            
            <p>Aunque compuestas de forma independiente, estas canciones adquirieron sentido conjunto porque, sea en la superficie o en la profundidad, todas participan del concepto de lugar. Queriéndolo o no, han sido un ejercicio de reconocimiento de aquellos lugares que me definen y que intento habitar; que me proyectan y en los que me proyecto; de todos los rincones -¡vaya palabra!- que cargo conmigo.</p>
        </article>

        <!-- Pie de página con enlaces y firma -->
        <footer class="footer-container">
            <hr class="divider-bottom">
            <div class="footer-links-row">
                <div class="audio-links">
                    <!-- ============================================================== -->
                    <!-- REEMPLAZAR AQUÍ LOS ENLACES CUANDO TENGAS LAS URLS DEFINITIVAS -->
                    <!-- ============================================================== -->
                    <a href="https://open.spotify.com" target="_blank" rel="noopener noreferrer" class="link-item">Spotify</a>
                    <a href="https://youtube.com" target="_blank" rel="noopener noreferrer" class="link-item">YouTube</a>
                    <!-- ============================================================== -->
                </div>
                <div class="artist-name">
                    Mateo Fuertes
                </div>
            </div>
        </footer>
    </main>

</body>
</html>
"""

# Create CSS content
style_css = """/* ==========================================================================
   RESET & ESTILOS BASE
   ========================================================================== */
*, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

/* Fondo exterior sutilmente más oscuro para crear el efecto de "hoja sobre mesa/superficie" */
body {
    background-color: #e6e3dd;
    color: #2b2927;
    font-family: 'Cormorant Garamond', Georgia, 'Times New Roman', serif;
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: flex-start;
    padding: 40px 20px;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

/* ==========================================================================
   HOJA PRINCIPAL (PAPER CONTAINER)
   ========================================================================== */
.paper-container {
    background-color: #fcfbf7; /* Blanco cálido / Marfil / Papel de libro */
    width: 100%;
    max-width: 860px;
    padding: 70px 90px;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.03), 0 1px 3px rgba(0, 0, 0, 0.02);
    border-radius: 2px;
}

/* ==========================================================================
   CABECERA
   ========================================================================== */
.header-meta {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-family: 'Inter', -apple-system, sans-serif;
    font-size: 11px;
    font-weight: 400;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: #726e68;
    margin-bottom: 20px;
}

.divider-top {
    border: none;
    border-top: 1px solid #e2ded7;
    margin-bottom: 80px;
}

/* ==========================================================================
   TEXTO Y MANIFIESTO
   ========================================================================== */
.manifesto-content {
    max-width: 640px; /* Columna estrecha para máxima legibilidad editorial */
    margin: 0 auto;
    text-align: left;
}

.manifesto-title {
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 38px;
    font-weight: 500;
    line-height: 1.25;
    letter-spacing: -0.01em;
    color: #1a1918;
    margin-bottom: 50px;
}

.manifesto-content p {
    font-size: 20px;
    line-height: 1.75;
    font-weight: 400;
    color: #2b2927;
    margin-bottom: 28px;
    text-align: left;
}

.section-separator {
    text-align: center;
    font-size: 20px;
    color: #8c867e;
    margin: 50px 0;
}

/* ==========================================================================
   PIE DE PÁGINA Y ENLACES
   ========================================================================== */
.footer-container {
    max-width: 640px;
    margin: 100px auto 0 auto;
}

.divider-bottom {
    border: none;
    border-top: 1px solid #e2ded7;
    margin-bottom: 25px;
}

.footer-links-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-family: 'Inter', -apple-system, sans-serif;
    font-size: 12px;
    letter-spacing: 0.15em;
    text-transform: uppercase;
}

.audio-links {
    display: flex;
    gap: 30px;
}

.link-item {
    color: #55514b;
    text-decoration: none;
    transition: color 0.3s ease, opacity 0.3s ease;
}

.link-item:hover {
    color: #000000;
    opacity: 0.7;
}

.artist-name {
    color: #726e68;
    letter-spacing: 0.2em;
}

/* ==========================================================================
   ADAPTACIÓN MÓVIL (RESPONSIVE)
   ========================================================================== */
@media (max-width: 768px) {
    body {
        padding: 0; /* En celular ocupa todo el ancho sin bordes exteriores excesivos */
        background-color: #fcfbf7; /* El fondo unificado da más fluidez en pantalla chica */
    }

    .paper-container {
        padding: 45px 28px;
        box-shadow: none;
        border-radius: 0;
    }

    .divider-top {
        margin-bottom: 50px;
    }

    .manifesto-title {
        font-size: 28px;
        margin-bottom: 35px;
    }

    .manifesto-content p {
        font-size: 18px;
        line-height: 1.65;
        margin-bottom: 22px;
    }

    .section-separator {
        margin: 35px 0;
    }

    .footer-container {
        margin-top: 70px;
    }

    .footer-links-row {
        flex-direction: column;
        align-items: flex-start;
        gap: 20px;
    }

    .audio-links {
        gap: 25px;
    }
}
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_html)

with open("style.css", "w", encoding="utf-8") as f:
    f.write(style_css)

print("Files index.html and style.css created successfully.")