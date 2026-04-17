### HMMMREGT – History Match Region Transmissibility Gradient Cumulative Multipliers {#kw-HMMMREGT}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The HMMMREGT keyword multiplies the transmissibility between two regions by a constant, for when the History Match Gradient option has been activated by the [HMDIMS](#kw-HMDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. The constant should be a real number. Unlike the [MULTREGT](#kw-MULTREGT) keyword in the [GRID](#kw-GRID) section, the HMMMREGT keyword modifications are cumulative.

Note that the HMMMREGT keyword only declares the two regions and the multiplier between those regions, the transmissibility direction (DIR on the [MULTREGT](#kw-MULTREGT) keyword), type of transmissibility multiplier (TYPE on the [MULTREGT](#kw-MULTREGT) keyword), and the region number array to use (ARRAY on the [MULTREGT](#kw-MULTREGT) keyword), are all taken from the MULTREGY keyword. For example, the region number array can be [FLUXNUM](#kw-FLUXNUM), [MULTNUM](#kw-MULTNUM) or [OPERNUM](#kw-OPERNUM) and these arrays must be defined and be available before the [MULTREGT](#kw-MULTREGT) keyword is read by the simulator, and before the HMMMREGT keyword is used.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.