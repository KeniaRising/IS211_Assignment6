class ConversionNotPossible(Exception):
    pass


def convert(fromUnit, toUnit, value):
    temperature_units = {"Celsius", "Fahrenheit", "Kelvin"}
    distance_units = {"Miles", "Yards", "Meters"}

    if fromUnit == toUnit:
        if fromUnit in temperature_units | distance_units:
            return float(value)
        raise ConversionNotPossible("Unknown unit")

    if fromUnit in temperature_units and toUnit in temperature_units:
        if fromUnit == "Celsius":
            celsius = value
        elif fromUnit == "Fahrenheit":
            celsius = (value - 32) * 5 / 9
        else:
            celsius = value - 273.15

        if toUnit == "Celsius":
            return float(celsius)
        elif toUnit == "Fahrenheit":
            return float(celsius * 9 / 5 + 32)
        else:
            return float(celsius + 273.15)

    if fromUnit in distance_units and toUnit in distance_units:
        meters_per_unit = {
            "Miles": 1609.344,
            "Yards": 0.9144,
            "Meters": 1.0
        }

        meters = value * meters_per_unit[fromUnit]
        return float(meters / meters_per_unit[toUnit])

    raise ConversionNotPossible(
        f"Cannot convert {fromUnit} to {toUnit}"
    ) 

