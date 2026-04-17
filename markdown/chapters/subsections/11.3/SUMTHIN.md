### SUMTHIN – Define SUMMARY Data Reporting Time Steps {#kw-SUMTHIN}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword defines a time interval for writing out the [SUMMARY](#kw-SUMMARY) data to the [SUMMARY](#kw-SUMMARY) file and the RSM file, if the [RUNSUM](#kw-RUNSUM) keyword has also been activated in the [SUMMARY](#kw-SUMMARY) section. Only the data for the first time step in the time interval is written out and the other time steps are skipped until the next time interval, except for report time steps. Note that report time steps data are always written out regardless of the setting on this keyword.  This enables the size of the [SUMMARY](#kw-SUMMARY) files to be reduced depending on the size of the time interval. However, the keyword will produce irregular time steps reports of the [SUMMARY](#kw-SUMMARY) data.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | SUMSTEP | SUMSTEP is a real positive number that defines the time interval for which the first time step of data will be written to the [SUMMARY](#kw-SUMMARY) file (and the RSM file if RSM output has been activated). For example, if SUMSTEP is set to 30 days, and if the simulator takes time steps of 0, 5, 10, 16,  24, 30, 40, 45, 60, 90 days. Then the [SUMMARY](#kw-SUMMARY) data will be written out at time steps 0, 30, 40 and 60 days. | None |
| days | days | hours |  |
| Notes: |  |  |  |
: SUMTHIN Keyword Description {#tbl-11-33}
See also the [RPTONLY](#kw-RPTONLY) keyword in the [SUMMARY](#kw-SUMMARY) section that forces the [SUMMARY](#kw-SUMMARY) data to be only written out at report time steps, as oppose to all time steps or SUMSTEP time intervals.


#### Example


```
--
--       DEFINE SUMMARY DATA REPORTING TIME STEP INTERVAL
--
--       SUMSTEP
SUMTHIN
         30.0                                              /                                                                  /

```

The above example defines the [SUMMARY](#kw-SUMMARY) file time step interval to be 30 days for both field and metric units.