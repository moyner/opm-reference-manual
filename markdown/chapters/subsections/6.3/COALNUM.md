### COALNUM – Define the Coal Region Numbers


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The COALNUM keyword defines the coal region numbers for each grid block used with the Coal Bed Methane option (“CBM”). OPM Flow does not have a CBM option; however, the keyword is documented here for completeness.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | COALNUM | COALNUM defines an array of positive integers assigning a grid cell to a particular coal region. The maximum number of COALNUM regions is set by the NTCREG variable on REGDIMS keywords in the RUNSPEC section. | 1 |
| Notes: |  |  |  |

*Table 6.13: COALNUM Keyword Description*


#### Example

The example below sets three COALNUM regions for a 4 x 5 x 2 model.


```
--
--       DEFINE COALNUM REGIONS FOR ALL CELLS
--
COALNUM
         2  2  1  1  2  2  1  1  1  1  1  1  1  1  1  1  1  1  1  1
         3  3  1  1  3  3  1  1  1  1  1  1  1  1  1  1  1  1  1  1
/
```


The above will no effect in an OPM Flow input deck.
