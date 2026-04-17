### FAULTDIM – Define the Number of Fault Segments {#kw-FAULTDIM}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The FAULTDIM keyword defines the maximum number of records (or segments) that can be entered with the [FAULTS](#kw-FAULTS) keyword. The [FAULTS](#kw-FAULTS) keyword defines the faults in the grid than can be used for setting (or re-setting) transmissibility barriers across the fault planes.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | MFSEGS | A positive integer value that defines the maximum number of records (segments) for the [FAULTS](#kw-FAULTS) keyword. | 0 |
| Notes: |  |  |  |
: FAULTDIM Keyword Description {#tbl-5-13}
#### Example


```
--
--       FAULT
--       SEGMS
--
FAULTDIM
         10000                                                                 /
```


The above example defines the maximum number of records that can be entered using the FAULT keyword to be 10,000 segments.