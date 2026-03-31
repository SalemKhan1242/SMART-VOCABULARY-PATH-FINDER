import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from collections import deque

# Load Dictionary
def load_dictionary(file_path, word_length):
    words = set()
    try:
        with open(file_path, 'r') as file:
            for word in file:
                word = word.strip().lower()
                if len(word) == word_length:
                    words.add(word)
    except FileNotFoundError:
        print(" words.txt not found! Using fallback dictionary.")
        words = {"cat", "cot", "cog", "dog", "dot", "dat", "bat", "bot", "bog"}

    return words

# Generate Neighbors
def get_neighbors(word, word_set):
    neighbors = []
    alphabets = "abcdefghijklmnopqrstuvwxyz"

    for i in range(len(word)):
        for letter in alphabets:
            new_word = word[:i] + letter + word[i+1:]
            if new_word in word_set and new_word != word:
                neighbors.append(new_word)

    return neighbors

# BFS Algorithm
def bfs_word_ladder(start, goal, word_set):
    queue = deque([start])
    visited = set([start])
    parent = {start: None}

    while queue:
        current = queue.popleft()

        if current == goal:
            return reconstruct_path(parent, start, goal)

        for neighbor in get_neighbors(current, word_set):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)
 return None

# Reconstruct Path
def reconstruct_path(parent, start, goal):
    if goal not in parent:
        return None

    path = []
    current = goal

    while current:
        path.append(current)
        current = parent[current]

    path.reverse()
    return path
# Main Program
def main():
    print("\n Smart Vocabulary Path Finder \n")

    start = input("Enter start word: ").lower().strip()
    goal = input("Enter target word: ").lower().strip()
 # Validation
    if len(start) != len(goal):
        print(" Error: Words must be the same length!")
        return

    if start == goal:
        print(" Start and goal are the same!")
        print("Steps: 0")
        return
# Load dictionary
    word_set = load_dictionary("words.txt", len(start))

    if start not in word_set:
        word_set.add(start)
    if goal not in word_set:
        word_set.add(goal)
 # Run BFS
    path = bfs_word_ladder(start, goal, word_set)
# Output
    if path:
        print("\n Transformation found!")
        print(" → ".join(path))
        print(f"Steps required: {len(path) - 1}")
    else:
        print("\n No valid transformation path found!")

# Run Program
if __name__ == "__main__":
    main()
