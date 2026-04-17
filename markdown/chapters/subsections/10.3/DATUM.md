### DATUM – Define the Datum Depth for the Model {#kw-DATUM}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The DATUM keyword defines the datum depth for the model. This allows for all grid block potentials (depth corrected pressures) to be calculated at a common depth.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | DATUM | DATUM is a single positive value that defines the datum depth for the model. | None |
| feet | m | cm |  |
| Notes: |  |  |  |
: DATUM Keyword Description {#tbl-10-11}
See also the [DATUMR](#kw-DATUMR) and [DATUMRX](#kw-DATUMRX) keywords in the [SOLUTION](#kw-SOLUTION) section that also define the datum depth for the model.


#### Example


```
--       DATUM
--       DEPTH
--       ------
DATUM
         5000.0                                      / DATUM DEPTH FOR REPORTING

```

The above example defines the datum for the model to be 5000.0