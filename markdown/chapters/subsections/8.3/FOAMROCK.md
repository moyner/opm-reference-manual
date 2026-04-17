### FOAMROCK – Define Foam Rock Properties


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The FOAMROCK keyword defines the foam rock properties for when the Foam option has been activated by the FOAM keyword in the RUNSPEC section.

The keyword is recognized by the input deck parser and simulator support is available in the experimental "ebos" simulator.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | ADINDX | A positive integer of 1 or 2 that defines foam desorption option, as per: Only the default value of 1 is supported by OPM Flow. | Defined |
| dimensionless 1 | dimensionless 1 | dimensionless 1 |  |
| 2 | DENSITY | A real value that defines the rock in situ density, that is at reservoir conditions. | None |
| lb/rb | kg/rm3 | gm/rcc |  |
| Notes: |  |  |  |

*Table 8.38: FOAMROCK Keyword Description*


| Note In the commercial simulator if the POLYMER and SURFACT phases have been activated in conjunction with the FOAM phase then the mass density of rock will be set by the PLYROCK, SURFROCK, or the FOAMROCK keywords depending on the order entered in the run deck. This is not the case for OPM Flow. OPM Flow’s FOAM phase is a standalone implementation and cannot be used in conjunction with the either the POLYMER or SURFACT phases. |
| --- |


#### Example


```
--
--       FOAM-ROCK PROPERTIES
--
FOAMROCK
--       DESORP   INSITU
--       OPTN     DENSITY
--       ------   -------
           1      1800.0                                   / TABLE NO. 01
           2      1980.0                                   / TABLE NO. 02
           1      2005.0                                   / TABLE NO. 03

```

The above example defines three foam-rock tables, based on the NTSFUN variable on the TABDIMS keyword in the RUNSPEC section being equal to three.

There is no terminating “/” for this keyword.
