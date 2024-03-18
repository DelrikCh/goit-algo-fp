import uuid

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        # Унікальний ідентифікатор для кожного вузла
        self.id = str(uuid.uuid4())

    def __lt__(self, other):
        return self.val < other.val


def get_color(index):
    base_color = 101010
    result = base_color + index * base_color
    result = "#" + str(result)
    return result


def depth_first_traversal(node, colors):
    if node is None:
        return
    colors[node.id] = get_color(len(colors))
    depth_first_traversal(node.left, colors)
    depth_first_traversal(node.right, colors)


def breadth_first_traversal(node, colors):
    queue = [node]
    while queue:
        current_node = queue.pop(0)
        colors[current_node.id] = get_color(len(colors))
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        # Використання id та збереження значення вузла
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r,
                          y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, traversal_type):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = {}
    if traversal_type == "BFS":
        breadth_first_traversal(tree_root, colors)
    elif traversal_type == "DFS":
        depth_first_traversal(tree_root, colors)
    labels = {node[0]: node[1]['label'] for node in tree.nodes(
        data=True)}  # Використовуйте значення вузла для міток

    draw_colors = []
    for key in labels.keys():
        draw_colors.append(colors[key])

    plt.figure(figsize=(8, 8))
    plt.title(traversal_type + " traversal")
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=draw_colors)
    plt.show()


def main():
    # Створення дерева
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    # Відображення дерева
    draw_tree(root, "BFS")
    draw_tree(root, "DFS")


if __name__ == "__main__":
    main()
