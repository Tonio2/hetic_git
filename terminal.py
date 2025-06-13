import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--force", help="Hasher le fichier", action="store_true")
args = parser.parse_args()

print(f"L'option de hashage a pour valeur {args.force}")


#test

