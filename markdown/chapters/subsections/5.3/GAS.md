### GAS – Activate the Gas Phase in the Model {#kw-GAS}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword indicate that the gas phase is present in the model and must be used for oil-gas, gas-water, oil-water-gas input decks that contain the gas phase. The keyword will also invoke data input file checking to ensure that all the required gas phase input parameters are defined in the input deck.

There is no data required for this keyword and there is no terminating “/” for this keyword.


#### Example


```
--
--       GAS PHASE IS PRESENT IN THE RUN
--
GAS

```

The above example declares that the gas phase is active in the model.