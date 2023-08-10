# 图算法


一般图算法都比较难和抽象，仅做了解即可（问到就挺gg的）

https://github.com/dashidhy/algorithm-pattern-python/tree/master/basic_algorithm/graph


图这种数据结构有一些比较特殊的算法，比如二分图判断，有环图无环图的判断，拓扑排序，以及最经典的最小生成树，单源最短路径问题，更难的就是类似网络流这样的问题。

不过以我的经验呢，像网络流这种问题，你又不是打竞赛的，没时间的话就没必要学了；像 最小生成树 和 最短路径问题，虽然从刷题的角度用到的不多，但它们属于经典算法，学有余力可以掌握一下；像 二分图判定、拓扑排序这一类，属于比较基本且有用的算法，应该比较熟练地掌握。

路径题目：

union-find->kruskal最小生成树->Prim最小生成树->Dijkstra

## 深度优先搜索

其实就是经典的dfs

## 广度优先搜索

其实就是经典的bfs


Solution934: 岛屿问题+bfs，难点在于转化

Solution773: 核心还是在于问题的转化，将二维转成一维，官方解法更多也加入了回溯

## 拓扑排序


图的拓扑排序 (topological sorting) 一般用于给定一系列偏序关系，求一个全序关系的题目中。以元素为结点，以偏序关系为边构造有向图，然后应用拓扑排序算法即可得到全序关系。

包括3个步骤：构造图-判断是否有环-后序排序再调转（拓扑排序）

Solution207：图的构造+两数组+dfs+回溯

Solution210：Solution207+后序排序再调转


## 最小生成树

最小生成树算法主要有 Prim 算法（普里姆算法）和 Kruskal 算法（克鲁斯卡尔算法）两种，这两种算法虽然都运用了贪心思想，但从实现上来说差异还是蛮大的。

前置知识

union-find算法(路径压缩优化版)

```python
class UF:
    # 连通分量个数
    count: int
    # 存储每个节点的父节点
    parent: List[int]

    # n 为图中节点的个数
    def __init__(self, n: int):
        self.count = n
        self.parent = [i for i in range(n)]

    # 将节点 p 和节点 q 连通
    def union(self, p: int, q: int):
        rootP = self.find(p)
        rootQ = self.find(q)

        if rootP == rootQ:
            return

        self.parent[rootQ] = rootP
        # 两个连通分量合并成一个连通分量
        self.count -= 1

    # 判断节点 p 和节点 q 是否连通
    def connected(self, p: int, q: int) -> bool:
        rootP = self.find(p)
        rootQ = self.find(q)
        return rootP == rootQ

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # 返回图中的连通分量个数
    def count(self) -> int:
        return self.count

```

Kruskal 算法

```text

所谓最小生成树，就是图中若干边的集合（我们后文称这个集合为 mst，最小生成树的英文缩写），你要保证这些边：

1、包含图中的所有节点。

2、形成的结构是树结构（即不存在环）。

3、权重和最小。

有之前题目的铺垫，前两条其实可以很容易地利用 Union-Find 算法做到，关键在于第 3 点，如何保证得到的这棵生成树是权重和最小的。

这里就用到了贪心思路：

将所有边按照权重从小到大排序，从权重最小的边开始遍历，如果这条边和 mst 中的其它边不会形成环，则这条边是最小生成树的一部分，将它加入 mst 集合；否则，这条边不是最小生成树的一部分，不要把它加入 mst 集合。
```



Prim
```text
首先，Prim 算法也使用贪心思想来让生成树的权重尽可能小，也就是「切分定理」，这个后文会详细解释。

其次，Prim 算法使用 BFS 算法思想 和 visited 布尔数组避免成环，来保证选出来的边最终形成的一定是一棵树。

Prim 算法是从一个起点的切分（一组横切边）开始执行类似 BFS 算法的逻辑，借助切分定理和优先级队列动态排序的特性，从这个起点「生长」出一棵最小生成树
```


Dijkstra
```text
其实就是优先队列的贪心利用


```


## 最短路径


## 图的表示

两种表示



