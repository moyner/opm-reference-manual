### GDFILE – Load a Grid File {#kw-GDFILE}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The GDFILE keyword loads a [GRID](#kw-GRID) file that contains the structural data for the grid as a set of topological cuboidal cells, and EGRID files that contain structural and property data. Note OPM Flow only supports reading in EGRID files at this time.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | [GRIDFILE](#kw-GRIDFILE) | A character string enclosed in quotes that defines the [GRID](#kw-GRID) or EGRID file to be read in and be processed by OPM Flow. Again, OPM Flow only supports reading in EGRID files. | None |
| 2 | FMTOPT | A defined character string that defines the format of the [GRID](#kw-GRID) or EGRID file to be read and should be set to one of the following: If the variable FMTOPT is omitted then the default is for binary file input for the commercial simulator; whereas, OPM Flow derives FMTOPT from the file extension (*.EGRID or *.FEGRID), making FMTOPT superfluous. | U |
| Notes: |  |  |  |
: GDFILE Keyword Description {#tbl-6-40}
See also the [GRIDFILE](#kw-GRIDFILE) keyword in the [GRID](#kw-GRID) section for exporting the [GRID](#kw-GRID) and EGRID files from the current simulation run.


#### Examples

The first example shown below loads the NOR-OPM-A00-[GRID](#kw-GRID).EGRID file in binary format from the same directory as the data file.


```
--
--       LOAD A GRID FILE
--
GDFILE
         'NOR-OPM-A00-GRID.EGRID'      /

```

The next example loads the same EGRID file one directory above from where the data file is located.


```

--
--       LOAD a GRID FILE
--
GDFILE
         '../NOR-OPM-A00-GRID.EGRID'  /


```