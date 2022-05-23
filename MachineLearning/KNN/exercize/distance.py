star_wars = [125, 1977]
raiders = [115, 1981]
mean_girls = [97, 2004]

def distance(movie1,movie2):
  x = (movie1[0]-movie2[0])**2
  y = (movie1[1]-movie2[1])**2

  return (x+y)**.5



print(distance(star_wars,raiders))
print(distance(star_wars,mean_girls))


star_wars = [125, 1977, 11000000]
raiders = [115, 1981, 18000000]
mean_girls = [97, 2004, 17000000]

def distance(movie1, movie2):
  distance=0
  for i in range(len(movie1)):
    x = (movie1[i] - movie2[i]) ** 2
    distance +=x
  return distance**.5

print(distance(star_wars,raiders))
print(distance(star_wars,mean_girls))
