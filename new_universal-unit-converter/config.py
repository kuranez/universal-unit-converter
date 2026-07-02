"""Configuration values for the universal unit converter.

This file holds the `UNIT_TABLE` used by the natural-language parser in
`app.py`. The table groups a few common categories and defines canonical
unit names, conversion factors (to the category base unit) and aliases.
"""

UNIT_TABLE = {
	"length": [
		("meter", 1.0, ["meter", "meters", "metre", "metres", "m"]),
		("kilometer", 1000.0, ["kilometer", "kilometers", "kilometre", "kilometres", "km"]),
		("centimeter", 0.01, ["centimeter", "centimeters", "centimetre", "centimetres", "cm"]),
		("millimeter", 0.001, ["millimeter", "millimeters", "millimetre", "millimetres", "mm"]),
		("micrometer", 1e-6, ["micrometer", "micrometers", "micrometre", "micrometres", "um", "μm", "micron", "microns"]),
		("nanometer", 1e-9, ["nanometer", "nanometers", "nanometre", "nanometres", "nm"]),
		("inch", 0.0254, ["inch", "inches"]),
		("foot", 0.3048, ["foot", "feet", "ft"]),
		("yard", 0.9144, ["yard", "yards", "yd"]),
		("mile", 1609.344, ["mile", "miles", "mi"]),
	],
	"mass": [
		("gram", 1.0, ["gram", "grams", "g"]),
		("kilogram", 1000.0, ["kilogram", "kilograms", "kg"]),
		("milligram", 0.001, ["milligram", "milligrams", "mg"]),
		("microgram", 1e-6, ["microgram", "micrograms", "ug", "μg"]),
		("ounce", 28.349523125, ["ounce", "ounces", "oz"]),
		("pound", 453.59237, ["pound", "pounds", "lb", "lbs"]),
	],
	"volume": [
		("liter", 1.0, ["liter", "liters", "litre", "litres", "l"]),
		("milliliter", 0.001, ["milliliter", "milliliters", "millilitre", "millilitres", "ml"]),
		("centiliter", 0.01, ["centiliter", "centiliters", "centilitre", "centilitres", "cl"]),
		("deciliter", 0.1, ["deciliter", "deciliters", "decilitre", "decilitres", "dl"]),
		("cup", 0.2365882365, ["cup", "cups"]),
		("pint", 0.473176473, ["pint", "pints", "pt"]),
		("quart", 0.946352946, ["quart", "quarts", "qt"]),
		("gallon", 3.785411784, ["gallon", "gallons", "gal"]),
		("tablespoon", 0.01478676478125, ["tablespoon", "tablespoons", "tbsp"]),
		("teaspoon", 0.00492892159375, ["teaspoon", "teaspoons", "tsp"]),
		("fluid ounce", 0.0295735295625, ["fluid ounce", "fluid ounces", "fl oz"]),
	],
	"energy": [
		("joule", 1.0, ["joule", "joules", "j"]),
		("kilojoule", 1000.0, ["kilojoule", "kilojoules", "kj"]),
		("megajoule", 1000000.0, ["megajoule", "megajoules", "mj"]),
		("calorie", 4.184, ["calorie", "calories", "cal"]),
		("kilocalorie", 4184.0, ["kilocalorie", "kilocalories", "kcal"]),
		("watt hour", 3600.0, ["watt hour", "watt hours", "wh"]),
		("kilowatt hour", 3600000.0, ["kilowatt hour", "kilowatt hours", "kwh"]),
		("electronvolt", 1.602176634e-19, ["electronvolt", "electronvolts", "ev"]),
		("btu", 1055.05585262, ["btu", "british thermal unit", "british thermal units"]),
	],
    "time": [
        ("second", 1.0, ["second", "seconds", "s"]),
		("minute", 60.0, ["minute", "minutes", "min"]),
		("hour", 3600.0, ["hour", "hours", "h"]),
		("day", 86400.0, ["day", "days", "d"]),
		("week", 604800.0, ["week", "weeks", "wk"]),
		("month", 2629800.0, ["month", "months", "mo"]),  # Average month (30.44 days)
		("year", 31557600.0, ["year", "years", "yr"]),    # Average year (365.25 days)
	],
    "temperature": [
        ("celsius", 1.0, ["celsius", "degrees celsius", "°C"]),
        ("fahrenheit", 1.0, ["fahrenheit", "degrees fahrenheit", "°F"]),
        ("kelvin", 1.0, ["kelvin", "degrees kelvin", "K"]),
    ],
	"area": [
        ("square meter", 1.0, ["square meter", "square meters", "m²"]),
		("square kilometer", 1e6, ["square kilometer", "square kilometers", "km²"]),
		("square mile", 2.59e6, ["square mile", "square miles", "mi²"]),
		("acre", 4046.86, ["acre", "acres"]),
		("hectare", 10000.0, ["hectare", "hectares"]),
	],
}
