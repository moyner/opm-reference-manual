### SCDPTRAC – Allocate Sea Water Tracer for Scale Deposition {#kw-SCDPTRAC}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The SCDPTRAC keyword is used to allocate an existing passive water tracer defined by the [TRACER](#kw-TRACER) keyword in the [PROPS](#kw-PROPS) section, to represent the sea water flowing into a well connection as a fraction of the total water influx.  The keyword is used together with the [SCDPTAB](#kw-SCDPTAB) keyword in the [SCHEDULE](#kw-SCHEDULE) section to calculated the volume of scale deposited around the well connections.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | NAME | A three letter character string defining the tracer’s name that has previously been defined by the [TRACER](#kw-TRACER) keyword in the [PROPS](#kw-PROPS) section | None |
| Notes: |  |  |  |
: SCDPTRAC Keyword Description {#tbl-12-63}
#### Example

In the [PROPS](#kw-PROPS) section define a tracer in the water phase, for example:


```
--
--       DEFINE TRACER NAMES
--
--       TRACER   TRACER
--       NAME     PHASE
--       ------   ------
TRACER
        'SEA'     'WAT'                                    / SEA WATER TRACER

/
```

Then in the [SCHEDULE](#kw-SCHEDULE) section allocate the previously defined water tracer as a sea water tracer to be used with the scale deposition facility, that is:


```
--
--       ALLOCATE SEA WATER TRACER FOR SCALE DEPOSITION
--
--       TRACER
--       NAME
--       ------
SCDPTRAC
        'SEA'                                              / SEA WATER TRACER

/
```