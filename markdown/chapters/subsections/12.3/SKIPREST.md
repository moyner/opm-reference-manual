### SKIPREST – Activate Skipping of Restart Schedule Data {#kw-SKIPREST}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword turns on skipping of keywords up to the start of the restart point, as defined on the [RESTART](#kw-RESTART) keyword in the [RUNSPEC](#kw-RUNSPEC) section. The [RESTART](#kw-RESTART) keyword defines the parameters to restart the simulation from a previous run that has written a [RESTART](#kw-RESTART) file out to disk. Activating the SKIPREST keyword causes the simulator to only read in data it requires for restarting the run up to the [RESTART](#kw-RESTART) point (RSNUM on the [RESTART](#kw-RESTART) keyword in the [SOLUTION](#kw-SOLUTION) section). Note that certain keywords always need to be present in a restart run in the [SCHEDULE](#kw-SCHEDULE) section as the data is not stored on the [RESTART](#kw-RESTART) file, for example the VFP tables ([VFPPROD](#kw-VFPPROD) and [VFPINJ](#kw-VFPINJ) keywords). The SKIPREST keyword automatically processes the input deck and reads the required data.

There is no data required for this keyword.


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


Then in the [SCHEDULE](#kw-SCHEDULE) section the SKIPREST keyword is used to correctly read in the schedule data up to the [RESTART](#kw-RESTART) point.


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