### WSKPTAB – Assign Well Polymer Molecular Model Skin Tables {#kw-WSKPTAB}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The WSKPTAB keyword assigns the well polymer molecular water and polymer skin tables to water injection wells in OPM Flow's Polymer Molecular Weight Transport option, that uses the polymer molecular weight in calculating the polymer viscosity, as well as accounting for formation damage due to the water and polymer injection, by adjusting the wellbore skin pressure. This keyword should only be used if the [POLYMER](#kw-POLYMER) and [POLYMW](#kw-POLYMW) keywords in the [RUNSPEC](#kw-RUNSPEC) section are also activated. The keyword assigns the water [SKPRWAT](#kw-SKPRWAT) tables, that are defined via the [SKPRWAT](#kw-SKPRWAT) keyword in the [PROPS](#kw-PROPS) section, that are used to calculable the wellbore skin pressure during water injection. As well as the polymer [SKPRPOLY](#kw-SKPRPOLY) tables, that are defined via the [SKPRPOLY](#kw-SKPRPOLY) keyword in the [PROPS](#kw-PROPS) section, that are used to calculable the wellbore skin pressure during polymer injection.


::: {.callout-note}
This is an OPM Flow specific keyword that employs an alternative polymer flood model based on a Polymer Molecular Weight Transport equation, that is not available in the commercial simulator.
:::


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | WELNAME | A character string of up to eight characters in length, that defines the water injection well name, for which the well water injection skin table, SKKPRWAT, and the polymer skin injection table, [SKPRPOLY](#kw-SKPRPOLY), are to be assigned. Note that the well name (WELNAME) must have been declared previously using the [WELSPECS](#kw-WELSPECS) keyword in the [SCHEDULE](#kw-SCHEDULE) section, otherwise an error may occur. | None |
| 2 | [SKPRWAT](#kw-SKPRWAT) | A positive integer value that defines the corresponding [SKPRWAT](#kw-SKPRWAT) table to be allocated to the water injection well. A value less than or equal to zero means that no [SKPRWAT](#kw-SKPRWAT) table is allocated to the well | 0 |
| 3 | [SKPRPOLY](#kw-SKPRPOLY) | A positive integer value that defines the corresponding [SKPRPOLY](#kw-SKPRPOLY) table to be allocated to the water injection well. A value less than or equal to zero means that no [SKPRPOLY](#kw-SKPRPOLY) table is allocated to the well | 0 |
| Notes: |  |  |  |
: WSKPTAB Keyword Description {#tbl-12-123}
See also the [SKPRWAT](#kw-SKPRWAT) and [SKPRPOLY](#kw-SKPRPOLY) keywords in the [PROPS](#kw-PROPS) section, that describe the relationship of the wellbore skin pressure with respect to the injected water and polymer throughput and fluid velocity, for the simulator's Polymer Molecular Weight Transport option. As well as the [PLYMWINJ](#kw-PLYMWINJ) and [PLYVMH](#kw-PLYVMH) keywords, also in the [PROPS](#kw-PROPS) section, that are the additional keywords required for the Polymer Molecular Weight Transport option.

The [WPMITAB](#kw-WPMITAB) keyword in the [SCHEDULE](#kw-SCHEDULE) section may be used to assign the [PLYMWINJ](#kw-PLYMWINJ) keyword in the [PROPS](#kw-PROPS) section. Where [PLYMWINJ](#kw-PLYMWINJ), describes the relationship of the injected polymer molecular weight as a function of polymer throughput and polymer velocity, for the simulator's Polymer Molecular Weight Transport option

Note that the standard polymer property data keywords: [PLYROCK](#kw-PLYROCK), [PLYADS](#kw-PLYADS), [PLYMAX](#kw-PLYMAX), etc., are still required to fully describe the polymer fluid.


#### Example

Given NTSKWAT equals two and NTSKPOLY equals three on the [PINTDIMS](#kw-PINTDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section,  then:


```
--
--       ASSIGN WELL POLYMER MOLECULAR MODEL SKIN TABLES
--
-- WELL  SKPRWAT   SKPRPOLY
-- NAME  TABLE     TABLE
WSKPTAB
WI01     1         1                                              /
WI02     1         3                                              /
WI03     2         2                                              /
/
```

Assigns [SKPRWAT](#kw-SKPRWAT) table one to wells WI01 and WI02 and table two to WI03, and [SKPRPOLY](#kw-SKPRPOLY) tables one, two and three to wells WI01, WI03, and WI02, respectively.