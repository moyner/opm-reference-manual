### TIGHTENP – Tighten and Relax Numerical Controls Individually {#kw-TIGHTENP}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The TIGHTENP keyword is similar to the [TIGHTEN](#kw-TIGHTEN) keyword in the [SCHEDULE](#kw-SCHEDULE) section, in that it tightens up or slackens the numerical controls for the linear, non-linear and material balance convergence targets and also tightens or relaxes the maximum values for the aforementioned parameters. However, TIGHTENP allows for greater flexibility as there are four parameters on this keyword, as opposed to just one on the [TIGHTEN](#kw-TIGHTEN) keyword, that can be used to modify the numerical controls. The keyword should be used with caution as it may result in significantly increasing the run times.


Note that any subsequent use of the [TUNING](#kw-TUNING) keyword in the [SCHEDULE](#kw-SCHEDULE) section will result in resetting the numerical controls. See also the [TIGHTEN](#kw-TIGHTEN) keyword in the [SCHEDULE](#kw-SCHEDULE) section that has more limited flexibility in modifying the numerical controls.


This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.