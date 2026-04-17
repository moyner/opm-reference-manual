### PARALLEL – Define Parallel Run Configuration


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The PARALLEL keyword defines the run to use parallel processing and sets the domain decomposition options.  See section 2.2 Running OPM Flow 2023-04 From The Command Line on how to run OPM Flow in parallel mode.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | NPROCS | A positive integer that defines the number of domains or parallel processors to use for this run. | 1 |
| 2 | RTYPE | A character string set to either SERIAL to run the parallel code in serial mode for testing the code, or DISTRIBUTED to full utilize parallel processing. | DISTRIBUTED |
| Notes: |  |  |  |

*Table 5.33: PARALLEL Keyword Description*


OPM Flow uses a different numerical scheme which makes this keyword redundant; hence, OPM Flow  ignores this keyword. It is documented here for completeness.


#### Example


```
--
--       PARALLEL MULTI-CORE OPTIONS
--       NDMAIN     MACHINE TYPE
PARALLEL
           2        DISTRIBUTED                                                /

```

The above example sets the number of domains (or processors) to two and for the simulation to run in parallel mode.  This has no effect in OPM Flow input decks.
