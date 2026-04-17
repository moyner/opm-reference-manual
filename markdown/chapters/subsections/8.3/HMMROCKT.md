### HMMROCKT – History Match Rock Compaction Gradient Cumulative Multipliers {#kw-HMMROCKT}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

HMMROCKT defines the rock compaction gradient cumulative multipliers to be applied to the compaction data entered by the ROCTAB or [ROCKTABH](#kw-ROCKTABH) keywords in the PRROPS section,  for when the History Match Gradient option has been activated by the [HMDIMS](#kw-HMDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section

The [ROCKTAB](#kw-ROCKTAB) keyword defines the rock compaction attributes to be applied for when the rock compaction option has been invoked by the [ROCKCOMP](#kw-ROCKCOMP) keyword in the [RUNSPEC](#kw-RUNSPEC) section. [ROCKTAB](#kw-ROCKTAB) defines pore volume and transmissibility multipliers versus pressure that are used in the compaction calculations. If the [RKTRMDIR](#kw-RKTRMDIR) has been activated in the [PROPS](#kw-PROPS) section, then the transmissibility multiplier is directional dependent

This keyword should only be used if compaction option has been enabled.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.