### WPMITAB – Assign Well Polymer Molecular Model Injection Tables {#kw-WPMITAB}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The WPMITAB keyword assigns the well polymer molecular injection tables to water injection wells in OPM Flow's Polymer Molecular Weight Transport option, that uses the polymer molecular weight in calculating the polymer viscosity, as well as accounting for formation damage due to the water and polymer injection, by adjusting the wellbore skin pressure. This keyword should only be used if the [POLYMER](#kw-POLYMER) and [POLYMW](#kw-POLYMW) keywords in the [RUNSPEC](#kw-RUNSPEC) section are also activated. The keyword assigns the [PLYMWINJ](#kw-PLYMWINJ) tables that are defined via the [PLYMWINJ](#kw-PLYMWINJ) keyword in the [PROPS](#kw-PROPS) section.


::: {.callout-note}
This is an OPM Flow specific keyword that employs an alternative polymer flood model based on a Polymer Molecular Weight Transport equation, that is not available in the commercial simulator.
:::


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | WELNAME | A character string of up to eight characters in length, that defines the water injection well name, for which the well polymer molecular injection table, [PLYMWINJ](#kw-PLYMWINJ), is to be assigned. Note that the well name (WELNAME) must have been declared previously using the [WELSPECS](#kw-WELSPECS) keyword in the [SCHEDULE](#kw-SCHEDULE) section, otherwise an error may occur. | None |
| 2 | [PLYMWINJ](#kw-PLYMWINJ) | A positive integer value that defines the corresponding [PLYMWINJ](#kw-PLYMWINJ) table to be allocated to the water injection well. A value less than or equal to zero means that no PLYMWIN table is allocated to the well | 0 |
| Notes: |  |  |  |
: WPMITAB Keyword Description {#tbl-12-113}
See also the [PLYMWINJ](#kw-PLYMWINJ) keyword in the [PROPS](#kw-PROPS) section, that describes the relationship of the injected polymer molecular weight as a function of polymer throughput and polymer velocity, for the simulator's Polymer Molecular Weight Transport option, as well as the [SKPRWAT](#kw-SKPRWAT), [SKPRPOLY](#kw-SKPRPOLY), and [PLYVMH](#kw-PLYVMH) keywords, also in the [PROPS](#kw-PROPS) section, that are the additional keywords required for the Polymer Molecular Weight Transport option.

The [WSKPTAB](#kw-WSKPTAB) keyword in the [SCHEDULE](#kw-SCHEDULE) section may be used to assign the [SKPRWAT](#kw-SKPRWAT) and SKPRPOL tables to water injections wells, that enable the calculation of the wellbore skin pressure based on the fluids being injected.

Note that the standard polymer property data keywords: [PLYROCK](#kw-PLYROCK), [PLYADS](#kw-PLYADS), [PLYMAX](#kw-PLYMAX), etc., are still required to fully describe the polymer fluid.


#### Example

Given NTPMWINJ equals two on the [PINTDIMS](#kw-PINTDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section,  then:


```
--
--       ASSIGN WELL POLYMER MOLECULAR MODEL INJECTION TABLES
--
-- WELL  PLYMWINJ
-- NAME  TABLE
WPMITAB
WI01     1                                                        /
WI02     1                                                        /
WI03     2                                                        /
/

```

Assigns [PLYMWINJ](#kw-PLYMWINJ) table one to wells WI01 and WI02 and table two to WI03.