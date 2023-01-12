from collections import *
import time
from tqdm import tqdm
import mmap

"""
Please download origin file (i.e soc-LiveJournal1.txt) if it doesn't exist
"""

filenamePrefix = "soc-LiveJournal1"
suffix = ".txt"
filename = filenamePrefix + suffix

n = 1000
trimPrefix = f"{filenamePrefix}-trim-{n}"
trimFileName = trimPrefix + suffix

m = defaultdict(set)

def mapcount(filename):
    f = open(filename, "r+")
    buf = mmap.mmap(f.fileno(), 0)
    lines = 0
    readline = buf.readline
    while readline():
        lines += 1
    return lines

# totalLine = mapcount(filename)
totalLine = 68993777

start = time.time()
edges = 0
with open(filename, 'r') as f:
    for line in tqdm(f, total=totalLine):
        line = line.rstrip()
        if line[0] == "#":
            continue
        ss = line.split('\t')
        node1, node2 = ss[0], ss[-1]
        if int(node1) < n and int(node2) < n:
            m[node1].add(node2)
            m[node2].add(node1)
            edges += 1
end = time.time()
print(f'read file using {end-start} seconds')

trimGraphinfo = f"Nodes: {n} Edges: {edges}"

with open(trimFileName, 'w') as f:
    f.write(f"# {trimGraphinfo}\n")
    f.write("# FromNodeId	ToNodeId\n")
    
    for node1 in m:
        for node2 in m[node1]:
            f.write(f"{node1}\t{node2}\n")


# symEdges = 0
# for node in m:
#     symEdges += len(m[node])

# print(f"Nodes: {n} Edges: {symEdges}")