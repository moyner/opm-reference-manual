### TVDP – Define the Initial Equilibration Tracer Saturation versus Depth Functions {#kw-TVDP}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword defines the initial equilibration tracer concentration versus depth functions for each grid cell in the model, for when the Tracer option has been enabled by the [TRACERS](#kw-TRACERS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. The maximum number of tracers for each phase are declared on the [TRACERS](#kw-TRACERS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. Unlike other keywords, the TVDP keyword must be concatenated with the name of the tracer declared by the [TRACER](#kw-TRACER) keyword in the [PROPS](#kw-PROPS) section as outlined in @tbl-10-61.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | TVDP | A four letter character string equal to TVDP that is the root keyword name for this data set function. | None |
| 2 | STATE | A one letter character string defining the tracer’s state, which is concatenated to TVDP to give the partial name of the keyword. STATE should be set to F (“free”) or S (“solution”), with the latter related to a tracer that is dissolved in an associated phase. If the tracer defined by NAME is associated with the [OIL](#kw-OIL), [GAS](#kw-GAS) or [WATER](#kw-WATER) phases then STATE should be set to F.  If the tracer is associated with the [DISGAS](#kw-DISGAS) or [VAPOIL](#kw-VAPOIL) phases then STATE should be set to S. | None |
| 3 | NAME | A three letter character string defining the tracer’s name as defined by the [TRACER](#kw-TRACER) keyword, which is concatenated to TVDP and STATE to given the full name of the keyword.  For example, if the [TRACER](#kw-TRACER) keyword has been used to define a tracer named SEA in the WAT phase, then the full keyword name would be TVDPFSEA.  Whereas, if a tracer was defined as IGS for the [GAS](#kw-GAS) phase then it could be TVDPFIGS and/or TVDPSIGS depending if one was wishing to track the “free” or “solution” gas phase, or both. Note it is best to avoid names beginning with the letters F, S, and T as these names may create naming issues in post-processing software. | None |
: TVDP Keyword Name Format {#tbl-10-61}
Following the declaration of the full keyword name, TVDPSTATENAME,  the keyword is followed by the data as outlined below.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | [DEPTH](#kw-DEPTH) | A columnar vector of real monotonically increasing down the column   values that defines the depth values for the corresponding initial tracer saturations, TVDP | None |
| feet | m | cm |  |
| 2 | TVDPVAL | A columnar vector of real values, greater than or equal to zero, that defines the initial tracer concentration values at the corresponding [DEPTH](#kw-DEPTH). If tracer units have been defined by the UNITS parameter on the [TRACER](#kw-TRACER) keyword in the [PROPS](#kw-PROPS) section, then the units of TVDPVAL are the ratio of UNITS divided by the TVDPVAL units given below. For example, if UNITS was defined as kg, then for metric units TVDPVAL units would be kg/sm3. | None |
| Liquid: stb Gas: Mscf | Liquid: sm3 Gas: sm3 | Liquid: scc Gas: scc |  |
| Notes: |  |  |  |
: TVDP Keyword Description {#tbl-10-62}
See also the [TBLK](#kw-TBLK) keyword in the [SOLUTION](#kw-SOLUTION) section that also sets the initial tracer concentration for each grid block.


#### Example

This example is taken from Norne model, in which there are seven tracers related to the water phase.


```
-- ==============================================================================
--
-- RUNSPEC SECTION
--
-- ==============================================================================
RUNSPEC
--
--       MAX     MAX     RSVD    TVDP    TVDP
--       EQLNUM  DEPTH   NODES   TABLE   NODES
EQLDIMS
         9       1*      20      7       1*                                    /
-- ==============================================================================
--
-- PROPS SECTION
--
-- ==============================================================================
PROPS
--
--       DEFINE TRACER NAMES
--
--       TRACER   TRACER
--       NAME     PHASE
--       ------   ------
TRACER
         SEA      WAT                                      /
         HTO      WAT                                      /
         S36      WAT                                      /
         2FB      WAT                                      /
         4FB      WAT                                      /
         DFB      WAT                                      /
         TFB      WAT                                      /
/

-- ==============================================================================
--
-- SOLUTION SECTION
--
-- ==============================================================================
SOLUTION
--
--       INITIAL EQUILIBRATION TRACER SATURATION VERSUS DEPTH
--
--       DEPTH    TRACER
--                CONCENT
--       ------   --------
TVDPFSEA
         1000.0   0.0
         5000.0   0.0                       / TRACER FSEA CONCENTRATION VS DEPTH

TVDPFHTO
         1000.0   0.0
         5000.0   0.0                       / TRACER FHTO CONCENTRATION VS DEPTH

TVDPFS36
         1000.0   0.0
         5000.0   0.0                       / TRACER FS36 CONCENTRATION VS DEPTH

TVDPF2FB
         1000.0   0.0
         5000.0   0.0                       / TRACER F2FB CONCENTRATION VS DEPTH

TVDPF4FB
         1000.0   0.0
         5000.0   0.0                       / TRACER F4FB CONCENTRATION VS DEPTH

TVDPFDFB
         1000.0   0.0
         5000.0   0.0                       / TRACER FDFB CONCENTRATION VS DEPTH

TVDPFTFB
         1000.0   0.0
         5000.0   0.0                       / TRACER FTFB CONCENTRATION VS DEPTH

```

Here we first define the number of tracers in the model via the [EQLDIMS](#kw-EQLDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section, then the actual tracers themselves in the [PROPS](#kw-PROPS) section using the [TRACER](#kw-TRACER) keyword, and finally the initial tracer concentrations are all set to zero via the TVDP keyword in the [PROPS](#kw-PROPS) section.