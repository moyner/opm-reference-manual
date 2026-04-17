### ZMFVD  –  Define Compositional Components versus Depth {#kw-ZMFVD}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The ZMFVD keyword defines the compositional component mole fractions, for each component, as a function of depth, as such the keyword should have the same number of component columnar vectors as that declared via the [COMPS](#kw-COMPS) keyword in the [RUNSPEC](#kw-RUNSPEC) section, and the [NCOMPS](#kw-NCOMPS) keyword in the [PROPS](#kw-PROPS) section. The keyword should only be used if the [CO2STORE](#kw-CO2STORE) and [GASWAT](#kw-GASWAT) keywords in the [RUNSPEC](#kw-RUNSPEC) section have also be activated for the gas-water two component model.


::: {.callout-note}
This is an OPM Flow keyword used with OPM Flow’s [CO2STORE](#kw-CO2STORE) and [GASWAT](#kw-GASWAT) keywords in the [RUNSPEC](#kw-RUNSPEC) section, and should not be confused with the more general version of the ZMFVD keyword used in the commercial compositional simulator.
:::


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | [DEPTH](#kw-DEPTH) | A columnar vector of real monotonically increasing down the column   values that defines the depth values for the corresponding compositional component mole fractions. The default number of [DEPTH](#kw-DEPTH) values is 20, as defined by the NDRXVD parameter on the [EQLDIMS](#kw-EQLDIMS) keyword in the [RUNSPEC](#kw-RUNSPEC) section, and which may be used to reset the number of [DEPTH](#kw-DEPTH) values. | None |
| feet | m | cm |  |
| 2 | ZCOMP | A series of columnar vectors, with each columnar vector representing a compositional component mole fraction as a function of [DEPTH](#kw-DEPTH).  In addition, the sum of the compositional component mole fractions must sum to one for a given [DEPTH](#kw-DEPTH) value, otherwise an error will occur. Secondly, if the composition is independent of depth, then only one single row may be entered. Note that the number of columnar vectors, should be the same as that entered via the [NCOMPS](#kw-NCOMPS) keyword in the [PROPS](#kw-PROPS) section, and the [COMPS](#kw-COMPS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. Finally, only the default value of two components are currently supported by OPM Flow. | None |
| mole fraction | mole fraction | mole fraction |  |
| Notes: |  |  |  |
: ZMFVD Keyword Description {#tbl-8-201}
#### Example

The following example defines how to confirm a two component formulation, together with defining the names of the composition components, as well as the compositional gradient, to be used with the [CO2STORE](#kw-CO2STORE) and [GASWAT](#kw-GASWAT) options.


```
--
--       CONFIRM NUMBER OF COMPOSITIONAL COMPONENTS (OPM FLOW KEYWORD)
--
NCOMPS
                2                                                                      /
--
--       DEFINE COMPOSITIONAL COMPONENTS NAMES (OPM FLOW KEYWORD)
--
CNAMES
         'CO2'
         'H2O'                                                                  /
--
--       COMPOSITIONAL COMPONENT MOLE FRACTIONS VS DEPTH (OPM FLOW KEYWORD)
--
--       DEPTH   CO2   H2O
ZMFVD
         2000    0.0   1.0
         2100    0.0   1.0
/
```