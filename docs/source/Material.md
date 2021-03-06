# Materials

Materials can be found in the directory `fridge/data/materials`.
Each material in a problem requires its own YAML file and contains five mandatory variables and three optional variables.
Where each variable and its associate input can be seen in Table 1.

Table 1. Variables for Material YAML file.

|Variable Name   | Variable Type | Unit | Example|
|----------------|---------------|------|--------|
|Name  | string | -- | UO2|
|Elements | list of strs | -- | [U, O]|
|ZAIDs | list of ints | -- | [92000, 8000]|
|Weight Fractions | list of floats | wt % | [0.881467, 0.118533]|
|Enrichment ZAIDs<sup>*</sup> | list of ints | -- | [92000, 8000]|
|Enrichment Isotopes<sup>*</sup> | list of list of ints | -- | [[92234, 92235, 92238], [8016, 8017, 8018]]|
|Enrichment Vector<sup>*</sup> | list of list of floats | wt % | [[0.0, 0.03, 0.97], [1.0, 0.0, 0.0]]|
|Density | float | g/cc | 2.33|
|Linear Coefficient of Expansion | float | K<sup>-1</sup> |0.0|

<sup>*</sup> Optional variables if material has specific isotopics.

`Name` is a string containing the name of the element.
`Elements` is a list of element symbols to be used in the material.
**Note:** This element symbol is how FRIDGe finds the element in `fridge/data/CotN`, so ensure that the elements exists there and the symbol matches.
`Elemental ZAIDs` is list of integers, where each ZAID is denoted by 1000 * Z.
`Elemental Weight Fractions` is a list of floats whose entries are the weight fractions associated with the `ZAIDs` above.
**Note:** This value should sum to 1.0.
`Elemental Adjustment ZAIDs` is a list of ZAIDs whose isotopic fraction is different from the base element.
**Note:** If the isotopic composition is the same as the element in question, the element does not need to be included and it will be created as normal.
`Isotopic Adjustment ZAIDs` is a list of lists of isotopic ZAIDs, where each list corresponds to the the  `Elemental Adjustment ZAIDs` from above.
`Isotopic Weight Percents` is a list of lists of weight fractions (enrichment) of each isotope from `Enrichment Vector`.
**Note:** Each list should sum 1.0.
**Note:** If the element `Abundance` has a value, other than 0.0, for the weight percent, it must be included in the `Isotopics Adjustment ZAIDs` and the `Isotopic Weight Percents`.
For example, in Table 2, Uranium includes 92234 and sets the `Isotopic Weight Percent` to 0.0.
This will overwrite the elemental `Abundance` value of 0.000054 with 0.0, otherwise the total weight percent for uranium would be 1.000054.
The `Isotopic ZAIDs` of 92233 and 92236 for Uranium are not included because their weight percents are 0.0 in the elements `Abundance`.
`Density` is the density of the natural isotope in g/cc.
`Linear Coefficient of Expansion` is the coefficient of thermal expansion in K<sup>-1</sup>.