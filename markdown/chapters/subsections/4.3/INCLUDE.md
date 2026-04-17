### INCLUDE – Load Another Data File at the Current Position {#kw-INCLUDE}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The INCLUDE keyword informs OPM Flow to continue reading input data from the specified INCLUDE file. When the end of the INCLUDE file is reached, or the [ENDINC](#kw-ENDINC) keyword is encountered in the included file, input data is read from the next keyword in the current file. Although INCLUDE files can be nested, that is INCLUDE files within INCLUDE files etc., in practice this should be avoided due to the complexity of tracking the files.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | FILENAME | A character string enclosed in quotes that defines a file to read in and be processed by OPM Flow. | None |
| Notes: |  |  |  |
: INCLUDE Keyword Description {#tbl-4-4}
#### Examples

The first example shown below loads the grid file from the same directory as the data file.


```
--
--       LOAD INCLUDE FILE
--
INCLUDE
         'NOR-OPM-A00-GRID.inc'  /

```

The next example loads the same file one directory above from where the data file is located.


```
--
--       LOAD INCLUDE FILE
--
INCLUDE
         '../NOR-OPM-A00-FAULTS.inc'  /
```


The final example loads the same file from a separate include directory found in the parent directory relative to where the data file is located.


```
--
--       LOAD INCLUDE FILE
--
INCLUDE
         '../INCLUDE/NOR-OPM-A00-FAULTS.inc'  /
```