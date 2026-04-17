### WELSPECL – Define Well Specifications for Local Grid Refinements


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The WELSPECL keyword defines the general well specification data for all well types and must be used for all wells contained within a Local Grid Refinement (“LGR”) instead of the WELSPECS keyword. WELSPECL must declare wells first before any other LGR well specification keywords are used in the input file. The keyword declares the name of well, the group the well belongs to, the LGR the well is incorporated into, the wellhead location and other key parameters.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well specification data is being defined. | None |
| 2 | GRPNAME | A character string of up to eight characters in length that defines the group name for which the well is assigned to. The group named FIELD is the top most group and thus GRPNAME cannot be set to FIELD, although this is allowed in the commercial compositional simulator but not the commercial black-oil simulator. Note that the group hierarchy should be defined by the GRUPTREE keyword when there is more than one level of groups, otherwise all the groups will sit directly under the FIELD group in the group tree hierarchy. Secondly, groups defined by the GRUPTREE keyword cannot contain other groups and wells; that is, groups must either contain other groups or wells but not both. If necessary, wells can be re-allocated to a different group by re-entering a well's WELSPECS data together with a new value for GRPNAME. | None |
| 3 | LGRNAME | A character string of up to eight characters in length that defines the  name of the local grid refinement for which the well is assigned to. | None |
| 4 | I | A positive integer greater than or equal to zero and less than or equal to NX on the CARFIN keyword for Cartesian grids, that defines the wellhead location for a vertical or deviated well, or the heel for a horizontal well in the I-direction within the LGR. For radial LGRs this parameter should be set to one. | None |
| 5 | J | A positive integer greater than or equal to zero and less than or equal to NY on the CARFIN keyword for Cartesian grids, that defines the wellhead location for a vertical or deviated well, or the heel for a horizontal well in the J-direction within the LGR. For radial LGRs this parameter should be set to one. | None |
| 6 | BHPREF | A real value that defines the reference depth for reporting the bottom-hole pressure for the well. Ideally this value should be set to the midpoint of the perforations as defined by the COMPDATL keyword in the SCHEDULE section. If defaulted by 1* or set to a value less than or equal to zero, then the mid-point of shallowest connection defined by the COMPDATL keyword will be used. | Mid-point of shallowest connection defined by the COMPDATL keyword |
| feet | m | cm |  |
| 7 | TYPE | A defined character that defines the “main” phase for the well, and should be set to one of the following character strings: This parameter defines the phase used to calculate a well’s productivity  or injectivity index and the type of well, or a well’s connection, to close when a group’s production constraints, as defined on the GCONPROD keyword in the SCHEDULE section, have been violated. For example, if the well is declared as an oil well, then excessive gas and water connections will be subject to closure. | None |
| 8 | DRADIUS | A real value that defines the well drainage radius for the well used to calculate a well’s productivity or injectivity index. A default of zero results in the pressure equivalent radius of the grid blocks containing the well connections are used. | 0.0 |
| feet | m | cm |  |
| 9 | INFLOW | A defined character string that defines the inflow equation to be used for the well in calculating the well’s flow rates. INFLOW should be set to one of the following character strings: For oil and water wells the INFLOW should be set to STD, why for dry gas wells INFLOW can be set to either R-G or P-P; however, the P-P option is preferred for dry gas wells due to the more rigorous treatment of gas flow.  For wet gas wells, that is gas condensate wells, INFLOW should be set to GPP. Only INFLOW equal to STD and NO are currently implemented in OPM Flow. | STD |
| 10 | AUTO | A defined character string that defines the automatic action to be taken if the economic WCUT, GOR, or WGR limits are violated and the well is to cease production. AUTO should be set to one of the following character strings: The corrective action takes places at the end of the time step in which the constraint is violated. | SHUT |
| 11 | XFLOW | A defined character string that defines the if cross flow should occur within the wellbore, and should be set to either: In some cases numerical issues can occur if this variable is set to YES, and resetting it to NO may resolve the issue; however the results may not represent the physical process in this case. | YES |
| 12 | PVTNUM | A positive integer greater than or equal to zero that defines the PVT table used to calculate the wellbore fluid properties that define the relationship between reservoir and surface volume rates. The default value of zero sets PVTNUM to be the PVT table of the deepest connection in the well. | 0 |
| 13 | DENOPT | A defined character string that sets the type of density calculation used in calculating the wellbore hydrostatic head, and should be set to one of the following character strings: The default option of 1* invokes the SEG option and is the only option implemented in OPM Flow. | SEG |
| 14 | FIPNUM | An integer value defines the FIPNUM region used to determine the reservoir conditions in calculating the well’s reservoir volumes. If set to a negative integer value then the FIPNUM region of the deepest connection in the well will be used. If set to zero, the default value, then the average properties for the field will be used. If set to an integer value greater than zero, then the FIPNUM indicated by this value will be used. | 0 |
| 15 |  | Not used. |  |
| 16 |  | Not used. |  |
| 17 |  | Not used. |  |
| 18 |  | Not used. |  |
| Notes: |  |  |  |

*Table 12.91: WELSPECL Keyword Description*


See also the COMPDATL keyword to define a well’s connections in a LGR, the WCONPROD and WCONINJE keywords to define a well’s production and injections targets and constraints. All the aforementioned keywords are described in the SCHEDULE section.


#### Example

The following example defines three wells using the WELSPECL keyword


```
--
-- WELL SPECIFICATION DATA FOR LGR WELLS
--
-- WELL  GROUP    LGR    LOCATION  BHP    PHASE  DRAIN  INFLOW  SHUT  CROSS  PVT
-- NAME  NAME     NAME    I    J   DEPTH  FLUID  AREA   EQUA.   IN    FLOW  TABLE
WELSPECL
GI01     PLATFORM LGR01  14   13   1*     GAS    1*     P-P    SHUT   NO     1* /
GP01     PLATFORM LGR01  64   80   1*     GAS    1*     GPP    SHUT   NO     1* /
OP01     PLATFORM LGR02  24   10   1*     OIL    1*     STD    SHUT   NO     1* /
/
```


Here, well GI01 and GP01 are in the same LGR named LGR01 and OP01 is in a separate LGR named LGR02. GI01 is a dry gas injection well that uses the dry gas pseudo inflow equation, GP01 is a gas condensate well that uses the generalized gas pseudo pressure inflow equation, and finally, OP01 is an oil well that uses the standard inflow equation. All wells: will be shut if they are required to cease production, all wells disallow cross flow,  and the hydrostatic head calculation is defaulted to the segment option for all wells.
