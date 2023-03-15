import typing


class Node:
    left: "Node" = None
    right: "Node" = None
    key: typing.Any

    def __init__(self, key: typing.Any):
        self.key = key

    def __str__(self):
        return f"{self.key}"


class Tree:
    root: Node = None

    def print(self):
        print(self)

    def __str__(self):
        if self.root is None:
            return "no elements"
        keys = []

        def _collect(node, level, index):
            if len(keys) - 1 < level:
                keys.append([])
            if node is not None:
                keys[level].append((node, index))
                _collect(node.left, level + 1, index * 2)
                _collect(node.right, level + 1, index * 2 + 1)

        _collect(self.root, 0, 0)
        max_elem_len = 0
        for i, line in enumerate(keys):
            for elem, index_in_line in line:
                max_elem_len = max(max_elem_len, len(str(elem)))

        ext_keys = []
        for i, line in enumerate(keys):
            t = []
            for j, (elem, index_in_line) in enumerate(line):
                if j == 0:
                    if index_in_line != 0:
                        for _ in range(index_in_line):
                            t.append(None)
                    t.append(elem)
                else:
                    for _ in range(index_in_line - line[j-1][1] - 1):
                        t.append(None)
                    t.append(elem)
            if t:
                ext_keys.append(t)

        s = ''
        sep = 1
        k = max_elem_len % 2
        ext_keys = ext_keys[::-1]
        for i, line in enumerate(ext_keys):
            st = sep + (max_elem_len // 2)
            sep = st * 2 + k
            sh = st // 2 - 1
            t = ' ' * st
            v = t
            for j, elem in enumerate(line):
                if elem is None:
                    t += (' ' * max_elem_len) + (' ' * sep)
                else:
                    left = (t[:len(t) - sh] + '_' * sh) if elem.left else t
                    right = ('_' * sh + ' ' * (sep - sh)) if elem.right else ' ' * sep
                    t = left + str(elem).rjust(max_elem_len, '_' if elem.left else ' ') + right
                if elem is None:
                    v += (' ' * max_elem_len) + (' ' * sep)
                else:
                    v += ('|' * max_elem_len) + (' ' * sep)
            s = t + '\n' + s

        lines = [line for line in s.split('\n') if line]

        max_line_len = max(len(line) for line in lines)
        lines = [line.ljust(max_line_len, ' ') for line in lines]

        line_len = max_line_len
        left = 0
        finish = False

        def count_empty_columns(start_shift):
            ind = start_shift
            while ind < line_len:
                for j in range(len(lines)):
                    if not lines[j][ind] in [' ', '_']:
                        return ind - 2
                ind += 1
            return ind - 1

        while left < line_len:
            right = count_empty_columns(left)

            while right < 1 or right < left:
                left += 1
                if left >= line_len:
                    finish = True
                    break
                right = count_empty_columns(left)
            if not finish:
                lines = [line[:left] + line[right:] for line in lines]
                line_len = len(lines[0])
                left += 3
        s = '\n'.join(lines)
        return s

