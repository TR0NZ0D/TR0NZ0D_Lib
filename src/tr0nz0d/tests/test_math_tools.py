# -*- coding: utf-8 -*-

"""
The MIT License (MIT)

Copyright (c) 2015-2020 Rapptz

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.

Created by: Gabriel Menezes de Antonio (TR0NZ0D)
"""
import unittest

from tr0nz0d.tools.math_tools import (DatetimeTools, MathTools,
                                      UnitsOfMeasurement)


class TestMathTools(unittest.TestCase):
    """Test case for math tools"""
    tools = MathTools()
    # Length
    meter_unit = tools.build_unit(UnitsOfMeasurement.meter, 27.08)
    millimeter_unit = tools.build_unit(UnitsOfMeasurement.millimeter, 27.08)
    centimeter_unit = tools.build_unit(UnitsOfMeasurement.centimeter, 27.08)
    decimeter_unit = tools.build_unit(UnitsOfMeasurement.decimeter, 27.08)
    kilometer_unit = tools.build_unit(UnitsOfMeasurement.kilometer, 27.08)
    inch_unit = tools.build_unit(UnitsOfMeasurement.inch, 27.08)
    foot_unit = tools.build_unit(UnitsOfMeasurement.foot, 27.08)
    yard_unit = tools.build_unit(UnitsOfMeasurement.yard, 27.08)
    mile_unit = tools.build_unit(UnitsOfMeasurement.mile, 27.08)

    # Area
    square_meter_unit = tools.build_unit(
        UnitsOfMeasurement.square_meter, 27.08)
    square_inch_unit = tools.build_unit(UnitsOfMeasurement.square_inch, 27.08)
    square_feet_unit = tools.build_unit(UnitsOfMeasurement.square_feet, 27.08)
    square_yard_unit = tools.build_unit(UnitsOfMeasurement.square_yard, 27.08)
    square_mile_unit = tools.build_unit(UnitsOfMeasurement.square_mile, 27.08)

    # Volume
    cubic_meter_unit = tools.build_unit(UnitsOfMeasurement.cubic_meter, 27.08)
    cubic_inch_unit = tools.build_unit(UnitsOfMeasurement.cubic_inch, 27.08)
    cubic_foot_unit = tools.build_unit(UnitsOfMeasurement.cubic_foot, 27.08)
    cubic_yard_unit = tools.build_unit(UnitsOfMeasurement.cubic_yard, 27.08)
    liter_unit = tools.build_unit(UnitsOfMeasurement.liter, 27.08)
    milliliter_unit = tools.build_unit(UnitsOfMeasurement.milliliter, 27.08)
    centiliter_unit = tools.build_unit(UnitsOfMeasurement.centiliter, 27.08)
    deciliter_unit = tools.build_unit(UnitsOfMeasurement.deciliter, 27.08)
    hectoliter_unit = tools.build_unit(UnitsOfMeasurement.hectoliter, 27.08)
    gallon_unit = tools.build_unit(UnitsOfMeasurement.gallon, 27.08)

    # Time
    second_unit = tools.build_unit(UnitsOfMeasurement.second, 27.08)
    minute_unit = tools.build_unit(UnitsOfMeasurement.minute, 27.08)
    hour_unit = tools.build_unit(UnitsOfMeasurement.hour, 27.08)
    day_unit = tools.build_unit(UnitsOfMeasurement.day, 27.08)
    year_unit = tools.build_unit(UnitsOfMeasurement.year, 27.08)

    # Speed
    miles_per_hour_unit = tools.build_unit(
        UnitsOfMeasurement.miles_per_hour, 27.08)
    meters_per_second_unit = tools.build_unit(
        UnitsOfMeasurement.meters_per_second, 27.08)
    kilometer_per_hour_unit = tools.build_unit(
        UnitsOfMeasurement.kilometer_per_hour, 27.08)

    # Mass
    gram_unit = tools.build_unit(UnitsOfMeasurement.gram, 27.08)
    kilogram_unit = tools.build_unit(UnitsOfMeasurement.kilogram, 27.08)

    def test_meter_unit_conversion_to_millimeter(self):
        """Test conversion meter - millimiter"""
        result = self.tools.convert_measure_units(unit=self.meter_unit,
                                                  new_unit=UnitsOfMeasurement.millimeter)
        expected_conversion_result = 27080
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_meter_unit_conversion_to_centimeter(self):
        """Test conversion meter - centimiter"""
        result = self.tools.convert_measure_units(unit=self.meter_unit,
                                                  new_unit=UnitsOfMeasurement.centimeter)
        expected_conversion_result = 2708
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_meter_unit_conversion_to_decimeter(self):
        """Test conversion meter - decimeter"""
        result = self.tools.convert_measure_units(unit=self.meter_unit,
                                                  new_unit=UnitsOfMeasurement.decimeter)
        expected_conversion_result = 270.8
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_meter_unit_conversion_to_kilometer(self):
        """Test conversion meter - kilometer"""
        result = self.tools.convert_measure_units(unit=self.meter_unit,
                                                  new_unit=UnitsOfMeasurement.kilometer)
        expected_conversion_result = 0.02708
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_meter_unit_conversion_to_inch(self):
        """Test conversion meter - inch"""
        result = self.tools.convert_measure_units(unit=self.meter_unit,
                                                  new_unit=UnitsOfMeasurement.inch)
        expected_conversion_result = 1066.1417
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=2)

    def test_meter_unit_conversion_to_foot(self):
        """Test conversion meter - foot"""
        result = self.tools.convert_measure_units(unit=self.meter_unit,
                                                  new_unit=UnitsOfMeasurement.foot)
        expected_conversion_result = 88.845144
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=2)

    def test_meter_unit_conversion_to_yard(self):
        """Test conversion meter - yard"""
        result = self.tools.convert_measure_units(unit=self.meter_unit,
                                                  new_unit=UnitsOfMeasurement.yard)
        expected_conversion_result = 29.615048
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=1)

    def test_meter_unit_conversion_to_mile(self):
        """Test conversion meter - mile"""
        result = self.tools.convert_measure_units(unit=self.meter_unit,
                                                  new_unit=UnitsOfMeasurement.mile)
        expected_conversion_result = 0.016826732
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=4)

    def test_millimeter_unit_conversion_to_meter(self):
        """Test conversion millimiter - meter"""
        result = self.tools.convert_measure_units(unit=self.millimeter_unit,
                                                  new_unit=UnitsOfMeasurement.meter)
        expected_conversion_result = 0.02708
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_millimeter_unit_conversion_to_centimeter(self):
        """Test conversion millimiter - centimeter"""
        result = self.tools.convert_measure_units(unit=self.millimeter_unit,
                                                  new_unit=UnitsOfMeasurement.centimeter)
        expected_conversion_result = 2.708
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_millimeter_unit_conversion_to_decimeter(self):
        """Test conversion millimiter - decimeter"""
        result = self.tools.convert_measure_units(unit=self.millimeter_unit,
                                                  new_unit=UnitsOfMeasurement.decimeter)
        expected_conversion_result = 0.2708
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_millimeter_unit_conversion_to_kilometer(self):
        """Test conversion millimiter - kilometer"""
        result = self.tools.convert_measure_units(unit=self.millimeter_unit,
                                                  new_unit=UnitsOfMeasurement.kilometer)
        expected_conversion_result = 2.708e-5
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_millimeter_unit_conversion_to_inch(self):
        """Test conversion millimiter - inch"""
        result = self.tools.convert_measure_units(unit=self.millimeter_unit,
                                                  new_unit=UnitsOfMeasurement.inch)
        expected_conversion_result = 1.0661417
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_millimeter_unit_conversion_to_foot(self):
        """Test conversion millimiter - foot"""
        result = self.tools.convert_measure_units(unit=self.millimeter_unit,
                                                  new_unit=UnitsOfMeasurement.foot)
        expected_conversion_result = 0.088845144
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_millimeter_unit_conversion_to_yard(self):
        """Test conversion millimiter - yard"""
        result = self.tools.convert_measure_units(unit=self.millimeter_unit,
                                                  new_unit=UnitsOfMeasurement.yard)
        expected_conversion_result = 0.029615048
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_millimeter_unit_conversion_to_mile(self):
        """Test conversion millimiter - mile"""
        result = self.tools.convert_measure_units(unit=self.millimeter_unit,
                                                  new_unit=UnitsOfMeasurement.mile)
        expected_conversion_result = 1.682673e-5
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_centimeter_unit_conversion_to_meter(self):
        """Test conversion centimeter - meter"""
        result = self.tools.convert_measure_units(unit=self.centimeter_unit,
                                                  new_unit=UnitsOfMeasurement.meter)
        expected_conversion_result = 0.2708
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_centimeter_unit_conversion_to_millimeter(self):
        """Test conversion centimeter - millimeter"""
        result = self.tools.convert_measure_units(unit=self.centimeter_unit,
                                                  new_unit=UnitsOfMeasurement.millimeter)
        expected_conversion_result = 270.8
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_centimeter_unit_conversion_to_decimeter(self):
        """Test conversion centimeter - decimeter"""
        result = self.tools.convert_measure_units(unit=self.centimeter_unit,
                                                  new_unit=UnitsOfMeasurement.decimeter)
        expected_conversion_result = 2.708
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_centimeter_unit_conversion_to_kilometer(self):
        """Test conversion centimeter - kilometer"""
        result = self.tools.convert_measure_units(unit=self.centimeter_unit,
                                                  new_unit=UnitsOfMeasurement.kilometer)
        expected_conversion_result = 0.0002708
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_centimeter_unit_conversion_to_inch(self):
        """Test conversion centimeter - inch"""
        result = self.tools.convert_measure_units(unit=self.centimeter_unit,
                                                  new_unit=UnitsOfMeasurement.inch)
        expected_conversion_result = 10.661417
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=6)

    def test_centimeter_unit_conversion_to_foot(self):
        """Test conversion centimeter - foot"""
        result = self.tools.convert_measure_units(unit=self.centimeter_unit,
                                                  new_unit=UnitsOfMeasurement.foot)
        expected_conversion_result = 0.88845144
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_centimeter_unit_conversion_to_yard(self):
        """Test conversion centimeter - yard"""
        result = self.tools.convert_measure_units(unit=self.centimeter_unit,
                                                  new_unit=UnitsOfMeasurement.yard)
        expected_conversion_result = 0.29615048
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_centimeter_unit_conversion_to_mile(self):
        """Test conversion centimeter - mile"""
        result = self.tools.convert_measure_units(unit=self.centimeter_unit,
                                                  new_unit=UnitsOfMeasurement.mile)
        expected_conversion_result = 0.00016826732
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_decimeter_unit_conversion_to_meter(self):
        """Test conversion decimeter - meter"""
        result = self.tools.convert_measure_units(unit=self.decimeter_unit,
                                                  new_unit=UnitsOfMeasurement.meter)
        expected_conversion_result = 2.708
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_decimeter_unit_conversion_to_millimeter(self):
        """Test conversion decimeter - millimeter"""
        result = self.tools.convert_measure_units(unit=self.decimeter_unit,
                                                  new_unit=UnitsOfMeasurement.millimeter)
        expected_conversion_result = 2708
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_decimeter_unit_conversion_to_centimeter(self):
        """Test conversion decimeter - centimeter"""
        result = self.tools.convert_measure_units(unit=self.decimeter_unit,
                                                  new_unit=UnitsOfMeasurement.centimeter)
        expected_conversion_result = 270.8
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_decimeter_unit_conversion_to_kilometer(self):
        """Test conversion decimeter - kilometer"""
        result = self.tools.convert_measure_units(unit=self.decimeter_unit,
                                                  new_unit=UnitsOfMeasurement.kilometer)
        expected_conversion_result = 0.002708
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_decimeter_unit_conversion_to_inch(self):
        """Test conversion decimeter - inch"""
        result = self.tools.convert_measure_units(unit=self.decimeter_unit,
                                                  new_unit=UnitsOfMeasurement.inch)
        expected_conversion_result = 106.61417
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_decimeter_unit_conversion_to_foot(self):
        """Test conversion decimeter - foot"""
        result = self.tools.convert_measure_units(unit=self.decimeter_unit,
                                                  new_unit=UnitsOfMeasurement.foot)
        expected_conversion_result = 8.8845144
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_decimeter_unit_conversion_to_yard(self):
        """Test conversion decimeter - yard"""
        result = self.tools.convert_measure_units(unit=self.decimeter_unit,
                                                  new_unit=UnitsOfMeasurement.yard)
        expected_conversion_result = 2.9615048
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_decimeter_unit_conversion_to_mile(self):
        """Test conversion decimeter - mile"""
        result = self.tools.convert_measure_units(unit=self.decimeter_unit,
                                                  new_unit=UnitsOfMeasurement.mile)
        expected_conversion_result = 0.0016826732
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=5)

    def test_kilometer_unit_conversion_to_meter(self):
        """Test conversion kilometer - meter"""
        result = self.tools.convert_measure_units(unit=self.kilometer_unit,
                                                  new_unit=UnitsOfMeasurement.meter)
        expected_conversion_result = 27080
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_kilometer_unit_conversion_to_millimeter(self):
        """Test conversion kilometer - millimeter"""
        result = self.tools.convert_measure_units(unit=self.kilometer_unit,
                                                  new_unit=UnitsOfMeasurement.millimeter)
        expected_conversion_result = 27080000
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_kilometer_unit_conversion_to_centimeter(self):
        """Test conversion kilometer - centimeter"""
        result = self.tools.convert_measure_units(unit=self.kilometer_unit,
                                                  new_unit=UnitsOfMeasurement.centimeter)
        expected_conversion_result = 2708000
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_kilometer_unit_conversion_to_decimeter(self):
        """Test conversion kilometer - decimeter"""
        result = self.tools.convert_measure_units(unit=self.kilometer_unit,
                                                  new_unit=UnitsOfMeasurement.decimeter)
        expected_conversion_result = 270800
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_kilometer_unit_conversion_to_inch(self):
        """Test conversion kilometer - inch"""
        result = self.tools.convert_measure_units(unit=self.kilometer_unit,
                                                  new_unit=UnitsOfMeasurement.inch)
        expected_conversion_result = 1066139.5999999999
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_kilometer_unit_conversion_to_foot(self):
        """Test conversion kilometer - foot"""
        result = self.tools.convert_measure_units(unit=self.kilometer_unit,
                                                  new_unit=UnitsOfMeasurement.foot)
        expected_conversion_result = 88849.48
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=2)

    def test_kilometer_unit_conversion_to_yard(self):
        """Test conversion kilometer - yard"""
        result = self.tools.convert_measure_units(unit=self.kilometer_unit,
                                                  new_unit=UnitsOfMeasurement.yard)
        expected_conversion_result = 29625.519999999997
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_kilometer_unit_conversion_to_mile(self):
        """Test conversion kilometer - mile"""
        result = self.tools.convert_measure_units(unit=self.kilometer_unit,
                                                  new_unit=UnitsOfMeasurement.mile)
        expected_conversion_result = 16.826732
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=2)

    def test_inch_unit_conversion_to_meter(self):
        """Test conversion inch - meter"""
        result = self.tools.convert_measure_units(unit=self.inch_unit,
                                                  new_unit=UnitsOfMeasurement.meter)
        expected_conversion_result = 0.687832
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=5)

    def test_inch_unit_conversion_to_millimeter(self):
        """Test conversion inch - millimeter"""
        result = self.tools.convert_measure_units(unit=self.inch_unit,
                                                  new_unit=UnitsOfMeasurement.millimeter)
        expected_conversion_result = 687.832
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_inch_unit_conversion_to_centimeter(self):
        """Test conversion inch - centimeter"""
        result = self.tools.convert_measure_units(unit=self.inch_unit,
                                                  new_unit=UnitsOfMeasurement.centimeter)
        expected_conversion_result = 68.7832
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_inch_unit_conversion_to_decimeter(self):
        """Test conversion inch - decimeter"""
        result = self.tools.convert_measure_units(unit=self.inch_unit,
                                                  new_unit=UnitsOfMeasurement.decimeter)
        expected_conversion_result = 6.87832
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=4)

    def test_inch_unit_conversion_to_kilometer(self):
        """Test conversion inch - kilometer"""
        result = self.tools.convert_measure_units(unit=self.inch_unit,
                                                  new_unit=UnitsOfMeasurement.kilometer)
        expected_conversion_result = 0.000687832
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_inch_unit_conversion_to_foot(self):
        """Test conversion inch - foot"""
        result = self.tools.convert_measure_units(unit=self.inch_unit,
                                                  new_unit=UnitsOfMeasurement.foot)
        expected_conversion_result = 2.2566667
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_inch_unit_conversion_to_yard(self):
        """Test conversion inch - yard"""
        result = self.tools.convert_measure_units(unit=self.inch_unit,
                                                  new_unit=UnitsOfMeasurement.yard)
        expected_conversion_result = 0.75222222
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_inch_unit_conversion_to_mile(self):
        """Test conversion inch - mile"""
        result = self.tools.convert_measure_units(unit=self.inch_unit,
                                                  new_unit=UnitsOfMeasurement.mile)
        expected_conversion_result = 0.0004273989898989899
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_foot_unit_conversion_to_meter(self):
        """Test conversion foot - meter"""
        result = self.tools.convert_measure_units(unit=self.foot_unit,
                                                  new_unit=UnitsOfMeasurement.meter)
        expected_conversion_result = 8.253984
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_foot_unit_conversion_to_millimeter(self):
        """Test conversion foot - millimeter"""
        result = self.tools.convert_measure_units(unit=self.foot_unit,
                                                  new_unit=UnitsOfMeasurement.millimeter)
        expected_conversion_result = 8253.984
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_foot_unit_conversion_to_centimeter(self):
        """Test conversion foot - centimeter"""
        result = self.tools.convert_measure_units(unit=self.foot_unit,
                                                  new_unit=UnitsOfMeasurement.centimeter)
        expected_conversion_result = 825.3984
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_foot_unit_conversion_to_decimeter(self):
        """Test conversion foot - decimeter"""
        result = self.tools.convert_measure_units(unit=self.foot_unit,
                                                  new_unit=UnitsOfMeasurement.decimeter)
        expected_conversion_result = 82.53984
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_foot_unit_conversion_to_kilometer(self):
        """Test conversion foot - kilometer"""
        result = self.tools.convert_measure_units(unit=self.foot_unit,
                                                  new_unit=UnitsOfMeasurement.kilometer)
        expected_conversion_result = 0.008253984
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=4)

    def test_foot_unit_conversion_to_inch(self):
        """Test conversion foot - inch"""
        result = self.tools.convert_measure_units(unit=self.foot_unit,
                                                  new_unit=UnitsOfMeasurement.inch)
        expected_conversion_result = 324.96
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_foot_unit_conversion_to_yard(self):
        """Test conversion foot - yard"""
        result = self.tools.convert_measure_units(unit=self.foot_unit,
                                                  new_unit=UnitsOfMeasurement.yard)
        expected_conversion_result = 9.0266667
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_foot_unit_conversion_to_mile(self):
        """Test conversion foot - mile"""
        result = self.tools.convert_measure_units(unit=self.foot_unit,
                                                  new_unit=UnitsOfMeasurement.mile)
        expected_conversion_result = 0.0051287879
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_yard_unit_conversion_to_meter(self):
        """Test conversion yard - meter"""
        result = self.tools.convert_measure_units(unit=self.yard_unit,
                                                  new_unit=UnitsOfMeasurement.meter)
        expected_conversion_result = 24.761952
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=1)

    def test_yard_unit_conversion_to_millimeter(self):
        """Test conversion yard - millimeter"""
        result = self.tools.convert_measure_units(unit=self.yard_unit,
                                                  new_unit=UnitsOfMeasurement.millimeter)
        expected_conversion_result = 24761.952
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_yard_unit_conversion_to_centimeter(self):
        """Test conversion yard - centimeter"""
        result = self.tools.convert_measure_units(unit=self.yard_unit,
                                                  new_unit=UnitsOfMeasurement.centimeter)
        expected_conversion_result = 2476.1952
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_yard_unit_conversion_to_decimeter(self):
        """Test conversion yard - decimeter"""
        result = self.tools.convert_measure_units(unit=self.yard_unit,
                                                  new_unit=UnitsOfMeasurement.decimeter)
        expected_conversion_result = 247.61952
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_yard_unit_conversion_to_kilometer(self):
        """Test conversion yard - kilometer"""
        result = self.tools.convert_measure_units(unit=self.yard_unit,
                                                  new_unit=UnitsOfMeasurement.kilometer)
        expected_conversion_result = 0.024761952
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=4)

    def test_yard_unit_conversion_to_inch(self):
        """Test conversion yard - inch"""
        result = self.tools.convert_measure_units(unit=self.yard_unit,
                                                  new_unit=UnitsOfMeasurement.inch)
        expected_conversion_result = 974.88
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_yard_unit_conversion_to_foot(self):
        """Test conversion yard - foot"""
        result = self.tools.convert_measure_units(unit=self.yard_unit,
                                                  new_unit=UnitsOfMeasurement.foot)
        expected_conversion_result = 81.24
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_yard_unit_conversion_to_mile(self):
        """Test conversion yard - mile"""
        result = self.tools.convert_measure_units(unit=self.yard_unit,
                                                  new_unit=UnitsOfMeasurement.mile)
        expected_conversion_result = 0.015386364
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_mile_unit_conversion_to_meter(self):
        """Test conversion mile - meter"""
        result = self.tools.convert_measure_units(unit=self.mile_unit,
                                                  new_unit=UnitsOfMeasurement.meter)
        expected_conversion_result = 43571.719999999994
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_mile_unit_conversion_to_millimeter(self):
        """Test conversion mile - millimeter"""
        result = self.tools.convert_measure_units(unit=self.mile_unit,
                                                  new_unit=UnitsOfMeasurement.millimeter)
        expected_conversion_result = 43571720.0
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_mile_unit_conversion_to_centimeter(self):
        """Test conversion mile - centimeter"""
        result = self.tools.convert_measure_units(unit=self.mile_unit,
                                                  new_unit=UnitsOfMeasurement.centimeter)
        expected_conversion_result = 4357172.0
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_mile_unit_conversion_to_decimeter(self):
        """Test conversion mile - decimeter"""
        result = self.tools.convert_measure_units(unit=self.mile_unit,
                                                  new_unit=UnitsOfMeasurement.decimeter)
        expected_conversion_result = 435717.19999999995
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_mile_unit_conversion_to_kilometer(self):
        """Test conversion mile - kilometer"""
        result = self.tools.convert_measure_units(unit=self.mile_unit,
                                                  new_unit=UnitsOfMeasurement.kilometer)
        expected_conversion_result = 43.581036
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=1)

    def test_mile_unit_conversion_to_inch(self):
        """Test conversion mile - inch"""
        result = self.tools.convert_measure_units(unit=self.mile_unit,
                                                  new_unit=UnitsOfMeasurement.inch)
        expected_conversion_result = 1715788.8
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_mile_unit_conversion_to_foot(self):
        """Test conversion mile - foot"""
        result = self.tools.convert_measure_units(unit=self.mile_unit,
                                                  new_unit=UnitsOfMeasurement.foot)
        expected_conversion_result = 142982.4
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_mile_unit_conversion_to_yard(self):
        """Test conversion mile - yard"""
        result = self.tools.convert_measure_units(unit=self.mile_unit,
                                                  new_unit=UnitsOfMeasurement.yard)
        expected_conversion_result = 47660.8
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_square_meter_unit_conversion_to_square_inch(self):
        """Test conversion square meter - square inch"""
        result = self.tools.convert_measure_units(unit=self.square_meter_unit,
                                                  new_unit=UnitsOfMeasurement.square_inch)
        expected_conversion_result = 41974.0
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_square_meter_unit_conversion_to_square_feet(self):
        """Test conversion square meter - square feet"""
        result = self.tools.convert_measure_units(unit=self.square_meter_unit,
                                                  new_unit=UnitsOfMeasurement.square_feet)
        expected_conversion_result = 291.48669
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=2)

    def test_square_meter_unit_conversion_to_square_yard(self):
        """Test conversion square meter - square yard"""
        result = self.tools.convert_measure_units(unit=self.square_meter_unit,
                                                  new_unit=UnitsOfMeasurement.square_yard)
        expected_conversion_result = 32.38741
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_square_meter_unit_conversion_to_square_mile(self):
        """Test conversion square meter - square mile"""
        result = self.tools.convert_measure_units(unit=self.square_meter_unit,
                                                  new_unit=UnitsOfMeasurement.square_mile)
        expected_conversion_result = 1.045565e-5
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_square_inch_unit_conversion_to_square_meter(self):
        """Test conversion square inch - square meter"""
        result = self.tools.convert_measure_units(unit=self.square_inch_unit,
                                                  new_unit=UnitsOfMeasurement.square_meter)
        expected_conversion_result = 0.017470933
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_square_inch_unit_conversion_to_square_feet(self):
        """Test conversion square inch - square feet"""
        result = self.tools.convert_measure_units(unit=self.square_inch_unit,
                                                  new_unit=UnitsOfMeasurement.square_feet)
        expected_conversion_result = 0.18805556
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_square_inch_unit_conversion_to_square_yard(self):
        """Test conversion square inch - square yard"""
        result = self.tools.convert_measure_units(unit=self.square_inch_unit,
                                                  new_unit=UnitsOfMeasurement.square_yard)
        expected_conversion_result = 0.020895062
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_square_inch_unit_conversion_to_square_mile(self):
        """Test conversion square inch - square mile"""
        result = self.tools.convert_measure_units(unit=self.square_inch_unit,
                                                  new_unit=UnitsOfMeasurement.square_mile)
        expected_conversion_result = 6.745565e-9
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_square_feet_unit_conversion_to_square_meter(self):
        """Test conversion square feet - square meter"""
        result = self.tools.convert_measure_units(unit=self.square_feet_unit,
                                                  new_unit=UnitsOfMeasurement.square_meter)
        expected_conversion_result = 2.5158143
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_square_feet_unit_conversion_to_square_inch(self):
        """Test conversion square feet - square inch"""
        result = self.tools.convert_measure_units(unit=self.square_feet_unit,
                                                  new_unit=UnitsOfMeasurement.square_inch)
        expected_conversion_result = 3899.52
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_square_feet_unit_conversion_to_square_yard(self):
        """Test conversion square feet - square yard"""
        result = self.tools.convert_measure_units(unit=self.square_feet_unit,
                                                  new_unit=UnitsOfMeasurement.square_yard)
        expected_conversion_result = 3.0088889
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_square_feet_unit_conversion_to_square_mile(self):
        """Test conversion square feet - square mile"""
        result = self.tools.convert_measure_units(unit=self.square_feet_unit,
                                                  new_unit=UnitsOfMeasurement.square_mile)
        expected_conversion_result = 9.713613e-7
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_square_yard_unit_conversion_to_square_meter(self):
        """Test conversion square yard - square meter"""
        result = self.tools.convert_measure_units(unit=self.square_yard_unit,
                                                  new_unit=UnitsOfMeasurement.square_meter)
        expected_conversion_result = 22.642329
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_square_yard_unit_conversion_to_square_inch(self):
        """Test conversion square yard - square inch"""
        result = self.tools.convert_measure_units(unit=self.square_yard_unit,
                                                  new_unit=UnitsOfMeasurement.square_inch)
        expected_conversion_result = 35095.68
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_square_yard_unit_conversion_to_square_feet(self):
        """Test conversion square yard - square feet"""
        result = self.tools.convert_measure_units(unit=self.square_yard_unit,
                                                  new_unit=UnitsOfMeasurement.square_feet)
        expected_conversion_result = 243.72
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_square_yard_unit_conversion_to_square_mile(self):
        """Test conversion square yard - square mile"""
        result = self.tools.convert_measure_units(unit=self.square_yard_unit,
                                                  new_unit=UnitsOfMeasurement.square_mile)
        expected_conversion_result = 8.742252e-6
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_square_mile_unit_conversion_to_square_meter(self):
        """Test conversion square mile - square meter"""
        result = self.tools.convert_measure_units(unit=self.square_mile_unit,
                                                  new_unit=UnitsOfMeasurement.square_meter)
        expected_conversion_result = 70137200.0
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_square_mile_unit_conversion_to_square_inch(self):
        """Test conversion square mile - square inch"""
        result = self.tools.convert_measure_units(unit=self.square_mile_unit,
                                                  new_unit=UnitsOfMeasurement.square_inch)
        expected_conversion_result = 108699120000.0
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_square_mile_unit_conversion_to_square_feet(self):
        """Test conversion square mile - square feet"""
        result = self.tools.convert_measure_units(unit=self.square_mile_unit,
                                                  new_unit=UnitsOfMeasurement.square_feet)
        expected_conversion_result = 754990400.0
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_square_mile_unit_conversion_to_square_yard(self):
        """Test conversion square mile - square yard"""
        result = self.tools.convert_measure_units(unit=self.square_mile_unit,
                                                  new_unit=UnitsOfMeasurement.square_yard)
        expected_conversion_result = 83893840.0
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_cubic_meter_unit_conversion_to_cubic_inch(self):
        """Test conversion cubic meter - cubic inch"""
        result = self.tools.convert_measure_units(unit=self.cubic_meter_unit,
                                                  new_unit=UnitsOfMeasurement.cubic_inch)
        expected_conversion_result = 1652421.5999999999
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_cubic_meter_unit_conversion_to_cubic_foot(self):
        """Test conversion cubic meter - cubic foot"""
        result = self.tools.convert_measure_units(unit=self.cubic_meter_unit,
                                                  new_unit=UnitsOfMeasurement.cubic_foot)
        expected_conversion_result = 956.32117
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=1)

    def test_cubic_meter_unit_conversion_to_cubic_yard(self):
        """Test conversion cubic meter - cubic yard"""
        result = self.tools.convert_measure_units(unit=self.cubic_meter_unit,
                                                  new_unit=UnitsOfMeasurement.cubic_yard)
        expected_conversion_result = 35.419303
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=1)

    def test_cubic_meter_unit_conversion_to_liter(self):
        """Test conversion cubic meter - liter"""
        result = self.tools.convert_measure_units(unit=self.cubic_meter_unit,
                                                  new_unit=UnitsOfMeasurement.liter)
        expected_conversion_result = 27080
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_cubic_meter_unit_conversion_to_milliliter(self):
        """Test conversion cubic meter - milliliter"""
        result = self.tools.convert_measure_units(unit=self.cubic_meter_unit,
                                                  new_unit=UnitsOfMeasurement.milliliter)
        expected_conversion_result = 27080000
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_cubic_meter_unit_conversion_to_centiliter(self):
        """Test conversion cubic meter - centiliter"""
        result = self.tools.convert_measure_units(unit=self.cubic_meter_unit,
                                                  new_unit=UnitsOfMeasurement.centiliter)
        expected_conversion_result = 2708000
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_cubic_meter_unit_conversion_to_deciliter(self):
        """Test conversion cubic meter - deciliter"""
        result = self.tools.convert_measure_units(unit=self.cubic_meter_unit,
                                                  new_unit=UnitsOfMeasurement.deciliter)
        expected_conversion_result = 270800
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_cubic_meter_unit_conversion_to_hectoliter(self):
        """Test conversion cubic meter - hectoliter"""
        result = self.tools.convert_measure_units(unit=self.cubic_meter_unit,
                                                  new_unit=UnitsOfMeasurement.hectoliter)
        expected_conversion_result = 270.8
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_cubic_meter_unit_conversion_to_gallon(self):
        """Test conversion cubic meter - gallon"""
        result = self.tools.convert_measure_units(unit=self.cubic_meter_unit,
                                                  new_unit=UnitsOfMeasurement.gallon)
        expected_conversion_result = 7154.535999999999
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_cubic_inch_unit_conversion_to_cubic_meter(self):
        """Test conversion cubic inch - cubic meter"""
        result = self.tools.convert_measure_units(unit=self.cubic_inch_unit,
                                                  new_unit=UnitsOfMeasurement.cubic_meter)
        expected_conversion_result = 0.00044376169
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_cubic_inch_unit_conversion_to_cubic_foot(self):
        """Test conversion cubic inch - cubic foot"""
        result = self.tools.convert_measure_units(unit=self.cubic_inch_unit,
                                                  new_unit=UnitsOfMeasurement.cubic_foot)
        expected_conversion_result = 0.015671296
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_cubic_inch_unit_conversion_to_cubic_yard(self):
        """Test conversion cubic inch - cubic yard"""
        result = self.tools.convert_measure_units(unit=self.cubic_inch_unit,
                                                  new_unit=UnitsOfMeasurement.cubic_yard)
        expected_conversion_result = 0.00058041838
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_cubic_inch_unit_conversion_to_liter(self):
        """Test conversion cubic inch - liter"""
        result = self.tools.convert_measure_units(unit=self.cubic_inch_unit,
                                                  new_unit=UnitsOfMeasurement.liter)
        expected_conversion_result = 0.44376169
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=4)

    def test_cubic_inch_unit_conversion_to_milliliter(self):
        """Test conversion cubic inch - milliliter"""
        result = self.tools.convert_measure_units(unit=self.cubic_inch_unit,
                                                  new_unit=UnitsOfMeasurement.milliliter)
        expected_conversion_result = 443.76169
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=1)

    def test_cubic_inch_unit_conversion_to_centiliter(self):
        """Test conversion cubic inch - centiliter"""
        result = self.tools.convert_measure_units(unit=self.cubic_inch_unit,
                                                  new_unit=UnitsOfMeasurement.centiliter)
        expected_conversion_result = 44.376169
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=1)

    def test_cubic_inch_unit_conversion_to_deciliter(self):
        """Test conversion cubic inch - deciliter"""
        result = self.tools.convert_measure_units(unit=self.cubic_inch_unit,
                                                  new_unit=UnitsOfMeasurement.deciliter)
        expected_conversion_result = 4.4376169
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_cubic_inch_unit_conversion_to_hectoliter(self):
        """Test conversion cubic inch - hectoliter"""
        result = self.tools.convert_measure_units(unit=self.cubic_inch_unit,
                                                  new_unit=UnitsOfMeasurement.hectoliter)
        expected_conversion_result = 0.0044376169
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=6)

    def test_cubic_inch_unit_conversion_to_gallon(self):
        """Test conversion cubic inch - gallon"""
        result = self.tools.convert_measure_units(unit=self.cubic_inch_unit,
                                                  new_unit=UnitsOfMeasurement.gallon)
        expected_conversion_result = 0.11722944
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_cubic_foot_unit_conversion_to_cubic_meter(self):
        """Test conversion cubic foot - cubic meter"""
        result = self.tools.convert_measure_units(unit=self.cubic_foot_unit,
                                                  new_unit=UnitsOfMeasurement.cubic_meter)
        expected_conversion_result = 0.76682021
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=4)

    def test_cubic_foot_unit_conversion_to_cubic_inch(self):
        """Test conversion cubic foot - cubic inch"""
        result = self.tools.convert_measure_units(unit=self.cubic_foot_unit,
                                                  new_unit=UnitsOfMeasurement.cubic_inch)
        expected_conversion_result = 46794.24
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_cubic_foot_unit_conversion_to_cubic_yard(self):
        """Test conversion cubic foot - cubic yard"""
        result = self.tools.convert_measure_units(unit=self.cubic_foot_unit,
                                                  new_unit=UnitsOfMeasurement.cubic_yard)
        expected_conversion_result = 1.002963
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_cubic_foot_unit_conversion_to_liter(self):
        """Test conversion cubic foot - liter"""
        result = self.tools.convert_measure_units(unit=self.cubic_foot_unit,
                                                  new_unit=UnitsOfMeasurement.liter)
        expected_conversion_result = 766.82021
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=2)

    def test_cubic_foot_unit_conversion_to_milliliter(self):
        """Test conversion cubic foot - milliliter"""
        result = self.tools.convert_measure_units(unit=self.cubic_foot_unit,
                                                  new_unit=UnitsOfMeasurement.milliliter)
        expected_conversion_result = 766905.6
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_cubic_foot_unit_conversion_to_centiliter(self):
        """Test conversion cubic foot - centiliter"""
        result = self.tools.convert_measure_units(unit=self.cubic_foot_unit,
                                                  new_unit=UnitsOfMeasurement.centiliter)
        expected_conversion_result = 76690.56
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_cubic_foot_unit_conversion_to_deciliter(self):
        """Test conversion cubic foot - deciliter"""
        result = self.tools.convert_measure_units(unit=self.cubic_foot_unit,
                                                  new_unit=UnitsOfMeasurement.deciliter)
        expected_conversion_result = 7669.056
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_cubic_foot_unit_conversion_to_hectoliter(self):
        """Test conversion cubic foot - hectoliter"""
        result = self.tools.convert_measure_units(unit=self.cubic_foot_unit,
                                                  new_unit=UnitsOfMeasurement.hectoliter)
        expected_conversion_result = 7.6682021
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=2)

    def test_cubic_foot_unit_conversion_to_gallon(self):
        """Test conversion cubic foot - gallon"""
        result = self.tools.convert_measure_units(unit=self.cubic_foot_unit,
                                                  new_unit=UnitsOfMeasurement.gallon)
        expected_conversion_result = 202.57247
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=1)

    def test_cubic_yard_unit_conversion_to_cubic_meter(self):
        """Test conversion cubic yard - cubic meter"""
        result = self.tools.convert_measure_units(unit=self.cubic_yard_unit,
                                                  new_unit=UnitsOfMeasurement.cubic_meter)
        expected_conversion_result = 20.704146
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=2)

    def test_cubic_yard_unit_conversion_to_cubic_inch(self):
        """Test conversion cubic yard - cubic inch"""
        result = self.tools.convert_measure_units(unit=self.cubic_yard_unit,
                                                  new_unit=UnitsOfMeasurement.cubic_inch)
        expected_conversion_result = 1263552.7999999998
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_cubic_yard_unit_conversion_to_cubic_foot(self):
        """Test conversion cubic yard - cubic foot"""
        result = self.tools.convert_measure_units(unit=self.cubic_yard_unit,
                                                  new_unit=UnitsOfMeasurement.cubic_foot)
        expected_conversion_result = 731.16
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_cubic_yard_unit_conversion_to_liter(self):
        """Test conversion cubic yard - liter"""
        result = self.tools.convert_measure_units(unit=self.cubic_yard_unit,
                                                  new_unit=UnitsOfMeasurement.liter)
        expected_conversion_result = 20705.368
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_cubic_yard_unit_conversion_to_milliliter(self):
        """Test conversion cubic yard - milliliter"""
        result = self.tools.convert_measure_units(unit=self.cubic_yard_unit,
                                                  new_unit=UnitsOfMeasurement.milliliter)
        expected_conversion_result = 20705368.0
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_cubic_yard_unit_conversion_to_centiliter(self):
        """Test conversion cubic yard - centiliter"""
        result = self.tools.convert_measure_units(unit=self.cubic_yard_unit,
                                                  new_unit=UnitsOfMeasurement.centiliter)
        expected_conversion_result = 2070536.7999999998
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_cubic_yard_unit_conversion_to_deciliter(self):
        """Test conversion cubic yard - deciliter"""
        result = self.tools.convert_measure_units(unit=self.cubic_yard_unit,
                                                  new_unit=UnitsOfMeasurement.deciliter)
        expected_conversion_result = 207053.68
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_cubic_yard_unit_conversion_to_hectoliter(self):
        """Test conversion cubic yard - hectoliter"""
        result = self.tools.convert_measure_units(unit=self.cubic_yard_unit,
                                                  new_unit=UnitsOfMeasurement.hectoliter)
        expected_conversion_result = 207.04146
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=1)

    def test_cubic_yard_unit_conversion_to_gallon(self):
        """Test conversion cubic yard - gallon"""
        result = self.tools.convert_measure_units(unit=self.cubic_yard_unit,
                                                  new_unit=UnitsOfMeasurement.gallon)
        expected_conversion_result = 5470.16
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_liter_unit_conversion_to_cubic_meter(self):
        """Test conversion liter - cubic meter"""
        result = self.tools.convert_measure_units(unit=self.liter_unit,
                                                  new_unit=UnitsOfMeasurement.cubic_meter)
        expected_conversion_result = 0.02708
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_liter_unit_conversion_to_cubic_inch(self):
        """Test conversion liter - cubic inch"""
        result = self.tools.convert_measure_units(unit=self.liter_unit,
                                                  new_unit=UnitsOfMeasurement.cubic_inch)
        expected_conversion_result = 1652.523
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=1)

    def test_liter_unit_conversion_to_cubic_foot(self):
        """Test conversion liter - cubic foot"""
        result = self.tools.convert_measure_units(unit=self.liter_unit,
                                                  new_unit=UnitsOfMeasurement.cubic_foot)
        expected_conversion_result = 0.95632117
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=4)

    def test_liter_unit_conversion_to_cubic_yard(self):
        """Test conversion liter - cubic yard"""
        result = self.tools.convert_measure_units(unit=self.liter_unit,
                                                  new_unit=UnitsOfMeasurement.cubic_yard)
        expected_conversion_result = 0.035419303
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=4)

    def test_liter_unit_conversion_to_milliliter(self):
        """Test conversion liter - milliliter"""
        result = self.tools.convert_measure_units(unit=self.liter_unit,
                                                  new_unit=UnitsOfMeasurement.milliliter)
        expected_conversion_result = 27080
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_liter_unit_conversion_to_centiliter(self):
        """Test conversion liter - centiliter"""
        result = self.tools.convert_measure_units(unit=self.liter_unit,
                                                  new_unit=UnitsOfMeasurement.centiliter)
        expected_conversion_result = 2708
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_liter_unit_conversion_to_deciliter(self):
        """Test conversion liter - deciliter"""
        result = self.tools.convert_measure_units(unit=self.liter_unit,
                                                  new_unit=UnitsOfMeasurement.deciliter)
        expected_conversion_result = 270.8
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_liter_unit_conversion_to_hectoliter(self):
        """Test conversion liter - hectoliter"""
        result = self.tools.convert_measure_units(unit=self.liter_unit,
                                                  new_unit=UnitsOfMeasurement.hectoliter)
        expected_conversion_result = 0.2708
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_liter_unit_conversion_to_gallon(self):
        """Test conversion liter - gallon"""
        result = self.tools.convert_measure_units(unit=self.liter_unit,
                                                  new_unit=UnitsOfMeasurement.gallon)
        expected_conversion_result = 7.1537792
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=2)

    def test_milliliter_unit_conversion_to_cubic_meter(self):
        """Test conversion milliliter - cubic meter"""
        result = self.tools.convert_measure_units(unit=self.milliliter_unit,
                                                  new_unit=UnitsOfMeasurement.cubic_meter)
        expected_conversion_result = 2.708e-5
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_milliliter_unit_conversion_to_cubic_inch(self):
        """Test conversion milliliter - cubic inch"""
        result = self.tools.convert_measure_units(unit=self.milliliter_unit,
                                                  new_unit=UnitsOfMeasurement.cubic_inch)
        expected_conversion_result = 1.65252
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=4)

    def test_milliliter_unit_conversion_to_cubic_foot(self):
        """Test conversion milliliter - cubic foot"""
        result = self.tools.convert_measure_units(unit=self.milliliter_unit,
                                                  new_unit=UnitsOfMeasurement.cubic_foot)
        expected_conversion_result = 0.00095632117
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=6)

    def test_milliliter_unit_conversion_to_cubic_yard(self):
        """Test conversion milliliter - cubic yard"""
        result = self.tools.convert_measure_units(unit=self.milliliter_unit,
                                                  new_unit=UnitsOfMeasurement.cubic_yard)
        expected_conversion_result = 3.54193e-5
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_milliliter_unit_conversion_to_liter(self):
        """Test conversion milliliter - liter"""
        result = self.tools.convert_measure_units(unit=self.milliliter_unit,
                                                  new_unit=UnitsOfMeasurement.liter)
        expected_conversion_result = 0.02708
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_milliliter_unit_conversion_to_centiliter(self):
        """Test conversion milliliter - centiliter"""
        result = self.tools.convert_measure_units(unit=self.milliliter_unit,
                                                  new_unit=UnitsOfMeasurement.centiliter)
        expected_conversion_result = 2.708
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_milliliter_unit_conversion_to_deciliter(self):
        """Test conversion milliliter - deciliter"""
        result = self.tools.convert_measure_units(unit=self.milliliter_unit,
                                                  new_unit=UnitsOfMeasurement.deciliter)
        expected_conversion_result = 0.2708
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_milliliter_unit_conversion_to_hectoliter(self):
        """Test conversion milliliter - hectoliter"""
        result = self.tools.convert_measure_units(unit=self.milliliter_unit,
                                                  new_unit=UnitsOfMeasurement.hectoliter)
        expected_conversion_result = 0.0002708
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_milliliter_unit_conversion_to_gallon(self):
        """Test conversion milliliter - gallon"""
        result = self.tools.convert_measure_units(unit=self.milliliter_unit,
                                                  new_unit=UnitsOfMeasurement.gallon)
        expected_conversion_result = 0.0071537792
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=5)

    def test_centiliter_unit_conversion_to_cubic_meter(self):
        """Test conversion centiliter - cubic meter"""
        result = self.tools.convert_measure_units(unit=self.centiliter_unit,
                                                  new_unit=UnitsOfMeasurement.cubic_meter)
        expected_conversion_result = 0.0002708
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_centiliter_unit_conversion_to_cubic_inch(self):
        """Test conversion centiliter - cubic inch"""
        result = self.tools.convert_measure_units(unit=self.centiliter_unit,
                                                  new_unit=UnitsOfMeasurement.cubic_inch)
        expected_conversion_result = 16.52523
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=2)

    def test_centiliter_unit_conversion_to_cubic_foot(self):
        """Test conversion centiliter - cubic foot"""
        result = self.tools.convert_measure_units(unit=self.centiliter_unit,
                                                  new_unit=UnitsOfMeasurement.cubic_foot)
        expected_conversion_result = 0.0095632117
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=5)

    def test_centiliter_unit_conversion_to_cubic_yard(self):
        """Test conversion centiliter - cubic yard"""
        result = self.tools.convert_measure_units(unit=self.centiliter_unit,
                                                  new_unit=UnitsOfMeasurement.cubic_yard)
        expected_conversion_result = 0.00035419303
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_centiliter_unit_conversion_to_liter(self):
        """Test conversion centiliter - liter"""
        result = self.tools.convert_measure_units(unit=self.centiliter_unit,
                                                  new_unit=UnitsOfMeasurement.liter)
        expected_conversion_result = 0.2708
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_centiliter_unit_conversion_to_milliliter(self):
        """Test conversion centiliter - milliliter"""
        result = self.tools.convert_measure_units(unit=self.centiliter_unit,
                                                  new_unit=UnitsOfMeasurement.milliliter)
        expected_conversion_result = 270.8
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_centiliter_unit_conversion_to_deciliter(self):
        """Test conversion centiliter - deciliter"""
        result = self.tools.convert_measure_units(unit=self.centiliter_unit,
                                                  new_unit=UnitsOfMeasurement.deciliter)
        expected_conversion_result = 2.708
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_centiliter_unit_conversion_to_hectoliter(self):
        """Test conversion centiliter - hectoliter"""
        result = self.tools.convert_measure_units(unit=self.centiliter_unit,
                                                  new_unit=UnitsOfMeasurement.hectoliter)
        expected_conversion_result = 0.002708
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_centiliter_unit_conversion_to_gallon(self):
        """Test conversion centiliter - gallon"""
        result = self.tools.convert_measure_units(unit=self.centiliter_unit,
                                                  new_unit=UnitsOfMeasurement.gallon)
        expected_conversion_result = 0.071537792
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_deciliter_unit_conversion_to_cubic_meter(self):
        """Test conversion deciliter - cubic meter"""
        result = self.tools.convert_measure_units(unit=self.deciliter_unit,
                                                  new_unit=UnitsOfMeasurement.cubic_meter)
        expected_conversion_result = 0.002708
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_deciliter_unit_conversion_to_cubic_inch(self):
        """Test conversion deciliter - cubic inch"""
        result = self.tools.convert_measure_units(unit=self.deciliter_unit,
                                                  new_unit=UnitsOfMeasurement.cubic_inch)
        expected_conversion_result = 165.2523
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=1)

    def test_deciliter_unit_conversion_to_cubic_foot(self):
        """Test conversion deciliter - cubic foot"""
        result = self.tools.convert_measure_units(unit=self.deciliter_unit,
                                                  new_unit=UnitsOfMeasurement.cubic_foot)
        expected_conversion_result = 0.095632117
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=4)

    def test_deciliter_unit_conversion_to_cubic_yard(self):
        """Test conversion deciliter - cubic yard"""
        result = self.tools.convert_measure_units(unit=self.deciliter_unit,
                                                  new_unit=UnitsOfMeasurement.cubic_yard)
        expected_conversion_result = 0.0035419303
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=6)

    def test_deciliter_unit_conversion_to_liter(self):
        """Test conversion deciliter - liter"""
        result = self.tools.convert_measure_units(unit=self.deciliter_unit,
                                                  new_unit=UnitsOfMeasurement.liter)
        expected_conversion_result = 2.708
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_deciliter_unit_conversion_to_milliliter(self):
        """Test conversion deciliter - milliliter"""
        result = self.tools.convert_measure_units(unit=self.deciliter_unit,
                                                  new_unit=UnitsOfMeasurement.milliliter)
        expected_conversion_result = 2708
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_deciliter_unit_conversion_to_centiliter(self):
        """Test conversion deciliter - centiliter"""
        result = self.tools.convert_measure_units(unit=self.deciliter_unit,
                                                  new_unit=UnitsOfMeasurement.centiliter)
        expected_conversion_result = 270.8
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_deciliter_unit_conversion_to_hectoliter(self):
        """Test conversion deciliter - hectoliter"""
        result = self.tools.convert_measure_units(unit=self.deciliter_unit,
                                                  new_unit=UnitsOfMeasurement.hectoliter)
        expected_conversion_result = 0.02708
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_deciliter_unit_conversion_to_gallon(self):
        """Test conversion deciliter - gallon"""
        result = self.tools.convert_measure_units(unit=self.deciliter_unit,
                                                  new_unit=UnitsOfMeasurement.gallon)
        expected_conversion_result = 0.71537792
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=4)

    def test_hectoliter_unit_conversion_to_cubic_meter(self):
        """Test conversion hectoliter - cubic meter"""
        result = self.tools.convert_measure_units(unit=self.hectoliter_unit,
                                                  new_unit=UnitsOfMeasurement.cubic_meter)
        expected_conversion_result = 2.708
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_hectoliter_unit_conversion_to_cubic_inch(self):
        """Test conversion hectoliter - cubic inch"""
        result = self.tools.convert_measure_units(unit=self.hectoliter_unit,
                                                  new_unit=UnitsOfMeasurement.cubic_inch)
        expected_conversion_result = 165242.16
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_hectoliter_unit_conversion_to_cubic_foot(self):
        """Test conversion hectoliter - cubic foot"""
        result = self.tools.convert_measure_units(unit=self.hectoliter_unit,
                                                  new_unit=UnitsOfMeasurement.cubic_foot)
        expected_conversion_result = 95.632117
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=1)

    def test_hectoliter_unit_conversion_to_cubic_yard(self):
        """Test conversion hectoliter - cubic yard"""
        result = self.tools.convert_measure_units(unit=self.hectoliter_unit,
                                                  new_unit=UnitsOfMeasurement.cubic_yard)
        expected_conversion_result = 3.5419303
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_hectoliter_unit_conversion_to_liter(self):
        """Test conversion hectoliter - liter"""
        result = self.tools.convert_measure_units(unit=self.hectoliter_unit,
                                                  new_unit=UnitsOfMeasurement.liter)
        expected_conversion_result = 2708
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_hectoliter_unit_conversion_to_milliliter(self):
        """Test conversion hectoliter - milliliter"""
        result = self.tools.convert_measure_units(unit=self.hectoliter_unit,
                                                  new_unit=UnitsOfMeasurement.milliliter)
        expected_conversion_result = 2708000
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_hectoliter_unit_conversion_to_centiliter(self):
        """Test conversion hectoliter - centiliter"""
        result = self.tools.convert_measure_units(unit=self.hectoliter_unit,
                                                  new_unit=UnitsOfMeasurement.centiliter)
        expected_conversion_result = 270800
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_hectoliter_unit_conversion_to_deciliter(self):
        """Test conversion hectoliter - deciliter"""
        result = self.tools.convert_measure_units(unit=self.hectoliter_unit,
                                                  new_unit=UnitsOfMeasurement.deciliter)
        expected_conversion_result = 27080
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_hectoliter_unit_conversion_to_gallon(self):
        """Test conversion hectoliter - gallon"""
        result = self.tools.convert_measure_units(unit=self.hectoliter_unit,
                                                  new_unit=UnitsOfMeasurement.gallon)
        expected_conversion_result = 715.37792
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=1)

    def test_gallon_unit_conversion_to_cubic_meter(self):
        """Test conversion gallon - cubic meter"""
        result = self.tools.convert_measure_units(unit=self.gallon_unit,
                                                  new_unit=UnitsOfMeasurement.cubic_meter)
        expected_conversion_result = 0.10250895
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_gallon_unit_conversion_to_cubic_inch(self):
        """Test conversion gallon - cubic inch"""
        result = self.tools.convert_measure_units(unit=self.gallon_unit,
                                                  new_unit=UnitsOfMeasurement.cubic_inch)
        expected_conversion_result = 6255.48
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_gallon_unit_conversion_to_cubic_foot(self):
        """Test conversion gallon - cubic foot"""
        result = self.tools.convert_measure_units(unit=self.gallon_unit,
                                                  new_unit=UnitsOfMeasurement.cubic_foot)
        expected_conversion_result = 3.6200694
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_gallon_unit_conversion_to_cubic_yard(self):
        """Test conversion gallon - cubic yard"""
        result = self.tools.convert_measure_units(unit=self.gallon_unit,
                                                  new_unit=UnitsOfMeasurement.cubic_yard)
        expected_conversion_result = 0.13407665
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=4)

    def test_gallon_unit_conversion_to_liter(self):
        """Test conversion gallon - liter"""
        result = self.tools.convert_measure_units(unit=self.gallon_unit,
                                                  new_unit=UnitsOfMeasurement.liter)
        expected_conversion_result = 102.50895
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=1)

    def test_gallon_unit_conversion_to_milliliter(self):
        """Test conversion gallon - milliliter"""
        result = self.tools.convert_measure_units(unit=self.gallon_unit,
                                                  new_unit=UnitsOfMeasurement.milliliter)
        expected_conversion_result = 102497.79999999999
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_gallon_unit_conversion_to_centiliter(self):
        """Test conversion gallon - centiliter"""
        result = self.tools.convert_measure_units(unit=self.gallon_unit,
                                                  new_unit=UnitsOfMeasurement.centiliter)
        expected_conversion_result = 10249.779999999999
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_gallon_unit_conversion_to_deciliter(self):
        """Test conversion gallon - deciliter"""
        result = self.tools.convert_measure_units(unit=self.gallon_unit,
                                                  new_unit=UnitsOfMeasurement.deciliter)
        expected_conversion_result = 1025.0895
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=2)

    def test_gallon_unit_conversion_to_hectoliter(self):
        """Test conversion gallon - hectoliter"""
        result = self.tools.convert_measure_units(unit=self.gallon_unit,
                                                  new_unit=UnitsOfMeasurement.hectoliter)
        expected_conversion_result = 1.0250895
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=4)

    def test_second_unit_conversion_to_minute(self):
        """Test conversion second - minute"""
        result = self.tools.convert_measure_units(unit=self.second_unit,
                                                  new_unit=UnitsOfMeasurement.minute)
        expected_conversion_result = 0.45133333
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_second_unit_conversion_to_hour(self):
        """Test conversion second - hour"""
        result = self.tools.convert_measure_units(unit=self.second_unit,
                                                  new_unit=UnitsOfMeasurement.hour)
        expected_conversion_result = 0.0075222222
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_second_unit_conversion_to_day(self):
        """Test conversion second - day"""
        result = self.tools.convert_measure_units(unit=self.second_unit,
                                                  new_unit=UnitsOfMeasurement.day)
        expected_conversion_result = 0.00031342593
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_second_unit_conversion_to_year(self):
        """Test conversion second - year"""
        result = self.tools.convert_measure_units(unit=self.second_unit,
                                                  new_unit=UnitsOfMeasurement.year)
        expected_conversion_result = 8.587012e-7
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_minute_unit_conversion_to_second(self):
        """Test conversion minute - second"""
        result = self.tools.convert_measure_units(unit=self.minute_unit,
                                                  new_unit=UnitsOfMeasurement.second)
        expected_conversion_result = 1624.8
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_minute_unit_conversion_to_hour(self):
        """Test conversion minute - hour"""
        result = self.tools.convert_measure_units(unit=self.minute_unit,
                                                  new_unit=UnitsOfMeasurement.hour)
        expected_conversion_result = 0.45133333
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_minute_unit_conversion_to_day(self):
        """Test conversion minute - day"""
        result = self.tools.convert_measure_units(unit=self.minute_unit,
                                                  new_unit=UnitsOfMeasurement.day)
        expected_conversion_result = 0.018805556
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_minute_unit_conversion_to_year(self):
        """Test conversion minute - year"""
        result = self.tools.convert_measure_units(unit=self.minute_unit,
                                                  new_unit=UnitsOfMeasurement.year)
        expected_conversion_result = 5.152207e-5
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_hour_unit_conversion_to_second(self):
        """Test conversion hour - second"""
        result = self.tools.convert_measure_units(unit=self.hour_unit,
                                                  new_unit=UnitsOfMeasurement.second)
        expected_conversion_result = 97488
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_hour_unit_conversion_to_minute(self):
        """Test conversion hour - minute"""
        result = self.tools.convert_measure_units(unit=self.hour_unit,
                                                  new_unit=UnitsOfMeasurement.minute)
        expected_conversion_result = 1624.8
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_hour_unit_conversion_to_day(self):
        """Test conversion hour - day"""
        result = self.tools.convert_measure_units(unit=self.hour_unit,
                                                  new_unit=UnitsOfMeasurement.day)
        expected_conversion_result = 1.1283333
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_hour_unit_conversion_to_year(self):
        """Test conversion hour - year"""
        result = self.tools.convert_measure_units(unit=self.hour_unit,
                                                  new_unit=UnitsOfMeasurement.year)
        expected_conversion_result = 0.0030913242
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_day_unit_conversion_to_second(self):
        """Test conversion day - second"""
        result = self.tools.convert_measure_units(unit=self.day_unit,
                                                  new_unit=UnitsOfMeasurement.second)
        expected_conversion_result = 2339712
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_day_unit_conversion_to_minute(self):
        """Test conversion day - minute"""
        result = self.tools.convert_measure_units(unit=self.day_unit,
                                                  new_unit=UnitsOfMeasurement.minute)
        expected_conversion_result = 38995.2
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_day_unit_conversion_to_hour(self):
        """Test conversion day - hour"""
        result = self.tools.convert_measure_units(unit=self.day_unit,
                                                  new_unit=UnitsOfMeasurement.hour)
        expected_conversion_result = 649.92
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_day_unit_conversion_to_year(self):
        """Test conversion day - year"""
        result = self.tools.convert_measure_units(unit=self.day_unit,
                                                  new_unit=UnitsOfMeasurement.year)
        expected_conversion_result = 0.074191781
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_year_unit_conversion_to_second(self):
        """Test conversion year - second"""
        result = self.tools.convert_measure_units(unit=self.year_unit,
                                                  new_unit=UnitsOfMeasurement.second)
        expected_conversion_result = 854103200.0
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_year_unit_conversion_to_minute(self):
        """Test conversion year - minute"""
        result = self.tools.convert_measure_units(unit=self.year_unit,
                                                  new_unit=UnitsOfMeasurement.minute)
        expected_conversion_result = 14233248
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_year_unit_conversion_to_hour(self):
        """Test conversion year - hour"""
        result = self.tools.convert_measure_units(unit=self.year_unit,
                                                  new_unit=UnitsOfMeasurement.hour)
        expected_conversion_result = 237220.8
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_year_unit_conversion_to_day(self):
        """Test conversion year - day"""
        result = self.tools.convert_measure_units(unit=self.year_unit,
                                                  new_unit=UnitsOfMeasurement.day)
        expected_conversion_result = 9884.2
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_miles_per_hour_unit_conversion_to_meters_per_second(self):
        """Test conversion miles per hour - meters per second"""
        result = self.tools.convert_measure_units(unit=self.miles_per_hour_unit,
                                                  new_unit=UnitsOfMeasurement.meters_per_second)
        expected_conversion_result = 12.105843
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_miles_per_hour_unit_conversion_to_kilometer_per_hour(self):
        """Test conversion miles per hour - kilometer per hour"""
        result = self.tools.convert_measure_units(unit=self.miles_per_hour_unit,
                                                  new_unit=UnitsOfMeasurement.kilometer_per_hour)
        expected_conversion_result = 43.581036
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=1)

    def test_meters_per_second_unit_conversion_to_miles_per_hour(self):
        """Test conversion meters per second - miles per hour"""
        result = self.tools.convert_measure_units(unit=self.meters_per_second_unit,
                                                  new_unit=UnitsOfMeasurement.miles_per_hour)
        expected_conversion_result = 60.576235
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=2)

    def test_meters_per_second_unit_conversion_to_kilometer_per_hour(self):
        """Test conversion meters per second - kilometer per hour"""
        result = self.tools.convert_measure_units(unit=self.meters_per_second_unit,
                                                  new_unit=UnitsOfMeasurement.kilometer_per_hour)
        expected_conversion_result = 97.488
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_kilometer_per_hour_unit_conversion_to_miles_per_hour(self):
        """Test conversion kilometer per hour - miles per hour"""
        result = self.tools.convert_measure_units(unit=self.kilometer_per_hour_unit,
                                                  new_unit=UnitsOfMeasurement.miles_per_hour)
        expected_conversion_result = 16.826732
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=2)

    def test_kilometer_per_hour_unit_conversion_to_meters_per_second(self):
        """Test conversion kilometer per hour - meters per second"""
        result = self.tools.convert_measure_units(unit=self.kilometer_per_hour_unit,
                                                  new_unit=UnitsOfMeasurement.meters_per_second)
        expected_conversion_result = 7.5222222
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_gram_unit_conversion_to_kilogram(self):
        """Test conversion gram - kilogram"""
        result = self.tools.convert_measure_units(unit=self.gram_unit,
                                                  new_unit=UnitsOfMeasurement.kilogram)
        expected_conversion_result = 0.02708
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)

    def test_kilogram_unit_conversion_to_gram(self):
        """Test conversion kilogram - gram"""
        result = self.tools.convert_measure_units(unit=self.kilogram_unit,
                                                  new_unit=UnitsOfMeasurement.gram)
        expected_conversion_result = 27080
        self.assertAlmostEqual(
            result.value, expected_conversion_result, places=3)


