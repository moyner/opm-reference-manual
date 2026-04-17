### HMPROPS – History Match End-Point Section Start {#kw-HMPROPS}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

HMPROPS defines the start of a history match end-points section, for when the History Match Gradient option has been activated by the [HMDIMS](#kw-HMDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. In addition, the End-Point Scaling option must also be activated by the [ENDSCALE](#kw-ENDSCALE) keyword which is also in the [RUNSPEC](#kw-RUNSPEC) section. The keyword allows for the [BOX](#kw-BOX), [EQUALS](#kw-EQUALS), [COPY](#kw-COPY), [MINVALUE](#kw-MINVALUE), [MAXVALUE](#kw-MAXVALUE) and [ADD](#kw-ADD) keywords to be used with the [HA](#kw-HA) and [HM](#kw-HM) series of keywords that reference the end-point scaling arrays, that is:  HMKRG, HMKRGR, HMKRO, HMKRORG, HMKRORW, HMKRW,  HMKRWR, HMPCW, HMPCG, HMSGCR, HMSOWCR, HMSOGCR, HMSWCR, and HMSWL keywords.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.