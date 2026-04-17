### VFPTABL – Define Production Vertical Flow Performance ALQ Interpolation


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The VFPTABL keyword defines the interpolation method for production Vertical Flow Performance (“VFP”) tables for the Artificial Lift Quantity (“ALQ”).  Production VFP data is entered via the VFPPROD keyword in the SCHEDULE section. By default the simulator interpolates all the variables in the VFP tables using linear interpolation, including the ALQ quantity. However, if the ALQ values represent gas lift, then linear interpolation may not be insufficient, as the gradient change between the tabulated ALQ values may result in sudden changes. This is particularly important in gas lift optimization studies where the available gas lift gas is being allocated to a group of wells in order to maximize oil production rates. To overcome this issue the VFPTABL keyword allows the ALQ values to be interpolated using cubic spline interpolation, and results in a smother transition between the various ALQ entries.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | VFPTABL | VFPTABL is a defined positive integer that specifies the interpolation method to be used with the ALQ quantity in the VFP production tables, and should be set to one of the following: | 1 |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |

*Table 12.76: VFPTABL Keyword Description*


#### Example

The example sets cubic spline interpolation for the ALQ quantity in the VFPPROD tables, with linear interpolation used for all the variables.


```
--
--       ALQ INTERPOLATION OPTION
--
--       OPTION
VFPTABL
         2
/
```
