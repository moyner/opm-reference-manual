### DISPERC – Define the Mechanical Dispersivity for All Cells


| [RUNSPEC](#3.RUNSPEC SECTION\|outline) | [GRID](#4.GRID SECTION\|outline) | [EDIT](#5.EDIT SECTION\|outline) | [PROPS](#6.PROPS SECTION\|outline) | [REGIONS](#7.REGIONS SECTION\|outline) | [SOLUTION](#8.SOLUTION SECTION\|outline) | [SUMMARY](#9.SUMMARY SECTION\|outline) | [SCHEDULE](#10.SCHEDULE SECTION\|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [DISPERC](#REF_HEADING_KEYWORD_DISPERC_6_3) keyword defines the mechanical dispersivity for all cells in the model via an array.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
|  | Metric | Laboratory |  |
| 1 | [DISPERC](#REF_HEADING_KEYWORD_DISPERC_6_3) | [DISPERC](#REF_HEADING_KEYWORD_DISPERC_6_3) is an array of real positive values that defines the mechanical dispersivity for each cell in the model. Repeat counts may be used, for example 20*1.0. | None |
| feet | m | cm |  |
| Notes: |  |  |  |

*Table 6.3.39.1: [DISPERC](#REF_HEADING_KEYWORD_DISPERC_6_3) Keyword Description*


| Note The option has been tested in combination with the [CO2STORE](#__RefHeading___Toc387968_1616145207), [H2STORE](#REF_HEADING_KEYWORD_H2STORE), [BIOFILM](#REF_HEADING_KEYWORD_BIOFILM), or [MICP](#__RefHeading___Toc383375_111689907) keywords, but not for the general case at this point. |
| --- |


See also the [CO2STORE](#__RefHeading___Toc387968_1616145207) and [H2STORE](#REF_HEADING_KEYWORD_H2STORE) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section that active OPM Flow’s CO2 and H2 storage models respectively.


#### Example

The example sets the mechanical dispersivity for all cells in the model to 1.0.


```
--
--       SET MECHANICAL DISPERSIVITY FOR ALL CELLS (OPM FLOW KEYWORD)
--
DISPERC
         1000*1.0                                           /
```
