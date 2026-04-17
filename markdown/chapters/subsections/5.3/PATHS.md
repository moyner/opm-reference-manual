### PATHS – Define Filename Directory Path Aliases {#kw-PATHS}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

PATHS allows the user to define alias directory filenames to avoid long filenames with the [INCLUDE](#kw-INCLUDE), [IMPORT](#kw-IMPORT), [RESTART](#kw-RESTART) or [GDFILE](#kw-GDFILE) keywords.  To use the alias with the aforementioned keywords PATHS should be prefixed with the $ symbol.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | ALIAS | A character string enclosed in quotes defining the alias. | None |
| 2 | DIRC | A character string enclosed in quotes defining the directory filename. | None |
| Notes: |  |  |  |
: PATHS Keyword Description {#tbl-5-34}
#### Examples


```
--
--       PATH       PATH
--       ALIAS      DIRECTORY FILENAME
PATHS
        'GRID'      '/DISK1/NORNE/2017/GRID-INCLUDES'                          /
        'SCHD'      '/DISK1/NORNE/2017/SCHD-INCLUDES'                          /
/

```

The above example defines “[GRID](#kw-GRID)” and “SCHD” aliases in the [RUNSPEC](#kw-RUNSPEC) section than can be used in the [GRID](#kw-GRID) and [SCHEDULE](#kw-SCHEDULE) sections of the input deck. The next example shows how to use the “[GRID](#kw-GRID)” alias with the [INCLUDE](#kw-INCLUDE) keyword in the [GRID](#kw-GRID) section.


```
--
--       LOAD INCLUDE FILES
--
INCLUDE
         '$GRID/PORO.INC'                                                      /

INCLUDE
         '$GRID/PERMX.INC'                                                     /

INCLUDE
         '$GRID/NTG.INC'                                                       /
```


Here the porosity, permeability and net-to-gross arrays are loaded in the [GRID](#kw-GRID) section using the directory filename aliases declared in the [RUNSPEC](#kw-RUNSPEC) section.