### ENDSCALE – Activate Relative Permeability End-Point Scaling Option {#kw-ENDSCALE}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The ENDSCALE keyword activates OPM Flow’s relative permeability end-point scaling option. The relative permeability functions are defined using the either the:

- [SWOF](#kw-SWOF), [SGOF](#kw-SGOF), [SLGOF](#kw-SLGOF) series of saturation functions, or the
- [SWFN](#kw-SWFN), [SGFN](#kw-SGFN), [SGWFN](#kw-SGWFN), [SOF2](#kw-SOF2), [SOF3](#kw-SOF3), [SOF32D](#kw-SOF32D) series of functions.

And are allocated to the grid cells via the [SATNUM](#kw-SATNUM) keyword.

End-point scaling allows the entered relative permeability functions to be re-scaled based on the saturation end-points allocated to each cell by the [SWL](#kw-SWL), [SWCR](#kw-SWCR), [SWU](#kw-SWU), [SGL](#kw-SGL), [SGCR](#kw-SGCR), [SGU](#kw-SGU), [SOWCR](#kw-SOWCR), and [SOGCR](#kw-SOGCR)  saturation grid arrays for the saturation end-points, and the [KRG](#kw-KRG), [KRORG](#kw-KRORG), [KRORW](#kw-KRORW) and [KRW](#kw-KRW) relative permeability grid cell arrays for the relative permeability end-point data. In addition end-point scaling may be directional dependent in which case the directional dependent versions of the aforementioned arrays should be used, that is SWLX, SWLY and SWLZ instead of [SWL](#kw-SWL) etc. There is also the facility to make the directional end-point scaling reversible or non-reversible and if the non-reversible option is selected the non-reversible versions of the aforementioned arrays should be used, that is SWLX, SWLX-, SWLY, SWLY-  SWLZ and SWLZ-,  instead of [SWL](#kw-SWL) or the SWLX, SWLY and SWLZ set of keywords.

The keyword also defines the number of saturation end-point tables that allows for the re-scaling of the saturation functions to be a function of depth as opposed to being a grid property array. This is accomplished via the [ENKRVD](#kw-ENKRVD) and [ENPTVD](#kw-ENPTVD) keywords in the [PROPS](#kw-PROPS) section.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | DIRECT | A character string that activates or deactivates directional end-point scaling option. If DIRECT is set to NODIR then directional end-point scaling is switched off and the same saturation function is used in the x, y and z directions (unless activated otherwise by the [SATOPTS](#kw-SATOPTS) keyword in the [RUNSPEC](#kw-RUNSPEC) section). In this case the [SWL](#kw-SWL), [SWCR](#kw-SWCR), [SWU](#kw-SWU), [SGL](#kw-SGL), [SGCR](#kw-SGCR), [SGU](#kw-SGU), [SOWCR](#kw-SOWCR) and [SOGCR](#kw-SOGCR) saturation grid arrays and the [KRG](#kw-KRG), [KRORG](#kw-KRORG), [KRORW](#kw-KRORW) and [KRW](#kw-KRW) relative permeability grid cell arrays should be used to enter the grid block end-point data. If DIRECT is set to DIRECT then directional end-point scaling is switched on and different saturation functions are used in the x, y and z directions (unless activated otherwise by the [SATOPTS](#kw-SATOPTS) keyword in the [RUNSPEC](#kw-RUNSPEC) section). Here the directional form of the [SWL](#kw-SWL), [SWCR](#kw-SWCR), [SWU](#kw-SWU), [SGL](#kw-SGL), [SGCR](#kw-SGCR), [SGU](#kw-SGU), [SOWCR](#kw-SOWCR) and [SOGCR](#kw-SOGCR) saturation grid arrays and the [KRG](#kw-KRG), [KRORG](#kw-KRORG), [KRORW](#kw-KRORW) and [KRW](#kw-KRW) relative permeability grid cell arrays should be use to enter the grid block end-point data. For example SWLX, SWLY and SWLZ for [SWL](#kw-SWL). Only the default option is supported by OPM Flow. | NODIR |
| 2 | IRREVERS | A character string that activates or deactivates non-reversible end-point scaling option. If IRREVERS is set to REVERS then the end-point scaling is set to reversible and results in the same set of end-point arrays being used for flow from the xI to xI + 1 direction as for the flow from the xI to the xI – 1 for all directions (x, y and z). Here the SWLX, SWLY and SWLZ series of keywords should be used instead of [SWL](#kw-SWL) type of keywords. Alternatively, if IRREVERS is set to IRREVERS then the end-point scaling is set to non-reversible and results in different sets of end-point arrays being applied for flow from the xI to xI + 1 direction and the xI to the xI – 1 direction, for all directions (x, y, z). in this case the SWLX+, SWLX-, SWLY+, SWLY-  SWLZ+ and SWLZ- series of keywords should be utilized instead of [SWL](#kw-SWL) or the SWLX, SWLY and SWLZ set of keywords. Only the default option is supported by OPM Flow. | REVERS |
| 3 | NTENDP | A positive integer that defines the maximum number of saturation end-point depth tables. The end-point depth tables are used to re-scale the saturation tables as a function of depth as opposed to being a grid block property. NTENDP may also be specified on the [TABDIMS](#kw-TABDIMS) keyword,  and if specified on both here and on the [TABDIMS](#kw-TABDIMS) keyword the maximum value of the two is used. Only the default option is supported by OPM Flow. | 1 |
| 4 | NNODES | A positive integer the defines the maximum number entries for saturation end-point depth tables. | 20 |
| 5 | MODE | A positive integer that activates the options for temperature dependent saturation end-point scaling in the commercial compositional simulator. MODE should be defaulted with either 1* or zero, which means that scaling can only be performed by grid block end-point scaling properties or via saturation end-point depth tables. | 0 |
| Notes: |  |  |  |
: ENDSCALE Keyword Description {#tbl-5-10}
#### Example


```
--       DIRC   REVERSE  MAX     MAX
--       SCALE  SCALE    TABLES  NODES
ENDSCALE
         NODIR  REVERS   1*      1*                                            /

```

The above example invokes the end-point scaling option with end-point scaling being non-directional and reversible with the default number of saturation end-point depth tables (one) with 20 entries per table.