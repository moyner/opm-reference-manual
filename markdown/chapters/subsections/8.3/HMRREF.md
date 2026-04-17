### HMRREF – History Match Rock Table Reference Pressure Values {#kw-HMRREF}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The HMRREF keyword defines the history match rock compaction reference pressure gradient values to be used in conjunction with [HMMROCKT](#kw-HMMROCKT), [ROCKTAB](#kw-ROCKTAB) and [ROCKTABH](#kw-ROCKTABH) keywords in the [PROPS](#kw-PROPS) section, for when the History Match Gradient option has been activated by the [HMDIMS](#kw-HMDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. The history match rock compaction data is entered via the [HMMROCKT](#kw-HMMROCKT), [ROCKTAB](#kw-ROCKTAB) and [ROCKTABH](#kw-ROCKTABH) keywords in the [PROPS](#kw-PROPS) section.

See also the [HMDIMS](#kw-HMDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section that specifies the dimensions for the gradient option, including the maximum number of rock gradient parameters that can be used with the History Match Gradient option.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.