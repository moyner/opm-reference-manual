### TOPS – Define the Depth at the Center of the Top Face for Each Cell {#kw-TOPS}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

TOPS defines the depth of the top face of each cell in the model.

It can only be used with the Cartesian Regular Grid or Radial Grid models.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | TOPS | TOPS is an array of real numbers defining the depth at the top face of each cell in the model. One can either just enter the TOPS for the first layer only based on NX x NY entries and OPM Flow will calculate the remaining TOPS based on either [DZ](#kw-DZ) or [DZV](#kw-DZV). Alternatively NX x NY x NZ TOPS may be entered for each cell in the model. See the [DIMENS](#kw-DIMENS) keyword in the [RUNSPEC](#kw-RUNSPEC) section for the definition of NX, NY and NZ. Repeat counts may be used, for example 10*5201.0. | None |
| feet | m | cm |  |
| Notes: |  |  |  |
: TOPS Keyword Description {#tbl-6-129}
See also the DEPTHS keyword to define the structural depth for the cells.


#### Examples

The example below defines the TOPS of the cells for each cell for NX = 5, NY = 5 and NZ = 3 model, as well as the X and Y direction cells sizes.


```
--
--       DEFINE GRID BLOCK TOPS FOR THE TOP LAYER (NX=5, NY=5, and NZ=3)
--
TOPS
         25*3100  25*3105  25*3110                                             /                                                                                 --
--       DEFINE GRID BLOCK X DIRECTION CELL SIZE (BASED ON NX = 5)
--
DXV
         5*100                                                                 /                                                                                 --
--       DEFINE GRID BLOCK X DIRECTION CELL SIZE (BASED ON NY = 5)
--
DYV
         5*100                                                                 /

```

A second example is shown on the following page.

This example defines the same grid as before but with the TOPS keyword only defining the top layer and [DZV](#kw-DZV) keyword defining the cells thickness.


```
--
--       DEFINE GRID BLOCK TOPS FOR THE TOP LAYER (NX = 5, NY = 5, NZ = 3)
--
TOPS
         25*3100                                                               /
--
--       DEFINE GRID BLOCK Z DIRECTION CELL SIZE (BASED ON NZ = 3)
--
DZV
         3*5.0                                                                 /
--
--       DEFINE GRID BLOCK X DIRECTION CELL SIZE (BASED ON NX = 5)
--
DXV
         5*100                                                                 /                                                                                 --
--       DEFINE GRID BLOCK Y DIRECTION CELL SIZE (BASED ON NY = 5)
--
DYV
         5*100                                                                 /
```