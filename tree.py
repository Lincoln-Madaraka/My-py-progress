def draw_tree(height):
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        hashes = "#" * (2 * i - 1)
        print(spaces + hashes)

# Example usage
tree_height = int(input("Enter the height of the tree: "))
draw_tree(tree_height)
