### FOAMROCK – Define Foam Rock Properties {#kw-FOAMROCK}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The FOAMROCK keyword defines the foam rock properties for when the Foam option has been activated by the [FOAM](#kw-FOAM) keyword in the [RUNSPEC](#kw-RUNSPEC) section.

The keyword is recognized by the input deck parser and simulator support is available in the experimental "ebos" simulator.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | ADINDX | A positive integer of 1 or 2 that defines foam desorption option, as per: Only the default value of 1 is supported by OPM Flow. | Defined |
| dimensionless 1 | dimensionless 1 | dimensionless 1 |  |
| 2 | [DENSITY](#kw-DENSITY) | A real value that defines the rock in situ density, that is at reservoir conditions. | None |
| lb/rb | kg/rm3 | gm/rcc |  |
| Notes: |  |  |  |
: FOAMROCK Keyword Description {#tbl-8-38}
::: {.callout-note}
In the commercial simulator if the [POLYMER](#kw-POLYMER) and [SURFACT](#kw-SURFACT) phases have been activated in conjunction with the [FOAM](#kw-FOAM) phase then the mass density of rock will be set by the [PLYROCK](#kw-PLYROCK), [SURFROCK](#kw-SURFROCK), or the FOAMROCK keywords depending on the order entered in the run deck. This is not the case for OPM Flow. OPM Flow’s [FOAM](#kw-FOAM) phase is a standalone implementation and cannot be used in conjunction with the either the [POLYMER](#kw-POLYMER) or [SURFACT](#kw-SURFACT) phases.
:::


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

The above example defines three foam-rock tables, based on the NTSFUN variable on the [TABDIMS](#kw-TABDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section being equal to three.

There is no terminating “/” for this keyword.