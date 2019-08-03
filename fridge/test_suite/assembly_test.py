import fridge.Assembly.FuelAssembly as FuelAssembly
import fridge.Assembly.SmearAssembly as SmearAssembly
import fridge.Assembly.Assembly as Assembly
import fridge.driver.global_variables as gb
import numpy as np

global_vars = gb.GlobalVariables()
global_vars.read_input_file('A271_Assembly_Test')
assembly_info = [global_vars.file_name, '01A01', global_vars, None]

def test_assembly():
    """Check the base assembly init"""
    baseAssembly = Assembly.Assembly(assembly_info)
    assert baseAssembly.assembly_file_name == 'A271_Test'
    assert baseAssembly.assemblyPosition == '01A01'
    assert baseAssembly.universe == 100
    assert baseAssembly.cellNum == 100
    assert baseAssembly.surfaceNum == 100
    assert baseAssembly.materialNum == 100
    assert baseAssembly.assemblyType == ''
    assert baseAssembly.pinsPerAssembly == 0
    assert baseAssembly.assemblyPitch == 0
    assert baseAssembly.ductInnerFlatToFlat == 0
    assert baseAssembly.ductOuterFlatToFlat == 0
    assert baseAssembly.ductOuterFlatToFlat == 0
    assert baseAssembly.assemblyHeight == 0
    assert baseAssembly.coolantMaterial == ''
    assert baseAssembly.assemblyMaterial == ''


def test_updateIdentifiers():
    """Check the updateIdentifiers function"""
    baseAssembly = Assembly.Assembly(assembly_info)
    assert baseAssembly.universe == 100
    assert baseAssembly.cellNum == 100
    assert baseAssembly.surfaceNum == 100
    assert baseAssembly.materialNum == 100
    baseAssembly.update_global_identifiers(False)
    assert baseAssembly.universe == 100
    assert baseAssembly.cellNum == 101
    assert baseAssembly.surfaceNum == 101
    assert baseAssembly.materialNum == 101


