import heapq

schoolgraph = {
    '5A': {'5B': 1},
    '5B': {'5A': 1, '5C': 1},
    '5C': {'5B': 1, '5D': 1},
    '5D': {'5C': 1, '5E': 1},
    '5E': {'5D': 1},
    
    '4A': {'4B': 1},
    '4B': {'4A': 1, '4C': 1},
    '4C': {'4B': 1, '4D': 1},
    '4D': {'4C': 1, '4E': 1},
    '4E': {'4D': 1},
    
    '3A': {'3B': 1},
    '3B': {'3A': 1, '3C': 1},
    '3C': {'3B': 1, '3D': 1},
    '3D': {'3C': 1, '3E': 1},
    '3E': {'3D': 1},
    
    '2A': {'2B': 1},
    '2B': {'2A': 1, '2C': 1},
    '2C': {'2B': 1, '2D': 1},
    '2D': {'2C': 1, '2E': 1},
    '2E': {'2D': 1},
    
    '1A': {'1B': 1},
    '1B': {'1A': 1, '1C': 1},
    '1C': {'1B': 1, '1D': 1},
    '1D': {'1C': 1, '1E': 1},
    '1E': {'1D': 1}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    queue = []
    heapq.heappush(queue, [distances[start], start])
    
    while queue:
        current_distance, current_destination = heapq.heappop(queue)
        
    
    return


start_loc = input("시작 장소를 입력해주세요:")
dijkstra(schoolgraph, start_loc)