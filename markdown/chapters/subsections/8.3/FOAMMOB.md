### FOAMMOB – Define Foam Gas Mobility versus Foam Concentration Tables


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The FOAMMOB keyword defines the reduction in gas mobility as a function of the foam concentration within a grid block. The Foam option must be activated by the FOAM keyword in the RUNSPEC section in order to use this keyword.   In addition,  this keyword must be supplied if the foam model is activated.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | FOAMCON | A columnar vector of real monotonically increasing down the column values that defines the foam concentration for the corresponding gas mobility reduction factor (FOAMRATI). The first entry should be zero to define a no foam concentration data set. Units are dependent on the transport phase specified via the FOAMOPT1 variable on the FOAMOPTS keyword in the PROPS section. FOAMOPT1 should be set to either GAS or WATER. | None |
| Gas: lb/Mscf Water: lb/stb | Gas: kg/sm3 Water: kg/sm3 | Gas: gm/scc Water: gm/scc |  |
| 2 | FOAMRATI | A columnar vector of real decreasing down the column values that defines  the corresponding gas mobility reduction factor for a given FOAMCON. The first table data set entry should be one to define a no foam concentration data set. Each FOAMCON/FOAMRATI data set should be terminated by a “/” | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |

*Table 8.36: FOAMMOB Keyword Description*


See also the FOAM keyword in the RUNSPEC section, the FOAMADS, FOAMOPTS and FOAMROCK keywords in the PROPS section.


#### Example


```
--
--       FOAM GAS MOBILITY VERSUS FOAM CONCENTRATION TABLES
--
FOAMMOB
--       FOAM       FOAM
--       FOAMCON    FOAMRATI
--       -------    --------
           0.000     1.00000
           0.005     0.50000
           0.010     0.20000
           0.015     0.10000
           0.020     0.07500
           0.025     0.07000
           0.030     0.06500
           0.035     0.06500                               / TABLE NO. 01
--       FOAM       FOAM
--       FOAMCON    FOAMRATI
--       -------    --------
           0.000     1.00000
           0.010     0.50000
           0.015     0.25000
           0.020     0.07500
           0.025     0.07000
           0.030     0.07000                               / TABLE NO. 02
```


Given NTPVT equals two and NPPVT is greater and or equal to eight on the TABDIMS keyword in the RUNSPEC section, the example defines the foam gas mobility versus foam concentration tables for two tables.

There is no terminating “/” for this keyword.
