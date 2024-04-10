# Basic Node Before Values and Linked Nodes are entered
class Node:
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node
    
  def set_link_node(self, link_node):
    self.link_node = link_node
    
  def get_link_node(self):
    return self.link_node
  
  def get_value(self):
    return self.value

# Test Data for node class
yacko = Node("likes to yak")
wacko = Node("has a penchant for hoarding snacks")
dot = Node("enjoys spending time in movie lots")

# Set Yacko and dots linked nodes
yacko.set_link_node(dot)
dot.set_link_node(wacko)

# Get dot and wackos values from links
dots_data = yacko.get_link_node().get_value()
wackos_data = dot.get_link_node().get_value()
print(dots_data)
print(wackos_data)
