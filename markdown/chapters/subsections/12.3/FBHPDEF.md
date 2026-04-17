### FBHPDEF – Define Well Default BHP Target and Constraints


| [RUNSPEC](#3.RUNSPEC SECTION\|outline) | [GRID](#4.GRID SECTION\|outline) | [EDIT](#5.EDIT SECTION\|outline) | [PROPS](#6.PROPS SECTION\|outline) | [REGIONS](#7.REGIONS SECTION\|outline) | [SOLUTION](#8.SOLUTION SECTION\|outline) | [SUMMARY](#9.SUMMARY SECTION\|outline) | [SCHEDULE](#10.SCHEDULE SECTION\|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword, [FBHPDEF](#__RefHeading___Toc280243_803326780), defines the default well BHP target for production wells and the default BHP constraint for injection wells.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | TARGET_BHP | A real positive value that defines the default well BHP target for production wells. | 1.01325 barsa |
| psia | barsa | atma |  |
| 2 | LIMIT_BHP | A real positive value that defines the default well BHP limit for injection wells. | 6895 barsa |
| psia | barsa | atma |  |
| Notes: |  |  |  |

*Table 12.3.72.1: FBHPDEF Keyword Description*


See also the [WELTARG](#__RefHeading___Toc134888_2055188184) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section that modifies a well’s target and constraint values.


#### Example

The following examples sets the default BHP target for production wells to 1.01325, and the default BHP limit for injection wells to 6895:


```
--
--       DEFAULT BHP TARGET AND CONSTRAINTS
--
FBHPDEF
         1.01325  6895.  /
```
