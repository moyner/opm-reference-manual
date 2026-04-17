### SAVE – Activate Output of a SAVE File for Fast Restarts {#kw-SAVE}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword activates output of a SAVE file for fast restarts which are read in by the [LOAD](#kw-LOAD) keyword in the [RUNSPEC](#kw-RUNSPEC) section. No data is required for this keyword.

OPM Flow does not support the SAVE file format for fast restarts like the commercial simulator, but instead writes a standard [RESTART](#kw-RESTART) file at the requested time step in the [SCHEDULE](#kw-SCHEDULE) section, which can then be used to restart the simulation at a given point in time via the [RESTART](#kw-RESTART) keyword in the [RUNSPEC](#kw-RUNSPEC) section.


#### Example

The first example requests that a SAVE file be written out in the [RUNSPEC](#kw-RUNSPEC) section; however, OPM Flow will not write a [RESTART](#kw-RESTART) record if the SAVE keyword is encountered in the [RUNSPEC](#kw-RUNSPEC) section.


```
-- ==============================================================================
--
-- RUNSPEC SECTION
--
-- ==============================================================================
RUNSPEC
--
--       WRITE OUT SAVE FILE FOR FAST RESTARTS
--
SAVE
```


The second example shows how the keyword is used in the [SCHEDULE](#kw-SCHEDULE) section.


```
-- ==============================================================================
--
-- SCHEDULE SECTION
--
-- ==============================================================================
SCHEDULE

-- ------------------------------------------------------------------------------
-- SCHEDULE SECTION - 2020-01-01
-- ------------------------------------------------------------------------------
RPTSCHED
          'WELLS=2'    'WELSPECS'    'CPU=2'     FIP=2'                         /

DATES
          1  APR   2021  /
/
--
--       WRITE OUT SAVE FILE FOR FAST RESTARTS
--
SAVE
```


```
DATES
          1  JLY   2021  /
          1  OCT   2021  /
/
```

Here OPM Flow will write out a [RESTART](#kw-RESTART) file instead of a SAVE file at April 1st, 2021.