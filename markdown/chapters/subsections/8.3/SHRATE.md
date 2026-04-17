### SHRATE – Activate Log-based Polymer Shearing and Define the Shear Rate Constant {#kw-SHRATE}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword activates the logarithm-based polymer shear thinning/thickening option and defines the shear rate constant. This keyword can only be used in conjunction with the [PLYSHLOG](#kw-PLYSHLOG) in the [PROPS](#kw-PROPS) section


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | SHRATE | A positive real value that defines the shear rate constant. | 4.8 |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |
: SHRATE Keyword Description {#tbl-8-3-283-1}
#### Example

The following example activates the logarithm-based polymer shear thinning/thickening option and defines the shear rate constants for a run with two PVT regions.


```
--
--       ACTIVATE LOG-BASED POLYMER SHEAR THINNING-THICKENING OPTION
--       AND DEFINE THE SHEAR RATE CONSTANT
--
SHRATE
--       SHEAR RATE
--       CONSTANT
         4.8      /
         4.8      /

```