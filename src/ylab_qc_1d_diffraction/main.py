from cmath import exp, pi, sqrt

import matplotlib.pyplot as plt

tau = (1 + sqrt(5)) / 2
fib = [(0, 0), (0, 1), (1, 1)]


def F(n):
    r = []
    if n > 0:
        r.append(fib[0])
    if n > 1:
        r.append(fib[1])
    if n > 2:
        r.append(fib[2])
    if n > 3:
        for i in range(n - 3):
            _1 = r[i]
            _2 = r[i + 1]
            r.append((_1[0] + _2[0], _1[1] + _2[1]))

    def F(k):
        f = 0
        for i in range(n):
            _ = exp(2 * pi * 1j * k * (r[i][0] + r[i][1] * tau))
            if i == 0 or i == n - 1:
                f += _ / 2
            else:
                f += _

        return (f * f.conjugate()).real

    return F


if __name__ == "__main__":
    x = []
    y = []
    f = F(10)

    for i in range(200):
        _x = i * 4 * 0.005
        x.append(_x)
        y.append(f(_x))

    plt.plot(x, y)
    plt.show()
