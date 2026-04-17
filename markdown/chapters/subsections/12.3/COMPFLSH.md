### COMPFLSH – Assign COMPDAT Differential-Flash Liberation Ratios {#kw-COMPFLSH}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

COMPFLSH is used to assign saturated PVT differential-flash liberation ratios to individual well completions for both the oil formation volume factor and the gas-oil ratio. Only the saturated oil properties are changed by this keyword, that is only data entered via the [PVCO](#kw-PVCO) or [PVTO](#kw-PVTO) keywords in the [PROPS](#kw-PROPS) section will be used in the calculation.  The other fluid PVT property keywords: [PVTW](#kw-PVTW), [PVTG](#kw-PVTG), [DENSITY](#kw-DENSITY), etc.,  are not used.

The differential liberation expansion (“DLE”) experiment is designed to approximate the depletion process of an oil reservoir, and thereby provide suitable PVT data for calculating reservoir performance.  This is then coupled with surface faculties via the multi-stage separator flash data.  The multi-stage separator test is performed on an oil sample primarily to provide a basis for converting differential liberation data from a residual oil to a stock-tank oil basis. Occasionally, several separator tests are run to help choose separator conditions that maximize stock-tank oil production. Usually two or three stages of separation are used, with the last stage being at atmospheric pressure and near-ambient temperature (60 to 80 oF).

Note, normally the data on the [PVCO](#kw-PVCO) and [PVTO](#kw-PVTO) keywords should have already taken the two datasets into account and therefore this keyword should not normally be used in practice, unless there is a specific requirement to adjust the oil PVT data on a well connection basis.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.