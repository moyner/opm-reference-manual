### ROCKWNOD – Water Saturation Values for Compaction Pressure-Sw Tables {#kw-ROCKWNOD}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [ROCK2D](#kw-ROCK2D) and the [ROCK2DTR](#kw-ROCK2DTR) keywords in the [PROPS](#kw-PROPS) section define rock compressibility pore volume and transmissibility multipliers as a function of pressure and water saturation (“Sw”), for when the rock compaction option has been invoked by the [ROCKCOMP](#kw-ROCKCOMP) keyword in the [RUNSPEC](#kw-RUNSPEC) section. The pressure values are defined on [ROCK2D](#kw-ROCK2D) and the [ROCK2DTR](#kw-ROCK2DTR) keywords together with the multipliers. This keyword ROCKWNOD, defines the water saturations that are used in conjunction with the [ROCK2D](#kw-ROCK2D) and the [ROCK2DTR](#kw-ROCK2DTR) keywords.

This keyword should only be used if compaction option has been enabled.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | [SWAT](#kw-SWAT) | A columnar vector of real monotonically increasing down the column   values that defines the water saturations to be associated with the data on the [ROCK2D](#kw-ROCK2D) and the ROCKTR keywords. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |
: ROCKWNOD Keyword Description {#tbl-8-131}
See also the [OVERBURD](#kw-OVERBURD), [ROCKTAB](#kw-ROCKTAB),  [ROCK2D](#kw-ROCK2D) and [ROCK2DTR](#kw-ROCK2DTR) keywords in the [PROPS](#kw-PROPS) section.


#### Example

The following example defines two ROCKWNOD tables for the pore volume and transmissibility compaction tables, assuming NTROCC is equal to two on the [ROCKCOMP](#kw-ROCKCOMP) keyword and NSSFUN is greater than or equal to four on the [TABDIMS](#kw-TABDIMS) keyword.


```
--
--       WATER SATURATION VALUES FOR COMPACTION PRESSURE-SW TABLES
--
ROCKWNOD
--       COMPACT
--       SWAT
--       ------
          0.000
          0.200
          0.400
          1.000                                           / P-SW SET TABLE NO. 01
--       COMPACT
--       SWAT
--       ------
          0.000
          0.250
          0.750
          1.000                                           / P-SW SET TABLE NO. 02
```


Note that there must be exactly NTROCC tables entered for this keyword, otherwise an error will occur.