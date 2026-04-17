### SALTP – Define the Initial Precipitated Salt Volume Fraction for All Grid Blocks {#kw-SALTP}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The SALTP keyword defines the initial equilibration precipitated salt volume fraction values for all grid cells in the model and should be used in conjunction with the [PBUB](#kw-PBUB), [PDEW](#kw-PDEW), [PRESSURE](#kw-PRESSURE), [RS](#kw-RS), [RV](#kw-RV), [SGAS](#kw-SGAS), [SOIL](#kw-SOIL) and [SWAT](#kw-SWAT) keywords etc., to fully describe the initial state of the model. The keyword should only be used if the salt (brine) phase has been activated in the model via the [BRINE](#kw-BRINE) keyword, and the [PRECSALT](#kw-PRECSALT) keyword to activate OPM Flow’s Salt Precipitation Model. Both keywords are in the [RUNSPEC](#kw-RUNSPEC) section.

This is the non-standard method to initialize the model via enumeration and is seldom employed in the industry. The standard methodology is for OPM Flow to initialize a model using the parameters on the [EQUIL](#kw-EQUIL) keyword combined with other keywords to fully describe the initial state of the model.  The keyword can be used with all grid types.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | SALTP | SALTP is an array of real positive numbers that are greater than or equal to zero and less than or equal to one, that define the initial equilibration salt volume fraction values to each cell in the model. Repeat counts may be used, for example 20*0.15. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes: |  |  |  |
: SALTP Keyword Description {#tbl-10-37}
See also the [PBUB](#kw-PBUB), [PDEW](#kw-PDEW), [PRESSURE](#kw-PRESSURE), [RS](#kw-RS), [RV](#kw-RV), [SGAS](#kw-SGAS), [SOIL](#kw-SOIL) and [SWAT](#kw-SWAT) keywords to fully define the initial state of the model.


::: {.callout-note}
This is an OPM Flow specific keyword for the simulator’s Salt Precipitation Model that is activated by the [PRECSALT](#kw-PRECSALT) keyword and declaring that vaporized water is present in the run via the [VAPWAT](#kw-VAPWAT) in the [RUNSPEC](#kw-RUNSPEC) section. This keyword defines the initial precipitated salt volume fraction contained within the pore space. See [SALT](#kw-SALT) in the [SOLUTION](#kw-SOLUTION) section that defines the initial salt concentration within the water phase.
:::


#### Example

The example activates the standard Brine Tracking model using the [BRINE](#kw-BRINE) keyword, OPM Flow’s Salt Precipitation model using the [PRECSALT](#kw-PRECSALT) keyword, and OPM Flow’s vaporized water phase with the [VAPWAT](#kw-VAPWAT) keyword; all three keywords are in the [RUNSPEC](#kw-RUNSPEC) section.


```
-- ==============================================================================
--
-- RUNSPEC SECTION
--
-- ==============================================================================
RUNSPEC
--
--       MAX     MAX     RSVD    TVDP    TVDP
--       EQLNUM  DEPTH   NODES   TABLE   NODES
EQLDIMS
         3       1*      20      1*      1*                                    /
--
--       ACTIVATE STANDARD BRINE MODEL
--
BRINE
--
--       ACTIVATE THE OPM FLOW SALT PRECIPITATION MODEL (OPM FLOW KEYWORD)
--
PRECSALT
--
--       VAPORIZED WATER IN WET GAS IS PRESENT IN THE RUN (OPM FLOW KEYWORD)
--
VAPWAT

```

Then in the [SOLUTION](#kw-SOLUTION) section the SALTP keyword would be of the form:


```
-- ==============================================================================
--
-- SOLUTION SECTION
--
-- ==============================================================================
SOLUTION
--
--       DEFINE INITIAL PRECIPITATED SALT VOLUME FRACTION FOR ALL CELLS
--       BASED ON NX = 100, NY = 100 AND NZ = 3
--
SALTP
         1000*0.0000    1000*0.0000    1000*0.100                             /

```

Here the initial equilibration precipitated salt volume fraction values are set to 0.0000 for all the cells in the first and second layers and finally 0.1000 for all the cells in the third layer.