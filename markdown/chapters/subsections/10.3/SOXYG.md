### SOXYG – Define The Initial Equilibration Oxygen Concentration For All Grid Blocks


| [RUNSPEC](#3.RUNSPEC SECTION\|outline) | [GRID](#4.GRID SECTION\|outline) | [EDIT](#5.EDIT SECTION\|outline) | [PROPS](#6.PROPS SECTION\|outline) | [REGIONS](#7.REGIONS SECTION\|outline) | [SOLUTION](#8.SOLUTION SECTION\|outline) | [SUMMARY](#9.SUMMARY SECTION\|outline) | [SCHEDULE](#10.SCHEDULE SECTION\|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [SOXYG](#__RefHeading___Toc439460_111689907) keyword defines the initial equilibration oxygen concentration values for all grid cells in the model. The keyword should only be used if the [MICP](#__RefHeading___Toc383375_111689907) model has been activated in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.


| Note This is an OPM Flow specific keyword. |
| --- |


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [SOXYG](#__RefHeading___Toc439460_111689907) | [SOXYG](#__RefHeading___Toc439460_111689907) is an array of real numbers that are greater than or equal to zero assigning the initial equilibration oxygen concentration values to each cell in the model. Repeat counts may be used, for example 20*0.1500 | None |
| lb/stb | kg/sm3 | gm/scc |  |
| Notes: |  |  |  |

*Table 10.50: SOXYG Keyword Description*


See also the [SBIOF](#__RefHeading___Toc394934_111689907), [SCALC](#__RefHeading___Toc406066_111689907), [SMICR](#__RefHeading___Toc428289_111689907), and [SUREA](#__RefHeading___Toc450660_111689907) keywords to define the initial state of the model.


#### Example


```
--
--       DEFINE INITIAL EQUILIBRATION OXYGEN CONCENTRATION FOR ALL CELLS
--       BASED ON NX = 100, NY = 100 AND NZ = 3
--
SOXYG
         1000*0.0000 1000*0.0000 1000*0.1500                                   /

```

The above example defines the initial equilibration oxygen concentration values to be 0.0000 for all the cells in the first and second layers and finally 0.1500 for all the cells in the third layer.
