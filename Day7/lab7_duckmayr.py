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
		
def quadGraph(r, c):
	qGraph = {}
	for i in range(1, r*c):
		if i % c != 0: makeLink(qGraph, i, i + 1)
		if (r*c) - i >= c: makeLink(qGraph, i, i + c)
	return qGraph
			

# TODO: define a function countEdges

def countEdges(G):
	return sum([len(G[node]) for node in G.keys()])/2


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

makeLink(movies, dh, rd) # Wag the Dog x
makeLink(movies, rd, ms) # Marvin's Room x
makeLink(movies, dh, ss) # Midnight Mile x
makeLink(movies, dh, jr) # Hook x
makeLink(movies, dh, kb) # Sleepers 
makeLink(movies, ss, jr) # Stepmom x
makeLink(movies, kb, jr) # Flatliners x
makeLink(movies, kb, ms) # The River Wild x
makeLink(movies, ah, ms) # Devil Wears Prada x
makeLink(movies, ah, jr) # Valentine's Day x

# How many nodes in movies? 7 
# How many edges in movies? 10

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
movie_tour = [kb, dh, ss, jr, ah, ms, kb, jr, dh, rd] #(kb, dh), (dh, ss), (ss, jr), (jr, ah), (ah, ms), (ms, kb), (kb, jr), (jr, dh), (dh, rd), (rd, ms)
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


# print findShortestPath(movies, ms, ss)


# TODO: implement findAllPaths() to find all paths between two nodes




# allPaths = findAllPaths(movies, jr, ms)
# for path in allPaths:
#   print path

# Copyright (c) 2014 Matt Dickenson
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.