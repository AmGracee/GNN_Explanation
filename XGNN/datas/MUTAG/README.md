
MUTAG数据集：包含188个硝基化合物，labels是判断化合物是芳香族还是杂芳族。

总共3371个结点（原子），7442个边（化学键）。

MUTAG:图数量188个	图类别2个	图平均节点17.9	节点标签数7

n表示结点数，m表示边的个数，N表示图的个数 DS=dataset

数据集目录如下：

DS_A.txt (m lines)：图的邻接矩阵，每一行的结构为(row, col)，即一条边，记录了7442条边。

DS_graph_indicator.txt (n lines)：表明结点属于哪一个图的文件（图索引号从1-188编号）

DS_graph_labels.txt (N lines)：188个图每个图所对应的label（1或-1）。

DS_node_labels.txt (n lines)：记录3371个节点的每个节点的labels（从0-6编号）。

DS_edge_labels.txt (m lines)：记录7442条边每个边的类型，这里并未用上。

DS_edge_attributes.txt (m lines)：边特征。

DS_node_attributes.txt (n lines)：结点的特征。

DS_graph_attributes.txt (N lines)：图的特征，可以理解为全局变量。

Node labels:

0  C
1  N
2  O
3  F
4  I
5  Cl
6  Br

Edge labels:

0  aromatic 芳香烃
1  single 单个
2  double 双个
3  triple 三个

[MUTAG数据集下载](https://ls11-www.cs.uni-dortmund.de/people/morris/graphkerneldatasets/MUTAG.zip)