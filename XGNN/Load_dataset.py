import numpy as np
import scipy.sparse as  sp
import torch

def encode_onehot(labels):
    classes = set(labels)
    classes_dict = {c: np.identity(len(classes))[i,:] for i,c in
                    enumerate(classes)}

    labels_onehot = np.array(list(map(classes_dict.get,labels)),
                             dtype=np.int32)
    return labels_onehot
def normalize(mx): # 这里是计算D^-1A，而不是计算论文中的D^-1/2AD^-1/2
    # 函数实现的规范化方法是将输入左乘一个D^-1算子，就是将矩阵每行进行归一化
    rowsum = np.array(mx.sum(1))
    r_inv = np.power(rowsum,-1).flatten()
    r_inv[np.isinf(r_inv)] = 0.   #判断分母是否为0
    r_mat_inv = sp.diags(r_inv)  # 稀疏对角矩阵
    mx = r_mat_inv.dot(mx)  # D^-1A，对mx左乘D^-1
    return mx  # D^-1A，对mx左乘D^-1

def accuracy(output, labels):
    preds = output.max(1)[1].type_as(labels)
    # max(1)返回每一行最大值组成的一维数组和索引,output.max(1)[1]表示最大值所在的索引indice
    # type_as()将张量转化为labels类型
    correct = preds.eq(labels).double()
    # eq是判断preds与labels是否相等，相等的话对应元素置1，不等置0
    correct = correct.sum()
    # 计算correct正确的个数
    return correct / len(labels)

def load_split_MUTAG_data(path="datas/MUTAG", dataset="MUTAG_", split_train=0.7, split_val=0.15):
    """load MUTAG data"""
    print('Loading {} dataset'.format(dataset))

    # 加载图标签
    graph_labels = np.genformtxt("{}{}graph_labels.txt".format(path,dataset),dtype=np.dtype(int))
    graph_labels = encode_onehot(graph_labels)  #(188, 2)
    graph_labels = torch.LongTensor(np.where(graph_labels)[1]) #(188, 1)