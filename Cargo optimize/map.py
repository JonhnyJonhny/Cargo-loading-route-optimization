import math
import heapq

def euclidean_distance(x1,y1,x2,y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) * 111

city_coordinate = {
    "Ha Noi":(21.0278, 105.8342),
    "Hai Phong":(20.8449, 106.6881),
    "Da Nang":(16.0544, 108.2022),
    "Nha Trang":(12.2529, 109.1899),
    "Dalat":(11.9404, 108.453),
    "HCMC":(10.8231, 106.6297)
}

def distant_graph(coordinates):
    graph = {}
    cities = list(coordinates.keys())
    for i in range (len(cities)):
        for j in range (i + 1, len(cities)):
            city1, city2 = cities[i],cities[j]
            x1, y1 = coordinates[city1]
            x2, y2 = coordinates[city2]
            distant = euclidean_distance(x1,y1,x2,y2)

            if city1 not in graph:
                graph[city1] = {}
            if city2 not in graph:
                graph[city2] = {}

            graph[city1][city2] = distant
            graph[city2][city1] = distant
    return graph
    
def dijkstra(graph, start, target):
    priority_queue = [(0, start)]
    distances = {city: float("inf") for city in graph}
    distances[start] = 0
    previous_node = {city: None for city in graph}

    while priority_queue:
        current_cost, current_city = heapq.heappop(priority_queue)

        if current_city == target:
            break

        for neighbor, weight in graph[current_city].items():
            new_cost = current_cost + weight
            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                previous_node[neighbor] = current_city
                heapq.heappush(priority_queue, (new_cost, neighbor))

    path = []
    current_city = target
    while current_city is not None:
        path.append(current_city)
        current_city = previous_node[current_city]
    path.reverse()

    return path, distances[target]

city_graph = distant_graph(city_coordinate)

start_city = "Ha Noi"
target_city = "Dalat"

shortest_path, shortest_distance = dijkstra(city_graph, start_city, target_city)

print(f"Shortest Path from {start_city} to {target_city}: {' -> '.join(shortest_path)}")
print(f"Total Distance: {shortest_distance:.1f} km")