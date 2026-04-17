### EXCAVATE – Set the Status of a Grid Block To Active or Excavate {#kw-EXCAVATE}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword, EXCAVATE, sets the status of global and [LGR](#kw-LGR) grid blocks to active or excavate. Excavated grid blocks have all the transmissibilities set to zero thus disabling flow between the surrounding grid blocks.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.