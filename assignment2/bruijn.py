import python
import sys

pydef graphviz(edges: list[tuple[str, str]]):
    import graphviz
    g = graphviz.Digraph(format='png')
    for src, dst in edges:
        g.edge(src, dst)
        g.render('bruijn')

input_file = sys.argv[1]

for r in FASTA(input_file):
    s = r.seq
    
    graphviz()
    name = r.name