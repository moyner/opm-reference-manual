### PLYMWINJ – Polymer Molecular Weight Model Throughput and Velocity Table


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword, PLYMWINJ,  describes the relationship of the injected polymer molecular weight as a function of polymer throughput and polymer velocity, for the simulator's Polymer Molecular Weight Transport option, that uses the polymer molecular weight in calculating the polymer viscosity. The table is a two dimensional table that relates the polymer throughput values and velocity values to derive the resulting molecular weight of the injected polymer, which is then used via the PLYVHM keyword in the PROPS section, to derive the polymer molecular weight scaled viscosity.

This keyword should only be used if the POLYMER and POLYMW keywords in the RUNSPEC section are also activated.


::: {.callout-note}
This is an OPM Flow specific keyword that employs an alternative polymer flood model based on a Polymer Molecular Weight Transport equation, that is not available in the commercial simulator. The model has been tested using metric units; however, using either field or laboratory units with the option should be considered experimental.
:::


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1-1 | PLYMWNUM | A positive integer value greater than zero and less than or equal to the NTPMWINJ variable, as defined on the PINTDIMS keyword in the RUNSPEC section, that defines the PLYMWINJ Polymer Molecular Weight Model throughput and velocity table number. | None |
| 2-1 | THRUPUT | A real positive monotonically increasing vector, that defines the polymer throughput values.  The first entry should be zero to define a no throughput data set, and each vector record should be on a separate line terminated by a “/”. | None |
| feet3/feet2 | m3/m2 | cm3/cm2 |  |
| 3-1 | VELOCITY | A real positive monotonically increasing vector, that defines the polymer velocity values. The first entry should be zero to define a no velocity data set, and each vector record should be on a separate line terminated by a “/”. | None |
| feet/day | m/day | cm/hour |  |
| 4-1 | POLYMW | A series of real positive vectors representing the polymer molecular weights for all combinations of the polymer throughput values (THRUPUT) and velocity values (VELOCITY), organized as a series of vectors POLYMW(THRUPUT, VELOCITY). Thus, the first vector represents the molecular weights of the first THRUPUT value and each entry in the vector is the corresponding molecular weight of the associated VELOCITY vector. Each vector should be on a separate line and should be terminated by a “/”. Thus, if THRUPUT has three entries and VELOCITY has four, then there should be three vectors, with each vector containing four elements representing molecular weight values, as a function of THRUPUT and VELOCITY. | None |
| lb/lb-M | kg/kg-M | gm/gm-M |  |
| Notes: |  |  |  |

*Table 8.104: PLYMWINJ Keyword Description*


Unlike other PROPS section table keywords, that enable multiple tables following the keyword to be entered, the PLYMWINJ keyword requires that the keyword itself must be repeated for each table, as is shown in the example on the following page.

See also the WPMITAB keyword in the SCHEDULE section, that assigns the PLYMWINJ tables to the water injection wells,  as well as the SKPRWAT, SKPRPOLY, and PLYVMH keywords, in the PROPS section, that are the additional property keywords required for the Polymer Molecular Weight Transport option.

The WSKPTAB keyword in the SCHEDULE section may be used to assign the SKPRPOLY and SKPRWAT tables to water injections wells, that enable the calculation of the wellbore skin pressure based on the fluids being injected.

Note that the standard polymer property data keywords: PLYROCK, PLYADS, PLYMAX, etc., are still required to fully describe the polymer fluid.


#### Example

Given NTPMWINJ equals two on the PINTDIMS keyword in the RUNSPEC section,  then two PLYWINJ tables are required to be entered:


```
--
--       POLYMER MOLECULAR WEIGHT MODEL THROUGHPUT AND VELOCITY TABLE
--       (OPM FLOW PROPS KEYWORD)
--
PLYMWINJ
         1                             / TABLE NUMBER
--
--       THROUGHPUT VALUES
--
         0.0     200.0   400.0         /
--
--       VELOCITY VALUES
--
         0.0     50.0    80.0    100.0 /
--
--       POLYMW VALUES
--
         20.0    19.0    18.0    16.0  / POLYMW(OUTPUT=1, VELOCITY=1 TO N)
         20.0    16.0    14.0    12.0  / POLYMW(OUTPUT=2, VELOCITY=1 TO N)
         20.0    12.0     8.0     4.0  / POLYMW(OUTPUT=3, VELOCITY=1 TO N)
/
PLYMWINJ
         2                             / TABLE NUMBER
--
--       THROUGHPUT VALUES
--
         0.0     200.0   400.0         /
--
--       VELOCITY VALUES
--
         0.0     50.0    70.0    100.0 /
--
--       POLYMW VALUES
--
         20.0    19.0    18.0    16.0  / POLYMW(OUTPUT=1, VELOCITY=1 TO N)
         20.0    16.0    14.0    12.0  / POLYMW(OUTPUT=2, VELOCITY=1 TO N)
         20.0    12.0     8.0     4.0  / POLYMW(OUTPUT=3, VELOCITY=1 TO N)
/

```

As mentioned previously, the PLYMWINJ keyword requires that the keyword itself must be repeated for each table, as is shown in the above example.
