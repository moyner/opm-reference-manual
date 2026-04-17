### COMPTRAJ – Define Well Trajectory Connections to the Grid


| [RUNSPEC](#3.RUNSPEC SECTION\|outline) | [GRID](#4.GRID SECTION\|outline) | [EDIT](#5.EDIT SECTION\|outline) | [PROPS](#6.PROPS SECTION\|outline) | [REGIONS](#7.REGIONS SECTION\|outline) | [SOLUTION](#8.SOLUTION SECTION\|outline) | [SUMMARY](#9.SUMMARY SECTION\|outline) | [SCHEDULE](#10.SCHEDULE SECTION\|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [COMPTRAJ](#__RefHeading___Toc97651_32617439171) keyword defines how a well that has been declared as a trajectory well, using the [WELTRAJ](#__RefHeading___Toc268463_13666227011) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, is connected to the reservoir model by defining or modifying existing well perforation depths. The keyword can only be used for wells defined by the [WELTRAJ](#__RefHeading___Toc268463_13666227011) keyword, and [WELTRAJ](#__RefHeading___Toc268463_13666227011) defined wells must use the [COMPTRAJ](#__RefHeading___Toc97651_32617439171) keyword to define the connections to the grid, that is one cannot use [COMPDAT](#__RefHeading___Toc97651_3261743917) for these type of wells.


| Note This is an OPM Flow specific keyword and will therefore cause an error in the commercial simulator. |
| --- |


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well connection data are being defined. Note that the well name (WELNAME) must have been declared previously using the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, otherwise an error may occur. | None |
| 2 | IBRANCH | A positive integer greater than or equal to one and less than or equal to MXBRAN on [WSEGDIMS](#__RefHeading___Toc104259_3115110868) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section that defines the branch number of a segment. All segments on the main stem must have IBRANCH set to one and lateral branches should have values between two and MXSEGS on the  [WSEGDIMS](#__RefHeading___Toc104259_3115110868) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. Only the default value of one is currently supported, that is only the main branch of a multi-segment well is supported,  or a single trajectory for a conventional well. | 1 |
| 3 ‍ | TOP | A real positive value that defines the depth of the top of the perforation interval, and should be less than the value entered for the BOT parameter (the bottom perforation depth). | None |
| feet | m | cm |  |
| 4 ‍ | BOT | A real positive value that defines the depth of the base of the perforation interval, and should be greater than the value entered for the TOP parameter (the top perforation interval). | None |
| feet | m | cm |  |
| 5 | REF | REF is a defined character string that defines the reference depth type for TOP and BOT, and should be set to either: Only measured depth is currently supported, that is MD. | MD |
| 6 | ICOMP | An integer greater than or equal to one and less than or equal to MXCONS as defined on the [WELLDIMS](#__RefHeading___Toc82886_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, that defines the completion number of the currently defined perforation interval (connection interval). If defaulted with 1*, then ICOMP is set equal to one. | 1 |
| 7 | STATUS | A defined character string of length four that defines the connections’ operational status within the perforation interval, STATUS should be set to one of the following character strings: | OPEN |
| 8 | [SATNUM](#__RefHeading___Toc71136_2752266063) | An integer greater than or equal to zero and less than NTSFUN as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979), that defines the saturation table number to be used for flow between the reservoir grid block and the well connections. If [SATNUM](#__RefHeading___Toc71136_2752266063) is set to zero or defaulted with 1* then: | 0 |
| 9 | CONFACT | A real value greater than or equal to zero that defines the transmissibility connection factor between the well bore and the reservoir grid block. If set to zero or defaulted with 1* then items (10) through (13) are used to calculate CONFACT. | Defined |
| cP.rb/day/psia 0 | cP.rm3/day/bars 0 | cP.rcc/hr/atm 0 |  |
| 10 | DW | A real positive value that defines the well bore diameter of the connections for the well. DW is used in calculating a well’s productivity or injectivity index; however the value will be ignored in calculating the connections CONFACT value if CONFAC has been directly entered. | None |
| feet | m | cm |  |
| 11 | KH | A real value that defines the effective KH (permeability x length) for the connections within the perforation interval. If less than or equal to zero, or defaulted by 1*, then KH is calculated from the connected grid blocks. KH is ignored if CONFACT has been directly entered. | Calculated from connected grid blocks |
| mD.ft | mD.m | mD.cm |  |
| 12 | SKIN | A real value that defines the connections dimensionless skin factor. SKIN is used in calculating a well’s productivity or injectivity index; however, the value will be ignored in calculating the connections CONFACT value if CONFACT has been directly entered. | 0.0 |
| dimensionless | dimensionless | dimensionless |  |
| 13 | DFACT | A real value that defines the non-Darcy D factor coefficient for gas wells. This value should be defaulted with 1* and the non-Darcy D factor coefficient for gas wells defined via the [WDFAC](#__RefHeading___Toc442057_2026549522) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. Currently this option is not supported by OPM Flow. | 1* |
| day/Mscf | day/m3 | hour/sc |  |
| Notes: |  |  |  |

*Table 12.18: COMPTRAJ Keyword Description*


Using the [WELTRAJ](#__RefHeading___Toc268463_13666227011) and [COMPTRAJ](#__RefHeading___Toc97651_32617439171) keywords to define wells and how they are connected to grid, offers several advantages compared to the conventional approach based on the (I, J, K) co-ordinates of the grid. The approach allows for the wells to be independent of the grid, which is particularly useful when running ensemble cases, as the well connections are no longer required to be re-calculated for each ensemble case. In addition, quality control of the model is improved by using consistent perforation data in both the static and dynamic models.


| Note The term well connection is used to describe individual connections from the wellbore to the reservoir grid, as opposed to well completions. A well completion is used to describe a set of connections, for example, a well may consist of several completions with each completion consisting of multiple connections. For wells defined using the [WELTRAJ](#__RefHeading___Toc268463_13666227011) and [COMPTRAJ](#__RefHeading___Toc97651_32617439171) keywords, the [WELTRAJ](#__RefHeading___Toc268463_13666227011) keyword defines the trajectory of the well within the model, and the [COMPTRAJ](#__RefHeading___Toc97651_32617439171) defines the perforation intervals in the well.  A perforation interval will automatically generate various well connections to the grid, and in addition multiple perforation intervals may be grouped into a completion. |
| --- |


#### Example

The following example defines two trajectory wells oil wells, OP01 and OP02, using the [WELTRAJ](#__RefHeading___Toc268463_13666227011) keyword, together with their perforations using the [COMPTRAJ](#__RefHeading___Toc97651_32617439171) keyword.


```
--
--       WELL SPECIFICATION DATA
--
-- WELL  GROUP     LOCATION  BHP    PHASE  DRAIN  INFLOW  OPEN  CROSS  PVT
-- NAME  NAME        I    J  DEPTH  FLUID  AREA   EQUANS  SHUT  FLOW   TABLE
WELSPECS
OP01     PLATFORM   1*   1*   1*     OIL    1*     STD    SHUT   NO     1*     /
OP02     PLATFORM   1*   1*   1*     OIL    1*     STD    SHUT   NO     1*     /
/
--
--       WELL TRAJECTORY DATA
--
-- WELL   BRAN  XCORD         YCORD         TVDSS         MD
-- NAME   NO                                DEPTH         DEPTH
-- -----  ----  ------------  ------------  ------------  ------------
WELTRAJ
OP01      1*    2.805445e+06  3.602948e+06  -100.000000   0.0         /
OP01      1*    2.805445e+06  3.602948e+06  877.0000000   977.0       /
OP01      1*    2.805445e+06  3.602948e+06  957.9950240   1058.0      /
OP01      1*    2.805444e+06  3.602946e+06  1051.976081   1152.0      /
…………………...                                                            /
OP02      1*    2.810828e+06  3.604507e+06  9371.792711   11418.0     /
OP02      1*    2.810885e+06  3.604525e+06  9443.657000   11511.0     /
OP02      1*    2.810952e+06  3.604546e+06  9531.966162   11624.0     /
OP02      1*    2.810973e+06  3.604553e+06  9560.411742   11660.0     /
/
--
--
--       WELL TRAJECTORY CONNECTION DATA
--
-- WELL  BRAN  -- PERFORATION --  COMPL OPEN  SAT CONN  WELL   KH    SKIN  D
-- NAME  NO.    TOP    BOT   REF  NO.   SHUT  TAB FACT  DIA    FACT  FACT  FACT
COMPTRAJ
OP01     1*     8230   8244  MD    1    SHUT  1*  1*    0.708  1*    0.0   1*  /
OP01     1*     8352   8380  MD    1    SHUT  1*  1*    0.708  1*    0.0   1*  /
OP01     1*     9070   9100  MD    1    SHUT  1*  1*    0.708  1*    0.0   1*  /
OP01     1*     9220   9250  MD    2    SHUT  1*  1*    0.708  1*    0.0   1*  /
OP01     1*     9266   9280  MD    2    SHUT  1*  1*    0.708  1*    0.0   1*  /
OP01     1*     9693   9703  MD    3    SHUT  1*  1*    0.708  1*    0.0   1*  /
OP01     1*     9940   9974  MD    3    SHUT  1*  1*    0.708  1*    0.0   1*  /
OP02     1*     9979   9985  TVD   1*   SHUT  1*  1*    0.708  1*    0.0   1*  /
OP02     1*    10173  10183  TVD   1*   SHUT  1*  1*    0.708  1*    0.0   1*  /
OP02     1*    10190  10204  TVD   1*   SHUT  1*  1*    0.708  1*    0.0   1*  /
OP02     1*    10327  10333  TVD   1*   SHUT  1*  1*    0.708  1*    0.0   1*  /
OP02     1*    10339  10345  TVD   1*   SHUT  1*  1*    0.708  1*    0.0   1*  /
OP02     1*    11528  11538  TVD   1*   SHUT  1*  1*    0.708  1*    0.0   1*  /
/

```

Well OP01 has eight perforation intervals, with the intervals one to three grouped into one completion, perforation intervals four to five grouped into completion number two, and finally the bottom three perforations are grouped into completion number three. In contrast, OP02 has six perforated intervals with their completion interval defaulted to one.
