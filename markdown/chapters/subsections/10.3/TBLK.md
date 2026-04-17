### TBLK – Define Tracer Initial Grid Block Concentrations


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

TBLK keyword defines the initial tracer concentration for all or selected cells in the model, for when the TRACERS keyword in the RUNSPEC section has declared the maximum number of tracers for each phase, and the TRACER keyword in the PROPS section has defined the tracer.  This keyword is not in the standard keyword format due to the tracer name being concatenated to the keyword TBLK to fully define the tracer being initialized.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | NAME | A character string of up to eight characters, consisting of TBLK as the first four characters followed by a four letter character string defining the tracer’s name. The fifth character should either be the letter F or the letter S, that indicates the state of the tracer either to be free (F) or in solution (S). For example,  TBLKFIGS (free) or TBLKSIGS (solution). The last three characters of NAME (the effective tracer name) must also match an entry on the TRACER keyword’s NAME parameter, in the PROPS section. Note it is best to void names beginning with the letters F, S, and T as these names may create naming issues in post-processing software. | None |
| 2 | TBLK | TBLK is an array of real numbers greater than or equal to zero, that are assigned the tracer concentration values for each cell in the model or the current input BOX. Repeat counts may be used, for example 200*0.0. The units for the tracer, if required, are set on the TRACER keyword in the PROPS section. This should be the same as the PHASE in the model. | None |
| Liquid: TBLK/stb Gas: TBLK/Mscf | Liquid: TBLK/sm3 Gas: TBLK/sm3 | Liquid: TBLK/scc Gas: TBLK/scc |  |
| Notes: |  |  |  |

*Table 10.57: TBLK Keyword Description*


See also the TRACERS keyword in the RUNSPEC section to declared the maximum number of tracers for each phase, the TRACER keyword in the PROPS section to define the tracer, and the WTRACER keyword in the SCHEDULE section that defines the wells injecting the tracer.


::: {.callout-note}
Currently, one cannot initialize tracers using the EQUALS keyword. Instead use the array format, that is the keyword followed by the required number of values, or the TVDP keyword in the SOLUTION section to set the initial tracer concentrations as a function of depth.
:::


#### Example

The following TRACERS keyword in the RUNSPEC section declares the number of tracers in the model.


```
--
--       NUMBER AND TYPE OF TRACERS
--       NO OIL  NO WAT  NO GAS  NO ENV  DIFF    MAX    MIN    TRACER
--       TRACERS TRACERS TRACERS TRACERS CONTL   NONLIN NONLIN NONLIN
TRACERS
         0       0       1       0      'NODIFF' 1*     1*     1*              /
```


And the TRACER keyword in the PROPS section declares the tracer name and the phase for the tracer.


```
--
--       DEFINE TRACER NAMES
--
--       TRACER   TRACER
--       NAME     PHASE
--       ------   ------
TRACER
        'IGS'     'GAS'                                    / INJECTED GAS
/
```


Finally, the TBLK keyword in the SOLUTION section sets the initial tracer grid block concentrations in both the free and solution states.


```
--
--       INITIAL TRACER CONCENTRATIONS
--
TBLKFIGS
         1000*0.0                       / TRACER FIGS CONCENTRATIONS

TBLKSIGS
         1000*0.0                       / TRACER SIGS CONCENTRATIONS
```


Here the initial concentrations are set to zero.

Then in the SCHEDULE section one can us the WTRACER keyword to define the well injecting the tracer and the tracer concentration being injected,.


```
--
--       DEFINE CONCENTRATION OF TRACERS IN THE INJECTION STREAMS,
--       INJECTION TRACER CONCENTRATIONS NOT DEFINED USING THE WTRACER
--       KEYWORD ARE ASSUMED TO BE ZERO.
--
-- WELL  NAME    TRACER  TRACER  TRACER
-- NAME  TRACER  VALUE   CUM     GROUP
WTRACER
'GI01'   'IGS'   1.0                                                            /
/
```


In this case, well GI01 is a gas injection well injecting gas with a tracer concentration of 1.0. The example shows how to track dry gas injection in a gas condensate reservoir, although, the example can be used for any type of gas injection.
