import os
import sys

# Permet d'importer app.py situé à la racine du projet, un niveau au-dessus
# de ce fichier (api/index.py), quel que soit le repertoire de travail.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app import app  # noqa: E402,F401
