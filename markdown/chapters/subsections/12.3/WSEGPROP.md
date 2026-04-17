### WSEGPROP – Modify Multi-Segment Wells and Their Segment Structure {#kw-WSEGPROP}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The WSEGPROP keyword allows for the editing of exiting multi-segment wells created by [WELSEGS](#kw-WELSEGS) keyword in the [SCHEDULE](#kw-SCHEDULE) section without having to re-define all the information that is on the [WELSEGS](#kw-WELSEGS) keyword.  Note that the well must have been previously define by both the [WELSPECS](#kw-WELSPECS) and [WELSEGS](#kw-WELSEGS) keywords in the [SCHEDULE](#kw-SCHEDULE) section to use the WSEGPROP keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which a multi-segment well is being defined. Note that the well name (WELNAME) must have been declared previously using the [WELSPECS](#kw-WELSPECS) keyword in the [SCHEDULE](#kw-SCHEDULE) section, otherwise an error may occur. | None |
| 2 | ISEG1 | A positive integer greater than or equal to two and less than or equal to MXSEGS on [WSEGDIMS](#kw-WSEGDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section that defines the start of a segment | None |
| 3 | ISEG2 | A positive integer greater than or equal to two and less than or equal to ISEG1 on this record and MXSEGS on the [WSEGDIMS](#kw-WSEGDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section that defines the end of a segment. | None |
| 4 | ID | A real positive value that defines the tubing internal diameter of the segment for the well. | Previous Entered Value |
| feet | m | cm |  |
| 5 | EPSILON | A real positive value that defines the tubing absolute roughness of the segment for the well. | Previous Entered Value |
| feet | m | cm |  |
| 6 | XAREA | XAREA is real positive value equal to or greater than zero that defines the cross sectional area for fluid flow. Currently this option is not supported by OPM Flow. | Previous Entered Value |
| ft2 | m2 | cm2 |  |
| 7 | VOLSEG | VOLSEG is a real positive value that defines the effective segment volume for the this segment. Currently this option is not supported by OPM Flow. | Previous Entered Value |
| ft3 | m3 | cm3 |  |
| 8 | XAREAS | XAREAS is real positive value equal to or greater than zero that defines the cross sectional area of the pipe wall for this segment, that is used in thermal conductivity calculations for when the temperature calculation is activated by the [TEMP](#kw-TEMP) keyword in the [RUNSPEC](#kw-RUNSPEC) section. Currently this option is not supported by OPM Flow. | Previous Entered Value |
|  | ft2 | m2 | cm2 |
| 9 | VHEATCAP | VHEATCAP is real positive value equal to or greater than zero that defines the volumetric heat capacity of the pipe wall used in thermal conductivity calculations for when the temperature calculation is activated by the [TEMP](#kw-TEMP) keyword in the [RUNSPEC](#kw-RUNSPEC) section. Currently this option is not supported by OPM Flow. | Previous Entered Value |
| Btu/ft/day/°R | kJ/m/day/K | J/cm/hr/K |  |
| 10 | THCON | THCON is real positive value equal to or greater than zero that defines the thermal conductivity of the pipe wall used in thermal conductivity calculations for when the temperature calculation is activated by the [TEMP](#kw-TEMP) keyword in the [RUNSPEC](#kw-RUNSPEC) section. Currently this option is not supported by OPM Flow. | Previous Entered Value |
| Btu/ft/day/°R | kJ/m/day/K | J/cm/hr/K |  |
| Notes: |  |  |  |
: WSEGPROP Keyword Description {#tbl-12-119}
The total number of wells should be defined via the [WELLDIMS](#kw-WELLDIMS) keyword and the number of multi-segment wells should be declared on the [WSEGDIMS](#kw-WSEGDIMS) keyword, both keywords are in the [RUNSPEC](#kw-RUNSPEC) section.

See also the [WELSPECS](#kw-WELSPECS) keyword to define wells, the [COMPDAT](#kw-COMPDAT) keyword to define the well completions for both ordinary wells and multi-segment wells, and the [COMPSEGS](#kw-COMPSEGS) keyword to define a multi-segment well segment completions. All the aforementioned keywords are described in the [SCHEDULE](#kw-SCHEDULE) section.


#### Example

The following example modifies two segments in well OP01 and one segment in well OP02.


```
--
--       WELL SEGMENT SPECIFICATION DATA
--
-- WELL  SEG   SEG   TUBE   TUBE     XSEC  VOL
-- NAME  ISTR  IEND  ID     ROUGH    AREA  SEG
WSEGPROP
OPO1      12    14   0.3    0.00010                                            /
OP01      13    15   0.275  0.00010                                            /
OP02      14    14   0.275  0.00010                                            /
/
```


Note that the two multi-segment wells and their respective segments must have been previously defined by the [WELSEGS](#kw-WELSEGS) keyword.