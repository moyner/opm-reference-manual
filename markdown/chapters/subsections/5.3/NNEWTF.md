### NNEWTF – Activate the Non-Newtonian Fluid Model {#kw-NNEWTF}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword activates the Non-Newtonian Fluid phase and model for when the polymer phase is present in the model, as indicated by the [POLYMER](#kw-POLYMER) keyword in the [RUNSPEC](#kw-RUNSPEC) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | NTHRBL | A positive integer that defines the maximum number of Herschel-Bulkley versus polymer concentration tables to be used with the polymer model, as entered via the [FHERCHBL](#kw-FHERCHBL) keyword in the [PROPS](#kw-PROPS) section. The tables are allocated to different parts of the grid by the [HBNUM](#kw-HBNUM) keyword in the [REGIONS](#kw-REGIONS) section | NTPVT |
| 2 | NLNHBL | A positive integer that defines the maximum number of rows for each table entered by the [FHERCHBL](#kw-FHERCHBL) keyword in the [PROPS](#kw-PROPS) section. | 2 |
| Notes: |  |  |  |
: NNEWTF Keyword Description {#tbl-5-27}
#### Example


```
--
--       MAX     MAX
--       NTHRBL  NLNHBL
NNEWTF
          3      5                                                             /
```


The above example defines maximum number of Herschel-Bulkley tables to be three with a maximum number of rows for each table set to five.