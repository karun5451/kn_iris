from kn_iris.rectangulate import *
from numpy import zeros



def engroup(fname):
    try:
        strip = rectangle(fname)
        if strip == "invalid image":
            # print("feature vector 1")
            return "invalid image"

        grid = zeros([13, 36])
        for i in range(13):
            for j in range(36):
                block = strip[3 * i:3 * i + 3, 10 * j:10 * j + 10]
                for row in block:
                    grid[i, j] += sum(row)

        # Group encoding
        def encode(group):
            avg = sum(group) / 5
            group -= avg
            for i in range(1, 5):
                group[i] = sum(group[:i + 1])
            code = ''
            argmax = 0
            argmin = 0
            for i in range(5):
                if group[i] == max(group): argmax = i
                if group[i] == min(group): argmin = i
            for i in range(5):
                if i < argmax and i < argmin: code += '0'
                if i > argmax and i > argmin: code += '0'
                if i >= argmax and i <= argmin: code += '2'
                if i <= argmax and i >= argmin: code += '1'
            return code

        # Horizontal grouping
        horgroups = []
        # hor_ver_groups = []
        hor_ver_groups = ""
        for row in range(13):
            horgroups.append([])
            for col in range(32):
                group = zeros(5)
                for i in range(5): group[i] = grid[row, col + i]
                horgroups[row].append(encode(group))
                # hor_ver_groups.append(encode(group))
                # hor_ver_groups += encode(group)

        # Vertical grouping
        vergroups = []
        for col in range(36):
            vergroups.append([])
            for row in range(9):
                group = zeros(5)
                for i in range(5): group[i] = grid[row + i, col]
                vergroups[col].append(encode(group))
                # hor_ver_groups.append(encode(group))
                # hor_ver_groups += encode(group)


        return [horgroups, vergroups]
        # return hor_ver_groups
    except Exception as e:
        print("expression2", e)
