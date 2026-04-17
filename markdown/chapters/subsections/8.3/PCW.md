### PCW – End-Point Scaling of Grid Cell Water Capillary Pressure (Drainage)


| [RUNSPEC](#3.RUNSPEC SECTION\|outline) | [GRID](#4.GRID SECTION\|outline) | [EDIT](#5.EDIT SECTION\|outline) | [PROPS](#6.PROPS SECTION\|outline) | [REGIONS](#7.REGIONS SECTION\|outline) | [SOLUTION](#8.SOLUTION SECTION\|outline) | [SUMMARY](#9.SUMMARY SECTION\|outline) | [SCHEDULE](#10.SCHEDULE SECTION\|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

[PCW](#__RefHeading___Toc84164_621662414) defines the maximum drainage water-oil or water-gas capillary pressure values for all the cells in the model via an array.  The [ENDSCALE](#__RefHeading___Toc68146_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section should be activated to enable end-point scaling and the use of this keyword. The keyword can be used with all grid types.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [PCW](#__RefHeading___Toc84164_621662414) | [PCW](#__RefHeading___Toc84164_621662414) is an array of positive real numbers assigning the maximum drainage water capillary pressure values for each cell in the model. Repeat counts may be used, for example 30*100.0. | None |
| psia | bars | atm |  |
| Notes: |  |  |  |

*Table 8.96: PCW Keyword Description*


See also the [IPCW](#__RefHeading___Toc84166_621662414) keyword for the equivalent imbibition functionality.

The capillary pressure for a grid block is scaled by:


|  | (8.70) |
| --- | --- |

Where:

	=	the resulting drainage water capillary pressure for a grid cell.

	=	the maximum capillary pressure from the [PCW](#__RefHeading___Toc84164_621662414) array for a given cell.

	=	the capillary pressure in the drainage capillary pressure table allocated

to the grid block.

	=	the maximum capillary pressure in the drainage capillary pressure table

allocated to the grid block (that is at the connate water saturation).


#### Example


```
--
--       DEFINE GRID BLOCK PCW DATA FOR ALL CELLS (BASED ON NX x NY x NZ = 300)
--
PCW
         100*50.0  100*75.0  100*125.0                                        /
```


The above example defines the [PCW](#__RefHeading___Toc84164_621662414) for 300 cells in the model as defined by the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.
