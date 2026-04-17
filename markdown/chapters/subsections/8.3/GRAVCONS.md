### GRAVCONS – Re-Define Gravity Constant


| [RUNSPEC](#3.RUNSPEC SECTION\|outline) | [GRID](#4.GRID SECTION\|outline) | [EDIT](#5.EDIT SECTION\|outline) | [PROPS](#6.PROPS SECTION\|outline) | [REGIONS](#7.REGIONS SECTION\|outline) | [SOLUTION](#8.SOLUTION SECTION\|outline) | [SUMMARY](#9.SUMMARY SECTION\|outline) | [SCHEDULE](#10.SCHEDULE SECTION\|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [GRAVCONS](#__RefHeading___Toc449734_1414963541) keyword re-defines the gravity constant used in various calculations from the default value used by the simulator. Normally this keyword should not be used.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [GRAVCONS](#__RefHeading___Toc449734_1414963541) | [GRAVCONS](#__RefHeading___Toc449734_1414963541) is a positive real number number that defines the gravity constant used in various calculations. | Defined |
| ft2psi/lb 0.00694 | m2bars/kg 0.0000981 | cm2atm/gm 0.000968 |  |
| Notes: |  |  |  |

*Table 8.42: GRAVCONS Keyword Description*


#### Example


```
--
--       RE-DEFINE GRAVITY CONSTANT
--
GRAVITY
         0.0000980665                                      /

```

The above example re-defines the gravity constant to be 0.0000980665 ft2psi/lb from the default value of 0.00694  ft2psi/lb.
