from Objects.tree import Tree

import os

files = os.listdir("./test/fichiers/")

tree = Tree()
tree.setTree([os.path.join("./test/fichiers/", f) for f in files])