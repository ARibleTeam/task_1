import unittest
from  area_figures import Circle, Triangle

class TestCircle(unittest.TestCase):
    def setUp(self):
        self.circle = Circle(10)
    
    def test_area(self):
        self.assertEqual(self.circle.area, 314.1592653589793)

class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.triangle = Triangle(8, 15, 17)
    
    def test_area(self):
        self.assertEqual(self.triangle.area, 60.0)

if __name__ == "__main__":
    unittest.main()
