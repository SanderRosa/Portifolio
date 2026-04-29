import os
import re

file_path = 'index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update section description
old_desc = '<p class="section-description">Cada card tem espaço para imagem, print de tela, circuito, dashboard ou trecho de código.</p>'
new_desc = '<p class="section-description">Acesse o código-fonte completo de cada projeto nos meus repositórios do GitHub.</p>'
content = content.replace(old_desc, new_desc)

# 2. Remove all project-media blocks using regex
# It starts with <div class="project-media"> and ends with </div> before <div class="project-body">
content = re.sub(r'\s*<div class="project-media">.*?</div>\s*(?=<div class="project-body">)', '\n            ', content, flags=re.DOTALL)

# 3. Update the links for each project
replacements = [
    # Nexus
    ('<h3 class="project-title">NEXUS CONTROL — Plataforma de Automação com IA</h3>',
     '<a class="small-link" href="https://github.com/SanderRosa" target="_blank" rel="noopener">Repositório</a>\n                <a class="small-link" href="#" target="_blank" rel="noopener">Demonstração</a>',
     '<a class="small-link" href="https://github.com/SanderRosa/Nexus-Control" target="_blank" rel="noopener">Repositório no GitHub</a>'),
    
    # Genius
    ('<h3 class="project-title">Genius IoT ESP32 — Sistema Embarcado com Interface Web</h3>',
     '<a class="small-link" href="https://github.com/SanderRosa" target="_blank" rel="noopener">Repositório</a>\n                <a class="small-link" href="#" target="_blank" rel="noopener">Vídeo/print</a>',
     '<a class="small-link" href="https://github.com/SanderRosa/GeniusESP32" target="_blank" rel="noopener">Repositório no GitHub</a>'),
    
    # ERP
    ('<h3 class="project-title">Módulo de Compras — Sistema ERP em C++</h3>',
     '<a class="small-link" href="https://github.com/SanderRosa" target="_blank" rel="noopener">Repositório</a>',
     '<a class="small-link" href="https://github.com/SanderRosa/Modulo-de-Compras-Sistema-ERP" target="_blank" rel="noopener">Repositório no GitHub</a>'),
     
    # Ovos
    ('<h3 class="project-title">Contador de Ovos de C. elegans — Visão Computacional</h3>',
     '<a class="small-link" href="https://github.com/SanderRosa" target="_blank" rel="noopener">Repositório</a>',
     '<a class="small-link" href="https://github.com/SanderRosa/Contador-de-OVOS-de-C-elegans-Python" target="_blank" rel="noopener">Repositório no GitHub</a>'),
     
    # Semaforo
    ('<h3 class="project-title">Semáforo Inteligente em C</h3>',
     '<a class="small-link" href="https://github.com/SanderRosa" target="_blank" rel="noopener">Repositório</a>',
     '<a class="small-link" href="https://github.com/SanderRosa/Semaforo-Inteligente-C" target="_blank" rel="noopener">Repositório no GitHub</a>'),
     
    # Grow
    ('<h3 class="project-title">Sistema Especialista GROW</h3>',
     '<a class="small-link" href="https://github.com/SanderRosa" target="_blank" rel="noopener">Repositório</a>',
     '<a class="small-link" href="https://github.com/SanderRosa/SISTEMA-ESPECIALISTA-GROW" target="_blank" rel="noopener">Repositório no GitHub</a>'),
     
    # Arduino EEPROM
    ('<h3 class="project-title">Sensores Arduino com EEPROM</h3>',
     '<a class="small-link" href="https://github.com/SanderRosa" target="_blank" rel="noopener">Repositório</a>',
     '<a class="small-link" href="https://github.com/SanderRosa/projeto-arduino-temperatura" target="_blank" rel="noopener">Repositório no GitHub</a>'),
     
    # Logisim
    ('<h3 class="project-title">Circuito Lógico — Logisim</h3>',
     '<a class="small-link" href="https://github.com/SanderRosa" target="_blank" rel="noopener">Repositório</a>',
     '<a class="small-link" href="https://github.com/SanderRosa/Cirucuito-Logico-Logisim" target="_blank" rel="noopener">Repositório no GitHub</a>'),
]

for title, old_link, new_link in replacements:
    # Find the title to ensure we are replacing the link in the correct project block
    title_idx = content.find(title)
    if title_idx != -1:
        # Find the next occurrence of old_link after the title
        link_idx = content.find(old_link, title_idx)
        if link_idx != -1 and link_idx - title_idx < 1500: # ensure it's in the same block
            content = content[:link_idx] + new_link + content[link_idx + len(old_link):]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Modificações concluídas com sucesso.")
