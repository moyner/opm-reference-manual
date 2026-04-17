### TBLK – Define Tracer Initial Grid Block Concentrations


| [RUNSPEC](#3.RUNSPEC SECTION\|outline) | [GRID](#4.GRID SECTION\|outline) | [EDIT](#5.EDIT SECTION\|outline) | [PROPS](#6.PROPS SECTION\|outline) | [REGIONS](#7.REGIONS SECTION\|outline) | [SOLUTION](#8.SOLUTION SECTION\|outline) | [SUMMARY](#9.SUMMARY SECTION\|outline) | [SCHEDULE](#10.SCHEDULE SECTION\|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

[TBLK](#__RefHeading___Toc198434_3325167686) keyword defines the initial tracer concentration for all or selected cells in the model, for when the [TRACERS](#__RefHeading___Toc76509_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section has declared the maximum number of tracers for each phase, and the [TRACER](#__RefHeading___Toc121485_83452205) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section has defined the tracer.  This keyword is not in the standard keyword format due to the tracer name being concatenated to the keyword [TBLK](#__RefHeading___Toc198434_3325167686) to fully define the tracer being initialized.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | NAME | A character string of up to eight characters, consisting of [TBLK](#__RefHeading___Toc198434_3325167686) as the first four characters followed by a four letter character string defining the tracer’s name. The fifth character should either be the letter F or the letter S, that indicates the state of the tracer either to be free (F) or in solution (S). For example,  TBLKFIGS (free) or TBLKSIGS (solution). The last three characters of NAME (the effective tracer name) must also match an entry on the [TRACER](#__RefHeading___Toc121485_83452205) keyword’s NAME parameter, in the [PROPS](#__RefHeading___Toc39329_784232322) section. Note it is best to void names beginning with the letters F, S, and T as these names may create naming issues in post-processing software. | None |
| 2 | [TBLK](#__RefHeading___Toc198434_3325167686) | [TBLK](#__RefHeading___Toc198434_3325167686) is an array of real numbers greater than or equal to zero, that are assigned the tracer concentration values for each cell in the model or the current input [BOX](#__RefHeading___Toc42110_3671211675). Repeat counts may be used, for example 200*0.0. The units for the tracer, if required, are set on the [TRACER](#__RefHeading___Toc121485_83452205) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section. This should be the same as the PHASE in the model. | None |
| Liquid: [TBLK](#__RefHeading___Toc198434_3325167686)/stb Gas: [TBLK](#__RefHeading___Toc198434_3325167686)/Mscf | Liquid: [TBLK](#__RefHeading___Toc198434_3325167686)/sm3 Gas: [TBLK](#__RefHeading___Toc198434_3325167686)/sm3 | Liquid: [TBLK](#__RefHeading___Toc198434_3325167686)/scc Gas: [TBLK](#__RefHeading___Toc198434_3325167686)/scc |  |
| Notes: |  |  |  |

*Table 10.57: TBLK Keyword Description*


See also the [TRACERS](#__RefHeading___Toc76509_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section to declared the maximum number of tracers for each phase, the [TRACER](#__RefHeading___Toc121485_83452205) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section to define the tracer, and the [WTRACER](#__RefHeading___Toc97665_3261743917) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section that defines the wells injecting the tracer.


| Note Currently, one cannot initialize tracers using the [EQUALS](#__RefHeading___Toc296597_1576177388) keyword. Instead use the array format, that is the keyword followed by the required number of values, or the [TVDP](#__RefHeading___Toc210170_2884651453) keyword in the [SOLUTION](#__RefHeading___Toc43947_784232322) section to set the initial tracer concentrations as a function of depth. |
| --- |


#### Example

The following [TRACERS](#__RefHeading___Toc76509_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section declares the number of tracers in the model.


```
--
--       NUMBER AND TYPE OF TRACERS
--       NO OIL  NO WAT  NO GAS  NO ENV  DIFF    MAX    MIN    TRACER
--       TRACERS TRACERS TRACERS TRACERS CONTL   NONLIN NONLIN NONLIN
TRACERS
         0       0       1       0      'NODIFF' 1*     1*     1*              /
```


And the [TRACER](#__RefHeading___Toc121485_83452205) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section declares the tracer name and the phase for the tracer.


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


Finally, the [TBLK](#__RefHeading___Toc198434_3325167686) keyword in the [SOLUTION](#__RefHeading___Toc43947_784232322) section sets the initial tracer grid block concentrations in both the free and solution states.


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

Then in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section one can us the [WTRACER](#__RefHeading___Toc97665_3261743917) keyword to define the well injecting the tracer and the tracer concentration being injected,.


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
