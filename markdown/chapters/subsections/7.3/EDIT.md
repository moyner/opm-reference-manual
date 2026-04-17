### EDIT – Define the Start of the EDIT Section of Keywords {#kw-EDIT}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | EDIT | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The EDIT activation keyword marks the end of the [GRID](#kw-GRID) section and the start of the EDIT section that  enables modifications to the OPM Flow calculated properties derived from the data entered in the [GRID](#kw-GRID) section, for example grid block pore volumes via the [PORV](#kw-PORV) array and the transmissibilities via the [TRANX](#kw-TRANX), [TRANY](#kw-TRANY) and [TRANZ](#kw-TRANZ) family of keywords.

There is no data required for this keyword.


#### Example


```
-- ==============================================================================
--
-- EDIT SECTION
--
-- ==============================================================================
EDIT
```


The above example marks the end of the [GRID](#kw-GRID) section and the start of the EDIT section in the OPM Flow data input file.