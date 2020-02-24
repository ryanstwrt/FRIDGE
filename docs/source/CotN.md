# Chart of the Nuclides

To create materials in FRIDGe, the corresponding elements must be present in the directory `fridge/data/CotN`.
Each element needs is own YAML file and contains seven variables for inputting data; where each variable and its associate input can be seen in Table 1.

Table 1. Variables for Element YAML file.

|Variable Name  | Variable Type | Unit | Example|
|---------------|---------------|------|--------|
|Name  | str | -- | Silicon|
|Elemental ZAIDs | int | -- | 14000|
|Isotopic ZAID | list of ints | --| [14028, 14029, 14030]|
|Abundance | list of floats | wt % | [0.92223, 0.04685, 0.0392]|
|Mass | list of floats |  amu | [27.976926, 28.976494, 29.973777]|
|Density | float | g/cc | 2.33|
|Linear Coefficient of Expansion | float | K<sup>-1</sup> | 2.432e<sup>-6</sup>|

`Name` is a string containing the name of the element.
`Elemental ZAIDs` is an integer denoted by 1000 * Z (proton or atomic number).
`Isotopic ZAID` is a list of ZAID's where each isotope in the element is denoted by 1000 * Z + N.
Where N is the mass number (protons + neutrons) of the isotope, and Z is the atomic number.
`Abundance` is a list of the natural abundances for the isotopes (this is in atom percent and can be found in any Chart of the Nuclide).
**Note:** for elements with no natural abundances an entry of zero is allowed.
The weight percent can be set later in the material card.
`Mass` is a list of nuclide masses for each isotope listed and is given in amu's.
All abundances and masses were obtained using IAEA's Live Chart of Nuclides [1].
`Density` is the density of the natural isotope in g/cc.
`Linear Coefficient of Expansion` is the coefficient of thermal expansion in K<sup>-1</sup>.

[1] "Livechart - Table of Nuclides - Nuclear structure and decay data", www-nds.iaea.org, 2019. Available:
https://www-nds.iaea.org/relnsd/vcharthtml/VChartHTML.html.