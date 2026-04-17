### TRACERKP – Standard Partitioned Tracer Option K(P) Tables {#kw-TRACERKP}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword, TRACERKP, defines the Standard Partitioned Tracer option K(P) tables, for when the Partitioned Tracer option has been activate with the [PARTTRAC](#kw-PARTTRAC) keyword in the [RUNSPEC](#kw-RUNSPEC) section.  Standard partitioned tracers only have a “free” and “solution” phases; whereas, Multi-partitioned tracers can partition into any number of phases (oil, water, gas etc.) and have adsorption, decay and diffusion parameters specific to each phase. For the TRACERKP keyword the K(P) tables relate the ratio of the reference phase (the “free” phase) to the solution phase versus pressure. So for example, given a standard partitioned tracer in oil and gas, with the oil phase acting as the reference phase, then TRACERKP would consist of columnar vectors of:


$$
K(P) = \frac{{C}_{\mathit{gas}}}{{C}_{\mathit{oil}}}
$$ {#eq-8-93}

Where:

$K(P)$	= standard partitioned K(P)

$\mathit{Coil}$	= oil concentration

$\mathit{Cgas}$	= gas concentration


See also the [TRACERKM](#kw-TRACERKM) keyword in the [PROPS](#kw-PROPS) section that provides similar data for tmulti-partitioned tracers.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.