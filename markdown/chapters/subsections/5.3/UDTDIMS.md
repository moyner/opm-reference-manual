### UDTDIMS – Define the Dimensions of the User Defined Tables {#kw-UDTDIMS}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword defines the dimensions of the User Defined Tables (“[UDT](#kw-UDT)”) used by OPM Flow that can be used as lookup tables when assigning values to User Defined Quantities ("[UDQ](#kw-UDQ)") using the [UDQ](#kw-UDQ) keyword in the [SCHEDULE](#kw-SCHEDULE) section. UDTs are defined by the [UDT](#kw-UDT) keyword in the [SCHEDULE](#kw-SCHEDULE) section.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | MXUDT | MXUDT is a positive integer that defines the maximum number of User Defined Tables | 0 |
| 2 | NUDT | NUDT is a positive integer that defines the maximum number of rows in any given User Defined Table. | 0 |
| 3 | MXINTP | MXINTP is a positive integer that defines the maximum number of interpolation points allowed in any given dimension. | 0 |
| 4 | MXDIMS | MXDIMS is a positive integer that defines the maximum number of dimensions in any given User Defined Table. Only one dimensional tables are currently supported by OPM Flow. | 0 |
| Notes: |  |  |  |
: UDTDIMS Keyword Description {#tbl-5-53}
#### Example


```
--
--       USER DEFINED TABLE DIMENSIONS
--
--       MAX     MAX   MAX     MAX
--       TABLES  ROWS  INTPOL  DIMS
UDTDIMS
         3       20    3       2                                               /
```


In the above example the maximum number of [UDT](#kw-UDT) tables is set to three and the maximum number of rows for each table is 20, the maximum number of interpolation points in any given dimension is set to three and the maximum number of dimensions is defined as two.