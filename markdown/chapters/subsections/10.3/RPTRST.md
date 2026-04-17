### RPTRST – Define Data to be Written to the RESTART File


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword defines the data to be written to the RESTART file and the frequency at which restart points will be created. In addition to the solution data arrays required to restart a run, the user may request extra data to be written to the restart file for visualization in OPM ResInsight.

The RPTRST keyword should be followed by a series of character strings that indicate the data to be written. In most cases the character string is the keyword used to load the data in the OPM Flow input deck, for example KRG for the gas relative permeability of each grid block at the requested times. It is anticipated that OPM Flow will support additional functionality as development progresses.


| No. | Mnemonic | Description | Array Name |
| --- | --- | --- | --- |
| 1 | ALLPROPS | An alias for the BG, BO, BW, DEN, KRG, KRO, KRW, VGAS, VOIL and VWAT mnemonics combined that writes all the associated properties. |  |
| 2 | BASIC | The BASIC mnemonic defines the frequency at which the restart data and the additional requested data is written to the RESTART file. The mnemonic is assigned a value, using the form BASIC=OPTION, where OPTION is an integer variable set to one of the following: |  |
| 3 | BG | Gas formation volume factor. | 1OVERBG |
| 4 | BO | Oil formation volume factor. | 1OVERBO |
| 5 | BW | Water formation volume factor. | 1OVERBW |
| 6 | CONV | Identify the worst n cells causing convergence problems based on the residuals of each equation (CNV_XXX), using the form CONV=n. In addition, the number of Newton iterations required by each cell in order to satisfy the solution change convergence criteria at the last time step (CONV_NEW). | CNV_GAS CNV_OIL CNV_WAT CONV_NEW |
| 7 | DEN | Fluid phase densities at reservoir conditions. | GAS_DEN OIL_DEN WAT_DEN |
| 8 | FIP | Volumes in place for each phase at surface conditions. | FIPGAS FIPOIL FIPWAT |
| 9 | FLOWS | Inter-block volumetric flows at surface conditions for each phase (GAS, OIL, WAT) in the I+, J+ and K+ directions. The Array Name column shows the arrays for just the GAS phase, the other phases will have similar arrays. | FLOGASI+ FLOGASJ+ FLOGASK+ |
| 10 | FLOWS- | Inter-block volumetric flows at surface conditions for each phase (GAS, OIL, WAT) in the I-, J- and K- directions. The Array Name column shows the arrays for just the GAS phase, the other phases will have similar arrays. | FLOGASI- FLOGASJ- FLOGASK- |
| 11 | FLORES | Inter-block volumetric flows at reservoir conditions for each phase (GAS, OIL, WAT) in the I+, J+ and K+ directions. The Array Name column shows the arrays for just the GAS phase, the other phases will have similar arrays. | FLRGASI+ FLRGASJ+ FLRGASK+ |
| 12 | FLORES- | Inter-block volumetric flows at reservoir conditions for each phase (GAS, OIL, WAT) in the I-, J- and K- directions. The Array Name column shows the arrays for just the GAS phase, the other phases will have similar arrays. | FLRGASI- FLRGASJ- FLRGASK- |
| 13 | FREQ | The FREQ mnemonic defines the frequency at which restart data is written when BASIC=3, 4 or 5, using the form FREQ=n. |  |
| 14 | KRG | Gas relative permeability at the grid block's gas saturation. | GASKR |
| 15 | KRO | Oil relative permeability at the grid block's oil saturation. | OILKR |
| 16 | KRW | Water relative permeability at the grid block's water saturation. | WATKR |
| 17 | PBPD | Bubble point and dew point pressures. | PBUB PDEW |
| 18 | PCGW | Gas-water capillary pressure (gas-water simulations). | PCGW |
| 19 | PCOG | Gas-oil capillary pressure. | PCOG |
| 20 | PCOW | Oil-water capillary pressure. | PCOW |
| 21 | RESIDUAL | Component residuals after the last Newton iteration. | RES_GAS RES_OIL RES_WAT |
| 22 | RFIP | Volumes in place for each phase at reservoir conditions. | RFIPGAS RFIPOIL RFIPWAT |
| 23 | ROCKC | Rock compaction: Overburden pressure, minimum oil pressure, maximum water saturation, pore volume multiplier and transmissibility multiplier. | PRES_OVB PRESROCC SWMAX PORV_RC TMULT_RC |
| 24 | RSSAT | Saturated dissolved gas-oil ratio. | RSSAT |
| 25 | RSWSAT | Saturated dissolved gas-water ratio. This is an OPM Flow specific mnemonic that requires the command line option --enable-opm-rst-file=true is specified. | RSWSAT |
| 26 | RVSAT | Saturated vaporized oil-gas ratio. | RVSAT |
| 27 | RVWSAT | Saturated vaporized water-gas ratio. This is an OPM Flow specific mnemonic that requires the command line option --enable-opm-rst-file=true is specified. | RVWSAT |
| 28 | SFIP | Volumes in place for each phase at surface/separator conditions. | SFIPGAS SFIPOIL SFIPWAT |
| 29 | VGAS | Gas viscosity at reservoir conditions. | GAS_VISC |
| 30 | VISC | Fluid phase viscosities at reservoir conditions. | GAS_VISC OIL_VISC WAT_VISC |
| 31 | VOIL | Oil viscosity at reservoir conditions. | OIL_VISC |
| 32 | VWAT | Water viscosity at reservoir conditions. | WAT_VISC |
| Notes: |  |  |  |

