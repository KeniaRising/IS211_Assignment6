import unittest

from conversions import (
    convertCelsiusToKelvin,
    convertCelsiusToFahrenheit,
    convertFahrenheitToCelsius,
    convertFahrenheitToKelvin,
    convertKelvinToCelsius,
    convertKelvinToFahrenheit
)

from conversions_refactored import (
    convert,
    ConversionNotPossible
) 


class TestCelsiusConversions(unittest.TestCase):

    def test_celsius_to_kelvin(self):
        test_cases = [
            (0.0, 273.15),
            (100.0, 373.15),
            (-40.0, 233.15),
            (300.0, 573.15),
            (-273.15, 0.0)
        ]

        for celsius, expected in test_cases:
            print(f"Testing {celsius} C to Kelvin")
            with self.subTest(celsius=celsius):
                result = convertCelsiusToKelvin(celsius)
                self.assertAlmostEqual(result, expected, places=5)

    def test_celsius_to_fahrenheit(self):
        test_cases = [
            (0.0, 32.0),
            (100.0, 212.0),
            (-40.0, -40.0),
            (300.0, 572.0),
            (37.0, 98.6)
        ]

        for celsius, expected in test_cases:
            print(f"Testing {celsius} C to Fahrenheit")
            with self.subTest(celsius=celsius):
                result = convertCelsiusToFahrenheit(celsius)
                self.assertAlmostEqual(result, expected, places=5)

    def test_fahrenheit_to_celsius(self):
        cases = [
            (32.0, 0.0),
            (212.0, 100.0),
            (-40.0, -40.0),
            (98.6, 37.0),
            (572.0, 300.0)
        ]

        for value, expected in cases:
            print(f"Testing {value} F to Celsius")
            with self.subTest(value=value):
                self.assertAlmostEqual(
                    convertFahrenheitToCelsius(value), expected
                )

    def test_fahrenheit_to_kelvin(self):
        cases = [
            (32.0, 273.15),
            (212.0, 373.15),
            (-40.0, 233.15),
            (98.6, 310.15),
            (572.0, 573.15)
        ]

        for value, expected in cases:
            print(f"Testing {value} F to Kelvin")
            with self.subTest(value=value):
                self.assertAlmostEqual(
                    convertFahrenheitToKelvin(value), expected
                )

    def test_kelvin_to_celsius(self):
        cases = [
            (273.15, 0.0),
            (373.15, 100.0),
            (233.15, -40.0),
            (310.15, 37.0),
            (573.15, 300.0)
        ]

        for value, expected in cases:
            print(f"Testing {value} K to Celsius")
            with self.subTest(value=value):
                self.assertAlmostEqual(
                    convertKelvinToCelsius(value), expected
                )

    def test_kelvin_to_fahrenheit(self):
        cases = [
            (273.15, 32.0),
            (373.15, 212.0),
            (233.15, -40.0),
            (310.15, 98.6),
            (573.15, 572.0)
        ]

        for value, expected in cases:
            print(f"Testing {value} K to Fahrenheit")
            with self.subTest(value=value):
                self.assertAlmostEqual(
                    convertKelvinToFahrenheit(value), expected
                )

class TestRefactoredConversions(unittest.TestCase):
    def test_temperature_conversions(self):
        cases = [
            ("Celsius", "Kelvin", 0, 273.15),
            ("Celsius", "Fahrenheit", 100, 212),
            ("Fahrenheit", "Celsius", 32, 0),
            ("Fahrenheit", "Kelvin", 212, 373.15),
            ("Kelvin", "Celsius", 273.15, 0),
            ("Kelvin", "Fahrenheit", 373.15, 212)
        ]

        for source, target, value, expected in cases:
            print(f"Testing {source} to {target}")
            with self.subTest(source=source, target=target):
                self.assertAlmostEqual(
                    convert(source, target, value), expected
                )

    def test_distance_conversions(self):
        cases = [
            ("Miles", "Meters", 1, 1609.344),
            ("Meters", "Miles", 1609.344, 1),
            ("Yards", "Meters", 1, 0.9144),
            ("Meters", "Yards", 0.9144, 1),
            ("Miles", "Yards", 1, 1760),
            ("Yards", "Miles", 1760, 1)
        ]

        for source, target, value, expected in cases:
            print(f"Testing {source} to {target}")
            with self.subTest(source=source, target=target):
                self.assertAlmostEqual(
                    convert(source, target, value), expected
                )

    def test_same_unit(self):
        units = [
            "Celsius", "Fahrenheit", "Kelvin",
            "Miles", "Yards", "Meters"
        ]

        for unit in units:
            print(f"Testing {unit} to {unit}")
            with self.subTest(unit=unit):
                self.assertEqual(
                    convert(unit, unit, 25), 25.0
                )

    def test_incompatible_units(self):
        cases = [
            ("Celsius", "Meters"),
            ("Miles", "Kelvin"),
            ("Yards", "Fahrenheit"),
            ("Meters", "Celsius")
        ]

        for source, target in cases:
            print(f"Testing invalid conversion: {source} to {target}")
            with self.subTest(source=source, target=target):
                with self.assertRaises(ConversionNotPossible):
                    convert(source, target, 10)  

if __name__ == "__main__":
    unittest.main(verbosity=2) 