#4.2.4 배치용 교차 엔트로피 오차 구현하기
import numpy as np

def cross_entropy_error1(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    batch_size = y.shape[0]
    retrun -np.sum(t * np.log(y + 1e-7)) / batch_size

def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape
        y = y.reshape

    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arrange(batch_size), t] + 1e-7)) / batch_size