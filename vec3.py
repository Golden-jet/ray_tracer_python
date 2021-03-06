from math import sqrt

class Vec3:
	def __init__(self, x = 0, y = 0, z = 0):
		self.x = x
		self.y = y
		self.z = z

	def __str__(self):
		return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

	def __add__(self, v3):
		return Vec3(self.x + v3.x, self.y + v3.y, self.z + v3.z)
	def __sub__(self, v3):
		return Vec3(self.x - v3.x, self.y - v3.y, self.z - v3.z)
	def __mul__(self, t):
		return Vec3(self.x * t, self.y * t, self.z * t)
	def __truediv__(self, t):
		return Vec3(self.x / t, self.y / t, self.z / t)

	def dot(self, v3):
		return self.x * v3.x + self.y * v3.y + self.z * v3.z
	def cross(self, v3):
		return Vec3(self.y * v3.z - self.z * v3.y, self.z * v3.x - self.x * v3.z, self.x * v3.y - self.y * v3.x)
	def length(self):
		return sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
	def normalized(self):
		return self/self.length()
