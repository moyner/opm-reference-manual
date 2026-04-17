### MULTREGD – Multiply Diffusivities Between Regions {#kw-MULTREGD}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The MULTREGD keyword multiplies the diffusivity between two regions by a constant. The region number array can be [FLUXNUM](#kw-FLUXNUM), [MULTNUM](#kw-MULTNUM) or [OPERNUM](#kw-OPERNUM) and these arrays must be defined and be available before the MULTREGD keyword is read by the simulator. The constant should be a real number.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | REGION1 | A positive integer value that defines the from REGION number for which the CONSTANT in (3) should be applied. | None |
| 2 | REGION2 | A positive integer value that defines the to REGION number for which the CONSTANT in (3) should be applied. | None |
| 3 | CONSTANT | A real value to multiply the diffusivity between REGION1 and REGION2. | 1 |
| 4 | DIR | A character string that defines the direction to apply the diffusivity multiplier between the two regions, should be set to one of the following X, Y, Z, XY, XZ, YZ, or XYZ. | XYZ |
| 5 | TYPE | A character string that defines the type of connections the diffusivity multiplier should be applied to, should be one of the following: | [ALL](#kw-ALL) |
| 6 | REGION ARRAY | The REGION ARRAY to use for applying the CONSTANT in (3) based on the regions REGION1 and REGION2 in (1 and 2).  REGION ARRAY can have the following values: | M |
| Notes: |  |  |  |
: MULTREGD Keyword Description {#tbl-6-76}
#### Example


```
--
--    MULTIPLY DIFFUSIVITIES BETWEEN RESERVOIRS
--
--    REGION   REGION   DIFFS   DIREC   NNC    REGION ARRAY
--    FROM     TO       MULT    OPT     OPTS   M / F / O
MULTREGD
      1*       1*       1.05    1*     'ALL'   M           / ALL REGIONS
/

```

The above example multiplies the diffusivities between all the [MULTNUM](#kw-MULTNUM) regions by 1.05 in all directions and for all connections types.