### WHISTCTL – Define Well Historical Target Phase {#kw-WHISTCTL}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The WHISTCTL keyword changes the target control for wells declared as history match wells via the [WCONHIST](#kw-WCONHIST) keyword in the [SCHEDULE](#kw-SCHEDULE) section. The target phase is set on the [WCONHIST](#kw-WCONHIST) keyword and WHISTCTL overrides this value for all subsequent entries on the [WCONHIST](#kw-WCONHIST) keyword.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | TARGET | A defined character string that sets the observed target production phase for the well, all the other phases are calculated unconstrained and used for reporting only. The simulator will attempt to meet the TARGET based on the phase rate stated in items (4) to (6) and (10) on the [WCONHIST](#kw-WCONHIST) keyword. TARGET should be set to one of the following character strings: | None |
| 2 | [END](#kw-END) | A defined character string that defines if the simulation should terminate if the well has switch to BHP control by the simulator, and should be set to one of the following character strings: Wells set to BHP control via the [WCONHIST](#kw-WCONHIST) or WHISCTL keywords are ignored. Only [END](#kw-END) equal to NO is currently supported in OPM Flow. | NO |
| Notes: |  |  |  |
: WHISTCTL Keyword Description {#tbl-12-98}
History matching wells are handled differently then ordinary wells that use the [WCONPROD](#kw-WCONPROD) keyword for controlling their production targets and constraints. However, the wells still need to be defined like ordinary production wells using the [WELSPECS](#kw-WELSPECS) keyword in the [SCHEDULE](#kw-SCHEDULE) section. History matching wells are converted to ordinary wells by restating a well’s control mode using either the [WCONPROD](#kw-WCONPROD) or [WELTARG](#kw-WELTARG) keywords in the [SCHEDULE](#kw-SCHEDULE) section.

See also the [WCONHIST](#kw-WCONHIST) and [WCONINJH](#kw-WCONINJH) keywords that are used to define the historical production and injection data,  All the aforementioned keywords are described in the [SCHEDULE](#kw-SCHEDULE) section.


#### Example

The example below shows the observed gas rates for the OP01 oil producer for the first quarter of 2000.


```
-- ------------------------------------------------------------------------------
-- 01 JAN 2000 START OF SCHEDULE SECTION
-- ------------------------------------------------------------------------------
--
--       DEFINE WELL HISTORICAL TARGET PHASE
--
--       CNTL    BHP
--       MODE    STOP
WHISTCTL
         RESV    NO                                                   /
--
--       WELL HISTORICAL PRODUCTION CONTROLS
--
-- WELL  OPEN/  CNTL   OIL    WAT    GAS    VFP    VFP   THP   BHP
-- NAME  SHUT   MODE   RATE   RATE   RATE   TABLE  ALFQ  PRES  PRES
WCONHIST                                                                                                                          OP01     OPEN   ORAT  15.5E3  100.0  1550   10      1*   900.0 1*     /
/                                                                               DATES
01 FEB 2000 /
/
--
--       WELL HISTORICAL PRODUCTION CONTROLS
--
-- WELL  OPEN/  CNTL   OIL    WAT    GAS    VFP    VFP   THP   BHP
-- NAME  SHUT   MODE   RATE   RATE   RATE   TABLE  ALFQ  PRES  PRES
WCONHIST                                                                                                                          OP01     OPEN   ORAT  15.2E3  150.0  1520   1*      1*   875.0 3250.0 /
/                                                                               DATES
01 MAR 2000 /
/
--
--       WELL HISTORICAL PRODUCTION CONTROLS
--
-- WELL  OPEN/  CNTL   OIL    WAT    GAS    VFP    VFP   THP   BHP
-- NAME  SHUT   MODE   RATE   RATE   RATE   TABLE  ALFQ  PRES  PRES
WCONHIST                                                                                                                          OP01     OPEN   ORAT  15.0E3  200.0  1500   1*      1*   850.0 1*     /
/
```

From January 1, 2000 the [WCONHIST](#kw-WCONHIST) keyword defines well OP01, which is open and is on oil rate control, to produce 15,500 stb/d oil, with the observed rates of 100 stb/d of water and 15.5 MMscf/d of gas. However the WHISCTL keyword resets the target control to reservoir voidage from January 1, 2000 and onward. This is useful in initial history matching runs to get a “reasonable” pressure match, by ensuring that the total reservoir withdrawals are correct, although the individual phase withdrawals will not match. Once a reasonable pressure match is achieved for the reservoir then one can reset TARGET to the sales phase, [OIL](#kw-OIL) or [GAS](#kw-GAS), and continue with the matching of all the phases.