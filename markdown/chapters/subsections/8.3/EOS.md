### EOS – Specify Equation of State


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [EOS](#REF_HEADING_KEYWORD_EOS_5_3) keyword specifies the Equation Of State ([EOS](#REF_HEADING_KEYWORD_EOS_5_3)) to be used for each [EOS](#REF_HEADING_KEYWORD_EOS_5_3) region. The keyword should only be used if the compositional mode has been requested using the COMPS keyword in the RUNSPEC section.

OPM Flow does not currently support the general compositional modeling formulation.

This keyword is not supported by OPM Flow but it will be parsed and its data ignored.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | EQUATION | A defined character string that specifies the Equation of State to be used, and should be set to one of the following: | PR |
| Notes: |  |  |  |

*Table 8.3.51.1: [EOS](#REF_HEADING_KEYWORD_EOS_5_3) Keyword Description*


#### Example

The following example defines Peng-Robinson as the Equation of State for a model with a single [EOS](#REF_HEADING_KEYWORD_EOS_5_3) region.


```
--
--       SPECIFY EQUATION OF STATE
--
EOS
         PR                                     /

```

The following example defines Peng-Robinson as the Equation of State for [EOS](#REF_HEADING_KEYWORD_EOS_5_3) region one, and Soave-Redlich-Kwong as the Equation of State for [EOS](#REF_HEADING_KEYWORD_EOS_5_3) region two in a model with two [EOS](#REF_HEADING_KEYWORD_EOS_5_3) regions.


```
--
--       SPECIFY EQUATION OF STATE
--
EOS
         PR                                     /
         RK                                     /
```
