#! /usr/bin/env python

import os.path
import queue

test_input = [
    "1163751742",
    "1381373672",
    "2136511328",
    "3694931569",
    "7463417111",
    "1319128137",
    "1359912421",
    "3125421639",
    "1293138521",
    "2311944581"
]


def read_input_grid(input):
    g = []
    for line in input:
        g.append([int(p) for p in line])
    return g


def pg(g):
    for r in g:
        print(" ".join([str(c) for c in r]))

# A* search through grid, so need a goal function!
# Based on https://leetcode.com/problems/shortest-path-in-binary-matrix/discuss/313347/A*-search-in-Python


def get_goal_function(grid):
    # given grid, return a function which returns true if cell is goal
    max_r, max_c = len(grid) - 1, len(grid[0]) - 1

    def bottom_right(cell):
        return cell == (max_r, max_c)
    return bottom_right


def get_successor_function(grid):
    # given grid, return a function which returns list of all cells adjacent to cell
    def get_adjacent_cells(cell):
        # we can only move left, right, up or down
        max_r, max_c = len(grid) - 1, len(grid[0]) - 1
        if type(cell[1]) is tuple:
            # discard priority in cell[0]
            r, c = cell[1]
        else:
            r, c = cell
        results = []
        # up
        if r - 1 >= 0:
            results.append((r-1, c))
        # down
        if r + 1 <= max_r:
            results.append((r+1, c))
        # left
        if c - 1 >= 0:
            results.append((r, c-1))
        # right
        if c + 1 <= max_c:
            results.append((r, c+1))
        print(f"cell: {cell}, adjacent: {results}")
        return results
    return get_adjacent_cells


def a_star_graph_search(start, goal_function, successor_function, heuristic):
    visited = set()
    came_from = dict()
    distance = {start: 0}
    frontier = queue.PriorityQueue()
    frontier.put(start)
    while frontier:
        node = frontier.get_nowait()
        if type(node[1]) is tuple:
            node = node[1]
        if node in visited:
            continue
        if goal_function(node):
            return reconstruct_path(came_from, start, node)
        visited.add(node)
        for successor in successor_function(node):
            priority = distance[node] + 1 + heuristic(successor)
            frontier.put((priority, successor))
            if (successor not in distance
                    or distance[node] + 1 < distance[successor]):
                distance[successor] = distance[node] + 1
                came_from[successor] = node
    return None


def reconstruct_path(came_from, start, end):
    reverse_path = [end]
    while end != start:
        end = came_from[end]
        reverse_path.append(end)
    return list(reversed(reverse_path))


def get_heuristic(grid):
    max_r, max_c = len(grid) - 1, len(grid[0]) - 1

    def get_clear_distance_from_goal(cell):
        if type(cell[1]) is tuple:
            cell = cell[1]
        (i, j) = cell
        cost = grid[i][j]
        # manhattan distance
        distance = sum([abs(max_r - i), abs(max_c - j)])
        # how to combine cost + distance to get the right heuristic??
        return cost + distance
    return get_clear_distance_from_goal


def part1(input):
    grid = read_input_grid(input)
    pg(grid)

    max_r = len(grid) - 1
    max_c = len(grid[0]) - 1

    print(f"start (0,0) - {grid[0][0]}")
    print(f"end ({max_r},{max_c}) - {grid[max_r][max_c]}")

    shortest_path = a_star_graph_search(
        start=(0, 0),
        goal_function=get_goal_function(grid),
        successor_function=get_successor_function(grid),
        heuristic=get_heuristic(grid)
    )
    print(shortest_path)
    print(" ".join([str(grid[t[0]][t[1]]) for t in shortest_path]))
    print(sum([grid[t[0]][t[1]]
          for t in shortest_path[1:]]))  # skip origin cell
    return None


def part2(input):
    return None


day = os.path.basename(__file__).split('.')[0][-2:]
input = list((l.strip() for l in open(f"./inputs/day{day}").readlines()))
print(f"Day {day}")
print("test part 1:", part1(test_input))
# print("part 1:", part1(input))
# print("test part 2:", part2(test_input))
# print("part 2:", part2(input))
