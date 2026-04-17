### ROCKTHSG – Rock Compaction Hysteresis Tables (Dual Porosity) {#kw-ROCKTHSG}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The ROCKTHSG keyword defines the rock compaction hysteresis attributes to be applied for when the rock compaction option has been invoked by the [ROCKCOMP](#kw-ROCKCOMP) keyword in the [RUNSPEC](#kw-RUNSPEC) section and the either the Dual Permeability or Dual Porosity models are activated by the [DUALPERM](#kw-DUALPERM) and [DUALPORO](#kw-DUALPORO) keywords in the [RUNSPEC](#kw-RUNSPEC) section. ROCKTHSG specifies sigma multipliers versus pressure that are used in the dual porosity rock compaction calculations.  The keyword should only be used if the Rock Compaction Hysteresis option has been activated by either setting the ROCKOPT parameter on the [ROCKCOMP](#kw-ROCKCOMP) keyword to one of the available options.

Each data set consists of columnar vectors of sigma multipliers versus pressure that specify the elastic contraction and expansion and of the reservoir rock. The deflation curve is derived from the first data elements on each elastic curve. If the ROCKOPT parameter on the [ROCKCOMP](#kw-ROCKCOMP) keyword has been set to HYSTER, then the dilation curves are extrapolated to infinite pressure, that is the curves are unbounded. However, if [ROCKCOMP](#kw-ROCKCOMP) is set to BOBERG the last points of each elastic curve are used as the dilation curves.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.