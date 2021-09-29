planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
new_file = open('planets.txt', 'w', encoding='utf-8')
for planet in planets:
    new_file.write(planet + '\n')
new_file.close()
