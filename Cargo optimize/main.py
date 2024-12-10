class node: #create the node of the linked list
    def __init__(self, id, weight, volume, value, destination, distance):
        self.id = id
        self.weight = weight
        self.volume = volume
        self.value = value
        self.destination = destination
        self.distance = distance
        self.next = None

class linkedlist: #initialize the list
    def __init__(self):
        self.head = None
        self.current_id = 1
        self.city_distances = {
            "Ha Noi":40,
            "Hai Phong":150,
            "Da Nang":250,
            "Nha Trang":400,
            "Dalat":500,
            "HCMC":600
        }

    def add_package(self, weight, length, width, height, value, destination): #add package
        volume = length * width * height
        if weight < 0 or volume < 0 or value < 0: #check the package value, if below 0 then it is invalid
            raise ValueError("Weight, volume, value or distance must be a positive number.")
        if destination not in self.city_distances: #check if city is correct
            raise ValueError(f"Destination '{destination}' is not valid. Please choose from {list(self.city_distances.keys())}.")
        
        distance = self.city_distances[destination] #take the distance value from the dictionary
        new_node = node(self.current_id,weight,volume,value,destination,distance) #create a new node

        self.current_id += 1
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append({
                "id": current.id,
                "weight": current.weight,
                "volume": current.volume,
                "value": current.value,
                "destination": current.destination,
                "distance": current.distance,
            })
            current = current.next
        return result
    
    def sort(self):
        packages = self.to_list()

        packages.sort(key=lambda x: x['distance'])

        self.head = None
        for package in packages:
            sorted_node = node(
                package['id'],
                package['weight'],
                package['volume'],
                package['value'],
                package['destination'],
                package['distance']
            )
            if not self.head:
                self.head = sorted_node
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = sorted_node

    def display(self):
        current = self.head
        if not current:
            print("No packages in the list.")
            return
        while current:
            print(f"ID: {current.id}, Weight: {current.weight}, Volume: {current.volume}, Value: {current.value}, "
                f"Destination: {current.destination}, Distance: {current.distance} km")
            current = current.next

    def invoice(self, weight_rate, distance_rate): #print invoice
        current = self.head
        total_cost = 0

        print("\n--- Shipping Invoice ---") #header
        print(f"{'ID':<5}{'Destination':<15}{'Weight (kg)':<15}{'Distance (km)':<15}{'Cost (VNĐ)':<10}") #display in a columm
        print("-" * 60)

        while current: 
            cost = (current.weight * weight_rate) + (current.distance * distance_rate)
            total_cost += cost

            print(f"{current.id:<5}{current.destination:<15}{current.weight:<15}{current.distance:<15}{cost:<10.2f}")
            current = current.next #display according the columm

        print("-" * 60)
        print(f"{'Total Cost':<50}{total_cost:<10.2f}")
        print("-" * 60) #footer
