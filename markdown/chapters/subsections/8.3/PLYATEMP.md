### PLYATEMP – Define Polymer Adsorption Table Temperature {#kw-PLYATEMP}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword defines the polymer adsorption temperature for subsequent polymer adsorption tables entered via the [PLYADS](#kw-PLYADS) and [PLYADSS](#kw-PLYADSS) keywords in the [PROPS](#kw-PROPS) section. The Polymer option must have been activated by the [POLYMER](#kw-POLYMER) keyword in the [RUNSPEC](#kw-RUNSPEC) section and the Thermal option invoked by the  [THERMAL](#kw-THERMAL) keyword, also in the [RUNSPEC](#kw-RUNSPEC) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | PLYATEMP | Single real positive value that defines polymer adsorption temperature for subsequent polymer adsorption tables. | None |
| oF | oC | oC |  |
| Notes: |  |  |  |
: PLYATEMP Keyword Description {#tbl-8-101}
#### Example

The example shows how to enter the polymer adsorption data using the [PLYADS](#kw-PLYADS) keyword for two different temperatures.


```
--
--       RESERVOIR
--       TEMPERATURE
--       -----------
PLYATEMP
         60.0                                             / TEMPERATURE
--
--       POLYMER ROCK ADSORPTION TABLE
--
PLYADS
--       POLYMER    POLYMER
--       POLCON     POLRATIO
--       -------    --------
             0.0     0.00000
             2.0     0.00003
             4.0     0.00005
             6.0     0.00007
             8.0     0.00009
            10.0     0.00011
            12.0     0.00012
            14.0     0.00015                               / TABLE NO. 01

--
--       POLYMER    POLYMER
--       POLCON     POLRATIO
--       -------    --------
             0.0     0.00000
             3.0     0.00004
             5.0     0.00006
             7.0     0.00008
             8.0     0.00009
            10.0     0.00011                               / TABLE NO. 02
--
--       RESERVOIR
--       TEMPERATURE
--       -----------
PLYATEMP
         120.0                                            / TEMPERATURE
--
--       POLYMER ROCK ADSORPTION TABLE
--
PLYADS
--       POLYMER    POLYMER
--       POLCON     POLRATIO
--       -------    --------
             0.0     0.00000
             2.0     0.00003
             4.0     0.00005
             6.0     0.00007
             8.0     0.00009
            10.0     0.00011
            12.0     0.00012
            14.0     0.00015                               / TABLE NO. 01
--
--       POLYMER    POLYMER
--       POLCON     POLRATIO
--       -------    --------
             0.0     0.00000
             3.0     0.00004
             5.0     0.00006
             7.0     0.00008
             8.0     0.00009
            10.0     0.00011                               / TABLE NO. 02
```


Here the first PLYATEMP keyword defines the temperature to be 60 oF for the subsequent two polymer rock adsorption tables, assuming NTSFUN equals four and NSSFUN is greater than or equal to eight on the [TABDIMS](#kw-TABDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. The next PLYATEMP keyword defines the temperature to be 120 oF for the subsequent two polymer rock adsorption tables.