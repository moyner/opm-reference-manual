### NONNC – Deactivate Non-Neighbor Connections {#kw-NONNC}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The NONNC keyword deactivates non-neighbor connections (“NNCs”) in the current run.  NNCs create off-diagonal elements in the Jacobi matrix that impact the numerical efficiency of the solution algorithms, and thus if the run does not contain NNCs then there is the potential for greater computation efficiency.   Unfortunately, nearly all models, except for the most simple models, generate NNCs via for example:

- aquifer connections,
- faults, and
- manually entered NNCs,  including those automatically generate by pre-processing software.

There is no data required for this keyword and there is no terminating “/” for this keyword.


#### Example


```
--
--       DEACTIVATE NON-NEIGHBOR CONNECTIONS
--
NONNC

```

The above example switches off the NNCs.