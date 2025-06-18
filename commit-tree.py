# git commit-tree <tree_sha> -m "msg" [-p <parent>]

import argparse
from Objects.commit import Commit

parser = argparse.ArgumentParser()
parser.add_argument("tree_sha", help="SHA1 du tree à committer")
parser.add_argument("-m", help="message du commit", required=True)
parser.add_argument("-p", help="SHA1 du commit parent (optionnel)", required=False)

args = parser.parse_args()

commit = Commit()
commit.setCommit(args.tree_sha, args.m, args.p)