from chipfiring.CFGraph import CFGraph
from chipfiring.CFDivisor import CFDivisor
from chipfiring.algo import EWD

def main():
    # Create a simple graph
    vertices = {"A", "B", "C", "D", "E"}
    edges = [("A", "B", 1), ("B", "C", 1), ("C", "E", 1), ("B", "D", 1),("E", "D", 1), ("A", "C", 1)]
    graph = CFGraph(vertices, edges)

    # Create a divisor
    divisor = CFDivisor(graph, [("A", -2), ("B", 0), ("C", 0), ("D", 4),("E", -1)])

    # Run the EWD algorithm with visualization enabled.
    # The EWD function will now handle the visualization directly.
    is_winnable, _, _, visualizer = EWD(graph, divisor, optimized=False, visualize=True)

    print(f"Is the divisor winnable? {is_winnable}")

    visualizer.visualize()

if __name__ == "__main__":
    main()