### WELSPECS – Define Well Specifications {#kw-WELSPECS}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The WELSPECS keyword defines the general well specification data for all well types, and must be used for all wells before any other well specification keywords are used in the input file. The keyword declares the well, the name of the well, the group the well initial belongs to, the wellhead location and other key parameters.

OPM Flow also supports the use of the WELSPECS keyword to change the properties of one or more wells previously specified using the WELSPECS keyword. In particular, this supports changing the controlling group (GRPNAME) without affecting any other well properties such as the location of the well head (I, J) or the well reference depth (BHPREF), since defaulted properties are not changed in this case. However, the well reference depth can be re-defaulted by specifying a negative value for BHPREF. The wells to be changed can be specified using a well name, well name pattern or well list (WELNAME).


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well specification data are being defined. | None |
| 2 | GRPNAME | A character string of up to eight characters in length that defines the group name for which the well is assigned to. The group named [FIELD](#kw-FIELD) is the top most group. GRPNAME can be set to [FIELD](#kw-FIELD) although this is discouraged and a warning message will be issued. This is allowed in the commercial compositional simulator but not the commercial black-oil simulator. The [FIELD](#kw-FIELD) group cannot contain both groups and wells. Note that the group hierarchy should be defined by the [GRUPTREE](#kw-GRUPTREE) keyword when there is more than one level of groups, otherwise all the groups will sit directly under the [FIELD](#kw-FIELD) group in the group tree hierarchy. Secondly, groups defined by the [GRUPTREE](#kw-GRUPTREE) keyword cannot contain other groups and wells; that is, groups must either contain other groups or wells but not both. If necessary, wells can be re-allocated to a different group by re-entering a well's WELSPECS data together with a new value for GRPNAME. | None |
| 3 | I | A positive integer greater than or equal to zero and less than or equal to NX that defines the wellhead location for a vertical or deviated well, or the heel for a horizontal well in the I-direction. For wells being specified with the [COMPTRAJ](#kw-COMPTRAJ) and [WELTRAJ](#kw-WELTRAJ) keywords in [SCHEDULE](#kw-SCHEDULE) section, that allow for an alternative manner to define the well connections to the simulation grid blocks, this parameter should be defaulted with 1*. Since the simulator will calculate the wellhead location from the trajectory data on the [WELTRAJ](#kw-WELTRAJ) keyword. Note that the [COMPTRAJ](#kw-COMPTRAJ) and [WELTRAJ](#kw-WELTRAJ) keywords are OPM Flow specific keywords, and will cause an error in the commercial simulator. | None |
| 4 | J | A positive integer greater than or equal to zero and less than or equal to NY that defines the wellhead location for a vertical or deviated well, or the heel for a horizontal well in the J-direction. For wells being specified with the [COMPTRAJ](#kw-COMPTRAJ) and [WELTRAJ](#kw-WELTRAJ) keywords in [SCHEDULE](#kw-SCHEDULE) section, that allows for an alternative manner to define the well connections to the simulation grid blocks,  this parameter should be defaulted with 1*. Since the simulator will calculate the wellhead location from the trajectory data on the [WELTRAJ](#kw-WELTRAJ) keyword. Note that the [COMPTRAJ](#kw-COMPTRAJ) and [WELTRAJ](#kw-WELTRAJ) keywords are OPM Flow specific keywords, and will cause an error in the commercial simulator. | None |
| 5 | BHPREF | A real value that defines the reference depth for reporting the bottom-hole pressure for the well. Ideally this value should be set to the midpoint of the perforations as defined by the [COMPDAT](#kw-COMPDAT) keyword in the [SCHEDULE](#kw-SCHEDULE) section. If defaulted by 1* or set to a value less than or equal to zero, then the mid-point of shallowest connection defined by the [COMPDAT](#kw-COMPDAT) keyword will be used. | Mid-point of shallowest connection defined by the [COMPDAT](#kw-COMPDAT) keyword |
| feet | m | cm |  |
| 6 | TYPE | A defined character string that defines the “main” phase for the well, and should be set to one of the following character strings: This parameter defines the phase used to calculate a well’s productivity or injectivity index and the type of well, or a well’s connection, to close when a group’s production constraints, as defined on the [GCONPROD](#kw-GCONPROD) keyword in the [SCHEDULE](#kw-SCHEDULE) section, have been violated. For example, if the well is declared as an oil well, then excessive gas and water connections will be subject to closure. Note OPM Flow only currently supports options one to three, that is option four (LIQ) is not supported.  For producing wells this mostly matters if one plots the WPI summary vector (productivity index for well's preferred phase). In the current treatment WPI will not have contributions from the water phase if the declared preferred phase is LIQ. For injecting wells WELSPECS's preferred phase does not matter,  since the preferred phase is (typically) reset to the injected phase via the [WCONINJE](#kw-WCONINJE) and [WCONINJH](#kw-WCONINJH) keywords. | None |
| 7 | DRADIUS | A real value that defines the well drainage radius for the well used to calculate a well’s productivity or injectivity index. A default of zero results in the pressure equivalent radius of the grid blocks containing the well connections are used. | 0.0 |
| feet | m | cm |  |
| 8 | INFLOW | A defined character string that defines the inflow equation to be used for the well in calculating the well’s flow rates. INFLOW should be set to one of the following character strings: For oil and water wells the INFLOW should be set to STD, whereas for dry gas wells INFLOW can be set to either R-G or P-P; however, the P-P option is preferred for dry gas wells due to the more rigorous treatment of gas flow.  For wet gas wells, that is gas condensate wells, INFLOW should be set to GPP. Only INFLOW equal to STD and NO are currently implemented in OPM Flow. | STD |
| 9 | AUTO | A defined character string that specifies the action to be taken if the well is automatically closed/shut by the simulator, and should be set to one of the following: The corrective action takes places at the end of the time step in which the constraint is violated. | SHUT |
| 10 | XFLOW | A defined character string that defines the if cross flow should occur within the wellbore, and should be set to either: In some cases numerical issues can occur if this variable is set to YES, and resetting it to NO may resolve the issue; however, the results may not represent the physical down hole process in this case. | YES |
| 11 | [PVTNUM](#kw-PVTNUM) | A positive integer greater than or equal to zero that defines the PVT table used to calculate the wellbore fluid properties that define the relationship between reservoir and surface volume rates. The default value of zero sets [PVTNUM](#kw-PVTNUM) to be the PVT table of the deepest connection in the well. | 0 |
| 12 | DENOPT | A defined character string that sets the type of density calculation used in calculating the wellbore hydrostatic head, and should be set to one of the following character strings: The default option of 1* invokes the SEG option and is the only option implemented in OPM Flow. | SEG |
| 13 | [FIPNUM](#kw-FIPNUM) | An integer value defines the [FIPNUM](#kw-FIPNUM) region used to determine the reservoir conditions in calculating the well’s reservoir volumes and is determined by: | 0 |
| 14 | STRMLIN1 | Not used and should be defaulted with 1*. | 1* |
| 15 | STRMLIN2 | Not used and should be defaulted with 1*. | 1* |
| 16 | TYPECOMP | Commercial compositional simulator well type model option that is not used and should be defaulted with either STD or 1*. | STD |
| 17 | POLYTAB | A positive integer greater than or equal to zero that defines the polymer mixing table, as defined by the [PLMIXPAR](#kw-PLMIXPAR) and [PLYMAX](#kw-PLYMAX) keywords, to be used in calculating the well’s well bore properties. The default value of zero means the table allocated via the [PLMIXNUM](#kw-PLMIXNUM) array for the deepest connection in the well bore is utilized. Only the default value of zero is supported by OPM Flow. | 0 |
| Notes: |  |  |  |
: WELSPECS Keyword Description {#tbl-12-3-281-1}
See also the [COMPDAT](#kw-COMPDAT) keyword to define a well’s connections, the [WCONPROD](#kw-WCONPROD) and [WCONINJE](#kw-WCONINJE) keywords to define a well’s production and injection targets and constraints. All the aforementioned keywords are described in the [SCHEDULE](#kw-SCHEDULE) section.


#### Example

The following example defines three wells using the WELSPECS keyword


```
--
--       WELL SPECIFICATION DATA
--
-- WELL  GROUP     LOCATION  BHP    PHASE  DRAIN  INFLOW  OPEN  CROSS  PVT
-- NAME  NAME        I    J  DEPTH  FLUID  AREA   EQUANS  SHUT  FLOW   TABLE
WELSPECS
GI01     PLATFORM   14   13   1*     GAS    1*     P-P    SHUT   NO     1*     /
GP01     PLATFORM   64   80   1*     GAS    1*     GPP    SHUT   NO     1*     /
OP01     PLATFORM   24  110   1*     OIL    1*     STD    SHUT   NO     1*     /
/
```


Here, well GI01 is a dry gas injection well that uses the dry gas pseudo inflow equation, GP01 is a gas condensate well that uses the generalized gas pseudo pressure inflow equation, and finally, OP01 is an oil well that uses the standard inflow equation. All wells will be shut if they are required to cease production, all wells disallow cross flow,  and the hydrostatic head calculation is defaulted to the segment option for all wells.

If the same three wells are using the [COMPTRAJ](#kw-COMPTRAJ) and [WELTRAJ](#kw-WELTRAJ) keywords to specify the connections to the simulation grid, then the WELSPECS keyword should be;


```
--
--       WELL SPECIFICATION DATA
--
-- WELL  GROUP     LOCATION  BHP    PHASE  DRAIN  INFLOW  OPEN  CROSS  PVT
-- NAME  NAME        I    J  DEPTH  FLUID  AREA   EQUANS  SHUT  FLOW   TABLE
WELSPECS
GI01     PLATFORM   1*   1*   1*     GAS    1*     P-P    SHUT   NO     1*     /
GP01     PLATFORM   1*   1*   1*     GAS    1*     GPP    SHUT   NO     1*     /
OP01     PLATFORM   1*   1*   1*     OIL    1*     STD    SHUT   NO     1*     /
/
```

Notice how the well location parameters have been defaulted with 1* in this case.

The following example illustrates how the WELSPECS keyword can be used to change the controlling group for oil production wells previously specified by the WELSPECS keyword that have an oil production rate less than 100.


```
--
--       ACTIONX BLOCK
--
ACTIONX
  ACT01    1             /
  WOPR     'OP*' < 100.0 /
/
WELSPECS
  '?'      'LOWPRESS'   /
/
ENDACTIO
```