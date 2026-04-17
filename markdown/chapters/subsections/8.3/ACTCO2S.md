### ACTCO2S – Activity Model for CO2


| [RUNSPEC](#3.RUNSPEC SECTION\|outline) | [GRID](#4.GRID SECTION\|outline) | [EDIT](#5.EDIT SECTION\|outline) | [PROPS](#6.PROPS SECTION\|outline) | [REGIONS](#7.REGIONS SECTION\|outline) | [SOLUTION](#8.SOLUTION SECTION\|outline) | [SUMMARY](#9.SUMMARY SECTION\|outline) | [SCHEDULE](#10.SCHEDULE SECTION\|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The keyword [ACTCO2S](#REF_HEADING_KEYWORD_ACTCO2S) specifies the activity model for salting-out effects when calculating mutual solubility in the CO2 storage module which is activated by the [CO2STORE](#__RefHeading___Toc387968_1616145207) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | ACTMODEL | A positive integer value selecting the activity model for the salting-out effect. The choices are: | 3 |
| Notes: |  |  |  |

*Table 8.3.1.1: [ACTCO2S](#REF_HEADING_KEYWORD_ACTCO2S) Keyword Description*


#### Example

The following example activates activity model number 1.


```
--
--       ACTIVITY MODEL FOR SALTING-OUT EFFECTS IN CO2
--
ACTCO2S
         1                                                 /

```
