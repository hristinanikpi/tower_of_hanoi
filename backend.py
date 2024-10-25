# Recursive function that solves Tower of Hanoi
def tower_of_hanoi_recursive(n, source, destination, auxiliary, moves):
    if n == 1:
        moves.append(f"Take disk 1 from rod {source} to rod {destination}.")
        return
    tower_of_hanoi_recursive(n-1, source, auxiliary, destination, moves)
    moves.append(f"Take disk {n} from rod {source} to rod {destination}.")
    tower_of_hanoi_recursive(n-1, auxiliary, destination, source, moves)


# Iterative funcion that solves Tower of Hanoi
def tower_of_hanoi_iterative(n, source, destination, auxiliary, moves):
    total_moves = 2**n - 1  # Total moves required
    for i in range(1, total_moves + 1):
        # Determine the source and destination rods based on the move number
        if i % 3 == 1:  # Move between source and destination
            moves.append(f"Take disk {((i - 1) % n) + 1} from rod {source} to rod {destination}.")
        elif i % 3 == 2:  # Move between source and auxiliary
            moves.append(f"Take disk {((i - 1) % n) + 1} from rod {source} to rod {auxiliary}.")
        else:  # Move between auxiliary and destination
            moves.append(f"Take disk {((i - 1) % n) + 1} from rod {auxiliary} to rod {destination}.")

# Function that solves Tower of Hanoi and returnes a JSON object 
def tower_of_hanoi_service(n):
    moves = []
    tower_of_hanoi_recursive(n, 'A', 'C', 'B', moves)
    #tower_of_hanoi_iterative(n, 'A', 'C', 'B', moves)
    return {"disks": n, "moves": moves}