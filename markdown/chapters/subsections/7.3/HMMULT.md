### HMMULT – History Match Grid Transmissibility & Pore Volume Gradient Cumulative Multipliers {#kw-HMMULT}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The HMMULT series of keywords defines the history match gradient cumulative permeability multipliers, for when the History Match Gradient option has been activated by the [HMDIMS](#kw-HMDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. The keyword consists of the first six characters of “HMMULT” followed by a one or two character string shown in @tbl-7-5, that determines the transmissibility direction, for example, HMMULTX.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.


| Mnemonic | Cartesian Grid | Radial Grid |  |  |
| --- | --- | --- | --- | --- |
| Grid Keyword | HMMULT Keyword | Grid Keyword | HMMULT Keyword |  |
| X/R | [MULTX](#kw-MULTX) | HMMULTX | [MULTR](#kw-MULTR) | HMMULTR |
| XY |  | HMMULTXY |  |  |
| Y/HT | [MULTY](#kw-MULTY) | hMMULTY | [MULTTHT](#kw-MULTTHT) | HMMULTTH |
| z | [MULTZ](#kw-MULTZ) | HMMULTZ | [MULTZ](#kw-MULTZ) | HMMULTZ |
| PV | [MULTPV](#kw-MULTPV) | HMMULTPV | [MULTPV](#kw-MULTPV) | HMMULTPV |
: HMMULT Keyword List {#tbl-7-5}
See also the [HMMLT](#kw-HMMLT) keyword in the [GRID](#kw-GRID) section.