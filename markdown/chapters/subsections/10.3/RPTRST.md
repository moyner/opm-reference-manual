### RPTRST – Define Data to be Written to the RESTART File {#kw-RPTRST}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword defines the data to be written to the [RESTART](#kw-RESTART) file and the frequency at which restart points will be created. In addition to the solution data arrays required to restart a run, the user may request extra data to be written to the restart file for visualization in OPM ResInsight.

The RPTRST keyword should be followed by a series of character strings that indicate the data to be written. In most cases the character string is the keyword used to load the data in the OPM Flow input deck, for example [KRG](#kw-KRG) for the gas relative permeability of each grid block at the requested times. It is anticipated that OPM Flow will support additional functionality as development progresses.


| No. | Mnemonic | Description | Array Name |
| --- | --- | :------ | --- |
| 1 | ALLPROPS | An alias for the BG, BO, BW, DEN, [KRG](#kw-KRG), [KRO](#kw-KRO), [KRW](#kw-KRW), VGAS, VOIL and VWAT mnemonics combined that writes all the associated properties. |  |
| 2 | BASIC | The BASIC mnemonic defines the frequency at which the restart data and the additional requested data is written to the [RESTART](#kw-RESTART) file. The mnemonic is assigned a value, using the form BASIC=OPTION, where OPTION is an integer variable set to one of the following: |  |
| 3 | BG | Gas formation volume factor. | 1OVERBG |
| 4 | BO | Oil formation volume factor. | 1OVERBO |
| 5 | BW | Water formation volume factor. | 1OVERBW |
| 6 | CONV | Identify the worst n cells causing convergence problems based on the residuals of each equation (CNV_XXX), using the form CONV=n. In addition, the number of Newton iterations required by each cell in order to satisfy the solution change convergence criteria at the last time step (CONV_NEW). | CNV_GAS CNV_OIL CNV_WAT CONV_NEW |
| 7 | DEN | Fluid phase densities at reservoir conditions. | GAS_DEN OIL_DEN WAT_DEN |
| 8 | [FIP](#kw-FIP) | Volumes in place for each phase at surface conditions. | FIPGAS FIPOIL FIPWAT |
| 9 | FLOWS | Inter-block volumetric flows at surface conditions for each phase ([GAS](#kw-GAS), [OIL](#kw-OIL), WAT) in the I+, J+ and K+ directions. The Array Name column shows the arrays for just the [GAS](#kw-GAS) phase, the other phases will have similar arrays. | FLOGASI+ FLOGASJ+ FLOGASK+ |
| 10 | FLOWS- | Inter-block volumetric flows at surface conditions for each phase ([GAS](#kw-GAS), [OIL](#kw-OIL), WAT) in the I-, J- and K- directions. The Array Name column shows the arrays for just the [GAS](#kw-GAS) phase, the other phases will have similar arrays. | FLOGASI- FLOGASJ- FLOGASK- |
| 11 | FLORES | Inter-block volumetric flows at reservoir conditions for each phase ([GAS](#kw-GAS), [OIL](#kw-OIL), WAT) in the I+, J+ and K+ directions. The Array Name column shows the arrays for just the [GAS](#kw-GAS) phase, the other phases will have similar arrays. | FLRGASI+ FLRGASJ+ FLRGASK+ |
| 12 | FLORES- | Inter-block volumetric flows at reservoir conditions for each phase ([GAS](#kw-GAS), [OIL](#kw-OIL), WAT) in the I-, J- and K- directions. The Array Name column shows the arrays for just the [GAS](#kw-GAS) phase, the other phases will have similar arrays. | FLRGASI- FLRGASJ- FLRGASK- |
| 13 | FREQ | The FREQ mnemonic defines the frequency at which restart data is written when BASIC=3, 4 or 5, using the form FREQ=n. |  |
| 14 | [KRG](#kw-KRG) | Gas relative permeability at the grid block's gas saturation. | GASKR |
| 15 | [KRO](#kw-KRO) | Oil relative permeability at the grid block's oil saturation. | OILKR |
| 16 | [KRW](#kw-KRW) | Water relative permeability at the grid block's water saturation. | WATKR |
| 17 | PBPD | Bubble point and dew point pressures. | [PBUB](#kw-PBUB) [PDEW](#kw-PDEW) |
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
: RPTRST Keyword Description {#tbl-10-26}
Note, older versions of the commercial simulator used integer values to control the output to the [RESTART](#kw-RESTART) file, this type of format is not supported by OPM Flow and thus the integers should be converted to the mnemonic format as outlined in @tbl-10-26.

Note that OPM Flow automatically writes out all the data required to make a restart run as outlined in the table below:


| No. | Mnemonic | Description | Array Name |
| --- | --- | :------ | --- |
| 1 | [BIOFILM](#kw-BIOFILM) | Biofilm volume fraction used when the [BIOFILM](#REF_HEADING_KEYWORD_BIOFILM) or [MICP](#kw-MICP) option has been activated in the [RUNSPEC](#kw-RUNSPEC) section. | [BIOFILM](#kw-BIOFILM) |
| 2 | CALCITE | Calcite volume fraction used when the [MICP](#kw-MICP) option has been activated in the [RUNSPEC](#kw-RUNSPEC) section. | CALCITE |
| 3 | [FOAM](#kw-FOAM) | Foam concentration used when the [FOAM](#kw-FOAM) option has been activated in the [RUNSPEC](#kw-RUNSPEC) section. | [FOAM](#kw-FOAM) |
| 4 | MICROBES | Microbe concentration used when the [BIOFILM](#REF_HEADING_KEYWORD_BIOFILM) or [MICP](#kw-MICP) option has been activated in the [RUNSPEC](#kw-RUNSPEC) section. | MICROBES |
| 5 | [MULTPV](#kw-MULTPV) | Pore volume multiplier output when [MULTPV](#kw-MULTPV) keyword is present in the input deck. | [MULTPV](#kw-MULTPV) |
| 6 | OXYGEN | Oxygen concentration used when the [MICP](#kw-MICP) option has been activated in the [RUNSPEC](#kw-RUNSPEC) section. | OXYGEN |
| 7 | [PERMFACT](#kw-PERMFACT) | Permeability multiplication factor as a function of porosity change used when the [PRECSALT](#kw-PRECSALT) option has been activated in the [RUNSPEC](#kw-RUNSPEC) section | [PERMFACT](#kw-PERMFACT) |
| 8 | [POLYMER](#kw-POLYMER) | Polymer concentration used when the [POLYMER](#kw-POLYMER) option has been activated in the [RUNSPEC](#kw-RUNSPEC) section | [POLYMER](#kw-POLYMER) |
| 9 | PPCW | Modified oil-water capillary pressure end-points used when the [SWATINIT](#kw-SWATINIT) keyword has been included in the input deck. | PPCW |
| 10 | [PRESSURE](#kw-PRESSURE) | Pressure data for each grid block. | [PRESSURE](#kw-PRESSURE) |
| 11 | [RS](#kw-RS) | Dissolved gas-oil ratio for each grid block. | [RS](#kw-RS) |
| 12 | [RSW](#REF_HEADING_KEYWORD_RSW_10_3) | Dissolved gas-water ratio for each grid block for use when the [DISGASW](#kw-DISGASW) option has been activated in the [RUNSPEC](#kw-RUNSPEC) section. | [RSW](#REF_HEADING_KEYWORD_RSW_10_3) |
| 13 | RSWSOL | Dissolved solvent-water ratio for each grid block for use when the [SOLVENT](#kw-SOLVENT) and [DISGASW](#kw-DISGASW) options have been activated in the [RUNSPEC](#kw-RUNSPEC) section. | RSWSOL |
| 14 | [RV](#kw-RV) | Vaporized oil-gas ratio for each grid block. | [RV](#kw-RV) |
| 15 | [RVW](#kw-RVW) | Vaporized water-gas ratio for each grid block for use when the [VAPWAT](#kw-VAPWAT) option has been activated in the [RUNSPEC](#kw-RUNSPEC) section. | [RVW](#kw-RVW) |
| 16 | [SALT](#kw-SALT) | Salt concentration for each grid block for use when the [BRINE](#kw-BRINE) option has been activated in the [RUNSPEC](#kw-RUNSPEC) section. | [SALT](#kw-SALT) |
| 17 | [SALTP](#kw-SALTP) | Precipitated salt volume fraction for each grid block for use when the [PRECSALT](#kw-PRECSALT) option has been activated in the [RUNSPEC](#kw-RUNSPEC) section. | [SALTP](#kw-SALTP) |
| 18 | [SGAS](#kw-SGAS) | Gas saturation for each grid block. | [SGAS](#kw-SGAS) |
| 19 | SGMAX | Maximum gas saturation reached used when gas-oil non-wetting phase relative permeability hysteresis has been activated. | SGMAX |
| 20 | SHMAX | Maximum wetting phase saturation reached used when gas-oil wetting phase relative permeability hysteresis has been activated. | SHMAX |
| 21 | [SOIL](#kw-SOIL) | Oil saturation each grid block. | [SOIL](#kw-SOIL) |
| 22 | SOMAX | Maximum oil saturation reached used when the [VAPPARS](#kw-VAPPARS) keyword has been included in the input deck, or when oil-water non-wetting phase relative permeability hysteresis has been activated. | SOMAX |
| 23 | SOMIN | Minimum oil saturation reached used when gas-oil capillary pressure hysteresis has been activated. | SOMIN |
| 24 | SSOLVENT | Solvent saturation for each grid block used when the [SOLVENT](#kw-SOLVENT) option has been activated in the [RUNSPEC](#kw-RUNSPEC) section. | SSOLVENT |
| 25 | [SWAT](#kw-SWAT) | Water saturation for each grid block. | [SWAT](#kw-SWAT) |
| 26 | SWHY1 | Minimum water saturation reached used when oil-water capillary pressure hysteresis has been activated. | SWHY1 |
| 27 | SWMAX | Maximum water saturation reached used when oil-water wetting phase relative permeability hysteresis has been activated. | SWMAX |
| 28 | [TEMP](#kw-TEMP) | Temperature of each grid block used when the [THERMAL](#kw-THERMAL) option has been activated in the [RUNSPEC](#kw-RUNSPEC) section. OPM Flow also supports the output of temperatures for non-thermal simulations when the [TEMP](#kw-TEMP) mnemonic is specified. | [TEMP](#kw-TEMP) |
| 29 | UREA | Urea concentration used when the [MICP](#kw-MICP) option has been activated in the [RUNSPEC](#kw-RUNSPEC) section. | UREA |
| Notes: |  |  |  |
: Data Sets Automatically Written to the RESTART File {#tbl-10-27}
::: {.callout-note}
Currently, OPM Flow distinguishes between those arrays which are required for restarting a run and those which are "merely" for visualization and analysis. However, this classification is imperfect and leads to potentially exporting arrays that are incompatible with the commercial simulator, such as the [TEMP](#kw-TEMP) array in non-thermal simulation runs. If one is willing to forego the ability to restart an OPM Flow simulation run, using the commercial simulator, e.g., simulating the historic period using OPM Flow and the prediction period using the commercial simulator, then additional arrays are available, including the [PBUB](#kw-PBUB) and [PDEW](#kw-PDEW) vectors generated by the PBPD option, by using the following command line option: --enable-opm-rst-file=true
:::


If the --enable-opm-rst-file=true command line option has been specified then the following OPM Flow specific data are also automatically output for visualization only as outlined in the table below:


| No. | Mnemonic | Description | Array Name |
| --- | --- | :------ | --- |
| 1 | XMFCO2 | CO2 liquid-phase mole fractions written when the [CO2STORE](#kw-CO2STORE) option has been activated in the [RUNSPEC](#kw-RUNSPEC) section. | XMFCO2 |
| 2 | XMFH2 | H2 liquid-phase mole fractions written when the [H2STORE](#REF_HEADING_KEYWORD_H2STORE) option has been activated in the [RUNSPEC](#kw-RUNSPEC) section. | XMFH2 |
| 3 | YMFWAT | Water gas-phase mole fractions written when either the [CO2STORE](#kw-CO2STORE) or [H2STORE](#REF_HEADING_KEYWORD_H2STORE) option has been activated in the [RUNSPEC](#kw-RUNSPEC) section. | YMFWAT |
| Notes: |  |  |  |
: Data Sets Automatically Written to the RESTART File for Visualization Only {#tbl-10-27}
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