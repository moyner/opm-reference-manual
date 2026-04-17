### ROCK – Define the Rock Compressibility for Various Regions


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

ROCK defines the rock compressibility for various regions in the model. The number of ROCK vector data sets is defined by the NTPVT parameter on the TABDIMS keyword in the RUNSPEC section and the allocation of the ROCK tables to different grid blocks in the model is done via the PVTNUM keyword in the REGIONS section. One data set consists of one record or line which is terminated by a “/”.

This keyword must be defined in the OPM Flow input deck.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | PRESS | PRESS is a real number defining the rock reference pressure for the other parameters for this data set. | Default |
| psia 14.7 | barsa 1.0132 | atma 1.0 |  |
| 2 | RCOMP | RCOMP is a real number defining the rock compressibility (cf) at the rock reference pressure and is defined as: $$ {c}_{f} = -\frac{1}{V}\left(\frac{\mathit{dV}}{\mathit{dP}}\right) $$ | Defined |
| 1/psia 0.0 | 1/barsa 0.0 | 1/atma 0.0 |  |
| Notes: Note, however, that if ROCKOPTS(ROCKOPT3) parameter has been used to set the allocation of the ROCK data via the ROCKNUM array, then the number of ROCK vectors should correspond to the value entered on TABDIMS(NTROCC) in the RUNSPEC section. Similarly, if the ROCKOPTS(ROCKOPT3) has been used to set the assignment of the ROCK data via the SATNUM array, then the number of vectors should correspond to the value entered via the TABDIMS(NTSFUN) parameter, since the tables will be allocated via the SATNUM array. |  |  |  |

*Table 8.125: ROCK Keyword Description*


The simulator adjusts the pore volume based on the reference pressure (PRESS), that is:


| $$ V({P}_{i}) = V({P}_{r})\left(1 + {c}_{f}\left({P}_{i} - {P}_{r}\right) + \frac{{\left({c}_{f}({P}_{i} - {P}_{r})\right)}^{2}}{2}\right) $$ | (8.91) |
| --- | --- |

where:

$$
{c}_{f}
$$

$$
{P}_{i}
$$

$$
{P}_{r}
$$

$$
V({P}_{i})
$$

$$
V({P}_{r})
$$


| Note If the Rock Compaction option has been activated via the ROCKCOMP keyword in the RUNSPEC section, then the ROCKTAB keyword in the PROPS section should be used instead of ROCK keyword. |
| --- |


See also the ROCKOPTS and ROCKTAB keywords in the PROPS section.


#### Examples

The following shows the ROCK keyword for when NTPVT on the TABDIMS keyword in the RUNSPEC section is set to one.


```
--
--       ROCK COMPRESSIBILITY
--
--       REFERENCE PRESSURE IS TAKEN FROM THE HCPV WEIGHTED RESERVOIR PRESSURE
--       AS THE PORV IS ALREADY AT RESERVOIR CONDITIONS (OPM FLOW USES THE
--       REFERENCE PRESSURE) TO CONVERT THE GIVEN PORV TO RESERVOIR CONDITIONS
--       USING THE DATA ON THE ROCK KEYWORD)
--
--       REF PRES  CF
--       PSIA      1/PSIA
--       --------  --------
ROCK
         3966.9    5.0E-06                                 / ROCK COMPRESSIBILITY
```


The next example shows the ROCK keyword for when NTPVT on the TABDIMS keyword in the RUNSPEC section is set to three.


```
--
--       ROCK COMPRESSIBILITY
--
--       REFERENCE PRESSURE IS TAKEN FROM THE HCPV WEIGHTED RESERVOIR PRESSURE
--       AS THE PORV IS ALREADY AT RESERVOIR CONDITIONS (OPM FLOW USES THE
--       REFERENCE PRESSURE) TO CONVERT THE GIVEN PORV TO RESERVOIR CONDITIONS
--       USING THE DATA ON THE ROCK KEYWORD)
--
--       REF PRES  CF
--       PSIA      1/PSIA
--       --------  --------
ROCK
         3566.9    5.0E-06                        / ROCK COMPRESSIBILITY REGION 1
         3966.9    5.5E-06                        / ROCK COMPRESSIBILITY REGION 2
         4566.9    6.0E-06                        / ROCK COMPRESSIBILITY REGION 3
```


The above example defines three ROCK tables and assumes that NTPVT equals three on the TABDIMS keyword in the RUNSPEC section.

There is no terminating “/” for this keyword, and thus the number entries must match the value entered via the TABDIMS(NTPVT), TABDIMS(NTROCC), or TABDIMS(NTSFUN) parameters, depending on the option selected via the ROCKOPTS keyword.