*Table 10.26: RPTRST Keyword Description*


Note, older versions of the commercial simulator used integer values to control the output to the RESTART file, this type of format is not supported by OPM Flow and thus the integers should be converted to the mnemonic format as outlined in Table 10.26.

Note that OPM Flow automatically writes out all the data required to make a restart run as outlined in the table below:


| No. | Mnemonic | Description | Array Name |
| --- | --- | --- | --- |
| 1 | BIOFILM | Biofilm volume fraction used when the [BIOFILM](#REF_HEADING_KEYWORD_BIOFILM) or MICP option has been activated in the RUNSPEC section. | BIOFILM |
| 2 | CALCITE | Calcite volume fraction used when the MICP option has been activated in the RUNSPEC section. | CALCITE |
| 3 | FOAM | Foam concentration used when the FOAM option has been activated in the RUNSPEC section. | FOAM |
| 4 | MICROBES | Microbe concentration used when the [BIOFILM](#REF_HEADING_KEYWORD_BIOFILM) or MICP option has been activated in the RUNSPEC section. | MICROBES |
| 5 | MULTPV | Pore volume multiplier output when MULTPV keyword is present in the input deck. | MULTPV |
| 6 | OXYGEN | Oxygen concentration used when the MICP option has been activated in the RUNSPEC section. | OXYGEN |
| 7 | PERMFACT | Permeability multiplication factor as a function of porosity change used when the PRECSALT option has been activated in the RUNSPEC section | PERMFACT |
| 8 | POLYMER | Polymer concentration used when the POLYMER option has been activated in the RUNSPEC section | POLYMER |
| 9 | PPCW | Modified oil-water capillary pressure end-points used when the SWATINIT keyword has been included in the input deck. | PPCW |
| 10 | PRESSURE | Pressure data for each grid block. | PRESSURE |
| 11 | RS | Dissolved gas-oil ratio for each grid block. | RS |
| 12 | [RSW](#REF_HEADING_KEYWORD_RSW_10_3) | Dissolved gas-water ratio for each grid block for use when the DISGASW option has been activated in the RUNSPEC section. | [RSW](#REF_HEADING_KEYWORD_RSW_10_3) |
| 13 | RSWSOL | Dissolved solvent-water ratio for each grid block for use when the SOLVENT and DISGASW options have been activated in the RUNSPEC section. | RSWSOL |
| 14 | RV | Vaporized oil-gas ratio for each grid block. | RV |
| 15 | RVW | Vaporized water-gas ratio for each grid block for use when the VAPWAT option has been activated in the RUNSPEC section. | RVW |
| 16 | SALT | Salt concentration for each grid block for use when the BRINE option has been activated in the RUNSPEC section. | SALT |
| 17 | SALTP | Precipitated salt volume fraction for each grid block for use when the PRECSALT option has been activated in the RUNSPEC section. | SALTP |
| 18 | SGAS | Gas saturation for each grid block. | SGAS |
| 19 | SGMAX | Maximum gas saturation reached used when gas-oil non-wetting phase relative permeability hysteresis has been activated. | SGMAX |
| 20 | SHMAX | Maximum wetting phase saturation reached used when gas-oil wetting phase relative permeability hysteresis has been activated. | SHMAX |
| 21 | SOIL | Oil saturation each grid block. | SOIL |
| 22 | SOMAX | Maximum oil saturation reached used when the VAPPARS keyword has been included in the input deck, or when oil-water non-wetting phase relative permeability hysteresis has been activated. | SOMAX |
| 23 | SOMIN | Minimum oil saturation reached used when gas-oil capillary pressure hysteresis has been activated. | SOMIN |
| 24 | SSOLVENT | Solvent saturation for each grid block used when the SOLVENT option has been activated in the RUNSPEC section. | SSOLVENT |
| 25 | SWAT | Water saturation for each grid block. | SWAT |
| 26 | SWHY1 | Minimum water saturation reached used when oil-water capillary pressure hysteresis has been activated. | SWHY1 |
| 27 | SWMAX | Maximum water saturation reached used when oil-water wetting phase relative permeability hysteresis has been activated. | SWMAX |
| 28 | TEMP | Temperature of each grid block used when the THERMAL option has been activated in the RUNSPEC section. OPM Flow also supports the output of temperatures for non-thermal simulations when the TEMP mnemonic is specified. | TEMP |
| 29 | UREA | Urea concentration used when the MICP option has been activated in the RUNSPEC section. | UREA |
| Notes: |  |  |  |

*Table 10.27: Data Sets Automatically Written to the RESTART File*


::: {.callout-note}
Currently, OPM Flow distinguishes between those arrays which are required for restarting a run and those which are "merely" for visualization and analysis. However, this classification is imperfect and leads to potentially exporting arrays that are incompatible with the commercial simulator, such as the TEMP array in non-thermal simulation runs. If one is willing to forego the ability to restart an OPM Flow simulation run, using the commercial simulator, e.g., simulating the historic period using OPM Flow and the prediction period using the commercial simulator, then additional arrays are available, including the PBUB and PDEW vectors generated by the PBPD option, by using the following command line option: --enable-opm-rst-file=true
:::


If the --enable-opm-rst-file=true command line option has been specified then the following OPM Flow specific data are also automatically output for visualization only as outlined in the table below:


| No. | Mnemonic | Description | Array Name |
| --- | --- | --- | --- |
| 1 | XMFCO2 | CO2 liquid-phase mole fractions written when the CO2STORE option has been activated in the RUNSPEC section. | XMFCO2 |
| 2 | XMFH2 | H2 liquid-phase mole fractions written when the [H2STORE](#REF_HEADING_KEYWORD_H2STORE) option has been activated in the RUNSPEC section. | XMFH2 |
| 3 | YMFWAT | Water gas-phase mole fractions written when either the CO2STORE or [H2STORE](#REF_HEADING_KEYWORD_H2STORE) option has been activated in the RUNSPEC section. | YMFWAT |
| Notes: |  |  |  |

*Table 10.27: Data Sets Automatically Written to the RESTART File for Visualization Only*


#### Examples

The first example request that the standard restart data be written out every month.


```
--
--       RESTART CONTROL BASIC = 4 (YEARLY) 5 (MONTHLY)
--
RPTRST
         BASIC=5                                                               /

```

The next example requests that the standard restart data be written at every report time step until this switch is reset and all the restarts are kept. In addition to the standard the data the gas, oil and water relative permeability data will also be written out at each report time step.


```
--
--       RESTART CONTROL BASIC = 4 (YEARLY) 5 (MONTHLY)
--
RPTRST
         BASIC=2  KRG   KRO   KRW                                             /

```
