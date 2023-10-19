from cmath import exp, pi, sqrt

import matplotlib.pyplot as plt

tau = (1 + sqrt(5)) / 2
r = [
    (0, 0),
    (1, 0),
    (0, 1),
    (2, 0),
    (1, 1),
    (3, 0),
    (0, 2),
]


def F(n):
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
    f = F(7)

    for i in range(200):
        _x = i * 4 * 0.005
        x.append(_x)
        y.append(f(_x))

    plt.plot(x, y)
    plt.show()
