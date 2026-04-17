### TNUM – Define Passive Tracer Concentration Regions {#kw-TNUM}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The TNUM keyword defines the regions associated with the series of tracers associated with a phase (oil, water, or gas) in the model. The maximum number of tracers for each phase are declared on the [TRACER](#kw-TRACER) keyword in the [RUNSPEC](#kw-RUNSPEC) section. Unlike other keywords, the TNUM keyword must be concatenated with the phase and the name of the tracer declared by [TRACER](#kw-TRACER) keyword in the [PROPS](#kw-PROPS) section. @tbl-9-24 outlines the format of the TNUM keyword name.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | TNUM | A four letter character equal to TNUM that is the root keyword name for this data set array. | None |
| 2 | PHASE | A one letter character string that must be equal to F or S, that is concatenated to TNUM. The letter F states that the tracer is for the “free” phase, for example oil or water, as well as gas cap gas (free gas). The letter S signifies that the tracer is a “solution” phase tracer, for example gas dissolved in oil (as activated by the [DISGAS](#kw-DISGAS) keyword in the [RUNSPEC](#kw-RUNSPEC) section), or condensate (vaporized oil) in the gas (as per the [VAPOIL](#kw-VAPOIL) keyword in the [RUNSPEC](#kw-RUNSPEC) section). Note tracers that are defined by the letter S to be in the “solution” phase, must also be initialized by the “free” phase as well. | None |
| 3 | NAME | A three letter character string defining the tracer’s name, which is concatenate to TNUM and PHASE to given the full name of the keyword Note it is best to void names beginning with the letters F, S, and T as these names may great naming issues in post-processing software. | None |
: TNUM Keyword Name Format {#tbl-9-24}
Following the declaration of the full keyword name, TNUMPHASENAME,  the keyword is followed by the data as outlined below.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | TNUMREG | TUNREG defines an array of positive integers assigning a grid cell to a particular tracer table region. The maximum number of TNUMREG regions is set by the NTTRVD variable on the [EQLDIMS](#kw-EQLDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. | 1 |
| Notes: |  |  |  |
: TNUM Keyword Data Description {#tbl-9-25}
See also the [TRACER](#kw-TRACER) keyword in the [PROPS](#kw-PROPS) section and the [TBLK](#kw-TBLK) keyword in the [SOLUTION](#kw-SOLUTION) section.


#### Example

First define four passive tracers one for a free gas, one for dissolved gas, one for oil and one to track the water.


```
--
--       DEFINE TRACER NAMES
--
--       TRACER   TRACER
--       NAME     PHASE
--       ------   ------
TRACER
        'GCG'     'GAS'                                    / GAS CAP GAS
        'DGS'     'GAS'                                    / DISOLVED GAS
        'OIL'     'OIL'                                    / OIL
        'WAT'     'WAT'                                    / WAT
/

```

Given a 100 x 100 x 5 grid with [DISGAS](#kw-DISGAS) activated in the [RUNSPEC](#kw-RUNSPEC) section, then the following TNUM keywords define the various tracer regions given that NTTRVD equals four on the [EQLDIMS](#kw-EQLDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.


```
--
--       DEFINE PASSIVE TRACER CONCENTRATION REGIONS
--
TNUMFGCG
         1000*1
         1000*2
         1000*2
         1000*2
         1000*2
/
TNUMSDGS
         1000*1
         1000*1
         1000*1
         1000*1
         1000*1
/
TNUMFOIL
         1000*3
         1000*3
         1000*3
         1000*3
         1000*3
/
TNUMFWAT
         1000*4
         1000*4
         1000*4
         1000*4
         1000*4
/
```


The keyword name is derived from the TNUM keyword, plus either F or S, plus the tracer name declared in the [TRACER](#kw-TRACER) keyword. For example for the gas cap (free gas) this would be TNUM+F+[GAS](#kw-GAS) to give the TNUMFGAS keyword. And for the dissolved (solution) gas this would be TNUM+S+DGS resulting in the TNUMSDGS keyword.