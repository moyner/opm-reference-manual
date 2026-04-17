### WTEMP – Define An Injection Well’s Fluid Temperature {#kw-WTEMP}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The WTEMP keyword defines the temperature of the injection fluid being injected by an injection well.

This keyword can only be used if OPM Flow’s thermal option has been activated by the [THERMAL](#kw-THERMAL) keyword in the [RUNSPEC](#kw-RUNSPEC) section. Note this is different to the commercial simulator that uses the [TEMP](#kw-TEMP) keyword in the [RUNSPEC](#kw-RUNSPEC) section to activate the black-oil thermal model.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for an injection well for which the injection well fluid’s temperature  data is being defined. Note that the well name (WELNAME) must have been declared previously using the [WELSPECS](#kw-WELSPECS) keyword in the [SCHEDULE](#kw-SCHEDULE) section, otherwise an error may occur. | None |
| 2 | [TEMP](#kw-TEMP) | A real positive value greater than zero that defines the temperature of the injected fluid. | None |
| oF | oC | oC |  |
| Notes: |  |  |  |
: WTEMP Keyword Description {#tbl-12-126}
See also the [GCONINJE](#kw-GCONINJE) keyword to define a group’s injection targets and constraints, and the [WCONINJE](#kw-WCONINJE) keyword to define an injection well’s targets and constraints. All the aforementioned keywords are described in the [SCHEDULE](#kw-SCHEDULE) section.


#### Example

The following example defines the injected fluid temperatures for three water injection wells for when the thermal option has been activated by the [THERMAL](#kw-THERMAL) keyword in the [RUNSPEC](#kw-RUNSPEC) section.


```
--
--       DEFINE INJECTION WELL FLUID TEMPERATURE
--
-- WELL  FLUID
-- NAME  TEMP.
--       --------
WTEMP
WI01     39.00                                             /
WI02     37.00                                             /
WI03     39.00                                             /
/
```


Here wells WI01 and WI03 inject water with a water temperature of 39 oF and well WI02’s injection water temperature is 37 oF.