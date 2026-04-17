### FOAMOPTS – Define Foam Model Options {#kw-FOAMOPTS}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The FOAMOPTS keyword defines the transport phase for the foam (gas, water or solvent) and how gas mobility reduction should be calculated for when the Foam option has been activated by the [FOAM](#kw-FOAM) keyword in the [RUNSPEC](#kw-RUNSPEC) section.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | FOAMOPT1 | A defined character string that specifies the transport phase for the foam, and should be set to one of the following: | [GAS](#kw-GAS) |
| 2 | FOAMOPT2 | A defined character string that specifies the method to be used to calculate the reduction in gas mobility, and should be set to one of the following: Only the default value of TAB is currently supported by OPM Flow. | TAB |
| Notes: |  |  |  |
: FOAMOPTS Keyword Description {#tbl-8-3-70-1}
#### Example


```
--
--       FOAMOPT1  FOAMOPT2
--       PHASE     MOBILITY
--       --------  --------
FOAMOPTS
         GAS       TAB                                     / FOAM MODEL OPTIONS
```


The above example defines the transport phase is to be gas and the gas mobility reduction is to use a table as defined by the [FOAMMOB](#kw-FOAMMOB) keyword as a function of foam concentration, the [FOAMMOBS](#kw-FOAMMOBS) keyword as a function of shear, or as a function of pressure using the [FOAMMOBP](#kw-FOAMMOBP) keyword.