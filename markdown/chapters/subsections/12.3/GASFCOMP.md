### GASFCOMP – Define Automatic Gas Compressors {#kw-GASFCOMP}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword, GASFCOMP, defines automatic gas compressors for when the Gas Field Operations option has been activated by the [GASFIELD](#kw-GASFIELD) keyword in the [RUNSPEC](#kw-RUNSPEC) section and the Standard Network option has been specified by the [GRUPTREE](#kw-GRUPTREE), GRUPNET and [GNETINJE](#kw-GNETINJE) series of keywords in the [SCHEDULE](#kw-SCHEDULE) section. Automatic gas compressors are automatically switch on for a group if a group’s gas production target cannot be satisfied. In addition, if a group’s gas target is reduced then the automatic compressors are initially switch off to test that the reduced gas rate target can be met without compression, if not, compression is switched back on. Note that all automatic compressors are  “switch on” when calculating a field’s gas deliverability.

There is no data required for this keyword and there is no terminating “/” for this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.