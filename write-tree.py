from Objects.tree import Tree

import os
print(os.listdir("./test/"))

files = os.listdir("./test/")

tree = Tree()
tree.setTree([os.path.join("./test/", f) for f in files])
print(tree.sha1)