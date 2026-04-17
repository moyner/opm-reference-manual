### HM – History Match End-Point Gradient Multiplicative Modifier {#kw-HM}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The HM series of keywords defines the history match end-point gradient parameters used to set the multiplicative cumulative end point data, for when the History Match Gradient option has been activated by the [HMDIMS](#kw-HMDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. In addition, the End-Point Scaling option must also be activated by the [ENDSCALE](#kw-ENDSCALE) keyword which is also in the [RUNSPEC](#kw-RUNSPEC) section. The keyword consists of the first two characters of “HM” followed by the end-point keyword shown in @tbl-8-46, for example, HMSWL.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.


| Type | End-Point Keyword | Oil-Water End-Point Definitions |
| --- | --- | --- |
| Saturation | [SWL](#kw-SWL) | Connate water saturation, that is the smallest water saturation in a water saturation function table. |
| [SWCR](#kw-SWCR) | Critical water saturation, that is the largest water saturation for which the water relative permeability is zero. |  |
| [SOWCR](#kw-SOWCR) | Critical oil-in-water saturation, that is the largest oil saturation for which the oil relative permeability is zero in an oil-water system. |  |
| Relative Permeability | [KRW](#kw-KRW) | Relative permeability of water at the maximum water saturation (normally the maximum water saturation is one). |
| [KRO](#kw-KRO) | Relative permeability of oil at the maximum oil saturation. |  |
| [KRWR](#kw-KRWR) | Relative permeability of water at the residual oil saturation or the residual gas saturation in a gas-water run. |  |
| [KRORW](#kw-KRORW) | Relative permeability of oil at the critical water saturation. |  |
| Capillary Pressure | [SWLPC](#kw-SWLPC) | Capillary pressure connate water saturation, that is the smallest water saturation in a water saturation function table. |
| Type | End-Point Keyword | Gas-Oil End-Point Definitions |
| Saturation | [SGL](#kw-SGL) | Connate gas saturation, that is the smallest gas saturation in a gas saturation function table. |
| [SGCR](#kw-SGCR) | Critical gas saturation, that is the largest gas saturation for which the gas relative permeability is zero. |  |
| [SOGCR](#kw-SOGCR) | Critical oil-in-gas saturation, that is the largest oil saturation for which the oil relative permeability is zero in an oil-gas-connate water system. |  |
| Relative Permeability | [KRG](#kw-KRG) | Relative permeability of gas at the maximum gas saturation. |
| [KRGR](#kw-KRGR) | Relative permeability of gas at the residual oil saturation or the critical water saturation in a gas-water run. |  |
| [KRORG](#kw-KRORG) | Relative permeability of oil at the critical gas saturation. |  |
| Capillary Pressure | [SGLPC](#kw-SGLPC) | Capillary pressure connate gas saturation, that is the smallest gas saturation in a gas saturation function table. |
: HM Keyword List {#tbl-8-46}
See also the [HMPROPS](#kw-HMPROPS) keyword in the [PROPS](#kw-PROPS) section that allows the use of the [ADD](#kw-ADD), [BOX](#kw-BOX), [EQUALS](#kw-EQUALS), [COPY](#kw-COPY), [MINVALUE](#kw-MINVALUE), and [MAXVALUE](#kw-MAXVALUE) keywords to be used with the [HA](#kw-HA) and HM series of keywords.