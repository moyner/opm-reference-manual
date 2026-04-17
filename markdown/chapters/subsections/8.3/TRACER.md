### TRACER – Define Passive Tracer Variables {#kw-TRACER}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The TRACER keyword defines a series of passive tracers that are associated with a phase (oil, water, or gas) in the model. The maximum number of tracers for each phase are declared on the [TRACERS](#kw-TRACERS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | NAME | A three letter character string defining the tracer’s name. NAME is used by the [TNUM](#kw-TNUM) keyword in the [REGIONS](#kw-REGIONS) section, and unlike other keywords, the [TNUM](#kw-TNUM) keyword itself must be concatenated with the phase and the name of the tracer defined by NAME. Similarly for the [TVDP](#kw-TVDP) keyword in the [SOLUTION](#kw-SOLUTION) section, where the [TVDP](#kw-TVDP) keyword itself must be concatenated with the either letter F (for free) or S (for solution), followed by the name of the tracer defined by NAME. Note it is best to void names beginning with the letters F, S, and T as these names may create naming issues in post-processing software. | None |
| 2 | PHASE | A three letter character string that defines the tracer given by NAME to a particular fluid phase. The character should be set to [OIL](#kw-OIL), WAT or [GAS](#kw-GAS). | None |
| 3 | UNITS | The units for the tracer. This can be any unit but should be consistent with values entered via the [TBLK](#kw-TBLK) and [TVDP](#kw-TVDP) keywords in the [SOLUTION](#kw-SOLUTION) section.  The default values are the same as the PHASE in the model. | Same as the phases in the model |
| Liquid: stb Gas: Mscf | Liquid: sm3 Gas: sm3 | Liquid: scc Gas: scc |  |
| 4 | SOLPHASE | A three or four letter character string defining the partitioned tracer’s solution phase. The character string should be set to [OIL](#kw-OIL), WAT, [GAS](#kw-GAS) or MULT. Note that SOLPHASE only needs to be defined if the partitioned tracer option has been activate with the [PARTTRAC](#kw-PARTTRAC) keyword in the [RUNSPEC](#kw-RUNSPEC) section. | None |
| 5 | KPNUM | The table number to be used with the partitioned tracers defined by the [PARTTRAC](#kw-PARTTRAC), [TRACERKP](#kw-TRACERKP) and [TRACERKM](#kw-TRACERKM) keywords. Note that KPNUM only needs to be defined if the partitioned tracer option has been activate with the [PARTTRAC](#kw-PARTTRAC) keyword in the [RUNSPEC](#kw-RUNSPEC) section. | None |
| 6 | ADSPHASE | A three letter character string defining the phase used for the adsorption calculation for when the MULT option has been for SOLPHASE. The character string should be set to [OIL](#kw-OIL), WAT, [GAS](#kw-GAS) or [ALL](#kw-ALL). Note that ADSPHASE only needs to be defined if the partitioned tracer option has been activate with the [PARTTRAC](#kw-PARTTRAC) keyword in the [RUNSPEC](#kw-RUNSPEC) section. | None |
| Notes: |  |  |  |
: TRACER Keyword Description {#tbl-8-194}
See also the [TNUM](#kw-TNUM) keyword in the REGION section that defines tracer regions, and the [TVDP](#kw-TVDP) keyword in the [SOLUTION](#kw-SOLUTION) section that sets the initial tracer saturation for all the cells as a function of depth.


#### Example


```
--
--       DEFINE TRACER NAMES
--
--       TRACER   TRACER
--       NAME     PHASE
--       ------   ------
TRACER
        'IGS'     'GAS'                                    / GAS INJECTOR
        'DGS'     'GAS'                                    / DISOLVED GAS
        'IW1'     'WAT'                                    / WAT INJECTOR 1
        'Iw2'     'WAT'                                    / WAT INJECTOR 2
/

```

The above example defines four passive tracers one for a gas injection well, one for tracking the dissolved gas, and two to track the injected water from two water injection wells.