def test_fuel_assembly():
    """Check the Fuel Assembly subclass of Assembly."""
    a = FuelAssembly.FuelAssembly(assembly_info)
    assert a.universe == 104
    assert a.cellNum == 114
    assert a.surfaceNum == 114
    assert a.materialNum == 114
    assert a.fuel is not None
    assert a.fuel is not None
    assert a.bond is not None
    assert a.clad is not None
    assert a.coolant is not None
    assert a.blankUniverse is not None
    assert a.blankCoolant is not None
    assert a.latticeUniverse is not None
    assert a.fuelUniverse is not None
    assert a.innerDuct is not None 
    assert a.duct is not None
    assert a.plenum is not None
    assert a.upperReflector is not None
    assert a.lowerReflector is not None
    assert a.upperSodium is not None
    assert a.lowerSodium is not None
    assert a.assemblyShell is not None
    assert a.everythingElse is not None

    assert a.cladOD == 0.53
    assert a.cladID == 0.53 - 0.037 * 2 
    assert np.allclose(a.fuelDiameter, 0.394907)
    assert a.fuelPitch == 0.66144
    assert a.wireWrapDiameter == 0.126
    assert a.fuelHeight == 60
    assert a.fuelMaterial == '5Pu22U10Zr'
    assert a.cladMaterial == 'HT9'
    assert a.bondMaterial == 'LiquidNa'

    assert a.plenumHeight == 60
    assert a.plenumMaterial == {'HT9': 0.25, 'Void': 0.25, 'LiquidNa': 0.5}
    assert a.plenumPosition == [0, 0, 60.6]

    assert a.reflectorHeight == 60
    assert a.reflectorMaterial == {'LiquidNa': 0.20, 'HT9': 0.80}

    assert a.fuel.cellCard == '100 100 0.04574 -100 u=101 imp:n=1 $Pin: Fuel'
    assert a.fuel.surfaceCard == '100 RCC 0.0 0.0 0.0 0 0 60.0 0.19745 $Pin: Fuel'
    assert a.bond.cellCard == '101 101 0.02428 100 -101 u=101 imp:n=1 $Pin: Bond'
    assert a.bond.surfaceCard == '101 RCC 0.0 0.0 0.0 0 0 60.6 0.228 $Pin: Bond - 1% higher than fuel'
    assert a.clad.cellCard == '102 102 0.08598 101 -102 u=101 imp:n=1 $Pin: Clad'
    assert a.clad.surfaceCard == '102 RCC 0.0 0.0 0.0 0 0 60.6 0.265 $Pin: Clad - 1% higher than fuel'
    assert a.coolant.cellCard == '103 103 0.02929 102 u=101 imp:n=1 $Pin: Wirewrap + Coolant'
    assert a.coolant.surfaceCard == '103 RHP 0.0 0.0 0.0 0 0 60.6 0.66144 0 0 $Pin: Coolant - 1% higher than fuel'
    assert a.blankCoolant.cellCard == '104 104 0.02428 -103 u=102 imp:n=1 $Pin: Blank Pin Coolant'
    assert a.blankCoolant.surfaceCard == '104 RHP 0.0 0.0 0.0 0 0 60.6 0.33072 0 0 $Pin: Blank Pin - 1%\
 higher than fuel'
    assert a.fuelUniverse.cellCard == '105 0 -104 lat=2 u=103 imp:n=1\n'\
                                      '     fill=-10:10 -10:10 0:0\n'\
                                      '      102 102 102 102 102 102 102 102 102 102\n'\
                                      '      102 102 102 102 102 102 102 102 102 102\n'\
                                      '      102 102 102 102 102 102 102 102 102 102\n'\
                                      '      102 101 101 101 101 101 101 101 101 101\n'\
                                      '      101 102 102 102 102 102 102 102 102 102\n'\
                                      '      102 101 101 101 101 101 101 101 101 101\n'\
                                      '      101 101 102 102 102 102 102 102 102 102\n'\
                                      '      102 101 101 101 101 101 101 101 101 101\n'\
                                      '      101 101 101 102 102 102 102 102 102 102\n'\
                                      '      102 101 101 101 101 101 101 101 101 101\n'\
                                      '      101 101 101 101 102 102 102 102 102 102\n'\
                                      '      102 101 101 101 101 101 101 101 101 101\n'\
                                      '      101 101 101 101 101 102 102 102 102 102\n'\
                                      '      102 101 101 101 101 101 101 101 101 101\n'\
                                      '      101 101 101 101 101 101 102 102 102 102\n'\
                                      '      102 101 101 101 101 101 101 101 101 101\n'\
                                      '      101 101 101 101 101 101 101 102 102 102\n'\
                                      '      102 101 101 101 101 101 101 101 101 101\n'\
                                      '      101 101 101 101 101 101 101 101 102 102\n'\
                                      '      102 101 101 101 101 101 101 101 101 101\n'\
                                      '      101 101 101 101 101 101 101 101 101 102\n'\
                                      '      102 101 101 101 101 101 101 101 101 101\n'\
                                      '      101 101 101 101 101 101 101 101 101 101\n'\
                                      '      102 102 101 101 101 101 101 101 101 101\n'\
                                      '      101 101 101 101 101 101 101 101 101 101\n'\
                                      '      102 102 102 101 101 101 101 101 101 101\n'\
                                      '      101 101 101 101 101 101 101 101 101 101\n'\
                                      '      102 102 102 102 101 101 101 101 101 101\n'\
                                      '      101 101 101 101 101 101 101 101 101 101\n'\
                                      '      102 102 102 102 102 101 101 101 101 101\n'\
                                      '      101 101 101 101 101 101 101 101 101 101\n'\
                                      '      102 102 102 102 102 102 101 101 101 101\n'\
                                      '      101 101 101 101 101 101 101 101 101 101\n'\
                                      '      102 102 102 102 102 102 102 101 101 101\n'\
                                      '      101 101 101 101 101 101 101 101 101 101\n'\
                                      '      102 102 102 102 102 102 102 102 101 101\n'\
                                      '      101 101 101 101 101 101 101 101 101 101\n'\
                                      '      102 102 102 102 102 102 102 102 102 101\n'\
                                      '      101 101 101 101 101 101 101 101 101 101\n'\
                                      '      102 102 102 102 102 102 102 102 102 102\n'\
                                      '      101 101 101 101 101 101 101 101 101 101\n'\
                                      '      102 102 102 102 102 102 102 102 102 102\n'\
                                      '      102 102 102 102 102 102 102 102 102 102\n'\
                                      '      102 102 102 102 102 102 102 102 102 102\n'\
                                      '      102'
    assert a.innerDuct.cellCard == '106 0 -106 u=100 fill=103 imp:n=1 $Assembly: Inner Portion of Assembly'
    assert a.innerDuct.surfaceCard == '106 RHP 0.0 0.0 0.0 0 0 60.6 0 5.505 0 $Assembly: Duct Inner Surface'
    assert a.plenum.cellCard == '107 107 0.03364 -107 u=100 imp:n=1 $Assembly: Plenum'
    assert a.plenum.surfaceCard == '107 RHP 0.0 0.0 60.6 0 0 60.0 0 5.505 0 $Assembly: Plenum'
    assert a.upperReflector.cellCard == '108 108 0.07364 -108 u=100 imp:n=1 $Assembly: Upper Reflector'
    assert a.upperReflector.surfaceCard == '108 RHP 0.0 0.0 120.6 0 0 60.0 0 5.505 0 $Assembly: Upper Reflector'
    assert a.lowerReflector.cellCard == '109 109 0.07364 -109 u=100 imp:n=1 $Assembly: Lower Reflector'
    assert a.lowerReflector.surfaceCard == '109 RHP 0.0 0.0 -60.0 0 0 60.0 0 5.505 0 $Assembly: Lower Reflector'
    assert a.duct.cellCard == '110 110 0.08598  106 109 108 107 -110 u=100 imp:n=1 $Assembly: Assembly Duct'
    assert a.duct.surfaceCard == '110 RHP 0.0 0.0 -60.0 0 0 240.6 0 5.80529 0 $Assembly: Duct Outer Surface'
    assert a.lowerSodium.cellCard == '111 111 0.02428 -111 u=100 imp:n=1 $Assembly: Lower Coolant'
    assert a.lowerSodium.surfaceCard == '111 RHP 0.0 0.0 -99.8 0 0 39.8 0 5.80529 0 $Assembly: Lower Coolant'
    assert a.upperSodium.cellCard == '112 112 0.02428 -112 u=100 imp:n=1 $Assembly: Upper Coolant'
    assert a.upperSodium.surfaceCard == '112 RHP 0.0 0.0 180.6 0 0 39.7 0 5.80529 0 $Assembly: Upper Coolant'
    assert a.assemblyShell.cellCard == '113 0 -113 fill=100 imp:n=1 $Assembly'
    assert a.assemblyShell.surfaceCard == '113 RHP 0.0 0.0 -99.7 0 0 320.0 0 5.805 0 $Assembly: Full Assembly Surface'
    assert a.everythingElse.cellCard == '114 0 113 imp:n=0 $Everything Else'


