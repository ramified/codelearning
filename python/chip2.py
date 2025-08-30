from chipfiring import CFGraph , CFDivisor, CFLaplacian , CFiringScript
import numpy as np

vertices = {"Alice", "Bob", "Charlie", "Elise"} 
edges = [ ("Alice", "Bob", 1), ("Alice", "Charlie", 1), ("Alice", "Elise", 2), ("Bob", "Charlie", 1), ("Charlie", "Elise", 1) ] 
graph = CFGraph(vertices , edges)
initial_divisor = CFDivisor(graph , [("Alice", 2), ("Bob", -3), ("Charlie", 4), ("Elise", -1)])

laplacian = CFLaplacian(graph)
script = {"Charlie": 1, "Bob": -1}
firing_script = CFiringScript(graph , script)
result_divisor = laplacian.apply(initial_divisor , firing_script)
print(f"Result: {result_divisor.degrees_to_str()}")