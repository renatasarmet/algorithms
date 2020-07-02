def find_cycle(graph):

	for x in graph:
		if is_cycle(graph, x, set()):
			return True

	return False


def is_cycle(graph, vertice, visited):
	# print("vertice = ", vertice)

	if len(graph[vertice]) == 0:
		return False

	visited.add(vertice)

	for x in graph[vertice]:
		if x in visited:
			return True
		visited.add(x)
		is_cycle(graph[vertice], x, visited)



graph = {
  'a': {'a2':{}, 'a3':{} },
  'b': {'b2':{}},
  'c': {}
}

print(find_cycle(graph))
# False
graph['c'] = graph
print(find_cycle(graph))
# True
