# return list of nodes front to back
def forward(head_node):
    list = []
    current_node = head_node
    while(current_node is not None):
        list.append(current_node.data)
        current_node = current_node.next
    return list


# return list of nodes back to front
def backward(head_node):
    list = []
    current_node = head_node
    while(current_node is not None):
        list.insert(0, current_node.data)
        current_node = current_node.next
    return list


# return list of nodes front to back (circular list)
def circular(last_node):
    if(last_node is None):
        return []
    list = []
    list.append(last_node.next.data)
    current_node = last_node.next.next
    while(current_node is not last_node.next):
        list.append(current_node.data)
        current_node = current_node.next
    return list


# return list of nodes level order (priority queue)
def priority(queue):
    list = []
    for node in queue:
        list.append(node.data)
    return list


# return list of nodes inorder - left, root, right
def inorder(current):
    # base case
    if(current is None):
        return []
    data = []
    # traverse left subtree
    temp = inorder(current.left)
    if(temp is not None):
        data += temp
    # add root to ordered list
    data.append(current.data)
    # traverse right subtree
    temp = inorder(current.right)
    if(temp is not None):
        data += temp
    return data


# return list of nodes preorder - root, left, right
def preorder(current):
    # base case
    if(current is None):
        return []
    data = []
    # add root to ordered list
    data.append(current.data)
    # traverse left subtree
    temp = preorder(current.left)
    if(temp is not None):
        data += temp
    # traverse right subtree
    temp = preorder(current.right)
    if(temp is not None):
        data += temp
    return data


# return list of nodes postorder - left, right, root
def postorder(current):
    # base case
    if(current is None):
        return []
    data = []
    # traverse left subtree
    temp = postorder(current.left)
    if(temp is not None):
        data += temp
    # traverse right subtree
    temp = postorder(current.right)
    if(temp is not None):
        data += temp
    # add root to ordered list
    data.append(current.data)
    return data
