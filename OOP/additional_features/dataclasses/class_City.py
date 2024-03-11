from dataclasses import dataclass


@dataclass
class City:
    name: str
    population: int
    founded: int


# Test №1
city = City('Tokyo', 14043239, 1457)

print(city)
print(city.name)
print(city.population)

# Test №2
city1 = City('Tokyo', 14043239, 1457)
city2 = City('New York', 8467513, 1624)
city3 = City('Tokyo', 14043239, 1457)

print(city1 == city2)
print(city1 != city2)
print(city1 == city3)
print(city1 != city3)
