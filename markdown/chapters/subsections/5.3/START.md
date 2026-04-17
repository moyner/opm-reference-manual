### START – Simulation Start Date {#kw-START}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword sets the start date for the simulation switches. If the [DATES](#kw-DATES) keyword is to be used during the simulation, then a start date should be entered.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | DAY | A positive integer that defines the day of the month, the value should be greater than or equal to one and less than or equal to 31. | None |
| 2 | MONTH | Character string for the month and should be one of the following 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL' (or 'JLY'), 'AUG', 'SEP', 'OCT', 'NOV', or 'DEC' | None |
| 3 | YEAR | A positive four digit integer value of the start year, which must be specified fully by four digits, that is 1986. | None |
| Notes: |  |  |  |
: START Keyword Description {#tbl-5-43}
#### Example


```
--
--       DEFINE THE START DATE FOR THE RUN
--
START
         01 'JAN' 2014                                                         /
```


The above example sets the start date for the run to be January 1, 2014.


::: {.callout-note}
Whenever possible it is a good idea to always set the start date to be at the beginning of the year as per the example.  As like most simulators, OPM Flow reports are always stated at the number of days from the start date (and sometimes at a given date). If the start date is at the beginning of the year, then calculating the actual date is relatively straight forward and simple.
:::