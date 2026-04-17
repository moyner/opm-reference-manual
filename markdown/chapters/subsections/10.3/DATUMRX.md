### DATUMRX – Define Datum Depths for the FIP Allocated Regions {#kw-DATUMRX}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The DATUMRX keyword defines the datum depth for each fluid in-place family region defined by the [FIP](#kw-FIP) keyword. This allows for all grid block potentials (depth corrected pressures) to be calculated at a common depth within a given [FIP](#kw-FIP) region. The [FIP](#kw-FIP) keyword in the [REGIONS](#kw-REGIONS) section allows one to define additional sets of fluid in-place regions to the standard [FIPNUM](#kw-FIPNUM) keyword. For example, one could use [FIPNUM](#kw-FIPNUM) to define the reservoir layers as fluid in-place regions and the [FIP](#kw-FIP) keyword to define the fluid in-place region for fault blocks.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | FIPNAME | A character string of up to five characters in length that defines the [FIP](#kw-FIP) family name for which the datum depth data is being defined. The default value of 1* will set [DATUMR](#kw-DATUMR) to the standard [FIPNUM](#kw-FIPNUM) region numbers. | 1* |
| 2 | [DATUMR](#kw-DATUMR) | [DATUMR](#kw-DATUMR) is a vector of positive values that defines the datum depth for each fluid in-place family region. There must be one entry for each region in the [FIP](#kw-FIP) family name. A maximum of NTFIP values, as declared by the [REGDIMS](#kw-REGDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section, may be entered for each FIPNAME entry. | None |
| feet | m | cm |  |
| Notes: |  |  |  |
: DATUMR Keyword Description {#tbl-10-13}
See also the [FIP](#kw-FIP) keyword in the [REGIONS](#kw-REGIONS) section to define [FIP](#kw-FIP) family regions, and the [DATUM](#kw-DATUM) and [DATUMR](#kw-DATUMR) keywords in the [SOLUTION](#kw-SOLUTION) section that also define the datum depth for the model.


#### Example


```
--
--       FIP       DATUM
--       NAME      DEPTH
DATUMRX
         'FLTBL'   5000.0  5000.0  5000.0  5000.0    / DATUM DEPTH FOR REPORTING
         'LICBL'   5000.0  5050.0                    / DATUM DEPTH FOR REPORTING
/
```


The above example defines the datum depth for two [FIP](#kw-FIP) families, FLTBL and LICBL, with the datum set to a constant 5000.0 psia for FLTBL family and different values for each of the regions in the LICBL family of regions.