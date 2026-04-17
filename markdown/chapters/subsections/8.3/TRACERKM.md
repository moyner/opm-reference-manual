### TRACERKM – Multi-Partitioned Tracer Option K(P) Tables {#kw-TRACERKM}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword, TRACERKM, defines the Multi-Partitioned Tracer option K(P) tables, for when the Partitioned Tracer option has been activate with the [PARTTRAC](#kw-PARTTRAC) keyword in the [RUNSPEC](#kw-RUNSPEC) section, and the SOLPHASE parameter on the [TRACER](#kw-TRACER) keyword in the [PROPS](#kw-PROPS) section has been set to MULT to activate the Multi-Partitioned Tracer option.  Multi-partitioned tracers can partition into any number of phases (oil, water, gas etc.) and have adsorption, decay and diffusion parameters specific to each phase; whereas the standard partitioned tracers only have a “free” and “solution” phases. For the TRACERKM keyword the K(P) tables relate the ratio of the reference phase to the other phases versus pressure. So for example, given a multi-partitioned tracer in oil, water and gas, with the water phase acting as the reference phase, then TRACERKM would consist of columnar vectors of:


$$
{K}_{\mathit{ow}}(P) = \frac{{C}_{\mathit{oil}}}{{C}_{\mathit{water}}}\text{    and    }{K}_{\mathit{gw}}(P) = \frac{{C}_{\mathit{gas}}}{{C}_{\mathit{water}}}
$$ {#eq-8-92}

Where:

$\mathit{Kow}(P)$		= multi-partitioned oil-water K(P)

$\mathit{Kgw}(P)$		= multi-partitioned gas-water K(P)

$\mathit{Coil}$		= oil concentration

$\mathit{Cgas}$		= gas concentration

$\mathit{Cwater}$		= water concentration


See also the [TRACERKP](#kw-TRACERKP) keyword in the [PROPS](#kw-PROPS) section that provides similar data for standard partitioned tracers.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.