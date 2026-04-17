### SBIOF – Define The Initial Equilibration Biofilm Volume Fraction For All Grid Blocks


| [RUNSPEC](#3.RUNSPEC SECTION\|outline) | [GRID](#4.GRID SECTION\|outline) | [EDIT](#5.EDIT SECTION\|outline) | [PROPS](#6.PROPS SECTION\|outline) | [REGIONS](#7.REGIONS SECTION\|outline) | [SOLUTION](#8.SOLUTION SECTION\|outline) | [SUMMARY](#9.SUMMARY SECTION\|outline) | [SCHEDULE](#10.SCHEDULE SECTION\|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [SBIOF](#__RefHeading___Toc394934_111689907) keyword defines the initial equilibration biofilm volume fraction for all grid cells in the model. The keyword should only be used if either the [BIOFILM](#REF_HEADING_KEYWORD_BIOFILM) or [MICP](#__RefHeading___Toc383375_111689907) model has been activated in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.


| Note This is an OPM Flow specific keyword. |
| --- |


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [SBIOF](#__RefHeading___Toc394934_111689907) | [SBIOF](#__RefHeading___Toc394934_111689907) is an array of real numbers that are greater than or equal to zero and less than or equal to one assigning the initial equilibration biofilm volume fraction values to each cell in the model. Repeat counts may be used, for example 20*0.0010. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |

*Table 10.41: SBIOF Keyword Description*


For both [BIOFILM](#REF_HEADING_KEYWORD_BIOFILM) and [MICP](#__RefHeading___Toc383375_111689907) models, see also the [SMICR](#__RefHeading___Toc428289_111689907) keyword, and for the [MICP](#__RefHeading___Toc383375_111689907) model, the [SCALC](#__RefHeading___Toc406066_111689907), [SOXYG](#__RefHeading___Toc439460_111689907), and [SUREA](#__RefHeading___Toc450660_111689907) keywords to define the initial state of the model.


#### Example


```
--
--       DEFINE INITIAL EQUILIBRATION BIOFILM VOLUME FRACTION FOR ALL CELLS
--       BASED ON NX = 100, NY = 100 AND NZ = 3
--
SBIOF
         10000*0.0000 10000*0.0000 10000*0.0010                                   /

```

The above example defines the initial equilibration biofilm volume fraction values to be 0.0000 for all the cells in the first and second layers and finally 0.0010 for all the cells in the third layer.
