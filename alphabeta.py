def minimax(node, depth, maximizing):
    scores = {'A':3, 'B':5, 'C':2, 'D':9, 'E':0, 'F':-1}
    if depth==0 or node not in children:
        return scores[node]
    
    if maximizing:
        return max(minimax(c, depth-1, False) for c in children[node])
    else:
        return min(minimax(c, depth-1, True) for c in children[node])

children = {
    'root':['A','B'],
    'A':['C','D'],
    'B':['E','F'],
    'C':[],'D':[],'E':[],'F':[]
}

print("Best value:", minimax('root',2,True))
