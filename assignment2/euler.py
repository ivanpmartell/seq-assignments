import python
import sys

class Graph:
    starts: list[str]
    edges: dict[str, tuple[str, dict[str, int]]]
    def __init__(self: Graph, edges: dict[str, tuple[str, dict[str, int]]]):
        destinations = dict[str, bool]()
        for src, dest in edges.items():
            destinations[dest[0]] = False
        self.starts = list[str]()
        for src in edges.keys():
            try:
                destinations[src]
            except:
                self.starts.append(src)
        self.edges = edges
    
    def get_longest_contig(self: Graph):
        longest_contig = ''
        for start in self.starts:
            current_edges = self.edges.copy()
            node = start
            sequence = node
            while current_edges[node][1]['w'] > 0:
                current_edges[node][1]['w'] -= 1
                node = current_edges[node][0]
                sequence += node[-1]
                try:
                    current_edges[node]
                except KeyError:
                    break
            if len(longest_contig) < len(sequence):
                longest_contig = sequence
        return longest_contig


    def DFS(self: Graph, node: str, current_edges):
        for n in current_edges[node]:
            if n[1] > 0:
                n[1] -= 1
                self.DFS(n[0], current_edges)
            else:
                return node + n[0]

pydef graphviz(edges: list[tuple[str, str, int]]):
    import graphviz
    g = graphviz.Digraph(format='png')
    for src, dst in edges.items():
        for i in range(dst[1]):
            g.edge(src, dst[0])
        g.render('bruijn3')

input_file = sys.argv[1]

kmer_dict = dict[str, int]()
for r in FASTA(input_file, fai=False):
    name = r.name
    s = r.seq
    kmers = s.kmers[Kmer[12]](1)
    for kmer in kmers:
        kmer_str = str(kmer)
        try:
            kmer_dict[kmer_str] += 1
        except:
            kmer_dict[kmer_str] = 1
edges = dict[str, tuple[str, dict[str, int]]]()
for kmer, weight in kmer_dict.items():
    source = kmer[:-1]
    destination = kmer[1:]
    edges[source] = (destination, {"w": weight})
debruijn = Graph(edges)
print(debruijn.get_longest_contig())
