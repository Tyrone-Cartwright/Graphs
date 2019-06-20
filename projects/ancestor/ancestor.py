class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


def search_ancestors(target, parent_rel_tree, lineages, cur_list):
    new_cur_list = cur_list.copy()
    new_cur_list.append(target)

    if target not in parent_rel_tree:
        lineages.push(new_cur_list)
        return
    else:
        for parent in parent_rel_tree[target]:
            search_ancestors(parent, parent_rel_tree, lineages, new_cur_list)


def closest_ancestor(relationships, target):
    parent_rel_tree = {}
    for relationship in relationships:
        if relationship[1] in parent_rel_tree:
            parent_rel_tree[relationship[1]].append(relationship[0])
        else:
            parent_rel_tree[relationship[1]] = [relationship[0]]

    lineages = Stack()
    lineages.push([target])

    if target not in parent_rel_tree:
        return -1

    search_ancestors(target, parent_rel_tree, lineages, [])

    max_len = 0
    for i in lineages.stack:
        if len(i) > max_len:
            max_len = len(i)

    ancestor_trees = [i[len(i)-1] for i in lineages.stack if len(i) == max_len]

    return min(ancestor_trees)


# test relationships
relationships = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7],
                 [4, 5], [4, 8], [8, 9], [11, 8], [10, 1]]

print(closest_ancestor(relationships, 6))
