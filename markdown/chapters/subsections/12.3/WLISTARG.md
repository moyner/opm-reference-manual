### WLISTARG – Modify Well List Target and Constraint Values (Static)


| [RUNSPEC](#3.RUNSPEC SECTION\|outline) | [GRID](#4.GRID SECTION\|outline) | [EDIT](#5.EDIT SECTION\|outline) | [PROPS](#6.PROPS SECTION\|outline) | [REGIONS](#7.REGIONS SECTION\|outline) | [SOLUTION](#8.SOLUTION SECTION\|outline) | [SUMMARY](#9.SUMMARY SECTION\|outline) | [SCHEDULE](#10.SCHEDULE SECTION\|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [WLISTARG](#__RefHeading___Toc585895_4263943340) keyword modifies the target and constraint values of both rates and pressures for wells previously defined in a well list by the [WLIST](#__RefHeading___Toc179534_3325167686) or [WLISTNAM](#__RefHeading___Toc592907_4263943340) keywords. [WLISTARG](#__RefHeading___Toc585895_4263943340) is similar to the [WELTARG](#__RefHeading___Toc134888_2055188184) keyword in it that allows for modifying targets and constraints without having to define all the variables on the well control keywords: [WCONPROD](#__RefHeading___Toc146754_4203985108), [WCONHIST](#__RefHeading___Toc134880_2055188184), [WCONINJE](#__RefHeading___Toc146750_4203985108), or [WCONINJH](#__RefHeading___Toc146752_4203985108) keywords. Variables not changed by the [WLISTARG](#__RefHeading___Toc585895_4263943340) keyword remain the same as those previously entered via the well control keywords or previously entered [WLISTARG](#__RefHeading___Toc585895_4263943340) keywords. Note that the well must still be initially be fully defined using the [WCONPROD](#__RefHeading___Toc146754_4203985108) or [WCONINJE](#__RefHeading___Toc146750_4203985108) keywords.  All the aforementioned keywords are described in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [WLIST](#__RefHeading___Toc179534_3325167686) | A character string of up to eight characters in length, enclosed in quotes, that defines the well list name declared by the [WLIST](#__RefHeading___Toc179534_3325167686) keyword. Note the first character must be asterisk (“*”) and the second character must be a letter, for example, *PROD. | None |
| 2 | TARGET | A defined character string that sets the item to be changed for the well the value of the item is set by item (3). | None |
| 3 | VALUE Liquid Gas Res Vol Pressure VFP LIFT | A real positive vector of values that defines the value of the variable declared by TARGET for all the wells contained in [WLIST](#__RefHeading___Toc179534_3325167686). For example if there are four wells in [WLIST](#__RefHeading___Toc179534_3325167686) then there must four real numbers for VALUE. The vector should be terminated by a “/” as indicated in the notes below. | None |
| stb/d Mscf/d rb/d psia dimensionless same as [VFPPROD](#__RefHeading___Toc121919_2556401936) or [VFPINJ](#__RefHeading___Toc121917_2556401936) | sm3/day sm3/day rm3/day barsa dimensionless same as [VFPPROD](#__RefHeading___Toc121919_2556401936) or [VFPINJ](#__RefHeading___Toc121917_2556401936) | scc/hour scc/hour rcc/hour atma dimensionless same as [VFPPROD](#__RefHeading___Toc121919_2556401936) or [VFPINJ](#__RefHeading___Toc121917_2556401936) |  |
| Notes: |  |  |  |

*Table 12.105: WLISTARG Keyword Description*


If a well is currently a history matching well, then WLISELTARG should only be used to change a wells bottom-hole pressure limit, vertical flow performance table number or the artificial lift quantity.


See also the [WELCNTL](#__RefHeading___Toc134886_2055188184) keyword, in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section that can be used to reset the control mode, as well as a well’s target and constraints of both rates and pressures.


#### Example

The following example defines two named well lists using the [WLIST](#__RefHeading___Toc179534_3325167686) keyword.


```
--
--       WELL LIST SPECIFICATION
--
-- LIST  OPER     WELL NAME LIST
-- NAME
WLIST
'*BLK-1' NEW      WEL-01M WEL-02M WEL-03M                                   /
'*BLK-2' NEW      WEL-03U WEL-05U WEL-06U WEL-10U                           /
/
--
--       WELL PRODUCTION AND INJECTION TARGETS
--
--  WELL WELL   TARGET
--  NAME TARG   VALUE
WLISTARG
‘*BLK-1’ ORAT   2000.0  2000.00  2000.0                     /
‘*BLK-2’ ORAT   3000.0  3500.00  4000.0  2000.0             /
/
```


The wells in the '*BLK-1' well list are all given an oil rate of 2,000 stb/d and wells in the  '*BLK-2' well list are given rates of 3,000, 3,500, 4,000 and 2,000 stb/d.
