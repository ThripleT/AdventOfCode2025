from fourFirst import DIAGRAM, check_diagram, GRID
import time

# Set to True to visualize at the end, False to skip visualization
VISUALIZE = False

if VISUALIZE:
    import matplotlib.pyplot as plt

def check_neighbors(diagram, y, x, GRID):
    """Check 8 neighbors of (y, x) to see which are now accessible rolls.
    A roll '@' is accessible if it has < 4 '@' neighbors.
    """
    accessible = []
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dy == 0 and dx == 0:
                continue
            ny, nx = y + dy, x + dx
            if 0 <= ny < len(diagram) and 0 <= nx < len(diagram[ny]):
                if diagram[ny][nx] == '@':
                    # Count '@' neighbors of (ny, nx)
                    counter = 0
                    for ddy, ddx in GRID:
                        if 0 <= ny+ddy < len(diagram) and 0 <= nx+ddx < len(diagram[ny]):
                            if diagram[ny+ddy][nx+ddx] == '@':
                                counter += 1
                    if counter < 4:
                        accessible.append((ny, nx))
    return accessible

def simulate_moves(diagram, position, accessible_positions, depth=5, top_k=5):
    """Simulate future moves using lookahead.
    
    Returns (best_next_roll, estimated_cost) for the first move that leads to best path depth moves ahead.
    """
    if depth == 0 or not accessible_positions:
        return None, 0
    
    # Get top_k candidates by distance
    sorted_pos = sorted(accessible_positions, key=lambda p: (abs(position[0] - p[0]) + abs(position[1] - p[1]), p[0], p[1]))
    candidates = sorted_pos[:min(top_k, len(sorted_pos))]
    
    best_move = None
    best_cost = float('inf')
    
    for candidate in candidates:
        # Simulate taking this move
        cost = abs(position[0] - candidate[0]) + abs(position[1] - candidate[1]) + 1
        
        if depth == 1:
            # Base case: only this move
            if cost < best_cost:
                best_cost = cost
                best_move = candidate
        else:
            # Recursive: simulate next moves
            temp_diagram = [row for row in diagram]
            temp_diagram[candidate[0]] = temp_diagram[candidate[0]][:candidate[1]] + 'X' + temp_diagram[candidate[0]][candidate[1]+1:]
            
            new_pos = candidate
            new_access = list(check_diagram(temp_diagram))
            
            # Recursively find best next move
            _, future_cost = simulate_moves(temp_diagram, new_pos, new_access, depth - 1, top_k)
            total_cost = cost + future_cost
            
            if total_cost < best_cost:
                best_cost = total_cost
                best_move = candidate
    
    return best_move, best_cost

def main():
    # it's not worth it, just take the best immediate move
    # it takes longer and is worse than the simple greedy approach (propably need more depth but takes too long then)
    depths_tops = [(1, 1)]
    for depth, top_k in depths_tops:
        print(f"Starting simulation with depth={depth}, top_k={top_k}")
        timer = time.time()
        diagram = [row for row in DIAGRAM]
        counter = 0
        position = (0, 0)
        moves = []  # Track all moves for replay
        
        # Initial full scan
        accessible_positions = list(check_diagram(diagram))

        while True:
            if not accessible_positions:
                break
            
            # Use lookahead to pick best move
            next_roll, _ = simulate_moves(diagram, position, accessible_positions, depth=depth, top_k=top_k)
            
            if next_roll is None:
                break
            
            # Record move
            moves.append((position, next_roll))
            
            # Update diagram
            diagram[next_roll[0]] = diagram[next_roll[0]][:next_roll[1]] + 'X' + diagram[next_roll[0]][next_roll[1]+1:]
            
            # Update position and counter
            counter += abs(position[0] - next_roll[0]) + abs(position[1] - next_roll[1]) + 1
            position = next_roll
            
            # Remove collected roll and reevaluate only 8 neighbors
            try:
                accessible_positions.remove(next_roll)
            except ValueError:
                pass
            new_accessible = check_neighbors(diagram, next_roll[0], next_roll[1], GRID)
            for pos in new_accessible:
                if pos not in accessible_positions:
                    accessible_positions.append(pos)
            #print(f"percent finished: {100 * len(moves) / 8727:.2f}%, {len(moves)}")
        print(f"Depth {depth}, Top {top_k} completed in {time.time() - timer:.2f}s, Total Time: {counter}")
    
    # Visualize at the end if enabled
    if VISUALIZE:
        replay_visualization(DIAGRAM, moves, counter)
    
    return counter

def replay_visualization(diagram_orig, moves, total_counter):
    """Replay the moves using visualization."""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_aspect('equal')
    
    height = len(diagram_orig)
    width = max(len(row) for row in diagram_orig) if diagram_orig else 0
    
    ax.set_xlim(-0.5, width - 0.5)
    ax.set_ylim(-0.5, height - 0.5)
    ax.invert_yaxis()
    
    # Plot all initial available rolls
    for i, row in enumerate(diagram_orig):
        for j, char in enumerate(row):
            if char == '@':
                ax.plot(j, i, 'yo', markersize=3, markeredgecolor='orange', markeredgewidth=0.5)
    
    ax.grid(True, alpha=0.3)
    
    # Replay moves
    diagram = [row for row in diagram_orig]
    position = (0, 0)
    counter = 0
    
    pos_marker, = ax.plot(position[1], position[0], 'r*', markersize=5, markeredgecolor='darkred', markeredgewidth=1)
    title = ax.set_title(f"Paper Roll Collection - Total Time: {counter}", fontsize=14, fontweight='bold')
    
    plt.ion()
    
    for from_pos, to_pos in moves:
        # Mark collected roll
        ax.plot(to_pos[1], to_pos[0], 'gs', markersize=3)
        
        # Update diagram
        diagram[to_pos[0]] = diagram[to_pos[0]][:to_pos[1]] + 'X' + diagram[to_pos[0]][to_pos[1]+1:]
        
        # Update position and counter
        counter += abs(position[0] - to_pos[0]) + abs(position[1] - to_pos[1]) + 1
        position = to_pos
        
        # Update visualization
        pos_marker.set_data([position[1]], [position[0]])
        title.set_text(f"Paper Roll Collection - Total Time: {counter}")
        plt.draw()
        plt.pause(0.01)
    
    plt.show()

if __name__ == "__main__":
    print(main())