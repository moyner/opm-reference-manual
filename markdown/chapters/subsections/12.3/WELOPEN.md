### WELOPEN – Define Well and Well Connection Flowing Status {#kw-WELOPEN}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The WELOPEN keyword defines the status of wells and well connections, and is used to open and shut previously defined wells and well connections without having to re-specify all the data on the well control keywords: [WCONPROD](#kw-WCONPROD), [WCONHIST](#kw-WCONHIST), [WCONINJE](#kw-WCONINJE), or [WCONINJH](#kw-WCONINJH) keywords.  Note that the well must still be initially fully defined using the [WCONPROD](#kw-WCONPROD) or [WCONINJE](#kw-WCONINJE) keywords.  All the aforementioned keywords are described in the [SCHEDULE](#kw-SCHEDULE) section.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well or well connection status data are being defined. Note that the well name (WELNAME) must have been declared previously using the [WELSPECS](#kw-WELSPECS) keyword in the [SCHEDULE](#kw-SCHEDULE) section, otherwise an error may occur. | None |
| 2 | STATUS | A defined character string of length four that defines the well or well connection operational status, STATUS should be set to one of the following character strings: | OPEN |
| 3 | I | An integer less than or equal to NX that defines the connection location in the I-direction. | Negative |
| 4 | J | An integer less than or equal to NY that defines the connection location in the J-direction. | Negative |
| 5 | K | An integer less than or equal to NZ that defines the connection location in the K-direction. | Negative |
| 6 | C1 | An integer less than or equal to the total number of completions that defines the first completion in the range. | Negative |
| 7 | C2 | An integer less than or equal to the total number of completions that defines the last completion in the range. | Negative |
| Notes: |  |  |  |
: WELOPEN Keyword Description {#tbl-12-87}
If variables I, J, K, C1 and C2 are all set to a negative number or defaulted with 1* then STATUS is applied to the well and the well connections remain unchanged.

If any of the variables I, J, K, C1 and C2 are set to zero or a positive value then STATUS is applied to the defined well connections and the well status remains unchanged. The defined well connections are those with the specified I, J, K locations and that are in the completion number range specified by C1 and C2. If a zero or negative value is specified for I, J or K then this matches any value for that index. If a zero or negative value is specified for C1 or C2 respectively then no lower or upper bound is applied to the completion range.

See also the [COMPDAT](#kw-COMPDAT) keyword to define a well’s connections, the [COMPLUMP](#kw-COMPLUMP) keyword to group well connections into well completions, the [WCONPROD](#kw-WCONPROD) and [WCONINJE](#kw-WCONINJE) keywords to define a well’s production and injections targets and constraints. All the aforementioned keywords are described in the [SCHEDULE](#kw-SCHEDULE) section.


#### Examples

The following example defines two vertical oil wells using the [WELSPECS](#kw-WELSPECS) keyword and their associated connection data.


```
-- WELL SPECIFICATION DATA
--
-- WELL     GROUP      LOCATION  BHP    PHASE  DRAIN  INFLOW  SHUT  CROSS  PRESS
-- NAME     NAME        I    J   DEPTH  FLUID  AREA   EQUA.   IN    FLOW   TABLE
WELSPECS
OP01      PLATFORM     14   13   1*      OIL   1*     STD     OPEN   NO    1*  /
OP02      PLATFORM     28   96   1*      OIL   1*     STD     OPEN   NO    1*  /
/
--
--       WELL PRODUCTION WELL CONTROLS
--
-- WELL  OPEN/  CNTL   OIL    WAT    GAS   LIQ    RES    BHP    THP   VFP    VFP
-- NAME  SHUT   MODE   RATE   RATE   RATE  RATE   RATE   PRES   PRES  TABLE  ALFQ
WCONPROD
‘*’      SHUT   GRUP   1*     1*     1*    1*     1*     200.0                  /
/
--       WELL CONNECTION DATA
--
-- WELL  --- LOCATION ---  OPEN   SAT   CONN   WELL   KH    SKIN   D     DIR
-- NAME   II  JJ  K1  K2   SHUT   TAB   FACT   DIA    FACT  FACT   FACT  PEN
COMPDAT
OP01      1*  1*   1  10   SHUT   1*    1*    0.708  1*    0.0    1*    'Z' /
OP01      1*  1*  15  30   SHUT   1*    1*    0.708  1*    0.0    1*    'Z' /
OP01      1*  1*  35  90   SHUT   1*    1*    0.708  1*    0.0    1*    'Z' /
OP02      1*  1*   1  10   SHUT   1*    1*    0.708  1*    0.0    1*    'Z' /
/
--
--       DEFINE WELL AND WELL CONNECTIONS FLOWING STATUS
--
--  WELL WELL   --LOCATION--  COMPLETION
--  NAME STAT     I   J    K  FIRST LAST
WELOPEN
OP01     OPEN                                              /
OP01     OPEN     0   0    1                               /
OP01     OPEN     0   0    2                               /
OP01     OPEN     0   0    3                               /
OP01     OPEN     0   0    4                               /
OP02     OPEN                                              /
OP02     OPEN     0   0    0                               /
/
```


In this example the first record for each well in the WELOPEN keyword changes the well status from shut (as per the [WCONPROD](#kw-WCONPROD) keyword) to open. Then for well OP01 well connections in layers one to four are opened for flow and all the connections for well OP02 are opened, that is the connections in layers one to ten.

The next example shows the use of the [COMPLUMP](#kw-COMPLUMP) keyword to group the well connections into well completions for wells OP01, OP02 and OP03, and then use the WELOPEN keyword to open the well and the well completions.


```
--
--       ASSIGN WELL CONNECTIONS TO COMPLETIONS
--
-- WELL  --- LOCATION ---  COMPL
-- NAME   II  JJ  K1  K2   NO.
COMPLUMP
OP01       0   0   1  10    1                              / COMPLETION NO. 01
OP01       0   0  15  30    2                              / COMPLETION NO. 02
OP01       0   0  35  90    3                              / COMPLETION NO. 03
OP02       0   0  15  30    2                              / COMPLETION NO. 02
OP02       0   0  35  90    3                              / COMPLETION NO. 03
OP03       0   0   1  10    1                              / COMPLETION NO. 01
OP03       0   0  35  90    3                              / COMPLETION NO. 03
/
--
--       DEFINE WELL AND WELL CONNECTIONS FLOWING STATUS
--
--  WELL WELL   --LOCATION--  COMPLETION
--  NAME STAT     I   J    K  FIRST LAST
WELOPEN
OP01     OPEN                                              /
OP01     OPEN     0   0    0     3     3                   /
OP02     OPEN                                              /
OP02     OPEN     0   0    0     2     2                   /
OP03     OPEN                                              /
OP03     OPEN     0   0    0     0     0                   /
/
```


Again, the first record of each well WELOPEN keyword changes the well status from shut (as per the [WCONPROD](#kw-WCONPROD) keyword) to open. Then for well OP01 well completion number three is opened (connections 35 to 90), completion two (connections 15 to 30) for well OP02 and completion numbers one to three (all the connections) for well OP03. Note that there is no completion number two for OP03 so connections 15 to 30 will not be opened.

Note the last completion number for well OP03 was named completion number three, but it could have been named number two as well. The reason why it was named number three instead of two was because it was assumed (for the example) that layers 35 to 90 represent a particular reservoir, and therefore allowing for the tracking of completions for individual reservoirs, as shown in the example.

This example shows how one can open all the wells and well completions for a given reservoir.


```
--
--       DEFINE WELL AND WELL CONNECTIONS FLOWING STATUS
--
--  WELL WELL   --LOCATION--  COMPLETION
--  NAME STAT     I   J    K  FIRST LAST
WELOPEN
‘*’      OPEN                                              /
‘*’      OPEN     0   0    0     3     3                   /
OP02     SHUT     0   0    0     0     0                   /
OP02     OPEN     0   0    0     2     2                   /
/
```


In this case wells OP01, OP02 and OP03 are opened via completion number three. All the connections for OP02 are then shut, and the connections associated with completion two are opened instead for this well.