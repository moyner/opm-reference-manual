### PLYSHEAR – Activate and Define Polymer Shearing Parameters {#kw-PLYSHEAR}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The PLYSHEAR keyword activates and defines the polymer shear thinning-thickening option for when the polymer option has been activated by the [POLYMER](#kw-POLYMER) keyword in the [RUNSPEC](#kw-RUNSPEC) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation
will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | VELOCITY | A columnar vector of real monotonically increasing down the column values that defines the water-polymer flow velocity. The VELOCITY value for the first row in the table should be zero. | None |
| feet/day | m/day | cm/hour |  |
| 2 | VISFAC | A columnar vector of real values that defines a factor that scales the effective water and polymer viscosities for when shear thinning-thickening of the polymer occurs. Normally VISFAC value for the first row in the table should be one. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |
: PLYSHEAR Keyword Description {#tbl-8-106}
#### Example


```
--
--       ACTIVATE AND DEFINE POLYMER SHEARING PARAMETERS
--
PLYSHEAR
--       WAT-POLY    VISCOSITY
--       VELOCITY    FACTOR
--       --------    ---------
             0.0       1.000
             1.0       0.900
             3.0       0.800
             6.0       0.700                               / TABLE NO. 01
--       WAT-POLY    VISCOSITY
--       VELOCITY    FACTOR
--       --------    ---------
             0.0       1.000
             1.0       0.900
             2.0       0.800
             4.0       0.750
             6.0       0.700
             8.0       0.650                               / TABLE NO. 02
```


The above example activates the polymer shear thinning-thickening option and defines two polymer shear thinning-thickening tables, based on the NTPVT variable on the [TABDIMS](#kw-TABDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section being equal to two and NPPVT variable on the same keyword being greater than or equal to six.