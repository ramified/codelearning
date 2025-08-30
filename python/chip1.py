from chipfiring import CFGraph , CFDivisor, CFDataProcessor, visualize
from chipfiring import linear_equivalence , is_winnable

vertices = {"Alice", "Bob", "Charlie", "Elise"} 
edges = [ ("Alice", "Bob", 1), ("Alice", "Charlie", 1), ("Alice", "Elise", 2), ("Bob", "Charlie", 1), ("Charlie", "Elise", 1) ] 
graph = CFGraph(vertices , edges)

divisor = CFDivisor(graph , [("Alice", 2), ("Bob", -2.1), ("Charlie", 4), ("Elise", -1)])
print(f"Total degree: {divisor.get_total_degree()}")
processor = CFDataProcessor()
print(divisor.is_effective())
print(f"Is effective: {divisor.is_effective()}")
print(is_winnable(divisor))  # is_winnable changes the divisor
visualize(divisor)
# print(f"Is effective: {divisor.is_effective()}")
# print(is_winnable(divisor))


# from chipfiring import tetrahedron , cube , octahedron , dodecahedron , icosahedron , visualize

# octa = octahedron()
# visualize(octa)