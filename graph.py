from ascii2graph import graph

text = r"""
a->boo
^   |   x
|   v  /
c<--d-e
    | |
    f-g"""

result = graph(text)
print(result)

print()

g2 = r"O->m"
result = graph(g2)
print(result)
