### JFUNCR – Activate the Leverett J-function Saturation Table Option


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

JFUNCR keyword activates Leverett-J-Function [Leverett, M. C.; “Capillary Behaviour in Porous Solids”, Trans. AIME (1941) 142, 152-168.] Saturation Table option which is a commonly used technique to normalize capillary pressure base on laboratory measured core plugs porosity and permeability values and the resulting capillary pressure data. This keyword is an extension of the JFUNC keyword in the GRID section that uses the parameters on the JFUNC keyword combined with a cell’s porosity and permeability to perform the scaling globally.  In comparison, the JFUNCR allows for the J-Function parameters to be declared per saturation table number, resulting in greater flexibility.

The keyword should only be used if end-point scaling is switched on using the ENDSCALE keyword in the RUNSPEC section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | JFOPT | A character string that defines which capillary data sets the J-Function option should be applied to, based on the following options: | BOTH |
| 2 | OWSTEN | A positive real number that defines oil-water surface tension used to de-normalized J-Function data entered in the PROPS section. | None |
| dynes/cm | dynes/cm | dynes/cm |  |
| 3 | OGSTEN | A positive real number that defines oil-gas surface tension used to de-normalized J-Function data entered in the PROPS section. | None |
| dynes/cm | dynes/cm | dynes/cm |  |
| 4 | ALPHA | A positive real value that defines an alternative power value for the porosity term in the J-Function equation, that is instead of$\sqrt{\frac{k}{\mathrm{φ}}}$ use $\frac{{k}^{0.5}}{{\mathrm{φ}}^{\mathrm{α}}}$instead in the transformation. | 0.5 |
| 5 | BETA | A positive real number that defines an alternative power value for the permeability term in the J-Function equation, that is instead of $\sqrt{\frac{k}{\mathrm{φ}}}$use $\frac{{k}^{\mathrm{β}}}{{\mathrm{φ}}^{0.5}}$instead in the transformation. | 0.5 |
| 6 | PERM | PERM is a character string that sets the permeability array to be used in the transform, based on the following options: | XY |
| Notes: |  |  |  |

*Table 6.54: JFUNCR Keyword Description*


Just like the relative permeability data capillary pressure data are measured on core plugs with varying quality and perhaps from different reservoirs. It is therefore necessary to determine averaged data, before employing the data in engineering calculations. This is commonly done by using the Leverett J-function [Leverett, M. C.; “Capillary Behaviour in Porous Solids”, Trans. AIME (1941) 142, 152-168.], which is defined as:


$$
J ({S}_{w}) = \frac{{P}_{c,\mathit{res}}({S}_{w}) \sqrt{\frac{k}{φ}}}{σ}
$$ {#eq-6-8}

Where:

J (Sw)	=	dimensionless function of water saturation

Pc (Sw) 	=	capillary pressure (kPa)

k	=	permeability, (m2)

φ 	=	porosity (fraction)

σ	=	interfacial tension (mN/m)

Θ	=	contact angle


Sometimes the equation is stated with the cos θ term included, that is:


$$
J ({S}_{w}) = \frac{{P}_{c,\mathit{res}}({S}_{w}) \sqrt{\frac{k}{φ}}}{σ cos Θ}
$$ {#eq-6-9}


Since the above function is just a normalizing function, then units are not important, as long as when we de-normalize the average curve we use the same unit set. Secondly, if all the capillary pressure data has been converted to reservoir conditions, we can actually ignore the denominator as it is a constant, and we can therefore just use:


$$
J ({S}_{w}) = {P}_{c,\mathit{res}}({S}_{w}) \sqrt{\frac{k}{φ}}
$$ {#eq-6-10}


However, in the simulator it is necessary to use the formal definition as outlined in equation (6.8). In addition to the standard the equation the keyword allows for de-normalizing the curve to use alternative power functions instead of the standard 0.5 used in equation (6.8), that is:


$$
J ({S}_{w}) = \frac{{P}_{c,\mathit{res}}({S}_{w}) \left(\frac{{k}^{\mathrm{β}}}{{φ}^{\mathrm{α}}}\right)}{σ}
$$ {#eq-6-11}

Where:

J (Sw)	=	dimensionless function of water saturation

Pc (Sw) 	=	capillary pressure (kPa)

k	=	permeability, (m2)

φ 	=	porosity (fraction)

σ	=	interfacial tension (mN/m)

Θ	=	contact angle

α	=	porosity power value

β	=	permeability value


The JFUNC keyword allows the data entered as capillary pressure in the saturation tables, for example, by using the SGFN and SWFN keywords in the PROPS section to be treated as J-functions instead, and to de-normalize these curves for each active cell in the model using the options and values defined with the JFUNC keyword combined with a cells porosity and permeability values.


::: {.callout-note}
If either the JFUNC or JFUNCR keywords are used to activate J-Function scaling then the ENDSCALE keyword in the RUNSPEC section must also be present in the input deck, in order for the dimensionless J-function values entered on the SWFN, SGFN or the SWOF, SGOF, SLGOF keywords to be re-scaled to capillary pressure data. Note if the ENDSCALE keyword is absent, then like the commercial simulator,  J-Function scaling is not performed, and the values entered on the SWFN, SGFN or the SWOF, SGOF, SLGOF keywords are used as entered.
:::


See also the JFUNC keyword in the GRID section that uses the parameters on the JFUNC keyword combined with a cell’s porosity and permeability to perform the scaling globally.


#### Example

The example below assumes NTSFUN is equal to five on the TABDIMS keyword in the RUNSPEC section.


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


Here the oil-water capillary pressure data entered on the SWFN keyword in the PROPS section are treated as J-Functions, and that the J-Function should be de-normalized using an oil-water surface density of 22.5 dynes/cm, using the default power values and the average of the PERMX and PERMY values for each grid block, for all five tables. Note that since all the JFUNCR parameters are the same for all saturation tables then the JFUNC keyword could be used instead in this instance.
