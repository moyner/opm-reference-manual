### WSCCLEAN – Well Deposited Scale Adjustment {#kw-WSCCLEAN}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The WSCCLEAN keyword adjusts the amount of scale currently accumulated around a well’s well connections for wells located in the global grid.  For example, if a workover has been performed on a well to remove (or reduce) the deposited scale over the perforations,  then this keyword can be used to implement the effects of the workover. Scale deposits reduce the productivity of well and this relationship is defined in the [SCDPTAB](#kw-SCDPTAB) and [SCDATAB](#kw-SCDATAB) keywords in [SCHEDULE](#kw-SCHEDULE) section. The tables are allocated to a well via the [WSCTAB](#kw-WSCTAB) keyword, which is also in the [SCHEDULE](#kw-SCHEDULE) section. Note that the Scale Deposition option must have been activated by declaring the dimensions of the scaling deposition tables using the [SCDPDIMS](#kw-SCDPDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.

See also the WSSCLENL keyword in the [SCHEDULE](#kw-SCHEDULE) section that performs similar functionality for wells located in a Local Grid Refinement.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.