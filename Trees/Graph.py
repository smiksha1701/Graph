import matplotlib.pyplot as plt
import networkx as nx
class MyGraph(nx.Graph):
    def Diameter(self):
        self.diamlen=nx.diameter(self.component)
        for somenode in self.component.nodes:
            for anothernode in self.component.nodes:
                if nx.shortest_path_length(self.component, somenode, anothernode) == self.diamlen:
                    diametern=nx.shortest_path(self.component, source = somenode, target = anothernode)
        return diametern
    def dfs(self,v):
        self.N.append(v)
        for w in self.neighbors(v):
            if(self.pozn[w]==-1):
                self.rebra_kist.append((w,v))
                self.pozn[w]=0
                self.dfs(w)
    def Kist(self):
        self.pozn=dict.fromkeys(self.component.nodes,-1)
        self.v=next(iter(self.component.nodes))
        self.pozn[self.v]=0
        self.dfs(self.v)
    def Supgraph(self):
        self.rebra_kist=[]
        self.N=[]
        self.diameter_nodes = []
        self.diameter_edges = []
        for numberofcomponent, c in enumerate(nx.connected_components(self)):
            self.component = self.subgraph(c)
            self.diam = self.Diameter()
            self.diameter_nodes.extend(self.diam)
            self.numberofcomponent=numberofcomponent
            self.Subgraph_info()
            self.Output_Diameter()
            self.Kist()
    def Output_Diameter(self):
        print(" Diameter edges:")
        for i in range(len(self.diam)-1):
            self.diameter_edges.append((self.diam[i], self.diam[i+1]))
            print(" {}-{}".format(self.diam[i],self.diam[i+1]),end=" ")
        print()
    def Nodes_Edges(self):
        print(" has:\n nodes:", len(self.component.nodes), "\n edges:", len(self.component.edges))
    def Degrees(self):
        print(" Degrees:")
        for j in self.component.degree():
            print("  {}:{}".format(j[0], j[1]))
    def Eccentricitys(self):
        print(" Eccentricity:")
        for i in nx.eccentricity(self.component).items():
            print("  {}:{}".format(i[0], i[1]))
    def Subgraph_Radius(self):
        print(" Radius of component:", nx.radius(self.component))
    def Subgraph_Diameter(self):
        print("Diameter of component:", self.diamlen)
    def Subgraph_info(self):
        print("{} component".format(self.numberofcomponent+1),end="")
        self.Nodes_Edges()
        self.Degrees()
        self.Eccentricitys()
        self.Subgraph_Radius()
        self.Subgraph_Diameter()
color1 = 'w'
color2 = 'black'
color3 = 'b'
color4 = 'g'
color5 = 'r'
color6 = 'y'
G = nx.read_edgelist("data.txt", create_using = MyGraph(), nodetype = str)
plt.figure(1)
nx.draw(G, node_color = color1, edgecolors = color2, with_labels = True, font_color = color2)
nodes_coords = {'A':(1,1),'B':(6,1),'C':(9,2),'D':(7,2),'E':(4,2),'F':(5,4),'G':(-4,4), 'J':(-5,1),'I':(-2,2), 'K':(11,4), 'L':(13,1),'M':(0,2),'N':(10,2),'O':(0,4)}
plt.figure(2)
nx.draw(G, pos = nodes_coords, node_color = color1, edgecolors = color2, with_labels = True, font_color = color2)
plt.savefig("Graph2.png", format="PNG")
G.Supgraph()
plt.figure(3)
nx.draw(G, pos = nodes_coords, node_color = color1, edgecolors = color2, with_labels = True, font_color = color2)
nx.draw_networkx_nodes(G, nodelist = G.diameter_nodes, pos = nodes_coords, node_color = color3)
nx.draw_networkx_edges(G, edgelist = G.diameter_edges, pos = nodes_coords, edge_color = color4, width = 5)
plt.savefig("Graph3.png", format="PNG")
plt.figure(4)
nx.draw(G, pos = nodes_coords, node_color = color1, edgecolors = color2, with_labels = True, font_color = color2)
nx.draw_networkx_edges(G, edgelist = G.rebra_kist, pos = nodes_coords, edge_color = color6, width = 5)
plt.savefig("Graph4.png", format="PNG")
plt.show(block = False)
input()
