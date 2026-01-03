#!/data/data/com.termux/files/usr/bin/bash

# Pfade basierend auf Ihrer reta.tar Struktur
PROJECT_DIR="$HOME/myRepos/reta"
MOJO_OUT="$PROJECT_DIR/mojo_migration"

mkdir -p $MOJO_OUT

echo "Analysiere RETA Projekt für Technologie (33) und Automatik (34)..."

# Erstellt die zentrale Mojo-Datei mit Ihren System-Parametern
cat <<EOF > $MOJO_OUT/main.mojo
from utils.vector import DynamicVector

struct RETA_System:
    alias TECH_ID = 33
    alias AUTO_ID = 34
    
    fn __init__(inout self):
        print("Mojo-System für RETA (ID 33/34) initialisiert.")

    fn verarbeite_paket(self, status: Int):
        if status == self.AUTO_ID:
            print("Status 34: Automatik-Verarbeitung.")
        elif status == self.TECH_ID:
            print("Status 33: Technologie-Modul.")

fn main():
    var sys = RETA_System()
    sys.verarbeite_paket(34)
EOF

echo "Mojo-Grundgerüst wurde in $MOJO_OUT erstellt."

