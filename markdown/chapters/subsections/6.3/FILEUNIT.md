### FILEUNIT – Activate Unit Consistency Checking {#kw-FILEUNIT}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The FILEUNIT keyword defines the units of the data set, and is used to verify that the units in the input deck and any associated include files are consistent. The keyword does not provide for the conversion between different sets of units.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | FILEUNIT | A character string that defines the units of the data set, and should be set to: | None |
| Notes: |  |  |  |
: FILEUNIT Keyword Description {#tbl-6-38}
OPM Flow's behavior is controllable through the "UNIT_SYSTEM_MISMATCH" environment variable. The default behavior if the check fails (i.e., if one of the [INCLUDE](#kw-INCLUDE) files has a unit system different from the main run specification) is to terminate the simulation with an error.


#### Example


```
--
--       ACTIVATE UNIT CONSISTENCY CHECKING
--
FILEUNIT
         FIELD                                                                 /
```


The above example defines the data set units to be [FIELD](#kw-FIELD) units.