"""Data Structures
Working with Graphs/Networks"""

def makeLink(G, node1, node2):
  if node1 not in G:
    G[node1] = {}
  (G[node1])[node2] = 1
  if node2 not in G:
    G[node2] = {}
  (G[node2])[node1] = 1
  return G 

# Ring Network
ring = {} # empty graph 

n = 5 # number of nodes 

# Add in edges
for i in range(n):
  ring = makeLink(ring, i, (i+1)%n)

# How many nodes?
print len(ring)

# How many edges?
print sum([len(ring[node]) for node in ring.keys()])/2 


# Grid Network
# TODO: create a square graph with 256 nodes and count the edges 
square = {}
n=15
for i in range(n):
    for k in range(n):
        square = makeLink(square, 16*i+k, 16*i+k+1)
        square = makeLink(square, 16*i+k, 16*(i+1)+k)
    square = makeLink(square, 16*i+15, 16*(i+1)+15)
    square = makeLink(square, 16*15+i, 16*15+i+1)
    
square={}
	
for i in range(1,256):
	if i%16!=0:
		makeLink(square,i,i+1)
	if (i-1)/16<15:
		makeLink(square,i,i+16)
		
def make_square_graph(n):
	square={}
	for i in range(1,n**2):
		if i%n!=0:
			makeLink(square,i,i+1)
		if (i-1)/n<n-1:
			makeLink(square,i,i+n)
	return square


# TODO: define a function countEdges
def count_edges(graph):
    return reduce((lambda x, y : x + y), map(len, graph.values()))/2

print "There are %d edges in the square"%count_edges(square)

# Social Network
class Actor(object):
  def __init__(self, name):
    self.name = name 

  def __repr__(self):
    return self.name 

ss = Actor("Susan Sarandon")
jr = Actor("Julia Roberts")
kb = Actor("Kevin Bacon")
ah = Actor("Anne Hathaway")
rd = Actor("Robert DiNero")
ms = Actor("Meryl Streep")
dh = Actor("Dustin Hoffman")

movies = {}

makeLink(movies, dh, rd) # Wag the Dog
makeLink(movies, rd, ms) # Marvin's Room
makeLink(movies, dh, ss) # Midnight Mile
makeLink(movies, dh, jr) # Hook
makeLink(movies, dh, kb) # Sleepers
makeLink(movies, ss, jr) # Stepmom
makeLink(movies, kb, jr) # Flatliners
makeLink(movies, kb, ms) # The River Wild
makeLink(movies, ah, ms) # Devil Wears Prada
makeLink(movies, ah, jr) # Valentine's Day

# How many nodes in movies?
print "There are %d nodes in movies"%len(movies)
# How many edges in movies?
print "There are %d edges in movies"%count_edges(movies)

def tour(graph, nodes):
  for i in range(len(nodes)):
    node = nodes[i] 
    if node in graph.keys():
      print node 
    else:
      print "Node not found!"
      break 
    if i+1 < len(nodes):
      next_node = nodes[i+1]
      if next_node in graph.keys():
        if next_node in graph[node].keys():
          pass 
        else:
          print "Can't get there from here!"
          break 

# TODO: find an Eulerian tour of the movie network and check it 
movie_tour = [kb,ms,rd,dh,kb,jr,dh,ss,jr,ah,ms] 
tour(movies, movie_tour)


def findPath(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        for node in graph[start]:
            if node not in path:
                newpath = findPath(graph, node, end, path)
                if newpath: return newpath
        return None

print findPath(movies, jr, ms)


# TODO: implement findShortestPath()
def findShortestPath(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        newpath=[]
        for node in graph[start]:
            if node not in path:
                newpath.append(findShortestPath(graph, node, end, path))
        newpath = filter(None, newpath)
        if newpath: return min(newpath, key=len)
        return None

print findShortestPath(movies, ms, ss)
print findShortestPath(movies, rd, ah)

# TODO: implement findAllPaths() to find all paths between two nodes
def findAllPaths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        newpath=[]
        for node in graph[start]:
            if node not in path:
                newpath.append(findAllPaths(graph, node, end, path))
        newpath = filter(None, newpath)
        if newpath: return newpath
        return None
allPaths = findAllPaths(movies, jr, ms)
for path in allPaths:
   print path
