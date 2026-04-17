### PERMJFUN – Define Leverett J-Function Permeability for All Cells {#kw-PERMJFUN}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

PERMJFUN defines the permeability to be used in de-normalizing the Leverett J-Functions^[Leverett, M. C.; “Capillary Behaviour in Porous Solids”, Trans. AIME (1941) 142, 152-168.] for when the PERM variable on the [JFUNC](#kw-JFUNC) or the [JFUNCR](#kw-JFUNCR) keyword in the [GRID](#kw-GRID) section has been set to “U”, as oppose to using [PERMX](#kw-PERMX), [PERMY](#kw-PERMY), [PERMZ](#kw-PERMZ) arrays etc.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | PERMJFUN | PERMJFUN is an array of real positive numbers assigning the permeability to be used in de-normalizing the Leverett J-Function to each cell in the model. Repeat counts may be used, for example 20*100.0. | None |
| mD | mD | mD |  |
| Notes: |  |  |  |
: PERMJFUN Keyword Description {#tbl-6-102}
For grid blocks that have not been assigned a PERMJFUN value the default directional permeability will be used, that is the average of [PERMX](#kw-PERMX) and [PERMY](#kw-PERMY).


See also the [PERMX](#kw-PERMX), [PERMY](#kw-PERMY) and [PERMZ](#kw-PERMZ) keywords to fully define the permeability for the model.


#### Example


```
--
--       DEFINE GRID BLOCK PERMJFUN FOR ALL CELLS (BASED ON NX x NY x NZ = 300)
--
PERMJFUN
         100*500.0   100*50.0   100*200.0                                      /

```

The above example defines the PERMJFUN to be 500.0, 50.0, and 200.0 for the first, second and third layers in the model for all 300 cells, as defined by the [DIMENS](#kw-DIMENS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.