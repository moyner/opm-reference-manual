### MINPV – Set a Minimum Grid Block Pore Volume Threshold for All Cells {#kw-MINPV}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

MINPV defines a minimum threshold pore volume that makes all grid blocks whose pore volume is below this value inactive in the model (inactive cells are not used in OPM Flow calculations). Note this keyword is different to the [MINPVV](#kw-MINPVV) keyword in the [GRID](#kw-GRID) section, that sets a minimum threshold pore volume for individual cells in the model.

Note that the [MINPORV](#kw-MINPORV) keyword is an alias for the MINPV keyword in the [GRID](#kw-GRID) section, and thus provides the same functionality.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | MINPV | MINPV is a real positive number that defines the minimum pore volume for a cell to be active in the model. | Defined |
| rb 1.0e-6 | rm3 1.0e-6 | rcc 1.0e-6 |  |
| Notes: |  |  |  |
: MINPV Keyword Description {#tbl-6-63}
The MINPV, [MINPORV](#kw-MINPORV), and [MINPVV](#kw-MINPVV) keywords only apply their minimum threshold pore volume values to active cells. Thus, cells that have been made inactive via setting their [ACTNUM](#kw-ACTNUM) values to zero, remain inactive, even if their pore volume exceeds the values set by the MINPV, [MINPORV](#kw-MINPORV), and [MINPVV](#kw-MINPVV) keywords.

Secondly, although the MINPV keyword allows one to set a minimum threshold pore volume below the default value, this is not recommended, as cells with small pore volumes can cause significant numerical convergence errors.  Thus, in practice, values greater than the default values are normally applied to eliminate cells that have relatively small pore volumes. In addition, the simulator reports the total pore volume and the number of cells made inactive, as well as the pore volume reduction, when the keyword is invoked; allowing one to run some sensitivities to the minimum pore volume value.

See also the [PINCH](#kw-PINCH) keyword for the treatment of inactive grid cells and pinch-outs.


#### Example


```
--
--       MINIMUM PORE VOLUME FOR ACTIVE CELLS
--
MINPV
         500.0                                                                  /

```

The above example defines 500 rb (or m3) as the minimum pore volume for a cell to be active in the model.