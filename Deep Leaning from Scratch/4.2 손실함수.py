#4.2 손실함수
import numpy as np

#4.2.1 평균 제곱 오차
def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t) ** 2)

#4.2.2 교차 엔트로피 오차
def cross_entropy_error(y, t):
    delta = 1e-7
    
    return -np.sum(t * np.log(y + delta))
