def simple_columnar_transposition(message, key):
    cipher = ''
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    num_cols = len(key)
    num_rows = -(-len(message) // num_cols)  # Ceiling division
    
    # Fill the grid
    grid = [['' for _ in range(num_cols)] for _ in range(num_rows)]
    for i, char in enumerate(message):
        grid[i // num_cols][i % num_cols] = char

    # Read out by columns based on the key order
    for k in key_order:
        for j in range(num_rows):
            cipher += grid[j][k]
            
    return cipher

# Example Usage
message = "Hello World"

key = "KEY"
encrypted_message = simple_columnar_transposition(message, key)
print("Encrypted message:", encrypted_message)
def advanced_columnar_transposition(message, key):
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    num_cols = len(key)
    num_rows = -(-len(message) // num_cols)  # Ceiling division

    # Fill the grid
    grid = [['' for _ in range(num_cols)] for _ in range(num_rows)]
    for i, char in enumerate(message):
        grid[i // num_cols][i % num_cols] = char

    # Rearrange rows based on key order
    rearranged_grid = [['' for _ in range(num_cols)] for _ in range(num_rows)]
    for i, order in enumerate(key_order):
        for j in range(num_rows):
            if (j * num_cols + order) < len(message):
                rearranged_grid[j][i] = grid[j][order]

    # Read out by columns
    cipher = ''
    for j in range(num_cols):
        for i in range(num_rows):
            cipher += rearranged_grid[i][j]

    return cipher

# Example Usage
message = "Hello World"
key = "KEY"
encrypted_message = advanced_columnar_transposition(message, key)
print("Encrypted message (Advanced):", encrypted_message)
