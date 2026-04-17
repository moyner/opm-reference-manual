### SHRATE – Activate Log-based Polymer Shearing and Define the Shear Rate Constant


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword activates the logarithm-based polymer shear thinning/thickening option and defines the shear rate constant. This keyword can only be used in conjunction with the PLYSHLOG in the PROPS section


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | SHRATE | A positive real value that defines the shear rate constant. | 4.8 |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |

*Table 8.3.283.1: SHRATE Keyword Description*


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
