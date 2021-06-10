import numpy as np


def main():
    phi = np.random.randint(100, size=(3, 2)) / 100
    etta = np.random.randint(100, size=(2, 3)) / 100
    p = np.random.randint(100, size=(3, 2, 3)) / 100
    n_dw = np.random.randint(100, size=(3, 3)) / 100
    n_dwt = np.random.randint(100, size=(3, 3, 2)) / 100
    n_wt = np.random.randint(100, size=(3, 2)) / 100
    n_td = np.random.randint(100, size=(2, 3)) / 100
    n_t = np.random.randint(100, size=(2)) / 100
    n_d = np.random.randint(100, size=(3)) / 100

    for e_m in range(5):
        print("p:")
        for i in range(len(p)):
            for j in range(len(p[i])):
                for k in range(len(p[i][j])):
                    p[i][j][k] = phi[i][j] * etta[j][k] / (phi[i][0] * etta[0][k] + phi[i][1] * etta[1][k])
                    if (i == 1) and (k == 2):
                        p[i][j][k] = 0
        print(p)

        for i in range(len(n_wt)):
            for j in range(len(n_wt[i])):
                n_wt[i][j] = 0
        for i in range(len(n_wt)):
            for j in range(len(n_wt[i])):
                for k in range(len(p[i][j])):
                    n_wt[i][j] += p[i][j][k]
        for i in range(len(n_t)):
            for j in range(len(n_wt[0])):
                n_t[i] = 0
        for i in range(len(n_wt[0])):
            for j in range(len(n_wt)):
                n_t[i] += n_wt[j][i]
        for i in range(len(phi)):
            for j in range(len(phi[i])):
                phi[i][j] = n_wt[i][j] / n_t[j]
        print('phi:')
        for i in range(len(phi)):
            str_ = ''
            for j in range(len(phi[i])):
                str_ += str(phi[i][j]) + ' '
            print(str_)
        for i in range(len(n_td)):
            for j in range(len(n_td[i])):
                n_td[i][j] = 0
        for i in range(len(n_td)):
            for j in range(len(n_td[i])):
                for k in range(len(p)):
                    n_td[i][j] += p[k][i][j]
        for i in range(len(n_d)):
            n_d[i] = 0
        for i in range(len(n_td)):
            for j in range(len(n_d)):
                n_d[j] += n_td[i][j]
        for i in range(len(etta)):
            for j in range(len(etta[i])):
                etta[i][j] = n_td[i][j] / n_d[j]

        print('etta:')
        for i in range(len(etta)):
            str_ = ''
            for j in range(len(etta[i])):
                str_ += str(etta[i][j]) + ' '
            print(str_)
        print('')
if __name__ == '__main__':
    main()
