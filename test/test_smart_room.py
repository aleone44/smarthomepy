import unittest
import mock.GPIO as GPIO
from unittest.mock import patch, PropertyMock
from unittest.mock import Mock

from mock.adafruit_bmp280 import Adafruit_BMP280_I2C
from src.smart_room import SmartRoom
from mock.senseair_s8 import SenseairS8


class TestSmartRoom(unittest.TestCase):


	@ patch.object(GPIO, "input")
	def test_check_room_occupated(self, mock_object:Mock):
		sr = SmartRoom()
		sr.check_room_occupancy()
		mock_object.assert_called_once_with(sr.INFRARED_PIN)
		self.assertTrue(sr.check_room_occupancy)

	@patch.object(GPIO, "input")
	def test_check_room_not_occupated(self, mock_object: Mock):
		sr = SmartRoom()
		sr.check_room_occupancy()
		mock_object.assert_called_once_with(sr.INFRARED_PIN)
		self.assertFalse(sr.check_room_occupancy)

	@patch.object(GPIO, "input")
	def test_check_room_not_occupated(self, mock_object: Mock):
		mock_object.return_value = GPIO.LOW
		sr = SmartRoom()
		sr.pin = 22
		self.assertFalse(sr.check_room_occupancy())
		mock_object.assert_called_once_with(22)

	@patch.object(GPIO, "input")
	def test_check_enough_light(self, mock_object: Mock):
		sr = SmartRoom()
		sr.check_enough_light()
		mock_object.return_value = GPIO.HIGH
		mock_object.assert_called_once_with(sr.PHOTO_PIN)
		self.assertTrue(sr.check_enough_light())

	@patch.object(GPIO, "input")
	def test_check_if_is_not_enough_light(self, mock_object: Mock):
		sr = SmartRoom()
		sr.check_enough_light()
		mock_object.return_value = GPIO.LOW
		mock_object.assert_called_once_with(sr.PHOTO_PIN)
		self.assertFalse(sr.check_enough_light())



	@patch.object(GPIO, "input")
	@patch.object(GPIO, "output")
	def test_manage_light_level(self, mock_output: Mock, mock_input: Mock):
		sr = SmartRoom()
		mock_input.side_effect = [GPIO.HIGH, GPIO.LOW]
		sr.manage_light_level()
		self.assertEqual(sr.light_on,True)

	@patch.object(PropertyMock, "adafruit_bmp280")
	def test_opening_window(self, mock_output: Mock):




