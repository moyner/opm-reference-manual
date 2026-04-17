### MULTOUTS – Activate Non-Unified Multiple Summary Output File Option {#kw-MULTOUTS}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword switches on the Multiple Output Files option for [SUMMARY](#kw-SUMMARY) files only,  and overwrites the [UNIFOUT](#kw-UNIFOUT) keyword in the [RUNSPEC](#kw-RUNSPEC) section that activates the Unified Output Files option for all output files.

There is no data required for this keyword and there is no terminating “/” for this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

See also OPM FLOW OUTPUT FILE FORMATS for a more detailed description of the various file types (ASCII or binary) and file structure formats (unified or non-unified formats).


#### Example


```
--
--       ACTIVATE MULTIPLE OUTPUT SUMMARY FILES ONLY OPTION
--
MULTOUTS
```


The above example switches on the multiple output file option.