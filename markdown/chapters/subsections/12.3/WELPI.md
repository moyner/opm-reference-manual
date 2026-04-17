### WELPI – Define Well Productivity and Injectivity Indices


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The WELPI keyword is used to define a well’s productivity or injectivity index at the time the keyword is activated. Productivity and injectivity indices are a function of both bottom-hole pressure and mobility and thus will vary in time as the bottom-hole pressure and fluids produce by the well are changing.  Thus, the values enter on this keyword for a given well will override any previously calculated values, or values previously entered, using this keyword.  This keyword should only be invoked after a well’s connection factors have been declared via the COMPDAT keyword in the SCHEDULE section.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well productivity index is being defined. Note that the well name (WELNAME) must have been declared previously using the WELSPECS keyword in the SCHEDULE section, otherwise an error may occur. | None |
| 2 | WELPI | A real positive value that defines the productivity or injectivity of a well at the time the keyword is activated in the input deck.  Subsequent use of the keyword for a given well will override all previously entered data, including the original productivity index calculated from the well’s COMPDAT connection data. Note that: Subsequent usage of the keyword for the same well may lead to unintended values; use the WPI series of variables in the SUMMARY section to output and verify that the values are consistent with the desired results. | 1.0 |
| Liquid stb/d/psia Gas Mscf/d/psia | Liquid sm3/day/bars Gas sm3/day/bars | Liquid scc/hour/atm Gas scc/hour/atm |  |
| Notes: |  |  |  |

*Table 12.89: WELPI Keyword Description*


Note that only a well’s currently opened connection factors, as entered via the COMPDAT keyword, are re-scaled to match the required productivity and injectivity index. See section Well Productivity on well productivity for further information on well productivity.


| Note One should not modify the productivity and injectivity index of gas wells that use: |
| --- |


See also the WPIMULT keyword in the SCHEDULE section to set the productivity and injectivity index for a well by scaling the current index by a scaling factor.


#### Example


```
--
--       DEFINE WELL PRODUCTIVITY/INJECTIVITY INDEX
--
-- WELL  PI
-- NAME  MULT
WELPI
OP01     1.250                                             /
OP02     2.750                                             /
OP03     1.100                                             /
/

```

In the above example the oil wells are are defined as having a well productivity indices of 1.250, 2.750 and 1.100 for the OP01, OP02 and OP03 wells, respectively.
