### DCQDEFN – Define Gas DCQ Units as Rate or Energy {#kw-DCQDEFN}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The DCQDEFN keyword defines the DCQ units to be rate or energy (calorific value) when using the Gas Field Operation model and the Gas Calorific Value control option. The gas DCQ rates are controlled by the [GASYEAR](#kw-GASYEAR), [GASPERIO](#kw-GASPERIO), [GDCQ](#kw-GDCQ), [GASFTARG](#kw-GASFTARG) or [GASFDECR](#kw-GASFDECR) keywords in the [SCHEDULE](#kw-SCHEDULE) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.