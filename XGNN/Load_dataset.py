import numpy as np
import scipy.sparse as  sp

def encode_onehot(labels):
    classes = set(labels)
    classes_dict = {c: np.identity(len(classes))[i,:] for i,c in
                    enumerate(classes)}

    labels_onehot = np.array(list(map(classes_dict.get,labels)),
                             dtype=np.int32)
    return labels_onehot
def normalize(mx):
    rowsum = np.array(mx.sum(1))
    r_inv = np.power(rowsum,-1).flatten()
    r_inv[np.isinf(r_inv)] = 0.
    r_mat_inv = sp.diags(r_inv)
    mx = r_mat_inv.dot(mx)
    return mx