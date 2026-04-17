### RPTGRIDL – Define GRID Section Reporting for LGRs {#kw-RPTGRIDL}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword defines the data in the [GRID](#kw-GRID) section that is to be printed to the output print file in human readable format for Local Grid Refinements (“LGRs”), for when LGRs have been activated for the input deck using the [LGR](#kw-LGR) keyword in the [RUNSPEC](#kw-RUNSPEC) section.

The keyword has two distinct forms, the first of which consists of the keyword followed by a series of integers on the next line indicating the data to be printed (see the first example). This is the original formal in the commercial simulator and was subsequently superseded by the second format. The second format consists of the keyword followed by a series of character strings that indicate the data to be printed. In most cases the character string is the keyword used to load the data in the OPM Flow input deck, for example [PORO](#kw-PORO) for the porosity array. Its is anticipated that OPM Flow will eventually support the functionality of the second format only, the first format although recognized will be completely ignored.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | ALLNCC | Print all the non-neighbor connections. | N/A |
| 2 | [COORD](#kw-COORD) | Print the coordinate lines. | N/A |
| 3 | COORDYS | Print the coordinate systems. | N/A |
| 4 | [DEPTH](#kw-DEPTH) | Print grid cells center depths. | N/A |
| …. |  | …. | N/A |
| 24 | ALLNNC | ALLNNC is a defined positive integer that specifies the type of Non-Neighbor Connections (“[NNC](#kw-NNC)”) to be printed, and should be set to one of the follow: | N/A |
| …. |  | …. | N/A |
| 57 | [EXTHOST](#kw-EXTHOST) | EXTHOSTS outputs host cells for Perpendicular Bisector (“[PEBI](#kw-PEBI)”)^[Heinemann, Z.E. and Brand, C.W. 1988. Gridding Techniques in Reservoir Simulation. Proc., First Intl. Forum on Reservoir Simulation, Alpbach, Austria, 339.] and ^[Heinemann, Z.E., Brand, C.W., Munka, M. et al. 1991. Modeling Reservoir Geometry With Irregular Grids. SPE Res Eng 6 (2): 225–232. SPE-18412-PA. http://dx.doi.org/10.2118/18412-PA]  LGRs. |  |
| …. |  | …. | N/A |
| Notes: |  |  |  |
: RPTGRIDL Keyword Description {#tbl-6-117}
::: {.callout-note}
This keyword has the potential to produce very large print files that some text editors may have difficulty loading, coupled with the fact that reviewing the data in this format is very cumbersome. A more efficient solution is to load the *.[INIT](#kw-INIT) file into OPM ResInsight to view the data graphically, this also has the benefit of being able to filter the grid based on I, J, K ranges and grid properties.
:::


#### Examples

The first example shows the original format of this keyword; although the keyword and format are recognized by OPM Flow, the format is ignored and is unlikely to be implemented in in the simulator.


```
--
--       DEFINE LGR GRID SECTION REPORT OPTION (ORIGINAL FORMAT)
–
RPTGRIDL
         1        2*0      1        3*1                                        /
```

The next example shows the second format of the keyword which may be supported in a future release of OPM Flow.


```
--       DEFINE LGR GRID SECTION REPORT OPTIONS
--
RPTGRIDL
         DX       DY       DZ       DEPTH    PORO     PERMX                    /
```