class TestDatetimeTools(unittest.TestCase):
    """Test case for datetime tools"""
    tools = DatetimeTools()
    remove_valid_dates = {
        "initial": tools.build_date(year=2022, month=11, day=10),
        "final": tools.build_date(day=5),
        "result": tools.build_date(year=2022, month=11, day=5)
    }
    add_valid_dates = {
        "initial": tools.build_date(year=2022, month=11, day=10),
        "final": tools.build_date(day=5),
        "result": tools.build_date(year=2022, month=11, day=15)
    }
    dif_valid_dates = {
        "initial": tools.build_date(year=2022, month=11, day=10),
        "final": tools.build_date(year=2022, month=11, day=5),
        "result": "5 dias"
    }
    dif_valid_date_times = {
        "initial": tools.build_date(year=2022, month=11, day=10, hour=18, minute=30, second=30),
        "final": tools.build_date(year=2022, month=11, day=5, hour=14, minute=15, second=15),
        "result": "5 dias, 4 horas, 15 minutos e 15 segundos"
    }
    remove_invalid_dates = {
        "initial": tools.build_date(year=2022, month=11, day=-1),
        "final": tools.build_date(day=5),
        "result": tools.build_date(year=2022, month=10, day=27)
    }
    add_invalid_dates = {
        "initial": tools.build_date(year=2022, month=11, day=-1),
        "final": tools.build_date(day=5),
        "result": tools.build_date(year=2022, month=11, day=6)
    }
    dif_invalid_dates = {
        "initial": tools.build_date(year=2022, month=10, day=32),
        "final": tools.build_date(year=2022, month=10, day=-1),
        "result": "30 dias"
    }
    dif_invalid_date_times = {
        "initial": tools.build_date(year=2022, month=11, day=10, hour=32, minute=70, second=90),
        "final": tools.build_date(year=2022, month=11, day=5, hour=-1, minute=-1, second=-1),
        "result": "5 dias, 23 horas, 59 minutos e 59 segundos"
    }

    def test_rem_valid_dates(self):
        """Test remove valid dates"""
        result = self.tools.remove_from_date(self.remove_valid_dates["initial"],
                                             self.remove_valid_dates["final"])
        self.assertEqual(result.as_datetime(),
                         self.remove_valid_dates["result"].as_datetime())

    def test_add_valid_dates(self):
        """Test add valid dates"""
        result = self.tools.add_to_date(self.add_valid_dates["initial"],
                                        self.add_valid_dates["final"])
        self.assertEqual(result.as_datetime(),
                         self.add_valid_dates["result"].as_datetime())

    def test_dif_valid_dates(self):
        """Test difference valid dates"""
        result = self.tools.calc_date_dif(self.dif_valid_dates["initial"],
                                          self.dif_valid_dates["final"])
        self.assertEqual(result, self.dif_valid_dates["result"])

    def test_dif_valid_date_time(self):
        """Test difference valid date time"""
        result = self.tools.calc_date_hour_dif(self.dif_valid_date_times["initial"],
                                               self.dif_valid_date_times["final"])
        self.assertEqual(result, self.dif_valid_date_times["result"])

    def test_rem_invalid_dates(self):
        """Test remove invalid dates"""
        result = self.tools.remove_from_date(self.remove_invalid_dates["initial"],
                                             self.remove_invalid_dates["final"])
        self.assertEqual(result.as_datetime(),
                         self.remove_invalid_dates["result"].as_datetime())

    def test_add_invalid_dates(self):
        """Test add invalid dates"""
        result = self.tools.add_to_date(self.add_invalid_dates["initial"],
                                        self.add_invalid_dates["final"])
        self.assertEqual(result.as_datetime(),
                         self.add_invalid_dates["result"].as_datetime())

    def test_dif_invalid_dates(self):
        """Test difference invalid dates"""
        result = self.tools.calc_date_dif(self.dif_invalid_dates["initial"],
                                          self.dif_invalid_dates["final"])
        self.assertEqual(result, self.dif_invalid_dates["result"])

    def test_dif_invalid_date_time(self):
        """Test difference invalid date time"""
        result = self.tools.calc_date_hour_dif(self.dif_invalid_date_times["initial"],
                                               self.dif_invalid_date_times["final"])
        self.assertEqual(result, self.dif_invalid_date_times["result"])


if __name__ == "__main__":
    unittest.main()