global_vars = gb.GlobalVariables()
global_vars.read_input_file('Smear_Assembly_Test')
assembly_info2 = [global_vars.file_name, '01A01', global_vars, None]


def test_smearAssembly():
    a = SmearAssembly.SmearAssembly(assembly_info2)
    assert a.assemblyPitch == 12
    assert a.coolantMaterial == 'LiquidNa'
    assert a.assemblyMaterial == 'HT9'
    assert a.smearMaterial == {'LiquidNa': 0.3, 'HT9': 0.7}

    assert a.smearRegion.cellCard == "100 100 0.06747 -100 u=100 imp:n=1 $Assembly: Smear Region"
    assert a.smearRegion.surfaceCard == "100 RHP 0.0 0.0 -60.0 0 0 240 0 5.80529 0 $Assembly: Smear Region"
    assert a.lowerCoolant.cellCard == '101 101 0.02428 -101 u=100 imp:n=1 $Assembly: Lower Coolant'
    assert a.lowerCoolant.surfaceCard == '101 RHP 0.0 0.0 -100.1 0 0 40.1 0 5.80529 0 $Assembly: Lower Coolant'
    assert a.upperCoolant.cellCard == '102 102 0.02428 -102 u=100 imp:n=1 $Assembly: Upper Coolant'
    assert a.upperCoolant.surfaceCard == '102 RHP 0.0 0.0 180.0 0 0 40.0 0 5.80529 0 $Assembly: Upper Coolant'
    assert a.assemblyShell.cellCard == '103 0 -103 fill=100 imp:n=1 $Assembly'
    assert a.assemblyShell.surfaceCard == '103 RHP 0.0 0.0 -100.0 0 0 320.0 0 5.805 0 $Assembly: Full Assembly Surface'


def test_getAssemblyLocation():
    assembly_info1 = ['Nonsense', '01A01', global_vars, None]
    a = None
    try:
        a = Assembly.Assembly(assembly_info1)
    except IndexError:
        assert a is None


global_vars = gb.GlobalVariables()
global_vars.read_input_file('A271_Assembly_Shifted_Test')
assembly_info3 = [global_vars.file_name, '01A01', global_vars, None]


