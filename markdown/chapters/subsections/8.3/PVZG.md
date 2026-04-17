### PVZG – Gas PVT Properties for Dry Gas (Z-Factor)


| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

PVZG defines the gas PVT properties for dry gas [Natural gas that occurs in the absence of condensate or liquid hydrocarbons, or gas that had condensable hydrocarbons removed, is called dry gas. It is primarily methane with some intermediates. The hydrocarbon mixture is solely gas in the reservoir and there is no liquid (condensate surface liquid) formed either in the reservoir or at surface. The term dry indicates that the gas does not contain heavier hydrocarbons to form liquids at the surface conditions. Dry gas typically has GOR's greater than 100,000 scf/stb or 18,000 Sm3/m3.] via the gas compressibility factor (z-factor), instead of the gas formation volume factor. If the gas has a constant and uniform vaporized oil concentration, Condensate-Gas Ratio (“CGR”), and if the reservoir pressure never drops below the saturation pressure (dew point pressure), then the model can be run more efficiently by omitting the OIL and VAPOIL keywords from the RUNSPEC section, treating the gas as a dry gas, and defining a constant Rv (CGR) value with keyword RVCONST or RVCONSTT in the PROPS section. This results in the model being run with as a dry gas problem with no active oil (condensate) phase. However, OPM Flow takes into account the constant Rv in the calculations and reporting.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.


| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1-1 | RTEMP | Single real positive value that defines the reservoir temperature for the data in the following records. |  |
| oF | oC | oC |  |
| 1-2 | / | Record terminated by a “/” | Not Applicable |
| 2-1 | PRESS | A columnar vector of real monotonically increasing down the column   values that defines the gas phase pressure. | None |
| psia | barsa | atma |  |
| 2-2 | GZFAC | A columnar vector of real values that defines the corresponding gas phase z-factor at the given pressure, PRESS. | None |
| 2-1 |  |  |  |
| dimensionless | dimensionless | dimensionless |  |
| 2-3 | GVISC | A columnar vector of real increasing down the column values that defines the corresponding gas phase viscosity. | None |
| cP | cP | cP |  |
| Notes: |  |  |  |

*Table 8.124: PVZG Keyword Description*

See also the RVCONST and RVCONSTT keywords to define the constant Rv for dry gas.

The ideal gas law provides a relationship between the pressure, the temperature and the specific volume of an ideal gas (pure component). This relationship is modified by use of a compressibility factor, Z [Standing, M. B.:” Volumetric and Phase Behaviour of Oil Field Hydrocarbon Systems”, Renihold Publishing Corp., New York City (1952).], to account for deviations, from ideal, to the behavior of real gases.  The PVT relation for a real gas can be defined by:


| $$ \mathit{PV} = \mathit{ZnRT} $$ | (8.84) |
| --- | --- |

As the gas formation volume factor is used to relate the volume of gas, as measured at reservoir conditions, to the volume of gas as measured at standard conditions (60 oF and 14.7 psia, or 15 oC and 101.325 kPa). This gas property is then defined as the actual volume occupied by a certain amount of gas at a specified pressure and temperature, divided by the same amount of gas at standard conditions.  Thus, using the above equation one can obtain the gas volumes at reservoir and standard conditions, i.e.


| $$ {V}_{\mathit{sc}} = \frac{{Z}_{\mathit{sc}}{\mathit{nRT}}_{\mathit{sc}}}{{P}_{\mathit{sc}}} $$ | (8.85) |
| --- | --- |


| $$ {V}_{i} = \frac{{Z}_{i}n{\mathit{RT}}_{i}}{{P}_{i}} $$ | (8.86) |
| --- | --- |

Thus the gas formation volume factor can be expressed as:


| $$ E = \frac{{V}_{\mathit{sc}}}{{V}_{i}} $$ | (8.87) |
| --- | --- |

And substituting equation (8.85) and (8.86) into (8.87) we obtain


| $$ E = \left(\frac{{P}_{i}}{{P}_{\mathit{sc}}}\right) \left(\frac{{T}_{\mathit{sc}}}{{T}_{i}}\right) \left(\frac{1}{{Z}_{i}}\right) $$ | (8.88) |
| --- | --- |

Incorporating standard pressure and temperature values gives in SI units:


| $$ E = \left(\frac{{P}_{i}}{101.325}\right) \left(\frac{273.15 + 15}{{T}_{i}}\right) \left(\frac{1}{{Z}_{i}}\right) = 2.84 \left(\frac{{P}_{i}}{{Z}_{i}{T}_{i}}\right) $$ | (8.89) |
| --- | --- |

or in field units:


| $$ E = \left(\frac{{P}_{i}}{14.7}\right) \left(\frac{460 + 60}{{T}_{i}}\right) \left(\frac{1}{{Z}_{i}}\right) = 35.37 \left(\frac{{P}_{i}}{{Z}_{i}{T}_{i}}\right) $$ | (8.90) |
| --- | --- |


Where,

$$
E
$$

$$
P
$$

$$
\mathit{Psc}
$$

$$
\mathit{Pi}
$$

$$
V
$$

$$
T
$$

$$
\mathit{Tsc}
$$

$$
\mathit{Ti}
$$

$$
R
$$


$$
\mathit{Ti}
$$

$$
{P}_{i}
$$


#### Example


```
---
--       GAS PVT TABLE USING GAS Z-FACTOR
--
PVZG
--       RESERVOIR TEMPERATURE FOR Z TO BG CONVERSION
--
         180.0                                             /
--
--        PRES       ZG          VISC
--        PSIA     DIMLESS      CPOISE
--       ------    ---------    -------
           14.7    0.998970     0.0130
          250.0    0.976260     0.0131
          500.0    0.954790     0.0134
          750.0    0.932050     0.0137
         1000.0    0.912990     0.0142
         1250.0    0.896320     0.0147
         1500.0    0.881610     0.0152
         1750.0    0.870830     0.0159
         2000.0    0.863130     0.0166
         2250.0    0.858920     0.0173
         2500.0    0.857800     0.0181
         2750.0    0.860430     0.0189
         3000.0    0.866440     0.0197
         3250.0    0.874980     0.0206
         3500.0    0.885470     0.0214
         3750.0    0.898350     0.0223
         4000.0    1.025120     0.0277                     / TABLE NO 01              --
--       GAS PVT TABLE USING GAS Z-FACTOR
--
PVZG
--       RESERVOIR TEMPERATURE FOR Z TO BG CONVERSION
--
         180.0                                             /
--
--        PRES       ZG          VISC
--        PSIA     DIMLESS      CPOISE
--       ------    ---------    -------
           14.7    0.998970     0.0130
          250.0    0.976260     0.0131
          500.0    0.954790     0.0134
          750.0    0.932050     0.0137
         1000.0    0.912990     0.0142
         1250.0    0.896320     0.0147
         1500.0    0.881610     0.0152
         1750.0    0.870830     0.0159
         2000.0    0.863130     0.0166
         2250.0    0.858920     0.0173
         2500.0    0.857800     0.0181
         2750.0    0.860430     0.0189
         3000.0    0.866440     0.0197
         3250.0    0.874980     0.0206
         3500.0    0.885470     0.0214
         3750.0    0.898350     0.0223
         4000.0    1.025120     0.0277                     / TABLE NO 01
```


The above example defines two dry PVZG tables assuming NTPVT equals two and NPPVT is greater than or equal to 17 on the TABDIMS keyword in the RUNSPEC section. There is no terminating “/” for this keyword.
