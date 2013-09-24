#============IMPORTS==========#
import vector
import unittest
from cells import Cell
#==========END IMPORTS========#

#Unit Test
TestCase = unittest.TestCase

#Food Class
class Food:
	"""Food items which are eaten by cells"""
	def __init__(self, x, y):
		#consider adding randomization factor
		self.energy = 0.5		#Energy which food will give cell when consumed
		self.pos = vector.Point(x, y)	#Starting Position

class CreationTest(TestCase):
	"""UnitTest for food"""
	def setUp(self):
		self.food_obj = Food(1, 2)
	def runTest(self):
		self.assertEquals(self.food_obj.energy, 1)
		self.assertEquals(self.food_obj.pos.x, 1)
		self.assertEquals(self.food_obj.pos.y, 2)

if __name__ == "__main__":
	unittest.main()

