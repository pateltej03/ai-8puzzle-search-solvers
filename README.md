# 🧠 AI Search Solvers for the 8-Puzzle Problem

This project contains my implementation of various search algorithms to solve classic and modified versions of the **8-puzzle problem**, as part of my Artificial Intelligence coursework at Penn State.

The work is organized into two parts:

-   **Q1:** Solve the standard 8-puzzle where the goal state is a sorted grid with the blank in the top-left.
-   **Q2:** Solve a modified 8-puzzle where the **sum of the top row must equal 11**.

---

## 🔍 Algorithms Implemented

For both Q1 and Q2, I implemented the following search algorithms:

-   Depth-First Search (**DFS**)
-   Breadth-First Search (**BFS**)
-   Uniform Cost Search (**UCS**)
-   A\* Search with:
    -   **Manhattan Distance Heuristic**
    -   **Straight-Line Distance Heuristic**

Each algorithm is designed to:

-   Accept an initial puzzle configuration from `input.txt`
-   Return the solution path as a list of directional moves
-   Track and optionally print the number of **node expansions** for performance evaluation

---

## 🧩 Example Input

Contents of `input.txt`:

    8,1,4,5,2,6,3,7,_

This represents the 3x3 puzzle grid where `'_'` is the blank space.

---

## 🗂️ File Structure

-   `solution_q1.py`: Solves Q1 using all 5 search strategies
-   `solution_q2.py`: Solves Q2 (goal: top row sum = 11) using all 5 search strategies
-   `input.txt`: Specifies the starting puzzle configuration

---

## 🚀 How to Run

Make sure Python 3.9+ is installed, then run:

    python3 solution_q1.py
    or
    python3 solution_q2.py

---

## ✅ Output Format

Each file prints solutions like:

    The solution of Q1.1a is: 2D,1D,4L,5U,6R...
    The solution of Q2.1e is: 3U,1L,2D...

Each move describes which tile moved and in what direction (e.g., `2D` means tile 2 moved **down**).

---

## 🧠 Learning Outcomes

-   Gained deep intuition into search strategies and their trade-offs in terms of completeness, optimality, and efficiency
-   Implemented real heuristics from scratch and validated their performance
-   Understood how small changes in goal definitions can shift search complexity drastically
-   Practiced clean, modular algorithm design

---

## 📌 Future Extensions

-   Visualize the puzzle solving process step-by-step
-   Implement iterative deepening search
-   Add a GUI to manually test puzzles and visualize algorithms
-   Profile performance with much larger puzzle variants (e.g., 15-puzzle)

---

## 🧠 Let’s Connect!

**Tej Jaideep Patel**  
B.S. Computer Engineering  
📍 Penn State University  
✉️ tejpatelce@gmail.com  
📞 814-826-5544

---
