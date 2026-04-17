### NOINSPEC – Deactivate Output of the INIT Index File {#kw-NOINSPEC}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The NOINSPEC keyword deactivates the writing out of the [INIT](#kw-INIT) index file (*.[INSPEC](#kw-INSPEC)). The initialization data (or static data) is written out to two files one file contains the data, *.[INIT](#kw-INIT), and the second file contains an index of the data (*.[INSPEC](#kw-INSPEC)) stored in the *.[INIT](#kw-INIT) file. This functionality is redundant as most post-processing software require the *.[INSPEC](#kw-INSPEC) file to load the *.[INIT](#kw-INIT) data set.

Hence, OPM Flow ignores this keyword. It is documented here for completeness.

There is no data required for this keyword and there is no terminating “/” for this keyword.


#### Example


```
--
--       DEACTIVATE OUTPUT OF THE INIT INDEX FILE *.INSPEC
--
NOINSPEC

```

The above example switches off the writing of the [INIT](#kw-INIT) index file (*.[INSPEC](#kw-INSPEC)); however, this has no effect in OPM Flow input decks.