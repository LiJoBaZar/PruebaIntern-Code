class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Definimos la función que verificara si un árbol binario es un árbol de búsqueda binario
def checkBST(root, min_val, max_val):

    if root is None:
        return True

    if root.data <= min_val or root.data >= max_val:
        return False

    return (checkBST(root.left, min_val, root.data) and
            checkBST(root.right, root.data, max_val))

# Esta función es la principal, toma la entrada y crea el árbol binario
def check_binary_search_tree_(root):
    return checkBST(root, float('-inf'), float('inf'))
