#!/usr/bin/env python3
import argparse
import sys
from ls_files import ls_files  # importe ta fonction ls_files

parser = argparse.ArgumentParser()
parser.add_argument(
    "--force",
    help="Hasher le fichier (uniquement pour hash-object)",
    action="store_true"
)
# on autorise les arguments inconnus pour récupérer ls-files
args, unknown = parser.parse_known_args()

# Si la première "commande" inconnue est ls-files ou ls_files, on l’exécute
if unknown and unknown[0] in ("ls-files", "ls_files"):
    ls_files()
    sys.exit(0)
# Sinon, on reste sur le comportement existant
print(f"L'option de hashage a pour valeur {args.force}")


