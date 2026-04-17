### CNAMES  –  Define Compositional Component Names {#kw-CNAMES}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The CNAMES keyword defines the names for each of the compositional components active in the model. The keyword should only be used if the compositional mode has been requested using the [COMPS](#kw-COMPS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.

OPM Flow does not currently support the general compositional modeling formulation.


::: {.callout-note}
This keyword is only supported by OPM Flow when the two phase gas-water CO2 storage model has been activated using the [CO2STORE](#kw-CO2STORE) keyword and either the [GASWAT](#kw-GASWAT) or the [GAS](#kw-GAS) and [WATER](#kw-WATER) keywords in the [RUNSPEC](#kw-RUNSPEC) section. Only the component names "H2O", "CO2" and "NACL" (water, CO2 and salt respectively) are recognized when the CNAMES keyword is used with the [CO2STORE](#kw-CO2STORE) keyword; any other component names are ignored.
:::


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | CNAMES | A series of character strings of up to eight characters in length that define the names for each of the compositional components active in the model. | None |
| Notes: |  |  |  |
: CNAMES Keyword Description {#tbl-8-25}
#### Example

The following example defines how to confirm a three component formulation, together with defining the names of the compositional components, to be used with the [CO2STORE](#kw-CO2STORE) and [GASWAT](#kw-GASWAT) options.


```
--
--       CONFIRM NUMBER OF COMPOSITIONAL COMPONENTS (OPM FLOW KEYWORD)
--
NCOMPS
                3                                                                      /
--
--       DEFINE COMPOSITIONAL COMPONENTS NAMES (OPM FLOW KEYWORD)
--
CNAMES
         'H2O'
         'CO2'
         'NACL'                                                                 /
```