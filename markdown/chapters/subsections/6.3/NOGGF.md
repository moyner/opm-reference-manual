### NOGGF – Deactivate Output of Grid Geometry File {#kw-NOGGF}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword deactivates the output of a standard [GRID](#kw-GRID) or extended [GRID](#kw-GRID) file, as well as the extensible EGRID file for post-processing applications.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

There is no data required for this keyword and there is no terminating “/” for this keyword.


#### Example


```
--
--       DEACTIVATE GRID GEOMETRY OUTPUT
--
NOGGF

```

The above example switches off the default behavior of writing out the grid geometry files.