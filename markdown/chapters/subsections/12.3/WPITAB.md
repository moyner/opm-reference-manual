### WPITAB – Assign Well Productivity Index versus Water Cut Tables {#kw-WPITAB}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The WPITAB keyword assigns the well productivity index multiplier versus water cut tables, that are used to scaled a well’s connection factors based on the connection’s current producing water cut, to a well. The tables are defined via the PIMULTAB keyword in the [SCHEDULE](#kw-SCHEDULE) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well productivity index multiplier versus water cut table, PIMULTAB, is being assigned. Note that the well name (WELNAME) must have been declared previously using the [WELSPECS](#kw-WELSPECS) keyword in the [SCHEDULE](#kw-SCHEDULE) section, otherwise an error may occur. | None |
| 2 | PIMULTAB | A positive integer value that defines the corresponding PIMULTAB table to be allocated to the well. A value less than or equal to zero means that no PIMULTAB table is allocated to the well | 0 |
| Notes: |  |  |  |
: WPITAB Keyword Description {#tbl-12-112}
See also the PIMULTAB keyword that defines productivity index multiplier versus water cut tables and also the [WPIMULT](#kw-WPIMULT) keyword that scales a well’s productivity index by a constant value, both of which are in the [SCHEDULE](#kw-SCHEDULE) section.


#### Example

Given NTPIMT equals two on the [PIMTDIMS](#kw-PIMTDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section,  then:


```
--
--       ASSIGN WELL PRODUCTIVITY INDEX VS WATER CUT TABLE
--
-- WELL  PI
-- NAME  TABLE
WPITAB
OP01     1                                                        /
OP02     1                                                        /
OP03     2                                                        /
/

```

Assigns PIMULTAB table one to wells OP01 and OP02 and table two to OP03.