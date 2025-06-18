#!/usr/bin/env python3
import os, struct, sys

def find_git_dir(path):
    prev = None
    while path != prev:
        dot = os.path.join(path, ".git")
        if os.path.isdir(dot):
            return dot
        prev, path = path, os.path.dirname(path)
    sys.exit("Erreur : pas de dépôt Git ici.")

def read_index_header(f):
    header = f.read(12)
    sig, version, n = struct.unpack(">4sLL", header)
    if sig != b"DIRC":
        sys.exit("Erreur : index corrompu.")
    return version, n

def read_index_entries(f, n_entries):
    entries = []
    for _ in range(n_entries):
        head = f.read(62)
        # les deux derniers octets de head sont les flags
        flags = struct.unpack(">H", head[60:62])[0]
        name_len = flags & 0x0FFF
        name = f.read(name_len).decode("utf-8", "surrogateescape")
        # calcul du padding à 8 octets
        total = 62 + name_len
        pad = (8 - (total % 8)) or 0
        f.read(pad)
        entries.append(name)
    return entries

def ls_files():
    gitdir = find_git_dir(os.getcwd())
    idx = os.path.join(gitdir, "index")
    if not os.path.exists(idx):
        sys.exit("")  # index inexistant → rien à lister
    with open(idx, "rb") as f:
        version, n = read_index_header(f)
        files = read_index_entries(f, n)
    for p in files:
        print(p)

if __name__ == "__main__":
    ls_files()
