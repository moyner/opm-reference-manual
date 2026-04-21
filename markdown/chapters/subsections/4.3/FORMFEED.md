### FORMFEED – Defined the Print File Form-Feed Character


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The FORMFEED keyword defines the form-feed character, or carriage control character, for the output print  (*.PRT) run summary (*.RSM) files. The keyword should be place at the very top of the input file.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | FORMFEED | Defines a single integer that defines the carriage control character activates, and should be set to: | 0 |
| Notes: |  |  |  |

*Table 4.3: FORMFEED Keyword Description*


This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


#### Example


```
--
--       ACTIVATE EXTRAPOLATION MESSAGES
--
FORMFEED
         3                                                                      /
```


The above example sets the carriage return character to no form-feed character.
