### GRAVDRM – Activate Alternative Gravity Drainage and Imbibition for Dual Porosity Model {#kw-GRAVDRM}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword switches on the alternative gravity drainage and imbibition modeling between the matrix and the fracture grid blocks in dual porosity and dual permeability runs.  Either the GRAVDRM or [GRAVDR](#kw-GRAVDR) keywords should be used to activate this standard or alternative type of formulation.

There is no data required for this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | OPTION1 | A defined character string that sets the matrix flow in and out of the matrix block option, and should be set to one of the following: | YES |
| Notes: |  |  |  |
: GRAVDRM Keyword Description {#tbl-5-17}
#### Example


```
--
--       ACTIVATE ALTERNATIVE GRAVITY DRAINAGE AND IMBIBITION MODEL
--
--       MATRIX
--       OPTION
GRAVDRM
         YES                                                                   /

```

The above example switches on the alternative gravity drainage and imbibition option for the run and sets oil flow to be bi-directional, that is oil can flow into and out of the matrix block.