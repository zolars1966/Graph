class Vertex:
	def __init__(self, name, pos):
		self.name = name
		self.pos = pos

	def __str__(self):
		return self.name

	def __repr__(self):
		return self.name

	def __eq__(self, vert_name):
		return self.name == vert_name

	def __hash__(self):
		return hash(self.name) ^ hash(self.pos)
