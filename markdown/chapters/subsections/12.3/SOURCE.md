### SOURCE – Define Source Term


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [SOURCE](#REF_HEADING_KEYWORD_SOURCE_12_3) keyword defines a mass and heat source term for a given pseudo component in the specified grid block.

One source term can be added to each grid block for each pseudo component active in the model. If the source term for a given pseudo component is later redefined in the same block this will replace the previous source term.

This is an OPM Flow specific keyword that is not supported by the commercial simulator.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | I | A positive integer greater than zero and less than or equal to NX that defines the location of the source term in the I-direction. | None |
| 2 | J | A positive integer greater than zero and less than or equal to NY that defines the location of the source term in the J-direction. | None |
| 3 | K | A positive integer greater than zero and less than or equal to NZ that defines the location of the source term in the K-direction. | None |
| 4 | COMP | A defined character string that defines the pseudo component to be injected by the source term, COMP should be set to one of the following character strings: The SOLVENT or POLYMER option should only be specified if the solvent or polymer model has been activated by the SOLVENT or POLYMER keyword respectively in the RUNSPEC section. MICR, OXYG, or UREA requires the MICP keyword. A pseudo component must be specified if the mass injection rate is non-zero. | NONE |
| 5 | RATE | A real value that defines the source term’s mass injection rate of the specified component COMP. | 0.0 |
| lb/day | kg/day | gm/hour |  |
| 6 | HRATE | A real value that defines the source term’s heat injection rate1. The heat injection rate should only be specified if the thermal model has been activated by the THERMAL keyword in the RUNSPEC section. | 0.0 |
| Btu/day | kJ/day | J/hour |  |
| 7 | TEMP | A real value that defines the temperature of the injected component1. The temperature of the source term should only be specified if the thermal model has been activated by the THERMAL keyword in the RUNSPEC section. | None |
| °F | °C | °C |  |
| Notes: |  |  |  |

*Table 12.3.223.1: SOURCE Keyword Description*


See also the [BCCON](#REF_HEADING_KEYWORD_BCCON) keyword in the GRID section and the [BCPROP](#REF_HEADING_KEYWORD_BCPROP) keyword in the SCHEDULE section that can be used to specify boundary conditions.


#### Example

The first example adds two source terms to block (I=2, J=4, K=6) that inject gas at a mass flow rate of 25,000 lb/day and inject water at a mass flow rate of 1,000 lb/day respectively.


```
--
--       DEFINE SOURCE TERM
--
-- I    J    K    COMP     MASS     HEAT    TEMP
-- --------------          RATE     RATE
SOURCE
   2    4    6    GAS      25000    1*      1*       /
   2    4    6    WATER     1000    1*      1*       /
/
```

The second example adds a source term to block (I=2, J=4, K=6) that injects gas at a mass flow rate of 25,000 lb/day and a heat injection rate of 1.25 × 106 Btu/day in a thermal black-oil simulation.


```
--
--       DEFINE SOURCE TERM
--
-- I    J    K    COMP     MASS     HEAT    TEMP
-- --------------          RATE     RATE
SOURCE
   2    4    6    GAS      25000    1.25E6      1*       /
/
```

The third example adds a source term to block (I=2, J=4, K=6) that injects gas at a mass flow rate of 25,000 lb/day and a temperature of 200°F in a thermal black-oil simulation.


```
--
--       DEFINE SOURCE TERM
--
-- I    J    K    COMP     MASS     HEAT    TEMP
-- --------------          RATE     RATE
SOURCE
   2    4    6    GAS      25000    1*      200      /
/
```
