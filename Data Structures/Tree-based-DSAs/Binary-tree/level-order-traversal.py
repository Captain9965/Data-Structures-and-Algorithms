"""
    level order traversal algorithm for binary trees:


"""

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val



"""
    Space complexity is O(n)
    time complexity worst case is O(n)

"""
def levelOrder(root):
    result = []
    fill_level_order(root, result)
    return result

def fill_level_order(root: Node, result, count = 0):
    if root is None:
        return
    count += 1
    if len(result) < count:
        new_array = [root.val]
        result.append(new_array)
    else:
        result[count - 1].append(root.val)
    fill_level_order(root.left, result, count)
    fill_level_order(root.right, result, count)


""" space and time complexity:
    space complexity is O(n)
    time complexity is O(n)



"""
def bfs(root: Node):
    if not root:
        return []
    result = []
    queue = []

    queue.append(root)
    starting_queue_size = 1
    sub_array = []
    processed_nodes = 0

    while queue:
        currentNode = queue.pop(0)
        sub_array.append(currentNode.val)
        processed_nodes += 1

        if currentNode.left:
            queue.append(currentNode.left)
           
        if currentNode.right:
            queue.append(currentNode.right) 
           
        if processed_nodes == starting_queue_size:
            result.append(sub_array)
            starting_queue_size = len(queue)
            sub_array = []
            processed_nodes = 0

    return result



if __name__ == "__main__":
  testTree = Node(3)
  testTree.left = Node(54)
  testTree.right = Node(5)

  print(levelOrder(testTree))

  print(bfs(testTree))