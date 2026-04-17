### NETWORK – Activate the Extended Network Option and Define Parameters {#kw-NETWORK}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

This keyword activates the Extended Network option and defines the maximum number of nodes and links (branches) in the network. The Extended Network option is a different facility to the Standard Network facility, as such, this keyword should only be used if the former network is required for the run.


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| 1 | NODMAX | NODMAX is a positive integer that defines the maximum number of nodes in the Extended Network model. | None |
| 2 | NBRMAX | NBRMAX is a positive integer that defines the maximum number of links in the Extended Network model. | None |
| 3 | NBCMAX | NBCMAX is a positive integer that defines the maximum number of branches that can be connected to a node in the Extended Network model,  used in the commercial compositional simulator. The parameter is ignored by OPM Flow and should be defaulted or set to the default value of 20. | 20 |
| Notes: |  |  |  |
: NETWORK Keyword Description {#tbl-5-25}
#### Example


```
--
--       ACTIVATE THE EXTENDED NETWORK OPTION AND DEFINE PARAMETERS
--
--       MAX.    MAX     NOT
--       NODE    LINK    USED
NETWORK
         10       12     1*                                                    /
```


In the above example the maximum number of nodes is set equal to ten and the maximum number of links (or branches) is set equal to 12, for the Extended Network option.