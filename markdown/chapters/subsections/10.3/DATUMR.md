### DATUMR – Define Datum Depths for the FIPNUM Regions {#kw-DATUMR}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The DATUMR keyword defines the datum depth for each fluid in-place region ([FIPNUM](#kw-FIPNUM)) declared in the model. This allows for all grid block potentials (depth corrected pressures) to be calculated at a common depth within a [FIPNUM](#kw-FIPNUM) region.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | DATUMR | DATUMR is a vector of positive values that defines the datum depth for each fluid in-place region. | None |
| feet | m | cm |  |
| Notes: |  |  |  |
: DATUMR Keyword Description {#tbl-10-12}
See also the [DATUM](#kw-DATUM) and [DATUMRX](#kw-DATUMRX) keywords in the [SOLUTION](#kw-SOLUTION) section that also define the datum depth for the model.


#### Example


```
--
--       DATUM
--       DEPTH
--       ------
DATUMR
         4800.0
         4900.0
         5000.0                                      / DATUM DEPTH FOR REPORTING
```


The above example defines the datum depth for three [FIPNUM](#kw-FIPNUM) regions, for when NTFIP has been set equal to three on the [REGDIMS](#kw-REGDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.