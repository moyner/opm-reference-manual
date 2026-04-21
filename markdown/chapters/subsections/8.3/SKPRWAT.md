### SKPRWAT – Polymer Molecular Weight Model Water Injection Skin Table


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword, SKPRWAT, describes the relationship of a water injection well's injected water skin pressure as a function of water throughput and water velocity, for the simulator's Polymer Molecular Weight Transport option. The table is a two dimensional table that relates the water throughput values and water velocity values to derive the resulting wellbore skin pressure of the injected water, which is then used to calculate the total wellbore skin pressure based on the polymer concentration.

This keyword should only be used if the POLYMER and POLYMW keywords in the RUNSPEC section are also activated.


::: {.callout-note}
This is an OPM Flow specific keyword that employs an alternative polymer flood model based on a Polymer Molecular Weight Transport equation, that is not available in the commercial simulator. The model has been tested using metric units; however, using either field or laboratory units with the option should be considered experimental.
:::


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1-1 | SKPRWNUM | A positive integer value greater than zero and less than or equal to the NTSKWAT variable, as defined on the PINTDIMS keyword in the RUNSPEC section, that defines the SKPRWAT Polymer Molecular Weight Model water injection skin pressure table number. | None |
| 2-1 | THRUPUT | A real positive monotonically increasing vector, that defines the water throughput values.  The first entry should be zero to define a no throughput data set, and each vector record should be on a separate line terminated by a “/”. | None |
| feet3/feet2 | m3/m2 | cm3/cm2 |  |
| 3-1 | VELOCITY | A real positive monotonically increasing vector, that defines the water velocity values. The first entry should be zero to define a no velocity data set, and each vector record should be on a separate line terminated by a “/”. | None |
| feet/day | m/day | cm/hour |  |
| 4-1 | PRESS | A series of real positive vectors representing the wellbore skin pressure, for all combinations of the water throughput values (THRUPUT) and velocity values (VELOCITY), organized as a series of vectors PRESS(THRUPUT, VELOCITY). Thus, the first vector represents the wellbore skin pressure of the first THRUPUT value and each entry in the vector is the corresponding wellbore skin pressure of the associated VELOCITY vector. Each vector should be on a separate line and should be terminated by a “/”. Thus, if THRUPUT has three entries and VELOCITY has four, then there should be three vectors, with each vector containing four elements representing wellbore skin pressure values, as a function of THRUPUT and VELOCITY. | None |
| psia | barsa | atma |  |
| Notes: |  |  |  |

*Table 8.157: SKPRWAT Keyword Description*


Unlike other PROPS section table keywords, that enable multiple tables following the keyword to be entered, the SKPRWAT keyword requires that the keyword itself must be repeated for each table, as is shown in the example on the following page.

The WSKPTAB keyword in the SCHEDULE section may be used to assign the SKPRPOLY and SKPRWAT tables to water injections wells, that enable the calculation of the wellbore skin pressure based on the fluids being injected.

See also the SKPRPOLY, PLYMWINJ, and PLYVMH keywords, in the PROPS section, that are the additional property keywords required for the Polymer Molecular Weight Transport option. In addition, see also the WPMITAB keyword in the SCHEDULE section, that assigns the PLYMWINJ tables to the water injection wells.

Note that the standard polymer property data keywords: PLYROCK, PLYADS, PLYMAX, etc., are still required to fully describe the polymer fluid.


#### Example

Given NTSKWAT equals two on the PINTDIMS keyword in the RUNSPEC section,  then two SKPRWAT tables are required to be entered:


```
--
--       POLYMER MOLECULAR WEIGHT MODEL WATER INJECTION SKIN TABLE
--       (OPM FLOW PROPS KEYWORD)
--
SKPRWAT
         1                             / TABLE NUMBER
--
--       THROUGHPUT VALUES
--
         0.0     200.0   400.0         /
--
--       VELOCITY VALUES
--
         0.0     50.0    70.0    100.0 /
--
--       PRESS SKIN VALUES
--
         0.0     2.0     4.0     8.0   / PRESS(THRUPUT=1, VELOCITY=1 TO N)
         0.0     20.0    40.0    80.0  / PRESS(THRUPUT=2, VELOCITY=1 TO N)
         0.0     50.0    100.0   200.0 / PRESS(THRUPUT=3, VELOCITY=1 TO N)
/
SKPRWAT
         2                             / TABLE NUMBER
--
--       THROUGHPUT VALUES
--
         0.0     200.0   400.0         /
--
--       VELOCITY VALUES
--
         0.0     30.0    50.0    100.0 /
--
--       PRESS SKIN VALUES
--
         0.0     2.0     4.0     8.0   / PRESS(THRUPUT=1, VELOCITY=1 TO N)
         0.0     20.0    40.0    80.0  / PRESS(THRUPUT=2, VELOCITY=1 TO N)
         0.0     50.0    100.0   200.0 / PRESS(THRUPUT=3, VELOCITY=1 TO N)
/

```

As mentioned previously, the SKPRWAT keyword requires that the keyword itself must be repeated for each table, as is shown in the above example.