def test_shifted_fuel_assembly():
    """Check the Fuel Assembly subclass of Assembly with a shifted Z position."""
    a = FuelAssembly.FuelAssembly(assembly_info3)
    assert a.universe == 104
    assert a.cellNum == 114
    assert a.surfaceNum == 114
    assert a.materialNum == 114
    assert a.fuel is not None
    assert a.fuel is not None
    assert a.bond is not None
    assert a.clad is not None
    assert a.coolant is not None
    assert a.blankUniverse is not None
    assert a.blankCoolant is not None
    assert a.latticeUniverse is not None
    assert a.fuelUniverse is not None
    assert a.innerDuct is not None
    assert a.duct is not None
    assert a.plenum is not None
    assert a.upperReflector is not None
    assert a.lowerReflector is not None
    assert a.upperSodium is not None
    assert a.lowerSodium is not None
    assert a.assemblyShell is not None
    assert a.everythingElse is not None

    assert a.cladOD == 0.53
    assert a.cladID == 0.53 - 0.037 * 2
    assert np.allclose(a.fuelDiameter, 0.394907)
    assert a.fuelPitch == 0.66144
    assert a.wireWrapDiameter == 0.126
    assert a.fuelHeight == 60
    assert a.fuelMaterial == '5Pu22U10Zr'
    assert a.cladMaterial == 'HT9'
    assert a.bondMaterial == 'LiquidNa'
    assert a.zPosition == -10
    assert a.position == [0, 0, -10]

    assert a.plenumHeight == 60
    assert a.plenumMaterial == {'HT9': 0.25, 'Void': 0.25, 'LiquidNa': 0.5}
    assert a.plenumPosition == [0, 0, 50.6]

    assert a.reflectorHeight == 60
    assert a.reflectorMaterial == {'LiquidNa': 0.20, 'HT9': 0.80}

    assert a.fuel.cellCard == '100 100 0.04574 -100 u=101 imp:n=1 $Pin: Fuel'
    assert a.fuel.surfaceCard == '100 RCC 0.0 0.0 -10.0 0 0 60.0 0.19745 $Pin: Fuel'
    assert a.bond.cellCard == '101 101 0.02428 100 -101 u=101 imp:n=1 $Pin: Bond'
    assert a.bond.surfaceCard == '101 RCC 0.0 0.0 -10.0 0 0 60.6 0.228 $Pin: Bond - 1% higher than fuel'
    assert a.clad.cellCard == '102 102 0.08598 101 -102 u=101 imp:n=1 $Pin: Clad'
    assert a.clad.surfaceCard == '102 RCC 0.0 0.0 -10.0 0 0 60.6 0.265 $Pin: Clad - 1% higher than fuel'
    assert a.coolant.cellCard == '103 103 0.02929 102 u=101 imp:n=1 $Pin: Wirewrap + Coolant'
    assert a.coolant.surfaceCard == '103 RHP 0.0 0.0 -10.0 0 0 60.6 0.66144 0 0 $Pin: Coolant - 1% higher than fuel'
    assert a.blankCoolant.cellCard == '104 104 0.02428 -103 u=102 imp:n=1 $Pin: Blank Pin Coolant'
    assert a.blankCoolant.surfaceCard == '104 RHP 0.0 0.0 -10.0 0 0 60.6 0.33072 0 0 $Pin: Blank Pin - 1% \
higher than fuel'
    assert a.fuelUniverse.cellCard == '105 0 -104 lat=2 u=103 imp:n=1\n'\
                                      '     fill=-10:10 -10:10 0:0\n'\
                                      '      102 102 102 102 102 102 102 102 102 102\n'\
                                      '      102 102 102 102 102 102 102 102 102 102\n'\
                                      '      102 102 102 102 102 102 102 102 102 102\n'\
                                      '      102 101 101 101 101 101 101 101 101 101\n'\
                                      '      101 102 102 102 102 102 102 102 102 102\n'\
                                      '      102 101 101 101 101 101 101 101 101 101\n'\
                                      '      101 101 102 102 102 102 102 102 102 102\n'\
                                      '      102 101 101 101 101 101 101 101 101 101\n'\
                                      '      101 101 101 102 102 102 102 102 102 102\n'\
                                      '      102 101 101 101 101 101 101 101 101 101\n'\
                                      '      101 101 101 101 102 102 102 102 102 102\n'\
                                      '      102 101 101 101 101 101 101 101 101 101\n'\
                                      '      101 101 101 101 101 102 102 102 102 102\n'\
                                      '      102 101 101 101 101 101 101 101 101 101\n'\
                                      '      101 101 101 101 101 101 102 102 102 102\n'\
                                      '      102 101 101 101 101 101 101 101 101 101\n'\
                                      '      101 101 101 101 101 101 101 102 102 102\n'\
                                      '      102 101 101 101 101 101 101 101 101 101\n'\
                                      '      101 101 101 101 101 101 101 101 102 102\n'\
                                      '      102 101 101 101 101 101 101 101 101 101\n'\
                                      '      101 101 101 101 101 101 101 101 101 102\n'\
                                      '      102 101 101 101 101 101 101 101 101 101\n'\
                                      '      101 101 101 101 101 101 101 101 101 101\n'\
                                      '      102 102 101 101 101 101 101 101 101 101\n'\
                                      '      101 101 101 101 101 101 101 101 101 101\n'\
                                      '      102 102 102 101 101 101 101 101 101 101\n'\
                                      '      101 101 101 101 101 101 101 101 101 101\n'\
                                      '      102 102 102 102 101 101 101 101 101 101\n'\
                                      '      101 101 101 101 101 101 101 101 101 101\n'\
                                      '      102 102 102 102 102 101 101 101 101 101\n'\
                                      '      101 101 101 101 101 101 101 101 101 101\n'\
                                      '      102 102 102 102 102 102 101 101 101 101\n'\
                                      '      101 101 101 101 101 101 101 101 101 101\n'\
                                      '      102 102 102 102 102 102 102 101 101 101\n'\
                                      '      101 101 101 101 101 101 101 101 101 101\n'\
                                      '      102 102 102 102 102 102 102 102 101 101\n'\
                                      '      101 101 101 101 101 101 101 101 101 101\n'\
                                      '      102 102 102 102 102 102 102 102 102 101\n'\
                                      '      101 101 101 101 101 101 101 101 101 101\n'\
                                      '      102 102 102 102 102 102 102 102 102 102\n'\
                                      '      101 101 101 101 101 101 101 101 101 101\n'\
                                      '      102 102 102 102 102 102 102 102 102 102\n'\
                                      '      102 102 102 102 102 102 102 102 102 102\n'\
                                      '      102 102 102 102 102 102 102 102 102 102\n'\
                                      '      102'
    assert a.innerDuct.cellCard == '106 0 -106 u=100 fill=103 imp:n=1 $Assembly: Inner Portion of Assembly'
    assert a.innerDuct.surfaceCard == '106 RHP 0.0 0.0 -10.0 0 0 60.6 0 5.505 0 $Assembly: Duct Inner Surface'
    assert a.plenum.cellCard == '107 107 0.03364 -107 u=100 imp:n=1 $Assembly: Plenum'
    assert a.plenum.surfaceCard == '107 RHP 0.0 0.0 50.6 0 0 60.0 0 5.505 0 $Assembly: Plenum'
    assert a.upperReflector.cellCard == '108 108 0.07364 -108 u=100 imp:n=1 $Assembly: Upper Reflector'
    assert a.upperReflector.surfaceCard == '108 RHP 0.0 0.0 110.6 0 0 60.0 0 5.505 0 $Assembly: Upper Reflector'
    assert a.lowerReflector.cellCard == '109 109 0.07364 -109 u=100 imp:n=1 $Assembly: Lower Reflector'
    assert a.lowerReflector.surfaceCard == '109 RHP 0.0 0.0 -70.0 0 0 60.0 0 5.505 0 $Assembly: Lower Reflector'
    assert a.duct.cellCard == '110 110 0.08598  106 109 108 107 -110 u=100 imp:n=1 $Assembly: Assembly Duct'
    assert a.duct.surfaceCard == '110 RHP 0.0 0.0 -70.0 0 0 240.6 0 5.80529 0 $Assembly: Duct Outer Surface'
    assert a.lowerSodium.cellCard == '111 111 0.02428 -111 u=100 imp:n=1 $Assembly: Lower Coolant'
    assert a.lowerSodium.surfaceCard == '111 RHP 0.0 0.0 -109.8 0 0 39.8 0 5.80529 0 $Assembly: Lower Coolant'
    assert a.upperSodium.cellCard == '112 112 0.02428 -112 u=100 imp:n=1 $Assembly: Upper Coolant'
    assert a.upperSodium.surfaceCard == '112 RHP 0.0 0.0 170.6 0 0 39.7 0 5.80529 0 $Assembly: Upper Coolant'
    assert a.assemblyShell.cellCard == '113 0 -113 fill=100 imp:n=1 $Assembly'
    assert a.assemblyShell.surfaceCard == '113 RHP 0.0 0.0 -109.7 0 0 320.0 0 5.805 0 $Assembly: Full Assembly Surface'
    assert a.everythingElse.cellCard == '114 0 113 imp:n=0 $Everything Else'
