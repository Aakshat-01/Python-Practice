g={
    "a":["b","c","d"],
    "b":["a","c"],
    "c":["a","b"],
    "d":["a","e","f"],
    "e":["d"],
    "f":["d"]
}

# #BFS in Graph
# q,v,r=['d'],{'d'},['d']
# while q:
#     p=q.pop(0)
#     for n in g[p]:
#         if n not in v:
#             q.append(n)
#             v.add(n)
#             r.append(n)
# print(r)

#DFS in Graph
def dfs(g,n,v,r):
    if n not in v:
        v.add(n)
        r.append(n)
        for i in g[n]:
            dfs(g,i,v,r)
    return r

print(dfs(g,"d",set(),[]))
