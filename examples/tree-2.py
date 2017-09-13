from Drawing import *

s = Drawing()

s.addColor("tPink", "#FF9896") # 255, 152,150

s.addNode("a")
s.addNode("b", [(0,4), (5,10)])
s.addNode("c", [(4,9)])
s.addNode("d", [(1,3)])

#s.addPath([(1,"b","a"), (4.5,"a","c"), (6, "c", "b")], 1, 5, color=11, width=6)
#s.addPath([(2,"b","d")], 1, 1, color=11, width=6)

s.addLink("a", "b", 2, 2, color=11, width=6)
s.addLink("b", "d", 2, 2, color=11, width=6)
s.addLink("a", "c", 5, 5, color=11, width=6)
s.addLink("b", "c", 6, 6, color=11, width=6)
s.addLink("b", "c", 7, 7, color=11, width=6)
s.addLink("b", "c", 8, 8, color=11, width=6)
s.addLink("a", "b", 8, 8, color=11, width=6)

s.addLink("a", "b", 1, 3)
s.addLink("b", "d", 2, 3)
s.addLink("a", "c", 4.5, 7.5, height=0.40)
s.addLink("a", "b", 7, 8)
s.addLink("b", "c", 6, 9)

s.addTimeNodeMark(2,"b",color="tPink",width=4)

s.addNodeCluster("a", [(2,6),(8,9)], color=11, width=60)
s.addNodeCluster("b", [(6,7),(8,10)], color=11, width=60)
s.addNodeCluster("c", [(5,6),(7,9)], color=11, width=60)
s.addNodeCluster("d", [(2,3)], color=11, width=60)

s.addTimeLine(ticks=2)
