### PERMZ – Define the Permeability in the Z Direction for All the Cells {#kw-PERMZ}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

PERMZ defines the permeability in the Z direction for all the cells in the model via an array. The keyword can be used for all grid types, except for the Radial Grid geometry.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| Field | Metric | Laboratory |  |
| 1 | PERMZ | PERMZ is an array of real positive numbers assigning the permeability in the Z direction to each cell in the model. Repeat counts may be used, for example 200*50.0. | None |
| mD | mD | mD |  |
| Notes: |  |  |  |
: PERMZ Keyword Description {#tbl-6-107}
::: {.callout-note}
Although [PERMX](#kw-PERMX) and [PERMY](#kw-PERMY) are commonly set to be equal, PERMZ is typically not equal to either [PERMX](#kw-PERMX) or [PERMY](#kw-PERMY). Normally PERMZ is set as a fraction of [PERMX](#kw-PERMX) with typical values ranging from 0.1 to 0.5 times [PERMX](#kw-PERMX).
:::


See also the [PERMX](#kw-PERMX) and [PERMY](#kw-PERMY) keywords to fully define the permeability for the model.


#### Example

The example below defines the PERMZ to be 50.0, 5.0, and 20.0 for the first, second and third layers in the model for all 300 cells, as defined by the [DIMENS](#kw-DIMENS) keyword in the [RUNSPEC](#kw-RUNSPEC) section.


```
--
--       DEFINE GRID BLOCK PERMZ DATA FOR ALL CELLS (BASED ON NX x NY x NZ = 300)
--
PERMZ
         100*50.0    100*5.0   100*20.0                                         /

```


The next example sets [PERMX](#kw-PERMX) to be 500.0, 50.0, and 200.0 for the first, second and third layers in the model for all 300 cells, as defined by the [DIMENS](#kw-DIMENS) keyword in the [RUNSPEC](#kw-RUNSPEC) section. It then copies the [PERMX](#kw-PERMX) values to the [PERMY](#kw-PERMY) and PERMZ arrays, and finally multiplies PERMZ by 0.1 times to get the final values for PERMZ.


```
--
--       DEFINE GRID BLOCK PERMX DATA FOR ALL CELLS
--
PERMX
         100*500.0   100*50.0   100*200.0                                      /
--
--       SOURCE      DESTIN.      ---------- BOX ---------
--                                I1  I2   J1  J2   K1  K2
COPY
         PERMX       PERMY        1*  1*   1*  1*   1*  1* / CREATE PERMY
         PERMX       PERMZ        1*  1*   1*  1*   1*  1* / CREATE PERMZ
/
--
--       ARRAY       CONSTANT     ---------- BOX ---------
--                                I1  I2   J1  J2   K1  K2
MULTIPLY
         PERMZ       0.10000      1*  1*   1*  1*   1*  1* / PERMZ * 0.1
/

```

The above sequence of keywords is quite common in input decks, that is copying the [PERMX](#kw-PERMX) data to the [PERMY](#kw-PERMY) and PERMZ arrays and then adjusting the [PERMY](#kw-PERMY) and PERMZ arrays as required using the [MULTIPLY](#kw-MULTIPLY) keyword.