### HMMULTFT – History Match Fault Transmissibility Gradient Cumulative Multipliers {#kw-HMMULTFT}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

HMMULTFT defines the history match fault transmissibility gradient cumulative multipliers to be applied to the fault transmissibilities for faults declared by the FAULT keyword in the [GRID](#kw-GRID) section, for when the History Match Gradient option has been activated by the [HMDIMS](#kw-HMDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.  The keyword allows for the re-scaling of the existing fault transmissibilities calculated by OPM Flow, or if the [MULTFLT](#kw-MULTFLT) keyword has been entered, then HMMULTFT is applied to the existing [MULTFLT](#kw-MULTFLT) multipliers.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.