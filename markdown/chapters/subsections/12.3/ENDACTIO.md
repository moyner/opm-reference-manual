### ENDACTIO – End the Definition of ACTION Commands {#kw-ENDACTIO}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The ENDACTIO keyword defines the end of a series of conditions that invoke run time processing of the [ACTION](#kw-ACTION) series of keywords, namely: [ACTION](#kw-ACTION), [ACTIONG](#kw-ACTIONG), [ACTIONR](#kw-ACTIONR), [ACTIONS](#kw-ACTIONS), [ACTIONW](#kw-ACTIONW) and [ACTIONX](#kw-ACTIONX). Only the [ACTIONX](#kw-ACTIONX) keyword is implemented in OPM Flow as this keyword implements the [ACTION](#kw-ACTION), [ACTIONG](#kw-ACTIONG), [ACTIONR](#kw-ACTIONR), [ACTIONS](#kw-ACTIONS), [ACTIONW](#kw-ACTIONW) functionality with greater flexibility.  See the [ACTIONX](#kw-ACTIONX) keyword in the [SCHEDULE](#kw-SCHEDULE) section for a full description of the [ACTION](#kw-ACTION) facility.

There is no data required for this keyword and there is no terminating “/” for this keyword.


#### Example

The example shows the use of the [ACTIONX](#kw-ACTIONX) and ENDACTIO keywords to test if the field’s gas production rate is less than 600 MMscf/d after 2020 and to open up additional wells if this occurs.


```
--
-- START OF ACTIONX FIELD PHASE-2 DEVELOPMENT DEFINITION
--
ACTIONX
     PHASE2       1               /
     GGPR  'FIELD' < 600E3 AND    /
     YEAR > 2020                  /
/
-- WELL PRODUCTION STATUS
--
--  WELL    WELL   --LOCATION--  COMPLETION
--  NAME    STAT     I   J    K  FIRST LAST
WELOPEN
GP10        OPEN                           /
GP11        OPEN                           /
/
--
-- END OF ACTIONX FIELD PHASE-2 DEVELOPMENT DEFINITION
--
ENDACTIO

```