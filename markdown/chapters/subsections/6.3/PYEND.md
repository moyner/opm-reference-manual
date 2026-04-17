### PYEND – End the Definition of a PYINPUT Section {#kw-PYEND}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The [PYINPUT](#kw-PYINPUT) and PYEND keywords are a part of OPM Flow’s Python scripting facility that processes standard Python commands that can be used to manipulate and define the simulators input parameters during processing of the input deck.  The main purpose of the facility is to script the construction of the various keywords.

[PYINPUT](#kw-PYINPUT) declares the start of a [PYINPUT](#kw-PYINPUT) Definition Section on a single separate line, which is then followed by various standard Python commands, with one command per line.  A [PYINPUT](#kw-PYINPUT) Definition Section is terminated by a PYEND keyword  (this keyword) on a separate single line.

There is no data required for this keyword and there is no terminating “/” for this keyword.

Although this keyword is read by OPM Flow and the script processing has been implemented, one should use caution when using this facility as it may result in OPM Flow aborting. This is because the [PYINPUT](#kw-PYINPUT) facility allows the user to implement complex functionality and the implementation is new for the 2020-04 release. Users should therefore use caution when using this facility.


::: {.callout-note}
This is an OPM Flow specific keyword for the simulator’s scripting facility using the standard Python interpreter, as such it gives more flexibility than the commercial simulator’s data editing keywords ([ADD](#kw-ADD), EQUAL, [MULTIPLY](#kw-MULTIPLY), etc.), although OPM Flow also supports these keywords as well. The [PYINPUT](#kw-PYINPUT) facility should be considered experimental as details of the OPM Flow - Python interface might change for future releases. In particular, the current implementation is quite minimal; however, future releases are expected to add more entry points in the simulator’s deck class which can be used to manipulate the input deck as the data is loaded.  As a user you are encouraged to come with wishes in this regard. The [PYINPUT](#kw-PYINPUT) facility is very powerful and allows for any piece of Python code to be included and run, including potentially malicious code. The important point is to scrutinize the Python code in between [PYINPUT](#kw-PYINPUT) and PYEND in a deck you receive from other parties.
:::


See also the [PYACTION](#kw-PYACTION) keyword in the [SCHEDULE](#kw-SCHEDULE) section which is also part of OPM Flow’s Python scripting facility, that loads a standard Python script file that can be used to define a series of conditions and actions as the simulation proceeds through time.


#### Example

The example shows how to construct the [DX](#kw-DX) variable in the [GRID](#kw-GRID) section and to add the resulting [DX](#kw-DX) array as part of the input deck.


```
--
--       START OF PYINPUT SECTION
--
PYINPUT
#
# Import Numpy Model
#
import numpy as np
#
# Define DX and Get the Input Decks Unit Systems
#
dx = np.array([100.0, 100.0, 100.0, 100.0])
active_unit_system  = context.deck.active_unit_system()
default_unit_system = context.deck.default_unit_system()
#
# Set DX in the Input Deck
#
kw = context.DeckKeyword( context.parser['DX'], dx, active_unit_system,
default_unit_system )
context.deck.add(kw)

PYEND

```

The active Parser objects are accessible as context.parser and the active Deck object is available as context.deck.