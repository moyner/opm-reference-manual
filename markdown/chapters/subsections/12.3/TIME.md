### TIME – Advance Simulation by Cumulative Reporting Time {#kw-TIME}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword advances the simulation to a given cumulative report time after which additional keywords may be entered to instruct OPM Flow to perform additional functions via the [SCHEDULE](#kw-SCHEDULE) section keywords, or further TIME keywords may be entered to advance the simulator to the next report time.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | TIME | A vector of real positive numbers that define the cumulative length of the of report times. | None |
| days | days | hours |  |
| Notes: |  |  |  |
: TIME Keyword Description {#tbl-12-64}
See also the [DATES](#kw-DATES) and [TSTEP](#kw-TSTEP) keyword in the [SCHEDULE](#kw-SCHEDULE) section. Note that since OPM Flow uses the standard Gregorian calendar and therefore leap years are accounted for in the [DATES](#kw-DATES) keyword. Thus, it is more accurate to use the [DATES](#kw-DATES) keyword to progress the simulator through time if one is matching actual production data.

Whenever possible it is a good idea to always set the start date to be at the beginning of the year, as like most simulators, OPM Flow reports are always stated at the number of days from the start date (and sometimes at a given date). If the start date is at the beginning of the year, then calculating the actual date is relatively straight forward and simple.


#### Examples

The fist example shows how to advance the simulation three years using the TIME keyword, from the given start date of January 1, 2022 set via the [START](#kw-START) keyword in the [RUNSPEC](#kw-RUNSPEC) section.


```
-- ==============================================================================
--
-- SCHEDULE SECTION
--
-- ==============================================================================
SCHEDULE

-- ------------------------------------------------------------------------------
-- SCHEDULE SECTION - 2022-01-01
-- ------------------------------------------------------------------------------
--
--       ADVANCE SIMULATION BY REPORTING TIME
--
TIME
         365.25  730.50  1095.75
/
```

The second example shows the same advance but using the [TSTEP](#kw-TSTEP) keyword instead.
      Atgeirr Rasmussen
      2017-09-22T12:22:06.652621000
      AFR
      Again, 2020 has 366 days.

      David Baxendale
      2017-10-02T19:01:11.673000000
      DBx
      Reply to Atgeirr Rasmussen (09/22/2017, 12:22): "..."
      I changed the year to simplify the example.


```
-- ==============================================================================
--
-- SCHEDULE SECTION
--
-- ==============================================================================
SCHEDULE

-- ------------------------------------------------------------------------------
-- SCHEDULE SECTION - 2022-01-01
-- ------------------------------------------------------------------------------
RPTSCHED
          'WELLS=2'    'WELSPECS'    'CPU=2'     FIP=2'                         /
--
--       ADVANCE SIMULATION BY REPORTING TIME
--
TSTEP
         3*365.25
/

```

Again, if the simulated production targets are actual production data or the results are going to be used in economic evaluations then the [DATES](#kw-DATES) keyword may be more useful in advancing the simulation via the reporting time steps, as the exact dates will be honored.