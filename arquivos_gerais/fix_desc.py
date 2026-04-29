import os
import subprocess

projects = {
    "Agente": "Agente",
    "Cirucuito Logico - Logisim": "Cirucuito-Logico-Logisim",
    "Contador de OVOS de C. elegans - Python": "Contador-de-OVOS-de-C-elegans-Python",
    "Genius_ESP32": "Genius_ESP32",
    "Modulo de Compras Sitema  EPR": "Modulo-de-Compras-Sitema--EPR",
    "SISTEMA ESPECIALISTA GROW": "SISTEMA-ESPECIALISTA-GROW",
    "Semaforo Inteligente - C": "Semaforo-Inteligente-C",
}

for folder, repo in projects.items():
    readme_path = os.path.join(folder, "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            first_line = f.readline().strip()
            if first_line.startswith("#"):
                desc = first_line.lstrip("#").strip()
                subprocess.run(["gh", "repo", "edit", f"SanderRosa/{repo}", "-d", desc], shell=False)
