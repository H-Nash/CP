# Getting Ready for Physics Class Project (Functions)
# Uncomment this when you reach the "Use the Force" section
# Globale var declaration
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Converts Fahrenheit to Celcius
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5 / 9
  return c_temp

# Converts Celcius to Fahrenheit
def c_to_f(c_temp):
  f_temp = c_temp * (9 / 5) + 32
  return f_temp

# Calculate Force
def get_force(mass, acceleration):
  return mass * acceleration

# Calculate energy
def get_energy(mass, c = 3*10**8):
  return mass*c

# Calculate Work
def get_work(train_mass, train_acceleration, train_distance):
  return get_force(train_mass, train_acceleration) * train_distance

# Main Body
f100_in_celsius = f_to_c(100)
c0_in_fahrent = c_to_f(0)

train_force = get_force(train_mass, train_acceleration)
print(f"The GE train supplies {train_force} Newtons of force.")

bomb_energy = get_energy(bomb_mass)
print(f"A 1kg bomb supplies {bomb_energy} Joules.")

train_work = get_work(train_mass, train_acceleration, train_distance)
print(f"the GE train does {train_work} Joules of work over {train_distance} meters.")
