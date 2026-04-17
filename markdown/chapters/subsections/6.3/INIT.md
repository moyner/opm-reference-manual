### INIT – Activate the INIT File Option {#kw-INIT}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword switches on the writing of the INIT file that contains the static data specified in the [GRID](#kw-GRID), [PROPS](#kw-PROPS) and [REGIONS](#kw-REGIONS) sections. For example, the [PORO](#kw-PORO), PERM and [NTG](#kw-NTG) arrays from the [GRID](#kw-GRID) section. The data is used in post-processing software, for example OPM ResInsight, to visualize the static grid properties.

The INIT file can either be written out in formatted form as ASCII i.e. text files, if the [FMTOUT](#kw-FMTOUT) keyword has been activated, or binary format if the [FMTOUT](#kw-FMTOUT) keyword has not been activated. Normally, this option is always activated by the user and when activated the binary form of the file is used.

There is no data required for this keyword and there is no terminating “/” for this keyword.


#### Example


```
--
--       ACTIVATE WRITING THE INIT FILE FOR POST-PROCESSING
INIT
```


The above example switches on the writing of the INIT file for post-processing in ResInsight.