### SOLVENT – Activate the SOLVENT Phase in the Model {#kw-SOLVENT}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword indicates that the solvent phase is present in the model and to activate the four component solvent model for this run. In addition to this keyword, the oil, water and gases phases should also be declared for the run using the [OIL](#kw-OIL), [WATER](#kw-WATER) and [GAS](#kw-GAS) keywords. The keyword will also invoke data input file checking to ensure that all the required Solvent phase input parameters are defined in the input deck.

There is no data required for this keyword and there is no terminating “/” for this keyword.


#### Example


```
--
--       SOLVENT PHASE IS PRESENT IN THE RUN
--
SOLVENT

```

The above example declares that the solvent phase is active in the model.