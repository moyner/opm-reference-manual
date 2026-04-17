### REGIONS – Define the Start of the REGIONS Section of Keywords {#kw-REGIONS}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | REGIONS | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The REGIONS activation keyword marks the end of the [PROPS](#kw-PROPS) section and the start of the REGIONS section that defines how various fluid and rock property data defined in the [PROPS](#kw-PROPS) section are allocated to the individual cells in the model.

There is no data required for this keyword.


#### Example


```
-- ==============================================================================
--
-- REGIONS SECTION
--
-- ==============================================================================
REGIONS
```


The above example marks the end of the [PROPS](#kw-PROPS) section and the start of the REGIONS section in the OPM Flow data input file.