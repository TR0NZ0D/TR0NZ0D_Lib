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
"""

from __future__ import annotations
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from enum import Enum


class UnitOf(Enum):
    length = 0
    area = 1
    volume = 2
    time = 3
    speed = 4
    mass = 5
    unknown = 6


class UnitsOfMeasurement(Enum):
    # Length
    meter = 0
    millimeter = 1
    centimeter = 2
    decimeter = 3
    kilometer = 4
    inch = 5
    foot = 6
    yard = 7
    mile = 8

    # Area
    square_meter = 9
    square_inch = 10
    square_feet = 11
    square_yard = 12
    square_mile = 13

    # Volume
    cubic_meter = 14
    cubic_inch = 15
    cubic_foot = 16
    cubic_yard = 17
    liter = 18
    milliliter = 19
    centiliter = 20
    deciliter = 21
    hectoliter = 22
    gallon = 23

    # Time
    second = 24
    minute = 25
    hour = 26
    day = 27
    year = 28

    # Speed
    miles_per_hour = 29
    meters_per_second = 30
    kilometer_per_hour = 31

    # Mass
    gram = 32
    kilogram = 33

    def group(self) -> UnitOf:
        match self:
            # Length
            case self.meter | self.millimeter | self.centimeter | self.decimeter | self.kilometer | self.inch | self.foot | self.yard | self.mile:
                return UnitOf.length
            # Area
            case self.square_meter | self.square_inch | self.square_feet | self.square_yard | self.square_mile:
                return UnitOf.area
            # Volume
            case self.cubic_meter | self.cubic_inch | self.cubic_foot | self.cubic_yard | self.liter | self.milliliter | self.centiliter | self.deciliter | self.hectoliter | self.gallon:
                return UnitOf.volume
            # Time
            case self.second | self.minute | self.hour | self.day | self.year:
                return UnitOf.time
            # Speed
            case self.miles_per_hour | self.meters_per_second | self.kilometer_per_hour:
                return UnitOf.speed
            # Mass
            case self.gram | self.kilogram:
                return UnitOf.mass
            case _:
                return UnitOf.unknown


class ConvertibleMeasureUnit:
    measure_unit: UnitsOfMeasurement
    value: float | int

    def __init__(self, unit: UnitsOfMeasurement, value: float | int) -> None:
        self.measure_unit = unit
        self.value = value

    def check_if_convertible(self, new_unit: UnitsOfMeasurement) -> bool:
        """ Cheks if current measure unit is convertible to new unit

        Args:
            new_unit (UnitsOfMeasurement): New unit desired type

        Returns:
            bool: True if convertible, otherwise False
        """
        return self.measure_unit.group().name == new_unit.group().name

    def convert_to(self, new_unit: UnitsOfMeasurement) -> ConvertibleMeasureUnit:
        """ Convert a measure unit to a new type, updating it's value (value convert is approximated)

        Args:
            new_unit (UnitsOfMeasurement): New desired unit type

        Raises:
            ConversionError: Conversion error if not possible to convert units

        Returns:
            ConvertibleMeasureUnit: A new converted ConvertibleMeasureUnit
        """
        if not self.check_if_convertible(new_unit):
            raise ConversionError(f"Impossible to convert {self.measure_unit.name} to {new_unit.name}")
        current_unit_group = self.measure_unit.group()

        match current_unit_group.name:
            case UnitOf.length.name:
                match self.measure_unit.name:
                    case UnitsOfMeasurement.meter.name:
                        match new_unit.name:
                            case UnitsOfMeasurement.millimeter.name:
                                new_value = (self.value * 1000)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.millimeter,
                                                              value=new_value)
                            case UnitsOfMeasurement.centimeter.name:
                                new_value = (self.value * 100)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.centimeter,
                                                              value=new_value)
                            case UnitsOfMeasurement.decimeter.name:
                                new_value = (self.value * 10)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.decimeter,
                                                              value=new_value)
                            case UnitsOfMeasurement.kilometer.name:
                                new_value = (self.value / 1000)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.kilometer,
                                                              value=new_value)
                            case UnitsOfMeasurement.inch.name:
                                new_value = (self.value * 39.37)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.inch,
                                                              value=new_value)
                            case UnitsOfMeasurement.foot.name:
                                new_value = (self.value * 3.281)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.foot,
                                                              value=new_value)
                            case UnitsOfMeasurement.yard.name:
                                new_value = (self.value * 1.094)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.yard,
                                                              value=new_value)
                            case UnitsOfMeasurement.mile.name:
                                new_value = (self.value / 1609)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.mile,
                                                              value=new_value)
                            case _:
                                return self
                    case UnitsOfMeasurement.millimeter.name:
                        match new_unit.name:
                            case UnitsOfMeasurement.meter.name:
                                new_value = (self.value / 1000)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.meter,
                                                              value=new_value)
                            case UnitsOfMeasurement.centimeter.name:
                                new_value = (self.value / 10)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.centimeter,
                                                              value=new_value)
                            case UnitsOfMeasurement.decimeter.name:
                                new_value = (self.value / 100)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.decimeter,
                                                              value=new_value)
                            case UnitsOfMeasurement.kilometer.name:
                                new_value = (self.value / 1e+6)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.kilometer,
                                                              value=new_value)
                            case UnitsOfMeasurement.inch.name:
                                new_value = (self.value / 25.4)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.inch,
                                                              value=new_value)
                            case UnitsOfMeasurement.foot.name:
                                new_value = (self.value / 304.8)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.foot,
                                                              value=new_value)
                            case UnitsOfMeasurement.yard.name:
                                new_value = (self.value / 914.4)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.yard,
                                                              value=new_value)
                            case UnitsOfMeasurement.mile.name:
                                new_value = (self.value / 1.609e+6)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.mile,
                                                              value=new_value)
                            case _:
                                return self
                    case UnitsOfMeasurement.centimeter.name:
                        match new_unit.name:
                            case UnitsOfMeasurement.meter.name:
                                new_value = (self.value / 100)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.meter,
                                                              value=new_value)
                            case UnitsOfMeasurement.millimeter.name:
                                new_value = (self.value * 10)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.millimeter,
                                                              value=new_value)
                            case UnitsOfMeasurement.decimeter.name:
                                new_value = (self.value / 10)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.decimeter,
                                                              value=new_value)
                            case UnitsOfMeasurement.kilometer.name:
                                new_value = (self.value / 100000)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.kilometer,
                                                              value=new_value)
                            case UnitsOfMeasurement.inch.name:
                                new_value = (self.value / 2.54)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.inch,
                                                              value=new_value)
                            case UnitsOfMeasurement.foot.name:
                                new_value = (self.value / 30.48)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.foot,
                                                              value=new_value)
                            case UnitsOfMeasurement.yard.name:
                                new_value = (self.value / 91.44)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.yard,
                                                              value=new_value)
                            case UnitsOfMeasurement.mile.name:
                                new_value = (self.value / 160900)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.mile,
                                                              value=new_value)
                            case _:
                                return self
                    case UnitsOfMeasurement.decimeter.name:
                        match new_unit.name:
                            case UnitsOfMeasurement.meter.name:
                                new_value = (self.value / 10)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.meter,
                                                              value=new_value)
                            case UnitsOfMeasurement.millimeter.name:
                                new_value = (self.value * 100)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.millimeter,
                                                              value=new_value)
                            case UnitsOfMeasurement.centimeter.name:
                                new_value = (self.value * 10)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.centimeter,
                                                              value=new_value)
                            case UnitsOfMeasurement.kilometer.name:
                                new_value = (self.value / 10000)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.kilometer,
                                                              value=new_value)
                            case UnitsOfMeasurement.inch.name:
                                new_value = (self.value * 3.937)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.inch,
                                                              value=new_value)
                            case UnitsOfMeasurement.foot.name:
                                new_value = (self.value / 3.048)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.foot,
                                                              value=new_value)
                            case UnitsOfMeasurement.yard.name:
                                new_value = (self.value / 9.144)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.yard,
                                                              value=new_value)
                            case UnitsOfMeasurement.mile.name:
                                new_value = (self.value / 16090)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.mile,
                                                              value=new_value)
                            case _:
                                return self
                    case UnitsOfMeasurement.kilometer.name:
                        match new_unit.name:
                            case UnitsOfMeasurement.meter.name:
                                new_value = (self.value * 1000)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.meter,
                                                              value=new_value)
                            case UnitsOfMeasurement.millimeter.name:
                                new_value = (self.value * 1e+6)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.millimeter,
                                                              value=new_value)
                            case UnitsOfMeasurement.centimeter.name:
                                new_value = (self.value * 100000)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.centimeter,
                                                              value=new_value)
                            case UnitsOfMeasurement.decimeter.name:
                                new_value = (self.value * 10000)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.decimeter,
                                                              value=new_value)
                            case UnitsOfMeasurement.inch.name:
                                new_value = (self.value * 39370)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.inch,
                                                              value=new_value)
                            case UnitsOfMeasurement.foot.name:
                                new_value = (self.value * 3281)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.foot,
                                                              value=new_value)
                            case UnitsOfMeasurement.yard.name:
                                new_value = (self.value * 1094)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.yard,
                                                              value=new_value)
                            case UnitsOfMeasurement.mile.name:
                                new_value = (self.value / 1.609)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.mile,
                                                              value=new_value)
                            case _:
                                return self
                    case UnitsOfMeasurement.inch.name:
                        match new_unit.name:
                            case UnitsOfMeasurement.meter.name:
                                new_value = (self.value / 39.37)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.meter,
                                                              value=new_value)
                            case UnitsOfMeasurement.millimeter.name:
                                new_value = (self.value * 25.4)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.millimeter,
                                                              value=new_value)
                            case UnitsOfMeasurement.centimeter.name:
                                new_value = (self.value * 2.54)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.centimeter,
                                                              value=new_value)
                            case UnitsOfMeasurement.decimeter.name:
                                new_value = (self.value / 3.937)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.decimeter,
                                                              value=new_value)
                            case UnitsOfMeasurement.kilometer.name:
                                new_value = (self.value / 39370)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.kilometer,
                                                              value=new_value)
                            case UnitsOfMeasurement.foot.name:
                                new_value = (self.value / 12)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.foot,
                                                              value=new_value)
                            case UnitsOfMeasurement.yard.name:
                                new_value = (self.value / 36)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.yard,
                                                              value=new_value)
                            case UnitsOfMeasurement.mile.name:
                                new_value = (self.value / 63360)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.mile,
                                                              value=new_value)
                            case _:
                                return self
                    case UnitsOfMeasurement.foot.name:
                        match new_unit.name:
                            case UnitsOfMeasurement.meter.name:
                                new_value = (self.value / 3.281)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.meter,
                                                              value=new_value)
                            case UnitsOfMeasurement.millimeter.name:
                                new_value = (self.value * 304.8)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.millimeter,
                                                              value=new_value)
                            case UnitsOfMeasurement.centimeter.name:
                                new_value = (self.value * 30.48)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.centimeter,
                                                              value=new_value)
                            case UnitsOfMeasurement.decimeter.name:
                                new_value = (self.value * 3.048)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.decimeter,
                                                              value=new_value)
                            case UnitsOfMeasurement.kilometer.name:
                                new_value = (self.value / 3281)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.kilometer,
                                                              value=new_value)
                            case UnitsOfMeasurement.inch.name:
                                new_value = (self.value * 12)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.inch,
                                                              value=new_value)
                            case UnitsOfMeasurement.yard.name:
                                new_value = (self.value / 3)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.yard,
                                                              value=new_value)
                            case UnitsOfMeasurement.mile.name:
                                new_value = (self.value / 5280)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.mile,
                                                              value=new_value)
                            case _:
                                return self
                    case UnitsOfMeasurement.yard.name:
                        match new_unit.name:
                            case UnitsOfMeasurement.meter.name:
                                new_value = (self.value / 1.094)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.meter,
                                                              value=new_value)
                            case UnitsOfMeasurement.millimeter.name:
                                new_value = (self.value * 914.4)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.millimeter,
                                                              value=new_value)
                            case UnitsOfMeasurement.centimeter.name:
                                new_value = (self.value * 91.44)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.centimeter,
                                                              value=new_value)
                            case UnitsOfMeasurement.decimeter.name:
                                new_value = (self.value * 9.144)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.decimeter,
                                                              value=new_value)
                            case UnitsOfMeasurement.kilometer.name:
                                new_value = (self.value / 1094)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.kilometer,
                                                              value=new_value)
                            case UnitsOfMeasurement.inch.name:
                                new_value = (self.value * 36)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.inch,
                                                              value=new_value)
                            case UnitsOfMeasurement.foot.name:
                                new_value = (self.value * 3)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.foot,
                                                              value=new_value)
                            case UnitsOfMeasurement.mile.name:
                                new_value = (self.value / 1760)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.mile,
                                                              value=new_value)
                            case _:
                                return self
                    case UnitsOfMeasurement.mile.name:
                        match new_unit.name:
                            case UnitsOfMeasurement.meter.name:
                                new_value = (self.value * 1609)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.meter,
                                                              value=new_value)
                            case UnitsOfMeasurement.millimeter.name:
                                new_value = (self.value * 1.609e+6)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.millimeter,
                                                              value=new_value)
                            case UnitsOfMeasurement.centimeter.name:
                                new_value = (self.value * 160900)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.centimeter,
                                                              value=new_value)
                            case UnitsOfMeasurement.decimeter.name:
                                new_value = (self.value * 16090)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.decimeter,
                                                              value=new_value)
                            case UnitsOfMeasurement.kilometer.name:
                                new_value = (self.value * 1.609)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.kilometer,
                                                              value=new_value)
                            case UnitsOfMeasurement.inch.name:
                                new_value = (self.value * 63360)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.inch,
                                                              value=new_value)
                            case UnitsOfMeasurement.foot.name:
                                new_value = (self.value * 5280)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.foot,
                                                              value=new_value)
                            case UnitsOfMeasurement.yard.name:
                                new_value = (self.value * 1760)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.yard,
                                                              value=new_value)
                            case _:
                                return self
                    case _:
                        return self
            case UnitOf.area.name:
                match self.measure_unit.name:
                    case UnitsOfMeasurement.square_meter.name:
                        match new_unit.name:
                            case UnitsOfMeasurement.square_inch.name:
                                new_value = (self.value * 1550)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.square_inch,
                                                              value=new_value)
                            case UnitsOfMeasurement.square_feet.name:
                                new_value = (self.value * 10.764)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.square_feet,
                                                              value=new_value)
                            case UnitsOfMeasurement.square_yard.name:
                                new_value = (self.value * 1.196)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.square_yard,
                                                              value=new_value)
                            case UnitsOfMeasurement.square_mile.name:
                                new_value = (self.value / 2.59e+6)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.square_mile,
                                                              value=new_value)
                            case _:
                                return self
                    case UnitsOfMeasurement.square_inch.name:
                        match new_unit.name:
                            case UnitsOfMeasurement.square_meter.name:
                                new_value = (self.value / 1550)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.square_meter,
                                                              value=new_value)
                            case UnitsOfMeasurement.square_feet.name:
                                new_value = (self.value / 144)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.square_feet,
                                                              value=new_value)
                            case UnitsOfMeasurement.square_yard.name:
                                new_value = (self.value / 1296)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.square_yard,
                                                              value=new_value)
                            case UnitsOfMeasurement.square_mile.name:
                                new_value = (self.value / 4.014e+9)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.square_mile,
                                                              value=new_value)
                            case _:
                                return self
                    case UnitsOfMeasurement.square_feet.name:
                        match new_unit.name:
                            case UnitsOfMeasurement.square_meter.name:
                                new_value = (self.value / 10.764)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.square_meter,
                                                              value=new_value)
                            case UnitsOfMeasurement.square_inch.name:
                                new_value = (self.value * 144)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.square_inch,
                                                              value=new_value)
                            case UnitsOfMeasurement.square_yard.name:
                                new_value = (self.value / 9)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.square_yard,
                                                              value=new_value)
                            case UnitsOfMeasurement.square_mile.name:
                                new_value = (self.value / 2.788e+7)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.square_mile,
                                                              value=new_value)
                            case _:
                                return self
                    case UnitsOfMeasurement.square_yard.name:
                        match new_unit.name:
                            case UnitsOfMeasurement.square_meter.name:
                                new_value = (self.value / 1.196)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.square_meter,
                                                              value=new_value)
                            case UnitsOfMeasurement.square_inch.name:
                                new_value = (self.value * 1296)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.square_inch,
                                                              value=new_value)
                            case UnitsOfMeasurement.square_feet.name:
                                new_value = (self.value * 9)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.square_feet,
                                                              value=new_value)
                            case UnitsOfMeasurement.square_mile.name:
                                new_value = (self.value / 3.098e+6)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.square_mile,
                                                              value=new_value)
                            case _:
                                return self
                    case UnitsOfMeasurement.square_mile.name:
                        match new_unit.name:
                            case UnitsOfMeasurement.square_meter.name:
                                new_value = (self.value * 2.59e+6)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.square_meter,
                                                              value=new_value)
                            case UnitsOfMeasurement.square_inch.name:
                                new_value = (self.value * 4.014e+9)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.square_inch,
                                                              value=new_value)
                            case UnitsOfMeasurement.square_feet.name:
                                new_value = (self.value * 2.788e+7)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.square_feet,
                                                              value=new_value)
                            case UnitsOfMeasurement.square_yard.name:
                                new_value = (self.value * 3.098e+6)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.square_yard,
                                                              value=new_value)
                            case _:
                                return self
                    case _:
                        return self
            case UnitOf.volume.name:
                match self.measure_unit.name:
                    case UnitsOfMeasurement.cubic_meter.name:
                        match new_unit.name:
                            case UnitsOfMeasurement.cubic_inch.name:
                                new_value = (self.value * 61020)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.cubic_inch,
                                                              value=new_value)
                            case UnitsOfMeasurement.cubic_foot.name:
                                new_value = (self.value * 35.315)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.cubic_foot,
                                                              value=new_value)
                            case UnitsOfMeasurement.cubic_yard.name:
                                new_value = (self.value * 1.308)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.cubic_yard,
                                                              value=new_value)
                            case UnitsOfMeasurement.liter.name:
                                new_value = (self.value * 1000)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.liter,
                                                              value=new_value)
                            case UnitsOfMeasurement.milliliter.name:
                                new_value = (self.value * 1e+6)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.milliliter,
                                                              value=new_value)
                            case UnitsOfMeasurement.centiliter.name:
                                new_value = (self.value * 100000)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.centiliter,
                                                              value=new_value)
                            case UnitsOfMeasurement.deciliter.name:
                                new_value = (self.value * 10000)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.deciliter,
                                                              value=new_value)
                            case UnitsOfMeasurement.hectoliter.name:
                                new_value = (self.value * 10)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.hectoliter,
                                                              value=new_value)
                            case UnitsOfMeasurement.gallon.name:
                                new_value = (self.value * 264.2)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.gallon,
                                                              value=new_value)
                            case _:
                                return self
                    case UnitsOfMeasurement.cubic_inch.name:
                        match new_unit.name:
                            case UnitsOfMeasurement.cubic_meter.name:
                                new_value = (self.value / 61020)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.cubic_meter,
                                                              value=new_value)
                            case UnitsOfMeasurement.cubic_foot.name:
                                new_value = (self.value / 1728)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.cubic_foot,
                                                              value=new_value)
                            case UnitsOfMeasurement.cubic_yard.name:
                                new_value = (self.value / 46660)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.cubic_yard,
                                                              value=new_value)
                            case UnitsOfMeasurement.liter.name:
                                new_value = (self.value / 61.024)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.liter,
                                                              value=new_value)
                            case UnitsOfMeasurement.milliliter.name:
                                new_value = (self.value * 16.387)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.milliliter,
                                                              value=new_value)
                            case UnitsOfMeasurement.centiliter.name:
                                new_value = (self.value * 1.639)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.centiliter,
                                                              value=new_value)
                            case UnitsOfMeasurement.deciliter.name:
                                new_value = (self.value / 6.102)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.deciliter,
                                                              value=new_value)
                            case UnitsOfMeasurement.hectoliter.name:
                                new_value = (self.value / 6102)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.hectoliter,
                                                              value=new_value)
                            case UnitsOfMeasurement.gallon.name:
                                new_value = (self.value / 231)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.gallon,
                                                              value=new_value)
                            case _:
                                return self
                    case UnitsOfMeasurement.cubic_foot.name:
                        match new_unit.name:
                            case UnitsOfMeasurement.cubic_meter.name:
                                new_value = (self.value / 35.315)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.cubic_meter,
                                                              value=new_value)
                            case UnitsOfMeasurement.cubic_inch.name:
                                new_value = (self.value * 1728)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.cubic_inch,
                                                              value=new_value)
                            case UnitsOfMeasurement.cubic_yard.name:
                                new_value = (self.value / 27)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.cubic_yard,
                                                              value=new_value)
                            case UnitsOfMeasurement.liter.name:
                                new_value = (self.value * 28.317)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.liter,
                                                              value=new_value)
                            case UnitsOfMeasurement.milliliter.name:
                                new_value = (self.value * 28320)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.milliliter,
                                                              value=new_value)
                            case UnitsOfMeasurement.centiliter.name:
                                new_value = (self.value * 2832)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.centiliter,
                                                              value=new_value)
                            case UnitsOfMeasurement.deciliter.name:
                                new_value = (self.value * 283.2)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.deciliter,
                                                              value=new_value)
                            case UnitsOfMeasurement.hectoliter.name:
                                new_value = (self.value / 3.532)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.hectoliter,
                                                              value=new_value)
                            case UnitsOfMeasurement.gallon.name:
                                new_value = (self.value * 7.481)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.gallon,
                                                              value=new_value)
                            case _:
                                return self
                    case UnitsOfMeasurement.cubic_yard.name:
                        match new_unit.name:
                            case UnitsOfMeasurement.cubic_meter.name:
                                new_value = (self.value / 1.308)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.cubic_meter,
                                                              value=new_value)
                            case UnitsOfMeasurement.cubic_inch.name:
                                new_value = (self.value * 46660)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.cubic_inch,
                                                              value=new_value)
                            case UnitsOfMeasurement.cubic_foot.name:
                                new_value = (self.value * 27)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.cubic_foot,
                                                              value=new_value)
                            case UnitsOfMeasurement.liter.name:
                                new_value = (self.value * 764.6)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.liter,
                                                              value=new_value)
                            case UnitsOfMeasurement.milliliter.name:
                                new_value = (self.value * 764600)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.milliliter,
                                                              value=new_value)
                            case UnitsOfMeasurement.centiliter.name:
                                new_value = (self.value * 76460)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.centiliter,
                                                              value=new_value)
                            case UnitsOfMeasurement.deciliter.name:
                                new_value = (self.value * 7646)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.deciliter,
                                                              value=new_value)
                            case UnitsOfMeasurement.hectoliter.name:
                                new_value = (self.value * 7.646)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.hectoliter,
                                                              value=new_value)
                            case UnitsOfMeasurement.gallon.name:
                                new_value = (self.value * 202)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.gallon,
                                                              value=new_value)
                            case _:
                                return self
                    case UnitsOfMeasurement.liter.name:
                        match new_unit.name:
                            case UnitsOfMeasurement.cubic_meter.name:
                                new_value = (self.value / 1000)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.cubic_meter,
                                                              value=new_value)
                            case UnitsOfMeasurement.cubic_inch.name:
                                new_value = (self.value * 61.024)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.cubic_inch,
                                                              value=new_value)
                            case UnitsOfMeasurement.cubic_foot.name:
                                new_value = (self.value / 28.317)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.cubic_foot,
                                                              value=new_value)
                            case UnitsOfMeasurement.cubic_yard.name:
                                new_value = (self.value / 764.6)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.cubic_yard,
                                                              value=new_value)
                            case UnitsOfMeasurement.milliliter.name:
                                new_value = (self.value * 1000)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.milliliter,
                                                              value=new_value)
                            case UnitsOfMeasurement.centiliter.name:
                                new_value = (self.value * 100)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.centiliter,
                                                              value=new_value)
                            case UnitsOfMeasurement.deciliter.name:
                                new_value = (self.value * 10)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.deciliter,
                                                              value=new_value)
                            case UnitsOfMeasurement.hectoliter.name:
                                new_value = (self.value / 100)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.hectoliter,
                                                              value=new_value)
                            case UnitsOfMeasurement.gallon.name:
                                new_value = (self.value / 3.785)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.gallon,
                                                              value=new_value)
                            case _:
                                return self
                    case UnitsOfMeasurement.milliliter.name:
                        match new_unit.name:
                            case UnitsOfMeasurement.cubic_meter.name:
                                new_value = (self.value / 1e+6)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.cubic_meter,
                                                              value=new_value)
                            case UnitsOfMeasurement.cubic_inch.name:
                                new_value = (self.value / 16.387)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.cubic_inch,
                                                              value=new_value)
                            case UnitsOfMeasurement.cubic_foot.name:
                                new_value = (self.value / 28320)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.cubic_foot,
                                                              value=new_value)
                            case UnitsOfMeasurement.cubic_yard.name:
                                new_value = (self.value / 764600)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.cubic_yard,
                                                              value=new_value)
                            case UnitsOfMeasurement.liter.name:
                                new_value = (self.value / 1000)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.liter,
                                                              value=new_value)
                            case UnitsOfMeasurement.centiliter.name:
                                new_value = (self.value / 10)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.centiliter,
                                                              value=new_value)
                            case UnitsOfMeasurement.deciliter.name:
                                new_value = (self.value / 100)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.deciliter,
                                                              value=new_value)
                            case UnitsOfMeasurement.hectoliter.name:
                                new_value = (self.value / 100000)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.hectoliter,
                                                              value=new_value)
                            case UnitsOfMeasurement.gallon.name:
                                new_value = (self.value / 3785)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.gallon,
                                                              value=new_value)
                            case _:
                                return self
                    case UnitsOfMeasurement.centiliter.name:
                        match new_unit.name:
                            case UnitsOfMeasurement.cubic_meter.name:
                                new_value = (self.value / 100000)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.cubic_meter,
                                                              value=new_value)
                            case UnitsOfMeasurement.cubic_inch.name:
                                new_value = (self.value / 1.639)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.cubic_inch,
                                                              value=new_value)
                            case UnitsOfMeasurement.cubic_foot.name:
                                new_value = (self.value / 2832)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.cubic_foot,
                                                              value=new_value)
                            case UnitsOfMeasurement.cubic_yard.name:
                                new_value = (self.value / 76460)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.cubic_yard,
                                                              value=new_value)
                            case UnitsOfMeasurement.liter.name:
                                new_value = (self.value / 100)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.liter,
                                                              value=new_value)
                            case UnitsOfMeasurement.milliliter.name:
                                new_value = (self.value * 10)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.milliliter,
                                                              value=new_value)
                            case UnitsOfMeasurement.deciliter.name:
                                new_value = (self.value / 10)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.deciliter,
                                                              value=new_value)
                            case UnitsOfMeasurement.hectoliter.name:
                                new_value = (self.value / 10000)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.hectoliter,
                                                              value=new_value)
                            case UnitsOfMeasurement.gallon.name:
                                new_value = (self.value / 378.5)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.gallon,
                                                              value=new_value)
                            case _:
                                return self
                    case UnitsOfMeasurement.deciliter.name:
                        match new_unit.name:
                            case UnitsOfMeasurement.cubic_meter.name:
                                new_value = (self.value / 10000)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.cubic_meter,
                                                              value=new_value)
                            case UnitsOfMeasurement.cubic_inch.name:
                                new_value = (self.value * 6.102)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.cubic_inch,
                                                              value=new_value)
                            case UnitsOfMeasurement.cubic_foot.name:
                                new_value = (self.value / 283.2)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.cubic_foot,
                                                              value=new_value)
                            case UnitsOfMeasurement.cubic_yard.name:
                                new_value = (self.value / 7646)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.cubic_yard,
                                                              value=new_value)
                            case UnitsOfMeasurement.liter.name:
                                new_value = (self.value / 10)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.liter,
                                                              value=new_value)
                            case UnitsOfMeasurement.milliliter.name:
                                new_value = (self.value * 100)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.milliliter,
                                                              value=new_value)
                            case UnitsOfMeasurement.centiliter.name:
                                new_value = (self.value * 10)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.centiliter,
                                                              value=new_value)
                            case UnitsOfMeasurement.hectoliter.name:
                                new_value = (self.value / 1000)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.hectoliter,
                                                              value=new_value)
                            case UnitsOfMeasurement.gallon.name:
                                new_value = (self.value / 37.854)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.gallon,
                                                              value=new_value)
                            case _:
                                return self
                    case UnitsOfMeasurement.hectoliter.name:
                        match new_unit.name:
                            case UnitsOfMeasurement.cubic_meter.name:
                                new_value = (self.value / 10)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.cubic_meter,
                                                              value=new_value)
                            case UnitsOfMeasurement.cubic_inch.name:
                                new_value = (self.value * 6102)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.cubic_inch,
                                                              value=new_value)
                            case UnitsOfMeasurement.cubic_foot.name:
                                new_value = (self.value * 3.531)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.cubic_foot,
                                                              value=new_value)
                            case UnitsOfMeasurement.cubic_yard.name:
                                new_value = (self.value / 7.646)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.cubic_yard,
                                                              value=new_value)
                            case UnitsOfMeasurement.liter.name:
                                new_value = (self.value * 100)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.liter,
                                                              value=new_value)
                            case UnitsOfMeasurement.milliliter.name:
                                new_value = (self.value * 100000)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.milliliter,
                                                              value=new_value)
                            case UnitsOfMeasurement.centiliter.name:
                                new_value = (self.value * 10000)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.centiliter,
                                                              value=new_value)
                            case UnitsOfMeasurement.deciliter.name:
                                new_value = (self.value * 1000)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.deciliter,
                                                              value=new_value)
                            case UnitsOfMeasurement.gallon.name:
                                new_value = (self.value * 26.417)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.gallon,
                                                              value=new_value)
                            case _:
                                return self
                    case UnitsOfMeasurement.gallon.name:
                        match new_unit.name:
                            case UnitsOfMeasurement.cubic_meter.name:
                                new_value = (self.value / 264.2)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.cubic_meter,
                                                              value=new_value)
                            case UnitsOfMeasurement.cubic_inch.name:
                                new_value = (self.value * 231)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.cubic_inch,
                                                              value=new_value)
                            case UnitsOfMeasurement.cubic_foot.name:
                                new_value = (self.value / 7.48)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.cubic_foot,
                                                              value=new_value)
                            case UnitsOfMeasurement.cubic_yard.name:
                                new_value = (self.value / 202)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.cubic_yard,
                                                              value=new_value)
                            case UnitsOfMeasurement.liter.name:
                                new_value = (self.value * 3.785)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.liter,
                                                              value=new_value)
                            case UnitsOfMeasurement.milliliter.name:
                                new_value = (self.value * 3785)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.milliliter,
                                                              value=new_value)
                            case UnitsOfMeasurement.centiliter.name:
                                new_value = (self.value * 378.5)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.centiliter,
                                                              value=new_value)
                            case UnitsOfMeasurement.deciliter.name:
                                new_value = (self.value * 37.854)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.deciliter,
                                                              value=new_value)
                            case UnitsOfMeasurement.hectoliter.name:
                                new_value = (self.value / 26.417)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.hectoliter,
                                                              value=new_value)
                            case _:
                                return self
                    case _:
                        return self
            case UnitOf.time.name:
                match self.measure_unit.name:
                    case UnitsOfMeasurement.second.name:
                        match new_unit.name:
                            case UnitsOfMeasurement.minute.name:
                                new_value = (self.value / 60)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.minute,
                                                              value=new_value)
                            case UnitsOfMeasurement.hour.name:
                                new_value = (self.value / 3600)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.hour,
                                                              value=new_value)
                            case UnitsOfMeasurement.day.name:
                                new_value = (self.value / 86400)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.day,
                                                              value=new_value)
                            case UnitsOfMeasurement.year.name:
                                new_value = (self.value / 3.154e+7)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.year,
                                                              value=new_value)
                            case _:
                                return self
                    case UnitsOfMeasurement.minute.name:
                        match new_unit.name:
                            case UnitsOfMeasurement.second.name:
                                new_value = (self.value * 60)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.second,
                                                              value=new_value)
                            case UnitsOfMeasurement.hour.name:
                                new_value = (self.value / 60)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.hour,
                                                              value=new_value)
                            case UnitsOfMeasurement.day.name:
                                new_value = (self.value / 1440)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.day,
                                                              value=new_value)
                            case UnitsOfMeasurement.year.name:
                                new_value = (self.value / 525600)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.year,
                                                              value=new_value)
                            case _:
                                return self
                    case UnitsOfMeasurement.hour.name:
                        match new_unit.name:
                            case UnitsOfMeasurement.second.name:
                                new_value = (self.value * 3600)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.second,
                                                              value=new_value)
                            case UnitsOfMeasurement.minute.name:
                                new_value = (self.value * 60)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.minute,
                                                              value=new_value)
                            case UnitsOfMeasurement.day.name:
                                new_value = (self.value / 24)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.day,
                                                              value=new_value)
                            case UnitsOfMeasurement.year.name:
                                new_value = (self.value / 8760)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.year,
                                                              value=new_value)
                            case _:
                                return self
                    case UnitsOfMeasurement.day.name:
                        match new_unit.name:
                            case UnitsOfMeasurement.second.name:
                                new_value = (self.value * 86400)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.second,
                                                              value=new_value)
                            case UnitsOfMeasurement.minute.name:
                                new_value = (self.value * 1440)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.minute,
                                                              value=new_value)
                            case UnitsOfMeasurement.hour.name:
                                new_value = (self.value * 24)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.hour,
                                                              value=new_value)
                            case UnitsOfMeasurement.year.name:
                                new_value = (self.value / 365)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.year,
                                                              value=new_value)
                            case _:
                                return self
                    case UnitsOfMeasurement.year.name:
                        match new_unit.name:
                            case UnitsOfMeasurement.second.name:
                                new_value = (self.value * 3.154e+7)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.second,
                                                              value=new_value)
                            case UnitsOfMeasurement.minute.name:
                                new_value = (self.value * 525600)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.minute,
                                                              value=new_value)
                            case UnitsOfMeasurement.hour.name:
                                new_value = (self.value * 8760)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.hour,
                                                              value=new_value)
                            case UnitsOfMeasurement.day.name:
                                new_value = (self.value * 365)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.day,
                                                              value=new_value)
                            case _:
                                return self
                    case _:
                        return self
            case UnitOf.speed.name:
                match self.measure_unit.name:
                    case UnitsOfMeasurement.miles_per_hour.name:
                        match new_unit.name:
                            case UnitsOfMeasurement.meters_per_second.name:
                                new_value = (self.value / 2.237)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.meters_per_second,
                                                              value=new_value)
                            case UnitsOfMeasurement.kilometer_per_hour.name:
                                new_value = (self.value * 1.609)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.kilometer_per_hour,
                                                              value=new_value)
                            case _:
                                return self
                    case UnitsOfMeasurement.meters_per_second.name:
                        match new_unit.name:
                            case UnitsOfMeasurement.miles_per_hour.name:
                                new_value = (self.value * 2.237)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.miles_per_hour,
                                                              value=new_value)
                            case UnitsOfMeasurement.kilometer_per_hour.name:
                                new_value = (self.value * 3.6)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.kilometer_per_hour,
                                                              value=new_value)
                            case _:
                                return self
                    case UnitsOfMeasurement.kilometer_per_hour.name:
                        match new_unit.name:
                            case UnitsOfMeasurement.miles_per_hour.name:
                                new_value = (self.value / 1.609)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.miles_per_hour,
                                                              value=new_value)
                            case UnitsOfMeasurement.meters_per_second.name:
                                new_value = (self.value / 3.6)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.meters_per_second,
                                                              value=new_value)
                            case _:
                                return self
                    case _:
                        return self
            case UnitOf.mass.name:
                match self.measure_unit.name:
                    case UnitsOfMeasurement.gram.name:
                        match new_unit.name:
                            case UnitsOfMeasurement.kilogram.name:
                                new_value = (self.value / 1000)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.kilogram,
                                                              value=new_value)
                            case _:
                                return self
                    case UnitsOfMeasurement.kilogram.name:
                        match new_unit.name:
                            case UnitsOfMeasurement.gram.name:
                                new_value = (self.value * 1000)
                                return ConvertibleMeasureUnit(unit=UnitsOfMeasurement.gram,
                                                              value=new_value)
                            case _:
                                return self
                    case _:
                        return self
            case _:
                return self


class MathTools:
    def build_unit(self, unit: UnitsOfMeasurement, value: float | int) -> ConvertibleMeasureUnit:
        """ Build ConvertibleMeasureUnit

        Args:
            unit (UnitsOfMeasurement): Unit type
            value (float | int): Unit value

        Returns:
            ConvertibleMeasureUnit: A new ConvertibleMeasureUnit class instance
        """
        return ConvertibleMeasureUnit(unit, value)

    def convert_measure_units(self, unit: ConvertibleMeasureUnit, new_unit: UnitsOfMeasurement) -> ConvertibleMeasureUnit:
        """ Convert a measure unit in another unit type if possible (shortcut to unit.convert_to())

        Args:
            unit (ConvertibleMeasureUnit): The unit that needs to be converted
            new_unit (UnitsOfMeasurement): The new unit type

        Returns:
            ConvertibleMeasureUnit: Converted unit ConvertibleMeasureUnit class
        """
        return unit.convert_to(new_unit)


class CalculableDate:
    _stored_year: int
    _stored_month: int
    _stored_day: int
    _stored_hour: int
    _stored_minute: int
    _stored_second: int

    def __init__(self, year: int = 1000, month: int = 1, day: int = 1, hour: int = 0,
                 minute: int = 0, second: int = 0) -> None:
        self._stored_year = year
        self._stored_month = month
        self._stored_day = day
        self._stored_hour = hour
        self._stored_minute = minute
        self._stored_second = second

    def _get_year(self):
        strfy_year = str(self._stored_year)
        match len(strfy_year):
            case 0:
                return 1
            case 1:
                return (self._stored_year * 1000)
            case 2:
                return (self._stored_year * 100)
            case 3:
                return (self._stored_year * 10)
            case 4:
                return self._stored_year
            case _ if len(strfy_year) > 4:
                return int(strfy_year[:4])

    def _set_year(self, year: int):
        self._stored_year = year

    def _get_month(self):
        strfy_month = str(self._stored_month)
        safe_month = self._stored_month
        match len(strfy_month):
            case 0:
                safe_month = 1
            case _ if len(strfy_month) > 2:
                safe_month = int(strfy_month[:2])

        if safe_month < 1:
            safe_month = 1
        elif safe_month > 12:
            safe_month = 12

        return safe_month

    def _set_month(self, month: int):
        self._stored_month = month

    def _get_day(self):
        strfy_day = str(self._stored_day)
        safe_day = self._stored_day
        match len(strfy_day):
            case 0:
                safe_day = 1
            case _ if len(strfy_day) > 2:
                safe_day = int(strfy_day[:2])

        if safe_day < 1:
            safe_day = 1
        elif safe_day > 31:
            safe_day = 31

        return safe_day

    def _set_day(self, day: int):
        self._stored_day = day

    def _get_hour(self):
        strfy_hour = str(self._stored_hour)
        safe_hour = self._stored_hour
        match len(strfy_hour):
            case 0:
                safe_hour = 0
            case _ if len(strfy_hour) > 2:
                safe_hour = int(strfy_hour[:2])

        if safe_hour < 0:
            safe_hour = 0
        elif safe_hour > 23:
            safe_hour = 23

        return safe_hour

    def _set_hour(self, hour: int):
        self._stored_hour = hour

    def _get_minute(self):
        strfy_minute = str(self._stored_minute)
        safe_minute = self._stored_minute
        match len(strfy_minute):
            case 0:
                safe_minute = 0
            case _ if len(strfy_minute) > 2:
                safe_minute = int(strfy_minute[:2])

        if safe_minute < 0:
            safe_minute = 0
        elif safe_minute > 59:
            safe_minute = 59

        return safe_minute

    def _set_minute(self, minute: int):
        self._stored_minute = minute

    def _get_second(self):
        strfy_second = str(self._stored_second)
        safe_second = self._stored_second
        match len(strfy_second):
            case 0:
                safe_second = 0
            case _ if len(strfy_second) > 2:
                safe_second = int(strfy_second[:2])

        if safe_second < 0:
            safe_second = 0
        elif safe_second > 59:
            safe_second = 59

        return safe_second

    def _set_second(self, second: int):
        self._stored_second = second

    year = property(_get_year, _set_year)
    month = property(_get_month, _set_month)
    day = property(_get_day, _set_day)
    hour = property(_get_hour, _set_hour)
    minute = property(_get_minute, _set_minute)
    second = property(_get_second, _set_second)

    def as_datetime(self) -> datetime:
        """ Converts data to a datetime class instance

        Returns:
            datetime: datetime with current stored values
        """
        return datetime(year=self.year, month=self.month, day=self.day, hour=self.hour,
                        minute=self.minute, second=self.second)

    def as_timedelta(self) -> timedelta:
        """ Generates a timedelta class with stored values

        Returns:
            timedelta: Stored values in a timedelta instance
        """
        return timedelta(days=self.day, hours=self.hour, minutes=self.minute, seconds=self.second)


class DatetimeTools:
    def build_date(self, year: int = 1000, month: int = 1, day: int = 1, hour: int = 0,
                   minute: int = 0, second: int = 0) -> CalculableDate:
        """ Build a CalculableDate

        Args:
            year (int, optional): Date's year [4 digits integer]. Defaults to 1000.
            month (int, optional): Date's month [1|2 digits integer]. Defaults to 1.
            day (int, optional): Date's day [1-31]. Defaults to 1.
            hour (int, optional): Date's hour [0-23]. Defaults to 0.
            minute (int, optional): Date's minute [0-59]. Defaults to 0.
            second (int, optional): Date's second [0-59]. Defaults to 0.

        Returns:
            CalculableDate: A new CalculableDate class instance
        """
        return CalculableDate(year=year, month=month, day=day, hour=hour, minute=minute, second=second)

    def calc_date_dif(self, data_inicial: CalculableDate, data_final: CalculableDate) -> str:
        """ Calculates the difference between two dates

        Args:
            data_inicial (CalculableDate): Initial date
            data_final (CalculableDate): End date

        Returns:
            str: The dif string. Currently only in PT-BR
        """
        rdelta = relativedelta(data_inicial.as_datetime(), data_final.as_datetime())

        if rdelta.days > 0:
            dia = f'{(rdelta.days)} dias' if (rdelta.days) > 1 else f'{(rdelta.days)} dia'
        elif rdelta.days < 0:
            dia = f'{(rdelta.days)*(-1)} dias' if (rdelta.days) * (-1) > 1 else f'{(rdelta.days)*(-1)} dia'
        else:
            dia = ''

        if rdelta.months > 0:
            mes = f'{(rdelta.months)} meses' if (rdelta.months) > 1 else f'{(rdelta.months)} mês'
        elif rdelta.months < 0:
            mes = f'{(rdelta.months)*(-1)} meses' if (rdelta.months) * (-1) > 1 else f'{(rdelta.months)*(-1)} mês'
        else:
            mes = ''

        if rdelta.years > 0:
            ano = f'{(rdelta.years)} anos' if (rdelta.years) > 1 else f'{(rdelta.years)} ano'
        elif rdelta.years < 0:
            ano = f'{(rdelta.years)*(-1)} anos' if (rdelta.years) * (-1) > 1 else f'{(rdelta.years)*(-1)} ano'
        else:
            ano = ''

        if ano and (mes and dia):
            sequencia = True
            texto = ", "
        elif ano and ((mes and not dia) or (not mes and dia)):
            sequencia = True
            texto = " e "
        else:
            sequencia = False
            texto = ""

        return f'{f"{ano}{texto}" if sequencia else f"{ano}" if ano else ""}{f"{mes} e " if mes and dia else f"{mes}" if mes else ""}{f"{dia}" if dia else ""}'  # NOSONAR:python:S3358

    def calc_date_hour_dif(self, data_inicial: CalculableDate, data_final: CalculableDate) -> str:
        """ Calculates the difference between two dates considering time

        Args:
            data_inicial (CalculableDate): Initial date
            data_final (CalculableDate): Final date

        Returns:
            str: The dif string. Currently only in PT-BR
        """
        rdelta = relativedelta(data_inicial.as_datetime(), data_final.as_datetime())

        if rdelta.days > 0:
            dia = f'{(rdelta.days)} dias' if (rdelta.days) > 1 else f'{(rdelta.days)} dia'
        elif rdelta.days < 0:
            dia = f'{(rdelta.days)*(-1)} dias' if (rdelta.days) * (-1) > 1 else f'{(rdelta.days)*(-1)} dia'
        else:
            dia = ''

        if rdelta.months > 0:
            mes = f'{(rdelta.months)} meses' if (rdelta.months) > 1 else f'{(rdelta.months)} mês'
        elif rdelta.months < 0:
            mes = f'{(rdelta.months)*(-1)} meses' if (rdelta.months) * (-1) > 1 else f'{(rdelta.months)*(-1)} mês'
        else:
            mes = ''

        if rdelta.years > 0:
            ano = f'{(rdelta.years)} anos' if (rdelta.years) > 1 else f'{(rdelta.years)} ano'
        elif rdelta.years < 0:
            ano = f'{(rdelta.years)*(-1)} anos' if (rdelta.years) * (-1) > 1 else f'{(rdelta.years)*(-1)} ano'
        else:
            ano = ''

        if rdelta.hours > 0:
            hora = f'{rdelta.hours} horas' if rdelta.hours > 1 else f'{rdelta.hours} hora'
        elif rdelta.hours < 0:
            hora = f'{rdelta.hours*(-1)} horas' if rdelta.hours * (-1) > 1 else f'{rdelta.hours*(-1)} hora'
        else:
            hora = ''

        if rdelta.minutes > 0:
            minuto = f'{rdelta.minutes} minutos' if rdelta.minutes > 1 else f'{rdelta.minutes} minuto'
        elif rdelta.minutes < 0:
            minuto = f'{rdelta.minutes*(-1)} minutos' if rdelta.minutes * (-1) > 1 else f'{rdelta.minutes*(-1)} minuto'
        else:
            minuto = ''

        if rdelta.seconds > 0:
            segundo = f'{rdelta.seconds} segundos' if rdelta.seconds > 1 else f'{rdelta.seconds} segundo'
        elif rdelta.seconds < 0:
            segundo = f'{rdelta.seconds*(-1)} segundos' if rdelta.seconds * (-1) > 1 else f'{rdelta.seconds*(-1)} segundo'
        else:
            segundo = ''

        existentes = []
        datas = []
        tempos = []
        if ano:
            existentes.append(ano)
            datas.append(ano)
        if mes:
            existentes.append(mes)
            datas.append(mes)
        if dia:
            existentes.append(dia)
            datas.append(dia)
        if hora:
            existentes.append(hora)
            tempos.append(hora)
        if minuto:
            existentes.append(minuto)
            tempos.append(minuto)
        if segundo:
            existentes.append(segundo)
            tempos.append(segundo)

        if len(tempos) == 1:
            tempo_simples = True
            tempo_sequencia = False
            tempo_texto = ' e '
        elif len(tempos) == 2:
            tempo_simples = False
            tempo_sequencia = True
            tempo_texto = ' e '
        elif len(tempos) > 2:
            tempo_simples = False
            tempo_sequencia = True
            tempo_texto = ', '
        else:
            tempo_simples = False
            tempo_sequencia = False
            tempo_texto = ''

        if len(datas) == 1 and tempo_simples:
            data_simples = True
            data_sequencia = False
            data_texto = ' e '
        elif len(datas) == 1 and tempo_sequencia:
            data_simples = True
            data_sequencia = False
            data_texto = ', '
        elif (len(datas) == 2 and tempo_simples) or (len(datas) > 2 and tempo_sequencia) or (len(datas) == 2 and tempo_sequencia) or (len(datas) > 2 and tempo_simples) or (len(datas) > 2 and not tempos):
            data_simples = False
            data_sequencia = True
            data_texto = ', '
        elif len(datas) == 2 and not tempos:
            data_simples = False
            data_sequencia = True
            data_texto = ' e '
        else:
            data_simples = False
            data_sequencia = False
            data_texto = ''

        if len(existentes) > 2:
            sequencia = True
            texto = ", "
        elif len(existentes) == 2:
            sequencia = True
            texto = " e "
        else:
            sequencia = False
            texto = ""

        if len(datas) > 0 and len(tempos) > 0:
            if data_simples and tempo_simples:
                data = f'{f"{ano}{data_texto}" if ano else ""}{f"{mes}{data_texto}" if mes else ""}{f"{dia}{data_texto}" if dia else ""}'
                tempo = f'{f"{hora}" if hora else ""}{f"{minuto}" if minuto else ""}{f"{segundo}" if segundo else ""}'
            elif data_simples and tempo_sequencia:
                data = f'{f"{ano}, " if ano else ""}{f"{mes}, " if mes else ""}{f"{dia}, " if dia else ""}'
                tempo = f'{f"{hora}{tempo_texto}" if hora else ""}{f"{minuto} e " if minuto and segundo else f"{minuto}" if minuto else ""}{f"{segundo}" if segundo else ""}'  # NOSONAR:python:S3358
            elif data_sequencia and tempo_simples:
                data = f'{f"{ano}{data_texto}" if ano else ""}{f"{mes}{data_texto}" if mes and dia else f"{mes} e " if mes else ""}{f"{dia} e " if dia else ""}'  # NOSONAR:python:S3358
                tempo = f'{f"{hora}" if hora else ""}{f"{minuto}" if minuto else ""}{f"{segundo}" if segundo else ""}'
            elif data_sequencia and tempo_sequencia:
                data = f'{f"{ano}{data_texto}" if ano else ""}{f"{mes}{data_texto}" if mes else ""}{f"{dia}{data_texto}" if dia else ""}'
                tempo = f'{f"{hora}{tempo_texto}" if hora else ""}{f"{minuto} e " if minuto and segundo else f"{minuto}" if minuto else ""}{f"{segundo}" if segundo else ""}'  # NOSONAR:python:S3358
            else:
                data = ''
                tempo = ''

        elif len(datas) > 0 and len(tempos) == 0:
            data = f'{f"{ano}{texto}" if ano and sequencia else f"{ano}" if ano else ""}{f"{mes} e " if mes and dia else f"{mes}" if mes else ""}{f"{dia}" if dia else ""}'  # NOSONAR:python:S3358
            tempo = ''

        elif len(datas) == 0 and len(tempos) > 0:
            data = ''
            tempo = f'{f"{hora}{texto}" if hora and sequencia else f"{hora}" if hora else ""}{f"{minuto} e " if minuto and segundo else f"{minuto}" if minuto else ""}{f"{segundo}" if segundo else ""}'  # NOSONAR:python:S3358

        else:
            data = ''
            tempo = ''

        return f'{f"{data}" if data else ""}{f"{tempo}" if tempo else ""}'

    def remove_from_date(self, data_inicial: CalculableDate, data_final: CalculableDate) -> CalculableDate:
        """ Remove a number of days, hours, minutes and seconds from date

        Args:
            data_inicial (CalculableDate): Initial date
            data_final (CalculableDate): Time to remove (Year and Month are not considered)

        Returns:
            CalculableDate: A new CalculableDate with the calculated date
        """
        date = data_inicial.as_datetime() - data_final.as_timedelta()
        return CalculableDate(year=date.year, month=date.month, day=date.day,
                              hour=date.hour, minute=date.minute, second=date.second)

    def add_to_date(self, data_inicial: CalculableDate, data_final: CalculableDate) -> CalculableDate:
        """ Adds a number of days, hours, minutes and seconds to date

        Args:
            data_inicial (CalculableDate): Initial date
            data_final (CalculableDate): Time to add (Year and Month are not considered)

        Returns:
            CalculableDate: A new CalculableDate with the calculated date
        """
        date = data_inicial.as_datetime() + data_final.as_timedelta()
        return CalculableDate(year=date.year, month=date.month, day=date.day,
                              hour=date.hour, minute=date.minute, second=date.second)


class ConversionError(Exception):
    pass
