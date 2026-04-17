### QDRILL – Define Sequential Drilling Queue Wells {#kw-QDRILL}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The QDRILL keyword places previously defined wells in the Sequential Drilling Queue. Wells in this type of queue will be automatically drilled and completed in the sequence entered in order to satisfy group targets, as defined by the [GCONPROD](#kw-GCONPROD), [GCONINJE](#kw-GCONINJE) and [GCONSALE](#kw-GCONSALE) keywords. or a group’s production potential as per the GDRILLPOT keyword.  All the previously mentioned keywords are in the [SCHEDULE](#kw-SCHEDULE) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.