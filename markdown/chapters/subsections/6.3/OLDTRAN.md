### OLDTRAN – Activate Cartesian Regular Grid Transmissibilities {#kw-OLDTRAN}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword switches on Cartesian Regular Grids geometry transmissibility calculation (or block centered transmissibility calculations), which is the default option for this type of grid. Grids defined by the [DX](#kw-DX), [DY](#kw-DY), and [DZ](#kw-DZ) series of keywords will always invoke this option by default.

For Irregular Corner-Point Grids defined by the [COORD](#kw-COORD) and [ZCORN](#kw-ZCORN) keywords Irregular Corner-Point Grid geometry transmissibility calculations should be activated via the [NEWTRAN](#kw-NEWTRAN) keyword. Again this is automatically invoked if this type of grid is being employed.

There is no data required for this keyword and there is no terminating “/” for this keyword.


#### Example


```
--
--       ACTIVATE CARTESIAN REGULAR GRID TRANSMISSIBILITIES
--
OLDTRAN
```


The above example manually activates Cartesian Regular Grid transmissibility calculations.