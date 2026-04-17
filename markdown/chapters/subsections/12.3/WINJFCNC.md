### WINJFCNC – Define Injection Well Filtrate Concentration {#kw-WINJFCNC}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [WINJFCNC](#REF_HEADING_KEYWORD_WINJFCNC) keyword defines the injected filtrate concentration for wells that have previously been defined by the [WELSPECS](#kw-WELSPECS) keyword in the [SCHEDULE](#kw-SCHEDULE) section.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the filter cake properties are being defined. Note that the well name (WELNAME) must have been declared previously using the [WELSPECS](#kw-WELSPECS) keyword in the [SCHEDULE](#kw-SCHEDULE) section, otherwise an error may occur. | None |
| 2 | FCONCPPM | A real positive value that defines the volumetric concentration of filtrate in the injected water. This value may be specified using a User Defined Argument (UDA). | 0 |
| ppm | ppm | ppm |  |
| Notes: |  |  |  |
: WINJFCNC Keyword Description {#tbl-12-3-296-1}
See also the [WINJDAM](#REF_HEADING_KEYWORD_WINJDAM) keyword to define the filter cake properties and the [WINJCLN](#REF_HEADING_KEYWORD_WINJCLN) keyword to signal that a filter cake should be completely or partially cleaned. All the aforementioned keywords are described in the [SCHEDULE](#kw-SCHEDULE) section.


#### Example

The following example defines the filtrate injection concentration for a water injection well using [WINJFCNC](#REF_HEADING_KEYWORD_WINJFCNC):


```
--
--       WELL FILTRATE INJECTION CONCENTRATION
--
-- WELL  FILTRATE
-- NAME  CONC
WINJFCNC
INJ-A1   10   /
INJ-B*   30   /
/
```


Well INJ-A1 has a filtrate concentration of 10 ppm in the injection water, and wells matching INJ-B* have a concentration of 30 ppm.