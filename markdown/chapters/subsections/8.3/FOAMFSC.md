### FOAMFSC – Define Foam Gas Mobility versus Surfactant Concentration Functions


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The FOAMFSC keyword defines the reduction in gas mobility as a function of the foam surfactant concentration within a grid block. The Foam option must be activated by the FOAM keyword in the RUNSPEC section in order to use this keyword. In addition,  the FOAMOPT2 parameter on the FOAMOPTS keyword in the PROPS section must be set to the character string FUNC, in order to activate the functional form of the gas mobility reduction calculations.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | FOAMCON | A real positive value that defines the foam surfactant concentration at which foam modeling becomes active in the model and a strong foam is formed. FOAMCON cannot be defaulted and must be specified for the first table. Subsequent tables can be defaulted and will in this case use the previous tables’ entries as the default value. | None |
| lb/stb | kg/sm3 | gm/scc |  |
| 2 | FOAMEXP | A real positive value that defines an exponent that determines the gradient in the change of the reduction in gas mobility due to foam (es in equation (8.51). Note if es is less than one then the slope of Fs in equation (8.51) will be infinite at Cs equal to zero.  In this case, small surfactant concentrations have a significant effect on the mobility, especially if the reference concentration Csr is also small. If this is the case use MINSURF on this keyword to set a minimum surfactant concentration to avoid small-scale numerical errors from affecting the simulation. | Defined |
| dimensionless 1.0 | dimensionless 1.0 | dimensionless 1.0 |  |
| 3 | MINSURF | MINSURF is a real positive value that defines the minimum surfactant concentration for which the reduction in gas mobility will be calculated. The default value of 1 x 10-20 implies that there is no minimum | Defined |
| lb/stb 1 x 10-20 | kg/sm3 1 x 10-20 | gm/scc 1 x 10-20 |  |
| 4 | MINSWAT | MINSWAT is a real positive value less than 1.0 that sets the minimum water saturation below which foam has no effect.  The default value of 1 x 10-6 implies that there is no minimum. Note that this parameter is only used in the commercial simulator’s compositional simulator and is therefore not used by OPM Flow or the commercial simulators black-oil simulator. | Defined |
| dimensionless 1 x 10-6 | dimensionless 1 x 10-6 | dimensionless 1 x 10-6 |  |
| Notes: |  |  |  |

*Table 8.35: FOAMFSC Keyword Description*


The gas mobility reduction as a function of surfactant concentration is of the form:


| ${F}_{s} = {\left(\frac{{C}_{s}}{{C}_{s}^{r}}\right)}^{{e}_{s}}$ | (8.51) |
| --- | --- |

Where:

Fs	=	the resulting gas mobility reduction factor as a function of surfactant

concentration,

Cs 	=	surfactant concentration,

Crs	=	reference surfactant concentration, that is Cs < Csr defines a weak foam and

Cs > Csr defines a strong foam (FOAMCON), and

es 	=	exponent that determines the gradient in the change of the reduction in

gas mobility due to foam (FAOAMEXP).


The functional form of the reduction in gas mobility factor (Mrf) is:


| ${M}_{\mathit{rf}} = \frac{1}{1 + \left({M}_{r} \times  {F}_{s} \times  {F}_{w} \times  {F}_{o} \times  {F}_{c}\right)}$ | (8.52) |
| --- | --- |

Where:

Mr	=	the reference mobility reduction factor, see the FOAMFRM keyword in the

PROPS section,

Fs 	=	gas mobility reduction factor as a function of surfactant concentration, see

the FOAMFSC keyword in the PROPS section,

Fw	=	gas mobility reduction factor as a function of water saturation, see

the FOAMFSW keyword in the PROPS section,

Fo 	=	gas mobility reduction factor as a function of oil saturation, see

the FOAMFSO keyword in the PROPS section, and

Fc 	=	gas mobility reduction factor as a function of capillary number, see

the FOAMFCN keyword in the PROPS section.


See also the FOAM keyword in the RUNSPEC section, the FOAMADS, FOAMMOB, FOAMOPTS and FOAMROCK keywords in the PROPS section.


#### Example


```
--
--       FOAM GAS MOBILITY VERSUS SURFACTANT CONCENTRATION FUNCTIONS
--
FOAMFSC
--       FOAM       FOAM      FOAM      FOAM
--       FOAMCON    FOAMEXP   MINSURF   MINSWAT
--       -------    -------   -------   -------
           0.001      1.010                            / TABLE NO. 01
           0.002      1.000                            / TABLE NO. 02
                                                       / TABLE NO. 03 (DEFAULTED)
           0.001      0.850  1.0E-10                   / TABLE NO. 04
           0.002      1.030                            / TABLE NO. 05
           0.002      1.000                            / TABLE NO. 06
```


Here, NTSFUN equals six on the TABDIMS keyword in the RUNSPEC section and therefore six entries are required for the FOAMFSC keyword. Table number three is completed defaulted and will therefore use all the properties from the previous table, that is table number two.
