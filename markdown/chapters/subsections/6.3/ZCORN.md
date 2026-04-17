### ZCORN – Define the Depth of Each Corner-Point of a Grid Block


| [RUNSPEC](#3.RUNSPEC SECTION\|outline) | [GRID](#4.GRID SECTION\|outline) | [EDIT](#5.EDIT SECTION\|outline) | [PROPS](#6.PROPS SECTION\|outline) | [REGIONS](#7.REGIONS SECTION\|outline) | [SOLUTION](#8.SOLUTION SECTION\|outline) | [SUMMARY](#9.SUMMARY SECTION\|outline) | [SCHEDULE](#10.SCHEDULE SECTION\|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

[ZCORN](#__RefHeading___Toc45757_7190362561) defines the depth of each corner point of a grid block on the pillars defining the reservoir grid. A total of 8 x NX x NY x NZ values are needed to fully define all the depths in the model. The depths specifying the top of the first layer are entered first with one point for each pillar for each grid block. The points are entered with the X axis cycling fastest. Next come the depths of the bottom of the first layer. The top of layer two follows etc.

The keyword can be only used be used with Irregular Corner-Point Grids.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [ZCORN](#__RefHeading___Toc45757_7190362561) | An array of depths with 8 depths for each cell, for a total of 8 x Nx x NY x NZ entries | None |
| feet | metres | cm |  |
| Notes: |  |  |  |

*Table 6.131: ZCORN Keyword Description*


See also the [SPECGRID](#__RefHeading___Toc45797_7190362561), [COORD](#__RefHeading___Toc45757_719036256) and [COORDSYS](#__RefHeading___Toc45759_719036256) keywords to fully define an Irregular Corner-Point Grid.


#### Example


```
--
--       SPECIFY CORNER-POINT DEPTHS FOR A 3 x 2 x 2 GRID,
--       WITH CONSTANT SLOPE IN THE X AND Y DIRECTIONS
--       SUCH THAT ALL CORNER POINTS OF NEIGHBOURING BLOCKS ALIGN
ZCORN
--
--                    top of layer 1
--
         1450   1500   1500   1550   1550   1600
         1500   1550   1550   1600   1600   1650
         1500   1550   1550   1600   1600   1650
         1550   1600   1600   1650   1650   1700
--
--                     bottom of layer 1
--
         1460   1510   1510   1560   1560   1610
         1510   1560   1560   1610   1610   1660
         1510   1560   1560   1610   1610   1660
         1560   1610   1610   1660   1660   1710
--
--                     top of layer 2
--
         1460   1510   1510   1560   1560   1610
         1510   1560   1560   1610   1610   1660
         1510   1560   1560   1610   1610   1660
         1560   1610   1610   1660   1660   1710
--
--                     bottom of layer 2
--
         1470   1520   1520   1570   1570   1620
         1520   1570   1570   1620   1620   1670
         1520   1570   1570   1620   1620   1670
         1570   1620   1620   1670   1670   1720
/
```


The above example defines depths of the vertical coordinate lines for a regular 3 by 2 by 2 grid with a constant slope in the x and y directions such that all the corner points of neighboring blocks are aligned.
