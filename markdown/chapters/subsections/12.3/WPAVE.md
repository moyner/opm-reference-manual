### Atgeirr Rasmussen
      2017-09-22T14:01:41.387549000
      AFR
      Not supported. It is used on Norne, but investigations showed no significant effect so we did not implement it.
     WPAVE
      David Baxendale
      2017-10-03T12:19:22.164000000
      DBx
      Reply to Atgeirr Rasmussen (09/22/2017, 14:01): "..."
      Okay, but if we done the work then perhaps we should implement it as it is one more feature we can say is implemented versus the commercial simulator.

      Will change to not implemented.
      – Well Block Average Pressure Calculation Parameters for All Wells


| [RUNSPEC](#3.RUNSPEC SECTION\|outline) | [GRID](#4.GRID SECTION\|outline) | [EDIT](#5.EDIT SECTION\|outline) | [PROPS](#6.PROPS SECTION\|outline) | [REGIONS](#7.REGIONS SECTION\|outline) | [SOLUTION](#8.SOLUTION SECTION\|outline) | [SUMMARY](#9.SUMMARY SECTION\|outline) | [SCHEDULE](#10.SCHEDULE SECTION\|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [WPAVE](#__RefHeading___Toc121923_2556401936) keyword defines the method and parameters for calculating a well’s block average pressures for all wells in the model. The resulting average pressure can be written out to the [SUMMARY](#__RefHeading___Toc43949_784232322) and RSM files in order to compare with field observed data via the WBP, WBP4, WBP5 and WBP9 vectors in the [SUMMARY](#__RefHeading___Toc43949_784232322) section.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | WPAVE1 | A real dimensionless value that defines the weighting factor between the inner block and the surrounding blocks used in the calculation of the connection factor weighted average pressure. If WPAVE1 is greater than or equal to zero and less than or equal to one, then the average pressure for each well connection is calculated based on this weighting factor. A value of zero indicates only the surrounding blocks should be used in the calculation; and a value of one indicates only the inner blocks should be used. If WPAVE1 is less than zero, then the average pressure for each well connection is weighted based on the pore volumes of the inner and surrounding blocks. | 0.5 |
| 2 | WPAVE2 | A real dimensionless value greater than or equal to zero and less than or equal to one, that defines the weighting factor between the connection factor weighted average pressures and the pore volume weighted average pressures. If WPAVE2 is equal to one, then the average pressures are calculated based only on the connection factor weighted average pressures. If WPAVE2 is equal to zero, then average pressures are calculated based  only on the pore volumes weighted average pressures. | 1.0 |
| 3 | WPAVE3 | A defined character string that determines how the hydrostatic head calculation is performed in correcting the pressures to the BHP reference depth on the [WELSPECS](#__RefHeading___Toc268463_1366622701) or [WPAVEDEP](#__RefHeading___Toc121639_2412586160) keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. WPAVE3 should be set to one of the following character strings: | WELL |
| 4 | WPAVE4 | A defined character string that determines which connections should be used in the calculations, WPAVE4 should be set to one of the following character strings: Only the OPEN option is currently supported by the simulator. | OPEN |
| Notes: |  |  |  |

*Table 12.3.309.1: WPAVE Keyword Description*


The keyword is not applicable and should not be used with radial and spider grid geometries.

See also the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword that defines a well and a well’s bottom-hole pressure reference depth, the [WPAVEDEP](#__RefHeading___Toc121639_2412586160) keyword that also defines a well’s bottom-hole pressure reference depth, and the [COMPDAT](#__RefHeading___Toc97651_3261743917) keyword to define a well’s connections. All the aforementioned keywords are described in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.


#### Examples

The following example defines the default well block average pressure calculation parameters


```
--
--       DEFINE WELL BLOCK AVERAGE PRESSURE CALCULATION PARAMETERS
--
--       INNER   PORV   WELL  OPEN
--       OUTER   CONN   RES   ALL
WPAVE
         0.5     1.0    WELL  ALL                                              /
```

And the next example shows the parameters used in the Norne model.


```
--
--       DEFINE WELL BLOCK AVERAGE PRESSURE CALCULATION PARAMETERS
--
--       INNER   PORV   WELL  OPEN
--       OUTER   CONN   RES   ALL
WPAVE
         1*      0.0    WELL  ALL                                              /
```

Here only pore volume weighting is used instead of connection weighting.
