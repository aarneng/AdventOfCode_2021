from math import sin, cos, pi
from collections import defaultdict


def rotation_matrix_x(t=pi/2):
    return [
        [1, 0     , 0],
        [0, cos(t), -sin(t)],
        [0, sin(t), cos(t)]
    ]


def rotation_matrix_y(t=pi/2):
    return [
        [cos(t) , 0, sin(t)],
        [0      , 1, 0],
        [-sin(t), 0, cos(t)]
    ]


def rotation_matrix_z(t=pi/2):
    return [
        [cos(t), -sin(t), 0],
        [sin(t), cos(t) , 0],
        [0     , 0      , 1]
    ]


def multiply(X, Y):
    ans = [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*Y)] for X_row in X]
    return [[round(i) for i in j] for j in ans]
    # result = [[0] * len(X)] * len(Y)
    # # iterate through rows of X
    # for i in range(len(X)):
    #     # iterate through columns of Y
    #     for j in range(len(Y[0])):
    #         # iterate through rows of Y
    #         for k in range(len(Y)):
    #             result[i][j] += X[i][k] * Y[k][j]
    # return result


def all_rotation_matrices():
    return [
        [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
        [[1, 0, 0], [0, 0, -1], [0, 1, 0]],
        [[0, 0, 1], [0, 1, 0], [-1, 0, 0]],
        [[0, -1, 0], [1, 0, 0], [0, 0, 1]],
        [[1, 0, 0], [0, -1, 0], [0, 0, -1]],
        [[-1, 0, 0], [0, 1, 0], [0, 0, -1]],
        [[-1, 0, 0], [0, -1, 0], [0, 0, 1]],
        [[1, 0, 0], [0, 0, 1], [0, -1, 0]],
        [[0, 0, -1], [0, 1, 0], [1, 0, 0]],
        [[0, 1, 0], [-1, 0, 0], [0, 0, 1]],
        [[0, 0, 1], [1, 0, 0], [0, 1, 0]],
        [[0, -1, 0], [0, 0, -1], [1, 0, 0]],
        [[0, 1, 0], [0, 0, -1], [-1, 0, 0]],
        [[0, -1, 0], [0, 0, 1], [-1, 0, 0]],
        [[-1, 0, 0], [0, 0, 1], [0, 1, 0]],
        [[-1, 0, 0], [0, 0, -1], [0, -1, 0]],
        [[0, 0, -1], [0, -1, 0], [-1, 0, 0]],
        [[0, 0, 1], [0, -1, 0], [1, 0, 0]],
        [[0, 1, 0], [1, 0, 0], [0, 0, -1]],
        [[0, -1, 0], [-1, 0, 0], [0, 0, -1]],
        [[0, 0, -1], [-1, 0, 0], [0, 1, 0]],
        [[0, 0, 1], [-1, 0, 0], [0, -1, 0]],
        [[0, 0, -1], [1, 0, 0], [0, -1, 0]],
        [[0, 1, 0], [0, 0, 1], [1, 0, 0]]
    ]


# def all_rotations(lst):
#     # x, y, z = rotation_matrix_x(), rotation_matrix_y(), rotation_matrix_z()
#     all_matrices_2 = []
#     l = [rotation_matrix_x, rotation_matrix_y, rotation_matrix_z]
#     for i in range(4):
#         for j in range(4):
#             for k in range(4):
#                 for x in range(3):
#                     for y in range(3):
#                         for z in range(3):
#                             m1 = l[x]
#                             m2 = l[y]
#                             m3 = l[z]
#                             r1 = multiply(m1(i * pi/2), m2(j * pi/2))
#                             r2 = multiply(r1, m3(k * pi/2))
#                             all_matrices_2.append(r2)
#     # all_matrices = [
#     #     multiply(multiply(x, z), x),
#     #     multiply(multiply(x, z), y),
#     #     multiply(multiply(x, y), x),
#     #     multiply(multiply(x, y), z),
#     #
#     #     multiply(multiply(y, x), y),
#     #     multiply(multiply(y, x), z),
#     #     multiply(multiply(y, z), y),
#     #     multiply(multiply(y, z), x),
#     #
#     #     multiply(multiply(z, y), z),
#     #     multiply(multiply(z, y), x),
#     #     multiply(multiply(z, x), z),
#     #     multiply(multiply(z, x), y),
#     #
#     #     multiply(multiply(x, z), x),
#     #     multiply(multiply(y, z), x),
#     #     multiply(multiply(x, y), x),
#     #     multiply(multiply(z, y), x),
#     #
#     #     multiply(multiply(y, x), y),
#     #     multiply(multiply(z, x), y),
#     #     multiply(multiply(y, z), y),
#     #     multiply(multiply(x, z), y),
#     #
#     #     multiply(multiply(z, y), z),
#     #     multiply(multiply(x, y), z),
#     #     multiply(multiply(z, x), z),
#     #     multiply(multiply(y, x), z),
#     # ]
#
#     uniques = []
#     for matrix in all_matrices_2:
#         if matrix not in uniques:
#             uniques.append(matrix)
#             print(matrix)
#     print(len(uniques))
#     print(len(all_matrices_2))


def main():
    with open("input_test.txt", "r") as f:
        lines = f.readlines()
        all_beacons = defaultdict(list)
        current = -1
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if line.startswith("---"):
                current += 1
                continue
            nums = [int(i) for i in line.split(",")]
            all_beacons[current].append(nums)
        print(all_beacons)


if __name__ == '__main__':
    main()

