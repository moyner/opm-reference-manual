### COALNUM – Define the Coal Region Numbers


| [RUNSPEC](#3.RUNSPEC SECTION\|outline) | [GRID](#4.GRID SECTION\|outline) | [EDIT](#5.EDIT SECTION\|outline) | [PROPS](#6.PROPS SECTION\|outline) | [REGIONS](#7.REGIONS SECTION\|outline) | [SOLUTION](#8.SOLUTION SECTION\|outline) | [SUMMARY](#9.SUMMARY SECTION\|outline) | [SCHEDULE](#10.SCHEDULE SECTION\|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [COALNUM](#__RefHeading___Toc82393_1778172979) keyword defines the coal region numbers for each grid block used with the Coal Bed Methane option (“CBM”). OPM Flow does not have a CBM option; however, the keyword is documented here for completeness.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | [COALNUM](#__RefHeading___Toc82393_1778172979) | [COALNUM](#__RefHeading___Toc82393_1778172979) defines an array of positive integers assigning a grid cell to a particular coal region. The maximum number of [COALNUM](#__RefHeading___Toc82393_1778172979) regions is set by the NTCREG variable on [REGDIMS](#__RefHeading___Toc70161_327352552) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. | 1 |
| Notes: |  |  |  |

*Table 6.13: COALNUM Keyword Description*


#### Example

The example below sets three [COALNUM](#__RefHeading___Toc82393_1778172979) regions for a 4 x 5 x 2 model.


```
--
--       DEFINE COALNUM REGIONS FOR ALL CELLS
--
COALNUM
         2  2  1  1  2  2  1  1  1  1  1  1  1  1  1  1  1  1  1  1
         3  3  1  1  3  3  1  1  1  1  1  1  1  1  1  1  1  1  1  1
/
```


The above will no effect in an OPM Flow input deck.
