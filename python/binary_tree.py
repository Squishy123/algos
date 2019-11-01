
# Creates a binary tree using list of list representation
def BinaryTree(r):
    return [r, [], []]

# Given the root node insert a new node to the left branch
def insertLeft(root, newNode):
    t=root.pop(1)
    # if the node already exists, insert the existent node as a left node of new brach
    if len(t) > 1:
        root.insert(1, [newNode,t,[]])
    # insert new branch with empty left and right nodes
    else:
        root.insert(1, [newNode,[],[]])
    return root

# Given the root node insert a new node to the right branch
def insertRight(root, newNode):
    t=root.pop(2)
    # if the node already exists, insert the existent node as a right node of new brach
    if len(t) > 1:
        root.insert(2, [newNode,[],t])
    # insert new branch with empty left and right nodes
    else:
        root.insert(2, [newNode,[],[]])
    return root

# Get the root value of a tree or branch
def getRootVal(root):
    return root[0]

# Set the root value of a tree or branch
def setRootVal(root,value):
    root[0]=value

# Get the left child
def getLeftChild(root):
    return root[1]

# Get the right child
def getRightChild(root):
    return root[2]

def getLen(root):
    def aux(root, count=0):
        if(root == []):
            return [count]
        else:
            count+=1
        
        if(root[1] == []):
            return aux(root[2], count)
        if(root[2] == []) :
            return aux(root[1], count)

        return aux(root[1], count) + aux(root[2], count)
    return max(aux(root))

def displayLayers(root):
    layers=dict()
    def generateLayers(root, count=0):
        if(root == []):
            return
        else:
            try:
                layers[count] += [root[0]]
            except:
                layers[count] = [root[0]]
                
            count+=1

            if(not root[1] == []):
                generateLayers(root[1], count)
            if(not root[2] == []) :
                generateLayers(root[2], count)

    generateLayers(root)
    for l in layers.keys():
        print(layers[l])

displayLayers([0, [1, [3, [4, [], []], []], []], [2, [3, [], []], []]])