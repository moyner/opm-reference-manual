### LOAD – Load a SAVE File for a Fast Restart {#kw-LOAD}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The LOAD keyword loads a previously generated [SAVE](#kw-SAVE) file to enable a fast restart. A [SAVE](#kw-SAVE) file contains all the data from a previous run’s [RUNSPEC](#kw-RUNSPEC), [GRID](#kw-GRID), [EDIT](#kw-EDIT), [PROPS](#kw-PROPS) and [REGIONS](#kw-REGIONS) sections, and thus there is no need for the simulator to calculate various parameters, including grid block transmissibilities etc. This allows for the current run to restart quicker than a conventional restart run using the [RESTART](#kw-RESTART) keyword in the [SOLUTION](#kw-SOLUTION) section via a [RESTART](#kw-RESTART) file (*.UNRST or *.FUNRST etc.). The keyword should be the first keyword in the input deck and the [RUNSPEC](#kw-RUNSPEC), [GRID](#kw-GRID), [EDIT](#kw-EDIT), [PROPS](#kw-PROPS) and [REGIONS](#kw-REGIONS) sections should be deleted from the input deck.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.