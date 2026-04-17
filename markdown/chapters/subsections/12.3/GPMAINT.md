### GPMAINT – Define Group Pressure Maintenance Targets and Controls {#kw-GPMAINT}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The GPMAINT keyword defines the groups under pressure maintenance control, the associated flow rate and pressure targets, and fluid in-place regions associated with pressure maintenance, as well as various pressure maintenance controls. GPMAINT allows for various regions, as defined by the [FIPNUM](#kw-FIPNUM) or [FIP](#kw-FIP) keywords in the [REGIONS](#kw-REGIONS) section, to have their average reservoir pressure maintained at a specified value.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | GRPNAME | A character string of up to eight characters in length that defines the group name for which the group’s associated [FIPNUM](#kw-FIPNUM) region will have a targeted average reservoir pressure maintained.  The group named [FIELD](#kw-FIELD) is the top most group and can also be used to set pressure target for the whole field. Note that the group hierarchy should be defined by the [GRUPTREE](#kw-GRUPTREE) keyword when there is more than one level of groups, otherwise all the groups will sit directly under the [FIELD](#kw-FIELD) group in the group tree hierarchy. | None |
| 2 | GRPCNTL | A defined character string of length four, that sets the production or injection control for the group, used to maintain the average pressure for the [FIPNUM](#kw-FIPNUM) region. GRPCNTL should be set to one of the following character strings: | None |
| 3 | [FIPNUM](#kw-FIPNUM) | A positive integer value that defines the region for which pressure maintenance is to be applied by GRPNAME, where [FIPNUM](#kw-FIPNUM) may be define as per the: The maximum number of [FIPNUM](#kw-FIPNUM) and [FIP](#kw-FIP) regions is set by the [REGDIMS](#kw-REGDIMS)(NMFIPR) or the [TABDIMS](#kw-TABDIMS)(NTFIP) keywords(variables) in the [RUNSPEC](#kw-RUNSPEC) section. If both [REGDIMS](#kw-REGDIMS)(NMFIPR) and [TABDIMS](#kw-TABDIMS)(NTFIP) have been defined then the maximum of the two is used. | None |
| 0 |  |  |  |
| 4 | FIPNAME | A character string of up to five characters in length, defining the fluid in-place’s name, as defined by the [FIP](#kw-FIP) keyword in the [REGIONS](#kw-REGIONS) section. For example, if the [FIP](#kw-FIP) keyword has been used to define a [FIP](#kw-FIP) group or family, named FIPBLK-A, then FIPNAME would be set to BLK-A. The default value of 1* means that [FIPNUM](#kw-FIPNUM) on this keyword applies to the standard [FIPNUM](#kw-FIPNUM) array and not to the [FIP](#kw-FIP) defined group regions. | 1* |
| 5 | TARGET | A real positive value that defines the average hydrocarbon pore volume weighted reservoir pressure target for the region, for which GRPNAME should attempt to satisfy. Note that the average pressure report in the [RPTSCHED](#kw-RPTSCHED) series of reports is a pore volume weight average reservoir pressure, not the  average hydrocarbon pore volume weighted reservoir pressure specified by TARGET on this keyword. Thus, there will be small differences between the two numbers. | None |
| 0 |  |  |  |
| psia | barsa | atma |  |
| 6 | ALPHA | A real positive value that defines the proportionality constant used to control the flow rates in order to maintain/reach the TARGET average hydrocarbon pore volume pressure for the region. See equation (12.26). Larger values of ALPHA accelerate the time for the region’s pressure to satisfy the required target pressure (TARGET).  However, ALPHA values that are too large may cause the region’s pressure to oscillate.  Thus, the value of ALPHA should be a value that gives the expected steady state flow rate (TARGET) of the group divided by a reasonable transient pressure error. | None |
| Liquid: stb/d/psi Gas: Mscf/d/psi RESV: rb/d/psi | Liquid: sm3/day/bars Gas: sm3/day/bars RESV: rm3/day/bars | Liquid: scc/hour/atm Gas: scc/hour/atm RESV: rcc/hour/atm |  |
| 7 | BETA | A real positive value that defines the time interval used to control the flow rates in order to maintain the TARGET average hydrocarbon pore volume pressure for the region. See equation (12.26). Larger values of BETA reduce the tendency for the regional pressure to oscillate, but consequently decrease the rate at which the pressure reaches its target value.  This is because the pressure error is measured at the end of the previous time step, resulting in a “delay” in the response.  Also, the larger the time steps the greater the propensity for the pressure to oscillate for given ALPHA and BETA. As a guide BETA should be set to a value that is at least as large as the maximum time step size (see the [TUNING](#kw-TUNING) keyword in the [SCHEDULE](#kw-SCHEDULE) section and section 2.2 Running OPM Flow 2023-04 From The Command Line for setting the maximum time step size). | 1* |
| day | day | day |  |
| Notes: |  |  |  |
: GPMAINT Keyword Description {#tbl-12-41}
The GPMAINT keyword utilizes control theory^[John Doyle, Bruce Francis, Allen Tannenbaum, Feedback Control Theory, Macmillan Publishing Co., 1990.], ^[Karl J. Åström; Richard M. Murray (2008). Feedback Systems: An Introduction for Scientists and Engineers. Princeton University Press. ISBN 978-0-691-13576-2.], ^[Andrei, Neculai (2005)., Modern Control Theory – A Historical Perspective, Research Institute for Informatics,  Center for Advanced Modeling and Optimization,8-10, Averescu Avenue, Bucharest 1, Romania.] and ^[Sontag, Eduardo (1998). Mathematical Control Theory: Deterministic Finite Dimensional Systems. Second Edition,  Springer. ISBN 978-0-387-98489-6.] to calculate the required injection and production rates to ensure some stability in the behavior of the average hydrocarbon pore volume reservoir pressure for a given region and the injection rates over time.  For example, if the group’s flow control (GRPCNTL) is set to one of the in situ reservoir volume injection rates (GINJ, OINJ or WINJ), say Q, then the group’s flow injection rates for each time step is calculated by:


$$
Q = {Q}_{i} + \mathrm{α} (({P}_{\mathit{TARGET}} - {P}_{i-1}) + \frac{{\sum }_{i=1}^{i-1}({P}_{\mathit{TARGET}} - {P}_{i-1})\times \mathrm{Δ}{t}_{i}}{\mathrm{β}})
$$ {#eq-12-26}

Where:

P TARGET	= 	the regions average hydrocarbon pore volume weighted reservoir

pressure target, the TARGET parameter in  @tbl-12-41.

Pi-1	= 	the resulting average hydrocarbon pore volume weighted reservoir

pressure for the region from the preceding completed time step.

Q	=	the new in situ reservoir volume rate.

Qi	= 	the initial in situ reservoir volume rate at the time the keyword was

activated in the input. Subsequent GPMAINT keywords will reset Qi.

α	=	the proportionality constant used to control the flow rates, the ALPHA

parameter in @tbl-12-41.

β	=  	the time interval parameter used to control the flow rates, the BETA

parameter in @tbl-12-41.

The ${\sum }_{i=1}^{i-1}({P}_{\mathit{TARGET}} - {P}_{i-1})\times \mathrm{Δ}{t}_{i}$term in equation (12.26) is the cumulative sum of the average hydrocarbon pore volume weighted reservoir pressure error for the region, times the time step length, from when the last GPMAINT keyword was entered, up to the preceding completed time step.

The objective of equation (12.26) is to stabilize the injection/production rates for the group for when there are changes to the average hydrocarbon pore volume weighted reservoir pressure target set by the initial and subsequent GPMAINT keywords, or by any group constraints applied afterwards. In addition, if the pressure error is small $({P}_{\mathit{TARGET}} - {P}_{i-1})$then the equation should result in approximately the same rates as the previous time step, if the GPMAINT has been previously entered.

However, if the first time the keyword is entered coincides with the start of injection, then Qi in equation (12.26) by definition will be zero, and the injection rate will start from zero and increase as calculated by the equation. The ALPHA and BETA parameters in @tbl-12-41 can be used to control how the rate is built up to meet the desired average hydrocarbon pore volume weighted reservoir pressure target.


#### Examples

The first example uses the gas surface rate to maintain the fields’ average hydrocarbon pore volume pressure at  225 barsa, with the ALPHA and BETA parameters set to 40.0 and 70.0 respectively.


```
--
--       GROUP PRESSURE MAINTENANCE TARGETS AND CONTROLS
--
-- GRUP  CNTL   FIPNUM  FIP     PRESS   ALPHA  BETA
-- NAME  MODE   REGION  FIPNAME TARGET  CONST  CONST
GPMAINT
FIELD    GINS   0       1*      225     40.0   70.0        /
```

/

The second example uses group’s BLK-A gas surface rate to maintain the average hydrocarbon pore volume pressure at 200 barsa for [FIPNUM](#kw-FIPNUM) regions one to four, with the ALPHA and BETA parameters set to 40.0 and 70.0 respectively.


```
--
--       GROUP PRESSURE MAINTENANCE TARGETS AND CONTROLS
--
-- GRUP  CNTL   FIPNUM  FIP     PRESS   ALPHA  BETA
-- NAME  MODE   REGION  FIPNAME TARGET  CONST  CONST
GPMAINT
BLK-A    GINS   1       1*      200     40.0   70.0        /
BLK-A    GINS   2       1*      200     40.0   70.0        /
BLK-A    GINS   3       1*      200     40.0   70.0        /
BLK-A    GINS   4       1*      200     40.0   70.0        /

BLK-B    WINJ   1       FLT-B   215     30.0   65.0        /
BLK-B    WINJ   2       FLT-B   215     30.0   65.0        /
BLK-B    WINJ   3       FLT-B   215     30.0   65.0        /
BLK-B    WINJ   4       FLT-B   215     30.0   65.0        /
/
```

For group BLK-B, water in situ reservoir volume injection rate (RESV) is used to maintain [FIP](#kw-FIP) group/family  FLT-B’s average reservoir pressure at 215 barsa for FIPFLT-B regions one to four. Here the ALPHA and BETA parameters set to 30.0 and 65.0 respectively.