### TRKPF – Define Partitioned Tracer Regions {#kw-TRKPF}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The TRKPF keyword defines the regions associated with the series of partition tracers and the partitioning tables allocated to grid blocks in the model, for when the Partitioned Tracer option has been enabled by the [PARTTRAC](#kw-PARTTRAC) keyword in the [RUNSPEC](#kw-RUNSPEC) section. The maximum number of tracers for each phase are declared on the [TRACERS](#kw-TRACERS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. Unlike other keywords, the TRKPF keyword must be concatenated with the name of the tracer declared by [TRACER](#kw-TRACER) keyword in the [PROPS](#kw-PROPS) section. @tbl-9-26 outlines the format of the TRKPF keyword name.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | TRKPF | A five letter character string equal to TRKPF that is the root keyword name for this data set array. | None |
| 2 | NAME | A three letter character string defining the tracer’s name, as declared by the [TRACER](#kw-TRACER) keyword, which is concatenate to TRKPF to given the full name of the keyword Note it is best to void names beginning with the letters F, S, and T as these names may great naming issues in post-processing software. | None |
: TRKPF Keyword Name Format {#tbl-9-26}
Following the declaration of the full keyword name, TRKPFNAME,  the keyword is followed by the data as outlined below.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | TRKPFREG | TRKPFREG defines an array of positive integers assigning a grid cell to a particular tracer table region. The maximum number of TRKPFREG regions is set by the NTTRVD variable on the [EQLDIMS](#kw-EQLDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. | 1 |
| Notes: |  |  |  |
:  TRKPF Keyword Data Description {#tbl-9-27}
See also the [TRACER](#kw-TRACER) and [TRACERKP](#kw-TRACERKP) keywords in the [PROPS](#kw-PROPS) section and the [TBLK](#kw-TBLK) keyword in the [SOLUTION](#kw-SOLUTION) section.


#### Example

First define one mult-partitioned tracer for the water phase.


```
--
--       DEFINE TRACER NAMES
--
--       TRACER   TRACER   TRACER  PARTITION  NUM   ADSOR
--       NAME     PHASE    VOLUME  PHASE      K(P)  PHASE
--       ------   ------   ------  ---------  ----  -----
TRACER
        'WAT'     'WAT'    1*      MULT       2     ALL    / WAT
/

```

Then for a given a 100 x 100 x 5 grid assign the partitioned tracer regions and K(P) tables, based on two regions.


```
--
--       DEFINE PARTITIONED TRACER REGIONS
--
TRKPFWAT
         1000*1
         1000*1
         1000*2
         1000*2
         1000*2
/
```


The keyword name is derived from the TRKPF keyword, plus the tracer name declared in the [TRACER](#kw-TRACER) keyword, in this case the keyword name is TRKPFWAT.