# Global Variables
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
attractions = [[] for i in destinations]

# Traveling to faraway lands
# Find dst location in list
def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

# Find traveler dst in list
def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

# Visiting interesting places
# Adds attraction to attractions list
def add_attraction(destination, attraction):
  destination_index = get_destination_index(destination)
  attractions_for_destination = attractions[destination_index].append(attraction)
  return attractions_for_destination

# Finding the best places to go
# Matches travelers interests with a location they may be interested in
def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []

  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = attraction[1]

    for interest in interests:
      if interest in attraction_tags: 
        attractions_with_interest.append(possible_attraction[0])

  return attractions_with_interest

# See th parts of a city you want to see
# Get attractions for location traveler is visiting
def get_attractions_for_travler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  interests_string = f"Hi {traveler[0]}, we think you'll like these places around {traveler_destination}: {traveler_attractions[0]}"
  return interests_string

# Main section
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

la_arts = find_attractions("Los Angeles, USA", ["art"])

smills_france = get_attractions_for_travler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)
