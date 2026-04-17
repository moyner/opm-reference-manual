### PPCWMAX – Define SWATINIT Calculated Capillary Pressure Constraints


| [RUNSPEC](#3.RUNSPEC SECTION\|outline) | [GRID](#4.GRID SECTION\|outline) | [EDIT](#5.EDIT SECTION\|outline) | [PROPS](#6.PROPS SECTION\|outline) | [REGIONS](#7.REGIONS SECTION\|outline) | [SOLUTION](#8.SOLUTION SECTION\|outline) | [SUMMARY](#9.SUMMARY SECTION\|outline) | [SCHEDULE](#10.SCHEDULE SECTION\|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [PPCWMAX](#__RefHeading___Toc150617_332691817) keyword defines the maximum capillary pressure allowed when scaling the capillary pressure tables to match the inputted [SWATINIT](#__RefHeading___Toc323952_1728001293) array. This is primary used for when the [SWATINIT](#__RefHeading___Toc323952_1728001293) array has values of water saturation above the connate water saturation significantly outside than capillary pressure transition zone, that is high on the structure. In this case OPM Flow may generate large values for the capillary pressure which may result in numerical converge problems. This keyword sets the maximum allowable calculated capillary pressure and how the water saturation should be treated when the limit is exceeded.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | PCWO | A columnar vector of real values that defines the maximum allowable capillary pressure for each [SATNUM](#__RefHeading___Toc71136_2752266063) region. The default value of infinity means there is no limit applied. | Infinity |
| psia | barsa | atma |  |
| 2 | OPTN | A columnar vector of character strings that should be set to: | No |
| Notes: |  |  |  |

*Table 8.111: PPCWMAX Keyword Description*


| Note Using this keyword to limit the re-scaled grid block capillary pressure values will effect the fluids in-place when the simulator has to re-calculate values due to the capillary pressure limit being exceeded. In addition, the high grid block capillary pressures may be indicative of an inconsistency between the tabular [SATNUM](#__RefHeading___Toc71136_2752266063) capillary pressure values and the provided [SWATINIT](#__RefHeading___Toc323952_1728001293) array water saturations. This inconsistency may be a result of the [SWATINIT](#__RefHeading___Toc323952_1728001293) array being derived using a saturation height function, as is customary in static modeling software, and the numerical models tabulated capillary pressure. Rather than resetting the maximum calculated capillary pressure using the [PPCWMAX](#__RefHeading___Toc150617_332691817) keyword,  it may be more appropriate to investigate the reason for the high capillary pressures values first, prior to applying the keyword. |
| --- |


#### Example


```
--
--       SET MAXIMUM PC FOR SWATINIT INITIALIZATION
--       MAX       MATCH
--       PC        SWATINIT
--       --------  --------
PPCWMAX
         100.0     YES                                     / TABLE NO 01
         125.0     YES                                     / TABLE NO 02
         135.0     YES                                     / TABLE NO 03
```


The above example sets the maximum capillary pressure for three saturation regions to 100, 125 and 135   with [SWATINIT](#__RefHeading___Toc323952_1728001293) reset to the connate water saturation for when the capillary pressure limit is exceeded.
