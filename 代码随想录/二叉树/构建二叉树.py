from tool_Tree import Tree

test_tree = [3, 1, 5, None, 2, 4, 6]
root = Tree.construct_binary_tree(test_tree)
print(Tree.printTree2(root))
# tree = Tree([])
# tree.root = root
# print(tree.printTree())