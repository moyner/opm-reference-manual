### ENDBOX – Define the End of the BOX Defined Grid {#kw-ENDBOX}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword marks the end of a previously defined [BOX](#kw-BOX) sub-grid as defined by a previously entered [BOX](#kw-BOX) keyword. The keyword resets the input grid to be the full grid as defined by the NX, NY, and NZ variables on the [DIMENS](#kw-DIMENS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.

There is no data required for this keyword.


#### Example


```
--
--       DEFINE INPUT BOX FOR EDITING INPUT ARRAYS
--
--       ---------- BOX ---------
--       I1  I2   J1  J2   K1  K2
BOX
         10  10   1   6    1   1                           / DEFINE BOX AREA
--
--
--       DEFINE GRID BLOCK PERMZ DATA FOR THE INPUT BOX
--
PERMZ
         6*0.01                                            /
--
--       DEFINE END OF INPUT BOX EDITING OF INPUT ARRAYS
--
ENDBOX
```


The above example defines a subset of the grid and sets the cells [PERMZ](#kw-PERMZ) values to 0.01 for that area. After which the ENDBOX keyword resets the input to be the full grid.


::: {.callout-note}
It is good practice to always use the ENDBOX keyword to reset the input back to the full grid when all the modifications for a sub-grid have been completed.
:::