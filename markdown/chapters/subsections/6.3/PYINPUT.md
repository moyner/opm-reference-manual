### PYINPUT – Define the Start of a PYINPUT Section {#kw-PYINPUT}


| [RUNSPEC](#kw-RUNSPEC) | [GRID](#kw-GRID) | [EDIT](#kw-EDIT) | [PROPS](#kw-PROPS) | [REGIONS](#kw-REGIONS) | [SOLUTION](#kw-SOLUTION) | [SUMMARY](#kw-SUMMARY) | [SCHEDULE](#kw-SCHEDULE) |
| --- | --- | --- | --- | --- | --- | --- | --- |


#### Description

The PYINPUT and [PYEND](#kw-PYEND) keywords are a part of OPM Flow’s Python scripting facility that processes standard Python commands that can be used to manipulate and define the simulators input parameters during processing of the input deck.  The main purpose of the facility is to script the construction of the various keywords used by the simulator.

PYINPUT declares the start of a PYINPUT Definition Section on a single separate line, which is then followed by various standard Python commands, with one command per line. A PYINPUT Definition Section is terminated by a [PYEND](#kw-PYEND) keyword on a separate single line.

There is no data required for this keyword and there is no terminating “/” for this keyword.

Although this keyword is read by OPM Flow and the script processing has been implemented, one should use caution when using this facility as it may result in OPM Flow aborting. This is because the PYINPUT facility allows the user to implement complex functionality and the implementation is new for the 2020-04 release. Users should therefore use caution when using this facility.


::: {.callout-note}
This is an OPM Flow specific keyword for the simulator’s scripting facility using the standard Python interpreter, as such it gives more flexibility than the commercial simulator’s data editing keywords ([ADD](#kw-ADD), [EQUALS](#kw-EQUALS), [MULTIPLY](#kw-MULTIPLY), etc.), although OPM Flow also supports these keywords as well. The PYINPUT facility should be considered experimental as details of the OPM Flow - Python interface might change for future releases. In particular, the current implementation is quite minimal; however, future releases are expected to add more entry points in the simulator’s deck class which can be used to manipulate the input deck as the data is loaded.  As a user you are encouraged to come with wishes in this regard. The PYINPUT facility is very powerful and allows for any piece of Python code to be included and run, including potentially malicious code. The important point is to scrutinize the Python code in between PYINPUT and [PYEND](#kw-PYEND) in a deck you receive from other parties.
:::


| No. | Name | Description | Default |
| --- | --- | :------ | --- |
| PYINPUT | PYINPUT declares the start of a PYINPUT Definition Section.  This is then followed by any number Python commands. | Not Applicable |  |
| 1-1 | PYTHON | A series of standard Python commands with one line per command. The active Parser objects are accessible as context.parser and the active Deck object is available as context.deck. |  |
| [PYEND](#kw-PYEND) | [PYEND](#kw-PYEND) declares the end of a PYINPUT Definition Section.  The Python code between PYINPUT and [PYEND](#kw-PYEND) is read and executed, and the simulator thenreturns to reading the normal simulation input deck. |  |  |
| Notes: |  |  |  |
: PYINPUT Keyword Description {#tbl-6-113}
The PYINPUT/[PYEND](#kw-PYEND) set of keywords is a result of combining two programming languages, the interactive Python interpreter and OPM Flow’s source code language C++. When combining two languages one extends and embeds one into the other. When extending Python with C++ the functionality implemented in C++ is made available to Python applications, when embedding Python in C++ one can call Python functions from within C++. The PYINPUT/[PYEND](#kw-PYEND) set of keywords is based on embedding a Python interpreter in the C++ OPM Flow simulator, but the Python code actually runs as part of the PYINPUT keyword is based on wrapping C++ objects in Python, that is extending Python.

The Python code in between the PYINPUT and [PYEND](#kw-PYEND) keywords are imported during processing of the input deck and as such this implies that basic Python syntax checking is performed during reading the Python script.

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


The active Parser objects is accessible as context.parser and the active Deck object is available as context.deck.