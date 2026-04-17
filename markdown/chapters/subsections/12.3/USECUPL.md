### USECUPL – Load a Reservoir Coupling File {#kw-USECUPL}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The USECUPL keyword causes the simulator to read a Reservoir Coupling file that has been previously created in a master run using the [DUMPCUPL](#kw-DUMPCUPL) keyword in the [SCHEDULE](#kw-SCHEDULE) section, for when reservoir coupling is invoked by the [GRUPMAST](#kw-GRUPMAST) and [SLAVES](#kw-SLAVES) keywords in the [SCHEDULE](#kw-SCHEDULE) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.