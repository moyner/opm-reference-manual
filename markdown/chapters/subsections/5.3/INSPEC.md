### INSPEC – Activate the INSPEC File Option {#kw-INSPEC}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword switches on the writing of the [INIT](#kw-INIT) Index file that specifies and defines the format and data type written to the *.[INIT](#kw-INIT) data file. The *.[INIT](#kw-INIT) data file contains the static data specified in the [GRID](#kw-GRID), [PROPS](#kw-PROPS) and [REGIONS](#kw-REGIONS) sections. For example, the [PORO](#kw-PORO), PERM and [NTG](#kw-NTG) arrays from the [GRID](#kw-GRID) section. The data is used in post-processing software, for example OPM ResInsight, to visualize the static grid properties.

The [INIT](#kw-INIT) Index file can either be written out in formatted form as ASCII i.e. text files, if the [FMTOUT](#kw-FMTOUT) keyword has been activated (*.FINSPEC), or binary format (*.INSPEC) if the [FMTOUT](#kw-FMTOUT) keyword has not been activated. If the [INIT](#kw-INIT) keyword in the [GRID](#kw-GRID) section has been used to switch on the writing of the *. [INIT](#kw-INIT) data file then a binary [INIT](#kw-INIT) Index file is automatically written out as well, unless the [NOINSPEC](#kw-NOINSPEC) keyword in the [RUNSPEC](#kw-RUNSPEC) section has been used to switch off the writing of the [INIT](#kw-INIT) Index file.

Note that most post-processing software require the *.INSPEC file to load the *.[INIT](#kw-INIT) data set, although OPM ResInsight does not require this file to be able to load the *.[INIT](#kw-INIT) data file.

There is no data required for this keyword and there is no terminating “/” for this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


#### Example


```
--
--       ACTIVATE WRITING THE INIT INDEX FILE FOR POST-PROCESSING
--
INSPEC
```


The above example switches on the writing of the [INIT](#kw-INIT) Index file for post-processing in ResInsight.