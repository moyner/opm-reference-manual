### PLMIXNUM – Define the Polymer Region Numbers {#kw-PLMIXNUM}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The PLMIXNUM keyword defines the polymer region number for each grid block that is used to assign the mixing tables as well as the maximum polymer and salt concentrations, as defined by the [PLMIXPAR](#kw-PLMIXPAR) and [PLYMAX](#kw-PLYMAX) keywords in the [PROPS](#kw-PROPS) section, for when the polymer option has been activated by the [POLYMER](#kw-POLYMER) keyword in the [RUNSPEC](#kw-RUNSPEC) section.

The maximum polymer concentration and the associated salt concentration are declared on the [PLYMAX](#kw-PLYMAX) keyword.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | PLMIXNUM | PLMIXNUM defines an array of positive integers greater than or equal to one, that assign a grid cell to a particular table of mixing parameters as defined by the [PLMIXPAR](#kw-PLMIXPAR) and [PLYMAX](#kw-PLYMAX) keywords. The maximum number of PLMIXNUM regions is set by the NPLMIX variable on the [REGDIMS](#kw-REGDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. | 1 |
| Notes: |  |  |  |
: PLMIXNUM Keyword Description {#tbl-9-16}
See also the [PLYADS](#kw-PLYADS), [PLYADSS](#kw-PLYADSS), PLYDHLF, [PLYMAX](#kw-PLYMAX), [PLYROCK](#kw-PLYROCK), [PLYSHEAR](#kw-PLYSHEAR), [PLYSHLOG](#kw-PLYSHLOG) and [PLYVISC](#kw-PLYVISC) keywords in the [PROPS](#kw-PROPS) section.


#### Example

The example below sets three PLMIXNUM regions in the model on a layer by layer basis, using the [EQUALS](#kw-EQUALS) keyword.


```
--
--       ARRAY       CONSTANT     ---------- BOX ---------
--                                I1  I2   J1  J2   K1  K2
EQUALS
         PLMIXNUM      1          1*  1*   1*  1*   1   12 / SET REGION 1
         PLMIXNUM      2          1*  1*   1*  1*   13  55 / SET REGION 2
         PLMIXNUM      3          1*  1*   1*  1*   56 120 / SET REGION 3
/
```