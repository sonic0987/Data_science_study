#5.6.3 Softmax-with-Loss 계층
import practice_function as pr

class SoftmaxWithLoss:
    def __init__(self):
        self.loss = None
        self.y = None
        self.t = None

    def forward(self, x, t):
        self.t = t
        self.y = pr.softmax(x)
        self.loss = pr.cross_entropy_error(self.y, self.t)

    def backward(self, dout = 1):
        batch_size = self.t.shape[0]
        dx = (self.y - self.t) / batch_size

        return dx