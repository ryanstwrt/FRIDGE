import fridge.driver.global_variables as gb


def test_global_variables_default():
    """Check that the default variables are set correctly"""

    global_variables = gb.GlobalVariables()
    assert global_variables.assembly_file_name == ''
    assert global_variables.xc_set == ''
    assert global_variables.xc_library == ''
    assert global_variables.universe == 100
    assert global_variables.cellNumber == 100
    assert global_variables.surfaceNumber == 100
    assert global_variables.materialNumber == 100
    assert global_variables.temperature == 0
    assert global_variables.temp_adjusted_density is False
    assert global_variables.temp_adjusted_volume is False
    assert global_variables.clad_smear is False
    assert global_variables.bond_smear is False
    assert global_variables.void_per == 0
    assert global_variables.file_name == ''
    assert global_variables.number_generations == 0
    assert global_variables.number_skipped_generations == 0
    assert global_variables.number_particles_generation == 0
    assert global_variables.kopts is False
    assert global_variables.ksens is False
    assert global_variables.output_name == ''
    assert global_variables.input_type == ''


def test_global_variables_read_assembly():
    """Check the read_assembly function"""
    global_variables = gb.GlobalVariables()
    global_variables.read_input_file('A271_Assembly_Test')

    assert global_variables.assembly_file_name == 'A271_Assembly_Test'
    assert global_variables.xc_set == '.71c'
    assert global_variables.xc_library == 'ENDFVII.0'
    assert global_variables.universe == 100
    assert global_variables.cellNumber == 100
    assert global_variables.surfaceNumber == 100
    assert global_variables.materialNumber == 100
    assert global_variables.temperature == 600
    assert global_variables.temp_adjusted_density is True
    assert global_variables.temp_adjusted_volume is True
    assert global_variables.clad_smear is True
    assert global_variables.bond_smear is True
    assert global_variables.file_name == 'A271_Test'
    assert global_variables.number_generations == 2300
    assert global_variables.number_skipped_generations == 300
    assert global_variables.number_particles_generation == 1e10
    assert global_variables.kopts is True
    assert global_variables.ksens is True
    assert global_variables.output_name == 'Fuel_Assembly_Test'
    assert global_variables.input_type == 'Single'
