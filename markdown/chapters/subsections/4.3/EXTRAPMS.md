### EXTRAPMS – Activate Extrapolation Warning Messages {#kw-EXTRAPMS}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The EXTRAPMS keyword activates extrapolation warning messages for when OPM Flow extrapolates the  PVT or VFP tables. Frequent extrapolation warning messages should be investigated and resolved as this would indicate possible incorrect data and may result in the simulator extrapolating to unrealistic values.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | EXTRAP | Defines a single integer that activates the extrapolation warning message options for PVT and VFP tables. EXTRAP can have the following values: | 0 |
| Notes: |  |  |  |
: EXTRAPMS Keyword Description {#tbl-4-2}
This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.


#### Example


```
--
--       ACTIVATE EXTRAPOLATION MESSAGES
--
EXTRAPMS
         2                                                                    /
```


The above example activates the default the VFP table extrapolation warnings option.