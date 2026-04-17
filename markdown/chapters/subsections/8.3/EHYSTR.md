### EHYSTR – Define Hysteresis Model and Parameters


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The EHYSTR keyword defines the hysteresis model and associated parameters when the hysteresis option has been activated by the HYSTER variable on the SATOPTS keyword in the RUNSPEC section. Both the Carlson [Carlson, F. M. “Simulation of Relative Permeability Hysteresis to the Non-Wetting Phase,” paper SPE 10157, presented at the SPE Annual Technical Conference & Exhibition, San Antonio, Texas, USA (October 5-7, 1981).] and Killough [Killough, J. E. “Reservoir Simulation with History-dependent Saturation Functions,” paper SPE 5106, Society of Petroleum Engineers Journal (1976) 16, No. 1, 37-48.] models are available.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | HYSTRCP | HYSTRCP is a positive real value that defines the Killough curvature parameter for capillary pressure hysteresis model. The value should range from 0.05 to 0.10. This item is not supported by OPM Flow and should be defaulted (1*). | 0.1 |
| 2 | HYSTMOD | An integer value that determines the relative permeability hysteresis model to be used depending on the phase and the wettability of the system. HYSTMOD should be set to one of the following values: | 0 |
| Water Wet Hysteresis Models |  |  |  |
| HYSTMOD | Non-Wetting Phases | Wetting Phase |  |
| -1 | Equilibration option for equilibrating the model with the SATNUM (drainage curves) and running the model with imbibition curves (IMBNUM). This option implies no hysteresis. |  |  |
| 0 | Carlson Hysteresis Model | SATNUM |  |
| 1 | Carlson Hysteresis Model | IMBNUM |  |
| 2 | Killough Hysteresis Model | SATNUM |  |
| 3 | Killough Hysteresis Model | IMBNUM |  |
| 4 | Killough Hysteresis Model | Killough Hysteresis Model |  |
| Oil Wet to Water Wet Water Wet |  |  |  |
| 5 | Carlson Non- Wetting Modeling for Gas and Water | SATNUM |  |
| 6 | Killough Non- Wetting Modeling for Gas and Water | SATNUM |  |
| 7 | Killough Non- Wetting Modeling for Gas and Water | Killough Non- Wetting Modeling for the Wetting Oil Phase |  |
| Only the HYSTMOD options not colored orange are currently support by OPM Flow. |  |  |  |
| 3 | HYSTREL | HYSTREL is a positive real number that defines the Killough’s wetting phase relative permeability curvature parameter. This parameter is only applicable if HYSMOD is set to either 4 or 7. This item is not supported by OPM Flow and should be defaulted (1*). | 1.0 |
| 4 | HYSTSGR | HYSTSGR is a positive real number that sets a scaling parameter for the trapped non-wetting phase saturation in the Killough model. This item is not supported by OPM Flow and should be defaulted (1*). | 0.1 |
| 5 | HYSTOPT | A defined character string that determines if the hysteresis model should be activated for relative permeability, capillary pressure, or both, and should be set to one of the following: | BOTH |
| 6 | HYSTSCAN | A defined character string that determines the shape of Killough capillary pressure scanning curves when secondary reversal occurs, that is for a drainage, imbibition, drainage cycle. Only the RETR option is supported by OPM Flow. | RETR |
| 7 | HYSTMOB | A defined character string that determines how to apply the mobility control correction invoked by the MOBILE variable on the EQLOPTS keyword in the RUNSPEC section. HYSTMOB should be set to one of the following: The Mobility Control option is not supported in OPM Flow so this parameter has no effect and will be ignored. This item should be defaulted. | DRAIN |
| 8 | HYSTWET | A defined character string that sets the wetting phase between oil and gas in three phase systems and should be set to one of the following: Note for all the above cases the gas relative permeability is always modelled as a non-wetting phase. Note oil is always the wetting phase to gas in two phase systems. This item is not supported by OPM Flow and should be defaulted (1*). | OIL |
| 9 | HYBAKOIL | Baker model one or model two relative permeability oil phase hysteresis option used in the commercial compositional simulator. This item is not supported by OPM Flow and should be defaulted (1*). | NO |
| 10 | HYBAKGAS | Baker model one or model two relative permeability gas phase hysteresis option used in the commercial compositional simulator. This item is not supported by OPM Flow and should be defaulted (1*). | NO |
| 11 | HYBAKWAT | Baker model one or model two relative permeability water phase hysteresis option used in the commercial compositional simulator. This item is not supported by OPM Flow and should be defaulted (1*). | NO |
| 12 | HYTHRESH | Killough’s hysteresis threshold saturation value used in the commercial compositional simulator. This item is not supported by OPM Flow and should be defaulted (1*). | 0.0 |
| 13 | HYSWETRP | Killough’s hysteresis wetting phase modification used in the commercial black-oil simulator. This item is not supported by OPM Flow and should be defaulted (1*). | 0 |
| 14 | HYSPCSCL | An integer value that determines if capillary pressure scaling should be enabled to correct the construction of the scanning capillary pressure curve. This option is currently disabled by default but this is likely to change as the correction is believed to be a bug fix. For more information see [#6383](https://github.com/OPM/opm-simulators/issues/6383#issuecomment-3329954105). This is an OPM Flow specific item that is not supported by the commercial simulator. | 0 |
| Notes: |  |  |  |

*Table 8.32: EHYSTR Keyword Description*


#### Example


```
--
--       HYSTERESIS MODEL AND PARAMETERS
--
--       PC-CUR  MODEL   RELPERM TRAPPED OPTION  SHAPE    MOBILIT  WET
--       HYSTRCP HYSTMOD HYSTREL HYSTSGR HYSTOPT HYSTSCAN HYSTMOB  HYSTWET
EHYSTR
         0.1     0       0.1     1*      KR      1*       1*       1*          /

```

The above example defines the hysteresis model and parameters used in the Norne model. Here the default value is used for the Killough curvature parameter for capillary pressure hysteresis mode, the Carlson hysteresis model is used for the non-wetting phase and SATNUM for the wetting phase, 0.1 is used for Killough’s wetting phase relative permeability curvature parameter (this parameter is ignored because the Carlson model has been selected), the default values for the trapped non-wetting phase saturation in the Killough mode (again, this parameter is ignored because the Carlson model has been selected, and the hysteresis modeling is only applied to relative permeability curves).
