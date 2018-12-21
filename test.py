from Queue import Queue
import numpy as np
from PIL import Image

im = Image.open('./map.png')
im.convert('L')
im_map = np.array(im)
# print im_map

all_nodes = []
bad_nodes = []
start_node = (0, 0)
end_node = (19, 0)
for y in range(im_map.shape[0]):
    for x in range(im_map.shape[1]):
        all_nodes.append((y, x))
        if not im_map[y, x]:
            bad_nodes.append((y, x))


def neighbors(node):
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    result = []

    for dir in dirs:
        neighbor = (node[0] + dir[0], node[1] + dir[1])
        if neighbor in all_nodes and neighbor not in bad_nodes:
            result.append(neighbor)
    return result


frontier = Queue()
frontier.put(start_node)
came_from = {start_node: None}

while not frontier.empty():
    current = frontier.get()
    for next in neighbors(current):
        if next not in came_from:
            frontier.put(next)
            came_from[next] = current
            if current == end_node: break

current = end_node
path = [current]
while current != start_node:
    current = came_from[current]
    path.append(current)

print
path

print
"   0 1 2 3 4 5 6 7 8 9"
for y in range(im_map.shape[0]):
    print
    str(y).rjust(2),
    for x in range(im_map.shape[1]):
        node = all_nodes[(y * (im_map.shape[1])) + x]
        if node in bad_nodes:
            print
            "X",
        elif node == start_node:
            print
            "S",
        elif node == end_node:
            print
            "E",
        elif node in path:
            print
            "-",
        else:
            print
            " ",
    print
print
neighbors(all_nodes[115])