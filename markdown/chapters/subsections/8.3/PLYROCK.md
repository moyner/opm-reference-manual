### PLYROCK – Define Polymer-Rock Properties


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The PLYROCK keyword defines rock properties for when the Polymer option has been activated by the POLYMER keyword in the RUNSPEC section.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | PSPACE | A real positive value that is greater than or equal to zero and less the maximum water saturation and less than one, that defines available pore space for this rock type. | None |
| dimensionless | dimensionless | dimensionless |  |
| 2 | PERMFAC | A real positive value that is greater than or equal to one that defines decrease in the rock permeability to the water phase when the maximum amount of polymer has been adsorbed. | None |
| dimensionless | dimensionless | dimensionless |  |
| 3 | DENSITY | A real value that defines the rock in-situ density, that is at reservoir conditions. | None |
| lb/rb | kg/rm3 | gm/rcc |  |
| 4 | ADINDX | A positive integer of 1 or 2 that defines the polymer desorption option. | Defined |
| dimensionless 1 | dimensionless 1 | dimensionless 1 |  |
| 5 | POLMAX | A real positive non-zero value that defines the maximum polymer adsorption to be used in the calculation of the resistance factor for the water phase. | None |
| lb/lb | kg/kg | gm/gm |  |
| Notes: |  |  |  |

*Table 8.105: PLYROCK Keyword Description*


#### Example


```
--
--       POLYMER-ROCK PROPERTIES
--
PLYROCK
--       PORE      PERM      INSITU    DESORP  MAX
--       SPACE     FACTOR    DENSITY   OPTN    POLY
--       ------   --------   -------   ------  -------
         0.1200    1.7500    1800.0      1     0.00012     / TABLE NO. 01
         0.1300    1.8500    1980.0      2     0.00015     / TABLE NO. 02
         0.1500    1.9500    2005.0      1     0.00014     / TABLE NO. 03
```


The above example defines three polymer-rock tables, based on the NTSFUN variable on the TABDIMS keyword in the RUNSPEC section being equal to three.

There is no terminating “/” for this keyword.
