### RPTSOL – Define SOLUTION Section Reporting {#kw-RPTSOL}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword defines the data in the [SOLUTION](#kw-SOLUTION) section that is to be printed to the output print file in human readable format. The keyword has two distinct forms, the first of which consists of the keyword followed by a series of integers on the next line indicating the data to be printed (see the first example). This is the original formal in the commercial simulator and was subsequently superseded by the second format. The second format consists of the keyword followed by a series of character strings that indicate the data to be printed. In most cases the character string is the keyword used to load the data in the OPM Flow input deck, for example [PVDG](#kw-PVDG) for the dry gas PVT tables. Its is anticipated that OPM Flow will eventually support the functionality of the second format only, the first format although recognized will be completely ignored.

OPM Flow provides only limited supported for this keyword and will ignore the unsupported options because they have no effect on the results.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | DENO | Print the oil reservoir density array | N/A |
| 2 | [EQUIL](#kw-EQUIL) | Print the equilibration report. | N/A |
| 3 | [FIP](#kw-FIP) | Print the fluid in-place report. The parameter is assigned a value, OPTION, using the form [FIP](#kw-FIP)=OPTION, where OPTION is an integer variable set to: | [FIP](#kw-FIP)=2 |
| 4 | FIPRESV | Print the reservoir volumes in-place report. | N/A |
| 5 | [WELSPECS](#kw-WELSPECS) | [WELSPECS](#kw-WELSPECS) switches on reporting of the well connections, wells and groups at each report time step. There are numerous reports associated with this option. Unlike the other reporting parameters that produce a report for each reporting time step, the [WELSPECS](#kw-WELSPECS) report option only produces a report if an associated keyword has been activated at the current reporting time step. For example, if the reporting time steps are January, February,  and March 2020, and the [RPTSCHED](#kw-RPTSCHED) [WELSPECS](#kw-WELSPECS) option is activated in January, with wells OP01 and OP02 being declared via the [WELSPECS](#kw-WELSPECS) and [COMPDAT](#kw-COMPDAT) keywords,  then a report will be printed for January for these two wells. If there are no further well activations until March, with well OP03 being declared, then there will be no report for February, and only well OP03 will reported at the March reporting time step. | N/A |
| Notes: |  |  |  |
: RPTSOL Keyword Description {#tbl-10-3-80-1}
::: {.callout-note}
Except for non-array like data, [FIP](#kw-FIP) etc., this keyword has the potential to produce very large print files that some text editors may have difficulty loading. A more efficient solution for array type data is to load the *.[INIT](#kw-INIT) and *.[RESTART](#kw-RESTART) files into OPM ResInsight to view the data graphically, this also has the benefit of being able to filter the grid based on I, J, K ranges and grid properties.
:::


#### Examples

The first example shows the original format of this keyword; although the keyword and format are recognized by OPM Flow, the format is ignored and is unlikely to be implemented in in the simulator.


```
--
--       DEFINE SOLUTION SECTION REPORT OPTION (ORIGINAL FORMAT)
–
RPTSOL
         1        2*0      1        3*1                                        /
```

The next example shows the second format of the keyword which may be supported in a future release of OPM Flow.


```
--
--       DEFINE SOLUTION SECTION REPORT OPTIONS
--
RPTSOL
         FIP=2    FIPRESV  RESTART=3                                           /


```