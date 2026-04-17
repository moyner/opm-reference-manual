### COMPDAT – Define Well Connections to the Grid


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The COMPDAT keyword defines how a well is connected to the reservoir by defining or modifying existing well connections. Ideally the connections should be declared in the correct sequence, starting with the connection nearest the well head and then working along the wellbore towards the bottom or toe of the well, however this may not be possible or convenient, for example when connections are added or removed from a well during the simulation (see COMPORD in the SCHEDULE section for options regarding connection ordering).


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well connection data are being defined. Note that the well name (WELNAME) must have been declared previously using the WELSPECS keyword in the SCHEDULE section, otherwise an error may occur. | None |
| 2 | I | A positive integer greater than or equal to zero and less than or equal to NX that defines the connection location in the I-direction. If set to zero or defaulted with 1* the location is taken from the wellhead location I-direction value on the WELSPECS keyword in the SCHEDULE section. | 0 |
| 3 | J | A positive integer greater than or equal to zero and less than or equal to NY that defines the connection location in the J-direction. If set to zero or defaulted with 1* the location is taken from the wellhead location J-direction value on the WELSPECS keyword in the SCHEDULE section. | 0 |
| 4 | K1 | A positive integer greater than or equal to one and less than or equal to NZ that defines the UPPER connection location in the K-direction. | None |
| 5 | K2 | A positive integer greater than or equal to K1 and less than or equal to NZ that defines the LOWER connection location in the K-direction. | None |
| 6 | STATUS | A defined character string of length four that defines the connections’ operational status, STATUS should be set to one of the following character strings: | OPEN |
| 7 | SATNUM | An integer greater than or equal to zero and less than NTSFUN as declared on the TABDIMS keyword in the RUNSPEC section, that defines the saturation table number to be used for flow between the reservoir grid block and the well connections. If SATNUM is set to zero or defaulted with 1* then: | 0 |
| 8 | CONFACT | A real value greater than or equal to zero that defines the transmissibility connection factor between the well bore and the reservoir grid block. If set to zero or defaulted with 1* then items (9) through (13) are used to calculate CONFACT. | Defined |
| cP.rb/day/psia 0 | cP.rm3/day/bars 0 | cP.rcc/hr/atm 0 |  |
| 9 | DW | A real positive value that defines the well bore diameter of the connections for the well. DW is used in calculating a well’s productivity or injectivity index; however the value will be ignored in calculating the connections CONFACT value if CONFACT has been directly entered. | None |
| feet | m | cm |  |
| 10 | KH | A real value that defines the effective KH (permeability x length) for the connections. If less than or equal to zero, or defaulted by 1*, then KH is calculated from the connected grid blocks. KH is ignored if CONFAC has been directly entered. | Calculated from connected grid blocks |
| mD.ft | mD.m | mD.cm |  |
| 11 | SKIN | A real value that defines the connections dimensionless skin factor. SKIN is used in calculating a well’s productivity or injectivity index; however, the value will be ignored in calculating the connections CONFACT value if CONFAC has been directly entered. | 0.0 |
| dimensionless | dimensionless | dimensionless |  |
| 12 | DFACT | A real value that defines the non-Darcy D factor coefficient for gas wells. It is recommended that the value should be defaulted with 1* and the non-Darcy D factor coefficient for gas wells defined via the WDFAC keyword in the SCHEDULE section. If the value is greater than or equal to zero then the value is used to define the well D factor and the simulator evaluates the connection D factors internally. If the value is less than zero then its sign is reversed and then used directly to define the connection D factors. In this case any D factor values previously defined using the WDFAC keyword for other connections will retained, whereas, any connection D factors previously defined for the entire well using the WDFACCOR keyword will be discarded. | 0.0 |
| day/Mscf | day/m3 | hour/sc |  |
| 13 | DIRECT | A defined character string of length one that defines the orientation of the connections and should be set to either X, Y, or Z. The direction of connections also determines the length of the connection used to calculate the connection factor if CONFACT has not been entered directly. The default value is for a vertical connection, that is DIRECT is defaulted to Z. | Z |
| Notes: |  |  |  |

*Table 12.3.23.1: COMPDAT Keyword Description*


Multiple grid block connections can be defined on one record for vertical wells by assigning different values to K1 and K2, for deviated and horizontal wells this may not be possible and therefore each grid block connection must be separately defined by using one record per connection, setting K1 equal to K2 in each record.

See also the WELSPECS keyword to define wells, the COMPIMB to reset the imbibition relative permeability table allocation, and the COMPORD to re-order the completions along the well trajectory. In addition, the COMPLUMP keyword groups well connections together to form well completions for a well. All the aforementioned keywords are described in the SCHEDULE section.


::: {.callout-note}
The term well connection is used to describe individual connections from the wellbore to the reservoir grid, as opposed to well completions. A well completion is used to describe a set of connections, for example, a well may consist of several completions with each completion consisting of multiple connections.
:::


#### Example

The following example defines two vertical oil wells using the WELSPECS keyword and their associated connection data.


```
--
--       WELL SPECIFICATION DATA
--
-- WELL  GROUP     LOCATION  BHP    PHASE  DRAIN  INFLOW  OPEN  CROSS  PRESS
-- NAME  NAME        I    J  DEPTH  FLUID  AREA   EQUANS  SHUT  FLOW   TABLE       WELSPECS
OP01     PLATFORM   14   13   1*     OIL    1*     STD    SHUT   NO     1*  /
OP02     PLATFORM   35   96   1*     OIL    1*     STD    SHUT   NO     1*  /
/
--
--       WELL CONNECTION DATA
--
-- WELL  --- LOCATION ---  OPEN   SAT   CONN   WELL   KH    SKIN   D     DIR
-- NAME   II  JJ  K1  K2   SHUT   TAB   FACT   DIA    FACT  FACT   FACT  PEN
COMPDAT
OP01      1*  1*  20  56   OPEN   1*    1*    0.708   1*    0.0    1*    'Z' /
OP01      1*  1*  75 100   SHUT   1*    1*    0.708   1*    0.0    1*    'Z' /
OP02      35  96  75 100   OPEN   1*    1*    0.708   1*    0.0    1*    'Z' /

```

Well OP01 has two sets of connections; the first one connects grid cells (14, 13, 20) to (14, 13, 56) to the well and is open to flow and the second connecting grid cells (14, 13, 75) to (14, 13, 100) is shut. Well OP02 has only one open set of connections from cells (35, 96, 75) to cells (35, 96, 100).
