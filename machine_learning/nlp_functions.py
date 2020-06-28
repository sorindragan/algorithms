import numpy as np

def softmax(vec):
    x = np.array(vec)
    exp = np.e**x
    row_sums = np.sum(exp, axis=1)
    print(exp.shape, row_sums.shape)
    return exp / row_sums[:,None]

def sigmoid(vec):
    return 1 / (1 + np.e**(-np.array(vec))) 

def tanh(vec):
    x = np.array(vec)
    return (np.e**(2*x) - 1) / (1 + np.e**(2*x))

def relu(vec):
    x = np.array(vec)
    return x * (x > 0)

# SRN step
def SRN(h, x, U, W, V):
    h_next = relu(np.array(U).dot(np.array(h)) + np.array(W).dot(np.array(x)))
    y = relu(np.array(V).dot(np.array(h_next)))
    return h_next, y

# GRU step
def GRU(h, x, Uz, Wz, Ur, Wr, U, W):
    z = sigmoid(np.array(Uz).dot(np.array(h)) + np.array(Wz).dot(np.array(x)))
    r = sigmoid(np.array(Ur).dot(np.array(h)) + np.array(Wr).dot(np.array(x)))
    h_ = tanh(np.array(U).dot(np.array(r)*np.array(h)) + np.array(W).dot(np.array(x)))
    h_next = (1 - np.array(z)) * np.array(h) + np.array(z) * np.array(h_)
    return z, r, h_, h_next

# LSTM step
def LSTM(h, c, x, Uf, Wf, Ug, Wg, Ui, Wi, Uo, Wo):
    f = sigmoid(np.array(Uf).dot(np.array(h)) + np.array(Wf).dot(np.array(x)))
    i = sigmoid(np.array(Ui).dot(np.array(h)) + np.array(Wi).dot(np.array(x)))
    g = tanh(np.array(Ug).dot(np.array(h)) + np.array(Wg).dot(np.array(x)))
    k = np.array(c) * np.array(f)
    j = np.array(g) * np.array(i)
    c_next = np.array(k) + np.array(j)
    o = sigmoid(np.array(Uo).dot(np.array(h)) + np.array(Wo).dot(np.array(x)))
    h_next = np.array(o) * np.array(c_next)    
    return f, i, g, k, j, o, c_next, h_next

# Attention step
def scaled_attention(Q, K, V, dk=1):
    inner_term = np.array(Q).dot(np.array(K).T) / np.sqrt(dk)
    att = np.array(softmax(inner_term)).dot(np.array(V))
    V_next = np.array(V) + att
    return att, V_next 
