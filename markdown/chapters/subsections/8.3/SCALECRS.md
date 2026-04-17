### SCALECRS – Define End-Point Scaling Option {#kw-SCALECRS}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The SCALECRS keyword sets the end-point scaling option to be either two-point or three-point scaling, for when the End-Point Scaling option has been invoked by the [ENDSCALE](#kw-ENDSCALE) keyword in the [RUNSPEC](#kw-RUNSPEC) section.   This determines which end-points on the relative permeability curves are used for scaling based on the supplied end-point arrays ([SGCR](#kw-SGCR), [SWCR](#kw-SWCR), etc.).


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | SCALEOPT | SCALEOPT is a character string that sets the end-point scaling option and should be set to either NO or YES: | NO |
| Notes: |  |  |  |
: SCALECRS Keyword Description {#tbl-8-143}
The end-point scaled for each option and the arrays used in the end-point scaling are summarized in the following table:


| Option | Phases | Relative Permeability End-Point | Minimum Saturation End-Point | Middle Saturation End-Point | Maximum Saturation End-Point |
| --- | --- | --- | --- | --- | --- |
| Two-Point | Water | [KRW](#kw-KRW) | [SWCR](#kw-SWCR) |  | [SWU](#kw-SWU) |
| Gas | [KRG](#kw-KRG) | [SGCR](#kw-SGCR) |  | [SGU](#kw-SGU) |  |
| Oil-Water | [KRORW](#kw-KRORW) | [SOWCR](#kw-SOWCR) |  | (1.0 – [SWL](#kw-SWL) - [SGL](#kw-SGL)) |  |
| Oil-Gas | [KRORG](#kw-KRORG) | [SOGCR](#kw-SOGCR) |  | (1.0 – [SWL](#kw-SWL) - [SGL](#kw-SGL)) |  |
| Three-Point | Water | [KRW](#kw-KRW) | [SWCR](#kw-SWCR) | (1.0 – [SOWCR](#kw-SOWCR) - [SGL](#kw-SGL)) | [SWU](#kw-SWU) |
| Gas | [KRG](#kw-KRG) | [SGCR](#kw-SGCR) | (1.0 - [SOGCR](#kw-SOGCR)-[SWL](#kw-SWL)) | [SGU](#kw-SGU) |  |
| Oil-Water | [KRORW](#kw-KRORW) | [SOWCR](#kw-SOWCR) | (1.0 – [SWCR](#kw-SWCR) - [SGL](#kw-SGL)) | (1.0 – [SWL](#kw-SWL) - [SGL](#kw-SGL)) |  |
| Oil-Gas | [KRORG](#kw-KRORG) | [SOGCR](#kw-SOGCR) | (1.0 – [SGCR](#kw-SGCR) - [SGL](#kw-SGL)) | (1.0 – [SWL](#kw-SWL) - [SGL](#kw-SGL)) |  |
| Two Phase Gas-Water Simulations |  |  |  |  |  |
| Water | [KRW](#kw-KRW) | [SWCR](#kw-SWCR) | (1.0 - [SGCR](#kw-SGCR)) | [SWU](#kw-SWU) |  |
| Gas | [KRG](#kw-KRG) | [SGCR](#kw-SGCR) | (1.0 -[SWCR](#kw-SWCR)) | [SGU](#kw-SGU) |  |
: End-Point Arrays Used in the End-Point Scaling Options {#tbl-8-144}
See also the [TZONE](#kw-TZONE) keyword in the [PROPS](#kw-PROPS) section that sets the transition zone end-point scaling options for the oil, gas and water phases.


#### Example


```
--
--       TWO-POINT END-POINT SCALING IS NO THREE POINT IS YES
--
--       SCALEOPT
--       ---------
SCALECRS
         YES                                               / SCALING OPTION
```

The above example activates three-point end-point scaling of the relative permeability curves.