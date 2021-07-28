import unittest

from myscripts import util

class TestUtils(unittest.TestCase):
  
  def test_get_holiday(self):
    self.assertEqual(util.get_holiday('a'), 'Public holiday')
    self.assertEqual(util.get_holiday('b'), 'Easter holiday')
    self.assertEqual(util.get_holiday('c'), 'Christmas')


  def test_get_holiday_return_none(self):
    self.assertEqual(util.get_holiday('0'), None)
    self.assertEqual(util.get_holiday('e'), None)

  def test_get_assortment(self):
    self.assertEqual(util.get_assortment('a'), "Basic")
    self.assertEqual(util.get_assortment('b'), "Extra")
    self.assertEqual(util.get_assortment('c'), "Extended")

  def test_get_month_year(self):
    

