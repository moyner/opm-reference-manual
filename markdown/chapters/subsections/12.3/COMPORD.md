### COMPORD – Define Well Connection Ordering {#kw-COMPORD}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The COMPORD keyword defines how the well connection data entered on the [COMPDAT](#kw-COMPDAT) keyword in the [SCHEDULE](#kw-SCHEDULE) section are to be ordered for a well.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well connection data are being defined. Note that the well name (WELNAME) must have been declared previously using the [WELSPECS](#kw-WELSPECS) keyword in the [SCHEDULE](#kw-SCHEDULE) section, otherwise an error may occur. | None |
| 2 | COMPORD | A character string that defines the method for ordering the well connections given on the [COMPDAT](#kw-COMPDAT) keyword, and should be set to [DEPTH](#kw-DEPTH), INPUT, or TRACK. All options are now supported by OPM Flow. | TRACK |
| Notes: |  |  |  |
: COMPORD Keyword Description {#tbl-12-15}
See also the [COMPDAT](#kw-COMPDAT) keyword in the [SCHEDULE](#kw-SCHEDULE) section.


::: {.callout-note}
If visual inspection of the well trajectories in the model indicate problematic or unrealistic well connections, the options on this keyword may be useful in correcting the issue.
:::


#### Example

The following example defines the connections for two vertical oil wells using the [COMPDAT](#kw-COMPDAT) keyword and the COMPORD to defined the connection ordering for the wells.


```
--
--       WELL CONNECTION DATA
--
-- WELL  --- LOCATION ---  OPEN   SAT   CONN   WELL   KH    SKIN   D     DIR
-- NAME   II  JJ  K1  K2   SHUT   TAB   FACT   DIA    FACT  FACT   FACT  PEN
COMPDAT
OP01      1*  1*  20  56   OPEN   1*    1*    0.708   1*    0.0    1*    'Z' /
OP01      1*  1*  75 100   SHUT   1*    1*    0.708   1*    0.0    1*    'Z' /
OP02      35  96  75 100   OPEN   1*    1*    0.708   1*    0.0    1*    'Z' /
--
--       DEFINE WELL CONNECTION ORDERING
--
-- WELL  COMPL
-- NAME  ORDER
COMPORD
OP01     DEPTH                                             /
OP02     DEPTH                                             /
/
```

The [DEPTH](#kw-DEPTH) option has been chosen because both wells are vertical. Also one could use the following format instead for the COMPORD:


```
--
--       DEFINE WELL CONNECTION ORDERING
--
-- WELL  COMPL
-- NAME  ORDER
COMPORD
*        DEPTH                                             /
/
```


as both wells should utilize the [DEPTH](#kw-DEPTH) option. This version would set all wells in the model to [DEPTH](#kw-DEPTH) connection ordering.