### WINJMULT – Define Well Pressure Dependent Injectivity Multipliers


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The WINJMULT keyword defines pressure dependent injectivity multipliers for injection wells and can be used to approximate the increase or decrease in a well’s injectivity due to hydraulic fracturing in water injection wells. Only injection wells are processed by this keyword, even if production wells have been entered by the keyword.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well connection data are being defined. Note that the well name (WELNAME) must have been declared previously using the WELSPECS keyword in the SCHEDULE section, otherwise an error may occur. | None |
| 2 | FRACPRES | FRACPRES is the fracture opening pressure (Pfractue) used in equation 12.3.296.1. | None |
| psia | barsa | atma |  |
| 3 | ALPHA | ALPHA is the multiplier gradient, α, in equation 12.3.296.1. | Defined |
| 1/psia 0.0 | 1/barsa 0.0 | 1/atma 0.0 |  |
| 4 | OPTION | A defined character string that determines how the data on this keyword is applied, and should be set to one of the following character strings: This option means that even if the pressures in the wellbore, and therefore the sand face pressures, later declines, injectivity remains unchanged for all the connections. The reversibility of this option means that if the pressures in the wellbore, and therefore the sand face pressures, later declines, injectivity will also decline for all the connections. The reversibility of this option means that if the pressures in the wellbore, later declines, injectivity will also decline for all the connections. | WREV |
| 5 | I | An integer value less than or equal to NX that defines the connection location in the I-direction. If set to zero, a negative value, or defaulted with 1* then all connections in the I-direction will be multiplied by ALPHA, depending on the selected OPTION value. | 1* |
| 6 | J | An integer value less than or equal to NY that defines the connection location in the J-direction. If set to zero, a negative value, or defaulted with 1* then all connections in the J-direction will be multiplied by ALPHA, depending on the selected OPTION value. | 1* |
| 7 | K | An integer value less than or equal to NZ that defines the connection location in the K-direction. If set to zero, a negative value, or defaulted with 1* then all connections in the K-direction will be multiplied by ALPHA, depending on the selected OPTION value. | 1* |
| Notes: |  |  |  |

*Table 12.3.296.1: WINJMULT Keyword Description*


The methodology for applying the well pressure dependent injectivity multipliers is outlined in equation 12.3.296.1.


$$
\begin{matrix}\mathit{Multiplier}= & 1.0 + α ({P}_{\mathit{WBHP}} - {P}_{\mathit{fracture}}) & \text{ for }{P}_{\mathit{WBHP}} > {P}_{\mathit{fracture}} \\ \mathit{Multiplier}= & 1.0 & \text{ for }{P}_{\mathit{WBHP}} < {P}_{\mathit{fracture}}\end{matrix}
$$ {#eq-12-3-296-1}

where:

Multiplier	=	the resulting multiplier to be applied to the selected connections.

α	= 	the ALPHA multiplier gradient in Table 12.3.296.1.

PWBHP	=	either the well’s current flowing bottom-hole pressure, or the selected

individual connection’s sand face pressure.

Pfracture	=  	the effective fracture opening pressure, FRACPRES in Table 12.3.296.1.


The equation is applied every time there is a calculation to determine a well’s flow rate, this results in the calculated mobility rates being scaled up by the Multiplier value in equation 12.3.296.1. Note also that since the scaling is performed on the connection fluid mobility values, then the reported connection transmissibilities in the print file etc. remain unchanged.


::: {.callout-note}
If all the connection parameters (I, J, K) are defaulted, or OPTION is set equal to WREV, then the multiplier is applied to all connections in the well. If any of the connection parameters (I, J, K) have positive values and OPTION is set equal to CIRR or CREV, then the multiplier is applied to the selected connections as determined by the (I, J, K) parameters.
:::


#### Example

The example below show the WINJMULT keyword for three water injection wells.


```
--
--       DEFINE WELL CONNECTION MULTIPLIERS
--
-- WELL  FRAC  MULT    FRAC  --LOCATION--
-- NAME  PRES  VALUE   OPTN    I   J   K
WINJMULT
WI01     4200  0.0250  1*      1*  1*  1*        /
WI02     4250  0.0025  CIRR    1*  1* 145        /
WI02     4250  0.0025  CIRR    1*  1* 146        /
WI02     4250  0.0025  CIRR    1*  1* 147        /
WI03     4400  0.0055  CREV    1*  1* 160        /
WI03     4400  0.0055  CREV    1*  1* 165        /
/
```


The first well, WI01, uses the default value for OPTION, that is WREV, which means that the injectivity multiplier will be applied to all the connections in the well and the well’s bottom-hole pressure is used in the calculation. In this case the process is reversible. The second well, WI02, applies the injectivity multiplier to all connections in layers 145 to 147 using the sand face pressures in the calculation, and the process is irreversible. Finally for well WI03, the multiplier is applied to all connections in layers 160 and 165 using the sand face pressures in the calculation, and in this case the process is reversible.
