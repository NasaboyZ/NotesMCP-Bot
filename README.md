# NotesMCP-Bot

📝 Josef – Simple MCP Note Bot

Josef ist mein erster MCP Note Bot und dient als bewusst minimalistisches Beispiel, um die Grundlagen von MCP (Model Context Protocol) zu verstehen und zu testen.

Der Bot wurde mit FastMCP umgesetzt und in Claude getestet.

🎯 Ziel

Dieses Projekt hat keinen Anspruch auf Vollständigkeit oder Produktreife.
Es soll zeigen, wie man mit MCP:

einfache Tools definiert

Ressourcen bereitstellt

Prompts generiert

und persistente Daten lokal speichert

✨ Funktionsumfang (bewusst simpel)

📝 Notizen zu einer lokalen Textdatei hinzufügen

📖 Alle gespeicherten Notizen auslesen

🕒 Die zuletzt gespeicherte Notiz abrufen

🤖 Einen Prompt erzeugen, um alle Notizen zusammenzufassen

🧪 Getestet mit

Claude (MCP-Unterstützung)

Lokale Dateispeicherung (notes.txt)

🛠️ Technische Details

MCP Framework: FastMCP

Servername: josef

Speicher: einfache Textdatei

Keine externe Datenbank

Keine Authentifizierung

Kein State außerhalb der Datei

📁 Dateistruktur
.
├── main.py
└── notes.txt

Die Datei notes.txt wird automatisch erstellt, falls sie nicht existiert.

🔧 MCP Tools
add_note(message: str)

Fügt eine neue Notiz hinzu.

read_notes()

Gibt alle gespeicherten Notizen zurück.

🌐 MCP Resource
notes://latest

Gibt die zuletzt hinzugefügte Notiz zurück.

💬 MCP Prompt
note_summary_prompt()

Erzeugt einen Prompt, der ein LLM auffordert, alle aktuellen Notizen zusammenzufassen.

🚧 Status

✅ Erster funktionsfähiger MCP Bot

✅ Fokus auf Einfachheit

🚧 Grundlage für spätere Experimente mit MCP

📌 Fazit

Dieses Projekt ist ein Lern- und Experimentierprojekt, um MCP praktisch zu verstehen.
Der Code ist bewusst einfach gehalten und eignet sich gut als Startpunkt für eigene MCP-Bots.
