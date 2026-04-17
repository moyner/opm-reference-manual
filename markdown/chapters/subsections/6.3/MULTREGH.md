### MULTREGH – Multiply Thermal Conductivities Between Regions


| [RUNSPEC](#3.RUNSPEC SECTION\|outline) | [GRID](#4.GRID SECTION\|outline) | [EDIT](#5.EDIT SECTION\|outline) | [PROPS](#6.PROPS SECTION\|outline) | [REGIONS](#7.REGIONS SECTION\|outline) | [SOLUTION](#8.SOLUTION SECTION\|outline) | [SUMMARY](#9.SUMMARY SECTION\|outline) | [SCHEDULE](#10.SCHEDULE SECTION\|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [MULTREGH](#__RefHeading___Toc246604_1841740821) keyword multiplies the thermal conductivity between two regions by a constant. The region number array can be [FLUXNUM](#__RefHeading___Toc45781_719036256), [MULTNUM](#__RefHeading___Toc61329_2752266063) or [OPERNUM](#__RefHeading___Toc67857_718313858) and these arrays must be defined and be available before the [MULTREGT](#__RefHeading___Toc296621_1576177388) keyword is read by the simulator. The constant should be a real number.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | REGION1 | A positive integer value that defines the from REGION number for which the CONSTANT in (3) should be applied. | None |
| 2 | REGION2 | A positive integer value that defines the to REGION number for which the CONSTANT in (3) should be applied. | None |
| 3 | CONSTANT | A real value to multiply the thermal conductivity between REGION1 and REGION2. | 1 |
| 4 | DIR | A character string that defines the direction to apply the thermal conductivity multiplier between the two regions, should be set to one of the following X, Y, Z, XY, XZ, YZ, or XYZ. | XYZ |
| 5 | TYPE | A character string that defines the type of connections the thermal conductivity multiplier should be applied to, should be one of the following: | [ALL](#__RefHeading___Toc4420_421927891) |
| 6 | REGION ARRAY | The REGION ARRAY to use for applying the CONSTANT in (3) based on the regions REGION1 and REGION2 in (1 and 2).  REGION ARRAY can have the following values: | M |
| Notes: |  |  |  |

*Table 6.77: MULTREGH Keyword Description*


#### Example


```
--
--    MULTIPLY THERMAL CONDUCTIVITIES BETWEEN RESERVOIRS
--
--    REGION   REGION   CONDS   DIREC   NNC    REGION ARRAY
--    FROM     TO       MULT    OPT     OPTS   M / F / O
MULTREGH
      1*       1*       1.05    1*     'ALL'   M           / ALL REGIONS
/

```

The above example multiplies the thermal conductivities between all the [MULTNUM](#__RefHeading___Toc61329_2752266063) regions by 1.05 in all directions and for all connections types.
