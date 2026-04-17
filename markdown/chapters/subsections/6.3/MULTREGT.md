### MULTREGT – Multiply Transmissibilities Between Regions


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The MULTREGT keyword multiplies the transmissibility between two regions by a constant. The region number array can be FLUXNUM, MULTNUM or OPERNUM and these arrays must be defined and be available before the MULTREGT keyword is read by the simulator. The constant should be a real number.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | REGION1 | A positive integer value that defines the from REGION number for which the CONSTANT in (3) should be applied. | None |
| 2 | REGION2 | A positive integer value that defines the to REGION number for which the CONSTANT in (3) should be applied. | None |
| 3 | CONSTANT | A real positive value to multiply the transmissibility between REGION1 and REGION2. | 1 |
| 4 | DIR | A character string that defines the direction to apply the transmissibility multiplier between the two regions, should be set to one of the following X, Y, Z, XY, XZ, YZ, or XYZ. | XYZ |
| 5 | TYPE | A character string that defines the type of connections the transmissibility multiplier should be applied to, should be one of the following: | ALL |
| 6 | REGION ARRAY | A single character that defines the REGION ARRAY that is used to specify the regions identified by REGION1 and REGION2.  REGION ARRAY can have the following values: | M |
| Notes: |  |  |  |

*Table 6.79: MULTREGT Keyword Description*


| Note Note if the MULTREGT keyword is used in the EDIT section, OPM Flow will always apply the changes irrespective, of if the TRANX, TRANY and TRANZ transmissibility arrays have been entered or not in the EDIT section. This behavior is different to the commercial simulator that only applies the keyword if the transmissibility arrays have been entered in the EDIT section. |
| --- |


#### Example


```
--
--    SET TRANSMISSIBILITES ACROSS DIFFERENT RESERVOIRS TO ZERO
--
--    REGION   REGION   TRANS   DIREC   NNC    REGION ARRAY
--    FROM     TO       MULT    OPT     OPTS   M / F / O
MULTREGT
      1*       1*       0.0     1*     'ALL'   M           / ALL REGIONS SEALED
/

```

The above example isolates all regions from one another by setting the transmissibility for the MULTNUM regions to zero in all directions and for all connections types.
