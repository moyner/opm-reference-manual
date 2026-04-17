### RESTART – Restart Run From an Existing Restart File {#kw-RESTART}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The RESTART keyword defines the parameters to restart the simulation from a previous run that has written a RESTART file out to disk. Only restarting from RESTART files is permitted by OPM Flow; restarting from [SAVE](#kw-SAVE) files is not implemented.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | RSNAME | The RSNAME variable is a character string that defines the root name of the RESTART file to be read into the current input deck. | None |
| 2 | RSNUM | A positive integer that defines the restart point on the RESTART file to be read and to be used to initialize the model. When OPM Flow writes a restart point a message is printed to the *.PRT file indicating the time step the restart was written out. | None |
| 3 | RSTYPE | A defined character sting set to [SAVE](#kw-SAVE) to read the restart data from the [SAVE](#kw-SAVE) file, otherwise defaulted to 1* to read the data from the RESTART file. The [SAVE](#kw-SAVE) file option is not supported by OPM Flow and should be defaulted with 1*. | 1* |
| 4 | RSFORMAT | A defined character string that defines the format of the [SAVE](#kw-SAVE) file to be read if RSTYPE has been set to [SAVE](#kw-SAVE), and should be set to one of the following: If the variable RSFORMAT omitted then the default is for binary file input. This option is not supported by OPM Flow and should be defaulted with 1*. | U |
| Notes: |  |  |  |
: RESTART Keyword Description {#tbl-10-25}
The most direct way to start a restart run is to:

- Copy the existing data file that created the RESTART file and give it a new name. For example if the RESTART file is from a case named NOR-OPM-A01.DATA, then the copied data file could be named NOR-OPM-A01-R1.DATA.
- Edit the copied data file (NOR-OPM-A01-R1.DATA) and delete all equilibration keywords ([EQUIL](#kw-EQUIL), [RSVD](#kw-RSVD), etc.) or the enumeration equilibration keywords ([PRESSURE](#kw-PRESSURE), [SGAS](#kw-SGAS), [SOIL](#kw-SOIL). [SWAT](#kw-SWAT), etc.) in the [SOLUTION](#kw-SOLUTION) section used to initialize the model.
- In the [SOLUTION](#kw-SOLUTION) section of NOR-OPM-A01-R1.DATA file insert the RESTART keyword, using NOR-OPM-A01 as RSNAME and the required RSNUM value for the time step to restart from.
- In the [SCHEDULE](#kw-SCHEDULE) section of NOR-OPM-A01-R1.DATA file insert the [SKIPREST](#kw-SKIPREST) keyword at the very beginning of the [SCHEDULE](#kw-SCHEDULE) section. The [SKIPREST](#kw-SKIPREST) keyword causes the simulator to only read in data it requires for restarting the run up to the RESTART point (RSNUM). Note that certain keywords always need to be present in a restart run in the [SCHEDULE](#kw-SCHEDULE) section as the data is not stored on the RESTART file, for example the VFP tables ([VFPPROD](#kw-VFPPROD) and [VFPINJ](#kw-VFPINJ) keywords). The [SKIPREST](#kw-SKIPREST) keyword automatically processes the input deck and reads the required data.
- In the [SCHEDULE](#kw-SCHEDULE) section of NOR-OPM-A01-R1.DATA file after the RESTART point make any required changes, save the file and run the NOR-OPM-A01-R1.DATA with OPM Flow.

See also [RPTRST](#kw-RPTRST), [RPTSCHED](#kw-RPTSCHED) and [SKIPREST](#kw-SKIPREST) keywords.


#### Example

The example below defines a restart from the previously run NOR-OPM-A01 case at time step number 40.


```
-- ==============================================================================
--
-- SOLUTION SECTION
--
-- ==============================================================================
SOLUTION
--
--       FLEXIBLE RESTART FROM PREVIOUS SIMULATION RUN
--
--       FILE                   RESTART   RESTART   FILE
--       NAME                   NUMBER    TYPE      FORMAT
RESTART
         'NOR-OPM-A01'          40        1*        1*     /
```


In addition in the [SCHEDULE](#kw-SCHEDULE) section the [SKIPREST](#kw-SKIPREST) keyword should be used to correctly read in the schedule data up to the RESTART point.


```
-- ==============================================================================
--
-- SCHEDULE SECTION
--
-- ==============================================================================
SCHEDULE
--
--       ACTIVATE SKIPREST OPTION TO AVOID MODIFYING SCHEDULE SECTION
--
SKIPREST

```

Note is advisable to place the [SKIPREST](#kw-SKIPREST) keyword at the very beginning of the [SCHEDULE](#kw-SCHEDULE) section.