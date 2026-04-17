### PLYVISC – Define Polymer Viscosity Scaling Factors {#kw-PLYVISC}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

PLYSVISC defines the polymer viscosity scaling factors used to determine the relationship of pure water viscosity with respect to increasing polymer concentration within a grid block. The polymer option must be activated by the [POLYMER](#kw-POLYMER) keyword in the [RUNSPEC](#kw-RUNSPEC) section in order to use this keyword.

The [BRINE](#kw-BRINE) option in the [RUNSPEC](#kw-RUNSPEC) should be deactivated if this keyword is to be used.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | POLCON | A columnar vector of real monotonically increasing down the column values that defines the polymer concentration in the solution surrounding the rock. The first entry should be zero to define a no polymer concentration. | None |
| lb/stb | kg/sm3 | gm/scc |  |
| 2 | VISFAC | A columnar vector of real increasing or equal values that defines a factor that scales the effective viscosity of the solution for the given POLCON entry. Normally VISFAC value for the first row in the table should be one. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |
: PLYVISC Keyword Description {#tbl-8-108}
#### Example


```
--
--       POLYMER VISCOSITY SCALING FACTOR TABLES
--
PLYVISC
--       POLYMER     VISCOSITY
--       POLCON      VISFAC
--       --------    ---------
          0.0000       1.000
          0.0002      10.000
          0.0004      20.000
          0.0008      40.000                               / TABLE NO. 01

--       POLYMER     VISCOSITY
--       POLCON      VISFAC
--       --------    ---------
          0.0000       1.000
          0.0003      10.000
          0.0005      20.000
          0.0007      40.000
          0.0009      45.000
          0.0011      55.000                               / TABLE NO. 02
```


The example defines two polymer viscosity scaling factor tables, based on the NTPVT variable on the [TABDIMS](#kw-TABDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section being equal to two and NPPVT variable on the same keyword being greater than or equal to six.