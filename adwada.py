# to print out the expression binary tree diagram 
class treeLayout():
    def print_tree(root, key="key", leftTree="leftTree", rightTree="rightTree"):
        # if there is no child
        if getattr(root, rightTree) is None and getattr(root, leftTree) is None:
            line = '%s' % getattr(root, key)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # if there is only left tree child
        if getattr(root, rightTree) is None:
            lines, n, p, x = display(getattr(root, leftTree))
            s = '%s' % getattr(root, key)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # if there is only right tree child
        if getattr(root, leftTree) is None:
            lines, n, p, x = display(getattr(root, rightTree))
            s = '%s' % getattr(root, key)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # if there is both right and left tree child
        leftTree, n, p, x = treeLayout.print_tree(getattr(root, leftTree))
        rightTree, m, q, y = treeLayout.print_tree(getattr(root, rightTree))
        s = '%s' % getattr(root, key)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '' + s + y * '' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            leftTree += [n * ' '] * (q - p)
        elif q < p:
            rightTree += [m * ' '] * (p - q)
        zipped_lines = zip(leftTree, rightTree)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2