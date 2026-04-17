### PERMX – Define the Permeability in the X Direction for All the Cells {#kw-PERMX}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

PERMX defines the permeability in the X direction for all the cells in the model via an array. The keyword can be used for all grid types, except for the Radial Grid geometry.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | PERMX | PERMX is an array of real positive numbers assigning the permeability in the X direction to each cell in the model. Repeat counts may be used, for example 20*100.0. | None |
| mD | mD | mD |  |
| Notes: |  |  |  |
: PERMX Keyword Description {#tbl-6-105}
See also the [PERMY](#kw-PERMY) and [PERMZ](#kw-PERMZ) keywords to fully define the permeability for the model.


#### Example


```
--
--       DEFINE GRID BLOCK PERMX DATA FOR ALL CELLS (BASED ON NX x NY x NZ = 300)
--
PERMX
         100*500.0   100*50.0   100*200.0                                       /

```

The above example defines the PERMX to be 500.0, 50.0, and 200.0 for the first, second and third layers in the model for all 300 cells, as defined by the [DIMENS](#kw-DIMENS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.