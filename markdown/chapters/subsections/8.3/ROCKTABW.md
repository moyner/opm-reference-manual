### ROCKTABW – Rock Compaction Tables (Water Induced) {#kw-ROCKTABW}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The ROCKTABW keyword defines the rock compaction tables induced by increasing water saturation within a grid cell due to water invasion, for when the rock compaction option has been invoked by the [ROCKCOMP](#kw-ROCKCOMP) keyword in the [RUNSPEC](#kw-RUNSPEC) section. ROCKTABW defines pore volume and transmissibility multipliers versus water saturation that are used in the compaction calculations. The keyword should be used together with the [ROCK](#kw-ROCK), [ROCKTAB](#kw-ROCKTAB) or [ROCKTABH](#kw-ROCKTABH) keywords that specify the pore volume and transmissibility multipliers as functions of pressure. Alternatively the [ROCKWNOD](#kw-ROCKWNOD), [ROCK2D](#kw-ROCK2D) and [ROCK2DTR](#kw-ROCK2DTR) keywords can be used to enter two dimensional tables of the data. All keywords are in the [PROPS](#kw-PROPS) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.