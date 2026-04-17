### JFUNCR – Activate the Leverett J-function Saturation Table Option


| [RUNSPEC](#3.RUNSPEC SECTION\|outline) | [GRID](#4.GRID SECTION\|outline) | [EDIT](#5.EDIT SECTION\|outline) | [PROPS](#6.PROPS SECTION\|outline) | [REGIONS](#7.REGIONS SECTION\|outline) | [SOLUTION](#8.SOLUTION SECTION\|outline) | [SUMMARY](#9.SUMMARY SECTION\|outline) | [SCHEDULE](#10.SCHEDULE SECTION\|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

[JFUNCR](#__RefHeading___Toc257142_2369005893) keyword activates Leverett-J-Function [Leverett, M. C.; “Capillary Behaviour in Porous Solids”, Trans. AIME (1941) 142, 152-168.] Saturation Table option which is a commonly used technique to normalize capillary pressure base on laboratory measured core plugs porosity and permeability values and the resulting capillary pressure data. This keyword is an extension of the [JFUNC](#__RefHeading___Toc86297_3218818441) keyword in the [GRID](#__RefHeading___Toc38674_784232322) section that uses the parameters on the [JFUNC](#__RefHeading___Toc86297_3218818441) keyword combined with a cell’s porosity and permeability to perform the scaling globally.  In comparison, the [JFUNCR](#__RefHeading___Toc257142_2369005893) allows for the J-Function parameters to be declared per saturation table number, resulting in greater flexibility.

The keyword should only be used if end-point scaling is switched on using the [ENDSCALE](#__RefHeading___Toc68146_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | JFOPT | A character string that defines which capillary data sets the J-Function option should be applied to, based on the following options: | BOTH |
| 2 | OWSTEN | A positive real number that defines oil-water surface tension used to de-normalized J-Function data entered in the [PROPS](#__RefHeading___Toc39329_784232322) section. | None |
| dynes/cm | dynes/cm | dynes/cm |  |
| 3 | OGSTEN | A positive real number that defines oil-gas surface tension used to de-normalized J-Function data entered in the [PROPS](#__RefHeading___Toc39329_784232322) section. | None |
| dynes/cm | dynes/cm | dynes/cm |  |
| 4 | ALPHA | A positive real value that defines an alternative power value for the porosity term in the J-Function equation, that is instead of use instead in the transformation. | 0.5 |
| 5 | BETA | A positive real number that defines an alternative power value for the permeability term in the J-Function equation, that is instead of use instead in the transformation. | 0.5 |
| 6 | PERM | PERM is a character string that sets the permeability array to be used in the transform, based on the following options: | XY |
| Notes: |  |  |  |

*Table 6.54: JFUNCR Keyword Description*


Just like the relative permeability data capillary pressure data are measured on core plugs with varying quality and perhaps from different reservoirs. It is therefore necessary to determine averaged data, before employing the data in engineering calculations. This is commonly done by using the Leverett J-function [Leverett, M. C.; “Capillary Behaviour in Porous Solids”, Trans. AIME (1941) 142, 152-168.], which is defined as:


|  | (6.8) |
| --- | --- |

Where:

J (Sw)	=	dimensionless function of water saturation

Pc (Sw) 	=	capillary pressure (kPa)

k	=	permeability, (m2)

φ 	=	porosity (fraction)

σ	=	interfacial tension (mN/m)

Θ	=	contact angle


Sometimes the equation is stated with the cos θ term included, that is:


|  | (6.9) |
| --- | --- |


Since the above function is just a normalizing function, then units are not important, as long as when we de-normalize the average curve we use the same unit set. Secondly, if all the capillary pressure data has been converted to reservoir conditions, we can actually ignore the denominator as it is a constant, and we can therefore just use:


|  | (6.10) |
| --- | --- |


However, in the simulator it is necessary to use the formal definition as outlined in equation (6.8). In addition to the standard the equation the keyword allows for de-normalizing the curve to use alternative power functions instead of the standard 0.5 used in equation (6.8), that is:


|  | (6.11) |
| --- | --- |

Where:

J (Sw)	=	dimensionless function of water saturation

Pc (Sw) 	=	capillary pressure (kPa)

k	=	permeability, (m2)

φ 	=	porosity (fraction)

σ	=	interfacial tension (mN/m)

Θ	=	contact angle

α	=	porosity power value

β	=	permeability value


The [JFUNC](#__RefHeading___Toc86297_3218818441) keyword allows the data entered as capillary pressure in the saturation tables, for example, by using the [SGFN](#__RefHeading___Toc106868_335817223) and [SWFN](#__RefHeading___Toc106882_335817223) keywords in the [PROPS](#__RefHeading___Toc39329_784232322) section to be treated as J-functions instead, and to de-normalize these curves for each active cell in the model using the options and values defined with the [JFUNC](#__RefHeading___Toc86297_3218818441) keyword combined with a cells porosity and permeability values.


| Note If either the [JFUNC](#__RefHeading___Toc86297_3218818441) or [JFUNCR](#__RefHeading___Toc257142_2369005893) keywords are used to activate J-Function scaling then the [ENDSCALE](#__RefHeading___Toc68146_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section must also be present in the input deck, in order for the dimensionless J-function values entered on the [SWFN](#__RefHeading___Toc106882_335817223), [SGFN](#__RefHeading___Toc106868_335817223) or the [SWOF](#__RefHeading___Toc45811_7190362561), [SGOF](#__RefHeading___Toc106870_335817223), [SLGOF](#__RefHeading___Toc106874_335817223) keywords to be re-scaled to capillary pressure data. Note if the [ENDSCALE](#__RefHeading___Toc68146_2267116897) keyword is absent, then like the commercial simulator,  J-Function scaling is not performed, and the values entered on the [SWFN](#__RefHeading___Toc106882_335817223), [SGFN](#__RefHeading___Toc106868_335817223) or the [SWOF](#__RefHeading___Toc45811_7190362561), [SGOF](#__RefHeading___Toc106870_335817223), [SLGOF](#__RefHeading___Toc106874_335817223) keywords are used as entered. |
| --- |


See also the [JFUNC](#__RefHeading___Toc86297_3218818441) keyword in the [GRID](#__RefHeading___Toc38674_784232322) section that uses the parameters on the [JFUNC](#__RefHeading___Toc86297_3218818441) keyword combined with a cell’s porosity and permeability to perform the scaling globally.


#### Example

The example below assumes NTSFUN is equal to five on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.


```
--
--       DEFINE LEVERETT J-FUNCTION PARAMETERS BY SATURATION TABLES
--       JFUN    OILWAT  GASOIL  PORO    PERM    PERM
--       OPTN    SDENS   SDEN    ALPHA   BETA    OPTN
JFUNCR
         WATER   22.5    1*      0.5     0.5     XY                            /
         WATER   22.5    1*      0.5     0.5     XY                            /
         WATER   22.5    1*      0.5     0.5     XY                            /
         WATER   22.5    1*      0.5     0.5     XY                            /
         WATER   22.5    1*      0.5     0.5     XY                            /
```


Here the oil-water capillary pressure data entered on the [SWFN](#__RefHeading___Toc106882_335817223) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section are treated as J-Functions, and that the J-Function should be de-normalized using an oil-water surface density of 22.5 dynes/cm, using the default power values and the average of the [PERMX](#__RefHeading___Toc45791_719036256) and [PERMY](#__RefHeading___Toc45793_719036256) values for each grid block, for all five tables. Note that since all the [JFUNCR](#__RefHeading___Toc257142_2369005893) parameters are the same for all saturation tables then the [JFUNC](#__RefHeading___Toc86297_3218818441) keyword could be used instead in this instance.
