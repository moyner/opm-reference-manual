### HMMLT – History Match Grid Permeability Gradient Cumulative Multipliers {#kw-HMMLT}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The HMMLT series of keywords defines the history match gradient cumulative permeability multipliers, for when the History Match Gradient option has been activated by the [HMDIMS](#kw-HMDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. The keyword consists of the first five characters of “HMMLT” followed by a two or three character string shown in @tbl-6-45, that determines the permeability direction, for example, HMMLTPX.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.


| Mnemonic | Cartesian Grid | Radial Grid |  |  |
| --- | --- | --- | --- | --- |
| Grid Keyword | [HMMULT](#kw-HMMULT) Keyword | Grid Keyword | [HMMULT](#kw-HMMULT) Keyword |  |
| PX/PR | [PERMX](#kw-PERMX) | HMMLTPX | [PERMR](#kw-PERMR) | HMMLTPR |
| PXY | PERMXY | HMMLTPXY |  |  |
| PY/THT | [PERMY](#kw-PERMY) | hMMLTPY | [PERMTHT](#kw-PERMTHT) | HMMLTTH |
| PZ | [PERMZ](#kw-PERMZ) | HMMLTPZ | [PERMZ](#kw-PERMZ) | HMMLTPZ |
: HMMLT Keyword List {#tbl-6-45}
See also the [HMMULT](#kw-HMMULT) keyword in the [EDIT](#kw-EDIT) section