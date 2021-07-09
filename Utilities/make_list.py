def forward(head_node):
    current_node = head_node
    list = []
    while(current_node != None):
        list.append(current_node.data)
        current_node = current_node.next
    return list


def backward(head_node):
    current_node = head_node
    list = []
    while(current_node != None):
        list.insert(0, current_node.data)
        current_node = current_node.next
    return list

# return list of nodes inorder - left, root, right


def inorder(current):
    # base case
    if(current == None):
        return None
    data = []
    # traverse left subtree
    temp = inorder(current.left)
    if(temp != None):
        data += temp
    # add root to ordered list
    data.append(current.data)
    # traverse right subtree
    temp = inorder(current.right)
    if(temp != None):
        data += temp
    return data


# return list of nodes preorder - root, left, right
def preorder(current):
    # base case
    if(current == None):
        return None
    data = []
    # add root to ordered list
    data.append(current.data)
    # traverse left subtree
    temp = preorder(current.left)
    if(temp != None):
        data += temp
    # traverse right subtree
    temp = preorder(current.right)
    if(temp != None):
        data += temp
    return data


# return list of nodes postorder - left, right, root
def postorder(current):
    # base case
    if(current == None):
        return None
    data = []
    # traverse left subtree
    temp = postorder(current.left)
    if(temp != None):
        data += temp
    # traverse right subtree
    temp = postorder(current.right)
    if(temp != None):
        data += temp
    # add root to ordered list
    data.append(current.data)
    return data
