xs = [line.strip().split('-') for line in open("input.txt")]
adj = {x : {p[1-p.index(x)] for p in xs if x in p} for x,x in xs}

def search(node,visited,twice=True):
	if node=="end":
		return 1

	if node=="start":
		return 0

	twice = twice or node in visited

	if not twice:
		if node.islower():
			return sum(search(x, visited | {node}, twice) for x in adj[node])
		return sum(search(x, visited, twice) for x in adj[node])
	if node.islower():
		return sum(search(x, visited | {node}) for x in adj[node].difference(visited))
	return sum(search(x, visited) for x in adj[node].difference(visited))

print("Star 1:", sum(search(x,{"start"}) for x in adj["start"]))
print("Star 2:", sum(search(x,{"start"},False) for x in adj["start"]))
