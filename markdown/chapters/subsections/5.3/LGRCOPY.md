### LGRCOPY – Activate Local Grid Refinement Inheritance {#kw-LGRCOPY}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The LGRCOPY keyword actives the Local Grid Refinement (“[LGR](#kw-LGR)”) Inheritance option that allows the [LGR](#kw-LGR) to inherit the properties of the global or host cell containing an [LGR](#kw-LGR) grid block when it is defined, as opposed to the normal process of applying this transform at the end of the [GRID](#kw-GRID) section. LGRCOPY can be used in the [RUNSPEC](#kw-RUNSPEC), [GRID](#kw-GRID) and [EDIT](#kw-EDIT) sections. If used in the [RUNSPEC](#kw-RUNSPEC) section then the option is applied to all LGRs defined in the input file, whereas if used in the [GRID](#kw-GRID) or [EDIT](#kw-EDIT) sections the keyword must be placed inside a [LGR](#kw-LGR) definition section, that is between a [CARFIN](#kw-CARFIN) (Cartesian [LGR](#kw-LGR) grid) or [RADFIN](#kw-RADFIN)/[RADFIN4](#kw-RADFIN4) (radial [LGR](#kw-LGR) grid) keyword and an [ENDFIN](#kw-ENDFIN) keyword. In the latter case inheritance is applied on an individual [LGR](#kw-LGR) basis.

Currently, OPM Flow does not support the local grid refinement feature and therefore this keyword is ignored by the simulator.


#### Example

The following example activates the [LGR](#kw-LGR) Inheritance option for all LGRs in the model.


```
-- ==============================================================================
--
-- RUNSPEC SECTION
--
-- ==============================================================================
RUNSPEC
--
--       ACTIVATE LOCAL GRID REFINEMENT INHERITANCE
--
LGRCOPY
```