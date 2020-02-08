import fridge.utilities.outputInterface as OI
import os
from collections import OrderedDict

def test_init():
    interface = OI.OutputReader(r'fridge/test_suite/test_interface.txt')
    assert interface.output == ['Test Interface\n', '\n', 'More Testing']
    assert interface.burnup == False
    assert interface.cycles == 0
    assert interface.cycle_dict == {}
    assert interface.core_name == 'test_interface'
    
def test_convert_rx_params():
    interface = OI.OutputReader(r'fridge/test_suite/FC_FS65_H75_23Pu4U10Zr_BU.out')
    assert interface.core_name == 'FC_FS65_H75_23Pu4U10Zr_BU'
    interface.cycle_dict['step_12'] = {}
    interface.scrap_rx_params(interface.output[268454:268454+83], 12)
    interface.convert_rx_params()
    step_0 = interface.cycle_dict['step_12']['rx_parameters']
    print(step_0['keff'])
    assert step_0['keff'][0] == 1.13466
    assert step_0['keff_unc'][0] == 0.00014
    assert step_0['prompt_removal_lifetime'][0] == (4.1290E-06, 1.6569E-09, 'seconds')
    assert step_0['avg_n_lethargy_fission'][0] == (7.4123E-01, 'mev')
    assert step_0['avg_n_energy_fission'][0] == (1.6782E-01, 'mev')
    assert step_0['thermal_fission_frac'][0] == (0.01)
    assert step_0['epithermal_fission_frac'][0] == (32.46)
    assert step_0['fast_fission_frac'][0] == (67.54)
    assert step_0['avg_n_gen_per_abs_fission'][0] == (1.882)
    assert step_0['avg_n_gen_per_abs_all'][0] == (1.2989)
    assert step_0['avg_n_gen_per_fission'][0] == (2.891)
 
    assert step_0['lifespan_esc'][0] == (1.79522E-06)
    assert step_0['lifespan_capt'][0] == (7.63721E-06)
    assert step_0['lifespan_fission'][0] == (5.72704E-07)
    assert step_0['lifespan_rem'][0] == (4.12287E-06)
    assert step_0['frac_esc'][0] == (1.27694E-01)
    assert step_0['frac_capt'][0] == (4.80438E-01)
    assert step_0['frac_fission'][0] == (3.91868E-01)
    assert step_0['frac_rem'][0] == (1.00000E+00)

    assert step_0['generation_time'][0] == (421.27908, 5.11714, ' (nsec)\n')
    assert step_0['rossi-alpha'][0] == (-8.41612E-06, 3.76984E-07, ' (/nsec)\n')
    assert step_0['beta'][0] == (0.00355, 0.00015)
    assert step_0['precursors'][0] == {1: {'beta-eff': 0.00011, 'beta-eff_unc': 0.00002, 'energy': 0.41927, 'energy_unc': 0.00198, 'energy_units': 'MeV', 'lambda-i': 0.01334, 'lambda-i_unc': 0.00000, 'lambda-i_units': '(/sec)', 'half-life': 51.95717, 'half-life_units': '(sec)'},
                                    2: {'beta-eff': 0.00065, 'beta-eff_unc': 0.00006, 'energy': 0.51754, 'energy_unc': 0.00079, 'energy_units': 'MeV', 'lambda-i': 0.03129, 'lambda-i_unc': 0.00000, 'lambda-i_units': '(/sec)', 'half-life': 22.14974, 'half-life_units': '(sec)'},
                                    3: {'beta-eff': 0.00064, 'beta-eff_unc': 0.00007, 'energy': 0.42396, 'energy_unc': 0.00081, 'energy_units': 'MeV', 'lambda-i': 0.11741, 'lambda-i_unc': 0.00001,  'lambda-i_units': '(/sec)', 'half-life': 5.90386, 'half-life_units': '(sec)'},
                                    4: {'beta-eff': 0.00134, 'beta-eff_unc': 0.00010, 'energy': 0.53274, 'energy_unc': 0.00073, 'energy_units': 'MeV', 'lambda-i': 0.30523, 'lambda-i_unc': 0.00002,  'lambda-i_units': '(/sec)', 'half-life': 2.27088, 'half-life_units': '(sec)'},
                                    5: {'beta-eff': 0.00060, 'beta-eff_unc': 0.00006, 'energy': 0.49371, 'energy_unc': 0.00101, 'energy_units': 'MeV', 'lambda-i': 0.87600, 'lambda-i_unc': 0.00006,  'lambda-i_units': '(/sec)', 'half-life': 0.79126, 'half-life_units': '(sec)'},
                                    6: {'beta-eff': 0.00020, 'beta-eff_unc': 0.00004, 'energy': 0.53827, 'energy_unc': 0.00194, 'energy_units': 'MeV', 'lambda-i': 2.90154, 'lambda-i_unc': 0.00056,  'lambda-i_units': '(/sec)', 'half-life': 0.23889, 'half-life_units': '(sec)'}}

    
def test_scrap_rx_params():
    interface = OI.OutputReader(r'fridge/test_suite/FC_FS65_H75_23Pu4U10Zr_BU.out')
    assert interface.core_name == 'FC_FS65_H75_23Pu4U10Zr_BU'
    interface.cycle_dict['step_12'] = {}
    interface.scrap_rx_params(interface.output[268454:268454+83], 12)
    step_0 = interface.cycle_dict['step_12']['rx_parameters']
    assert step_0['keff'] == 1.13466
    assert step_0['keff_unc'] == 0.00014
    assert step_0['prompt_removal_lifetime'] == (4.1290E-06, 1.6569E-09, 'seconds')
    assert step_0['avg_n_lethargy_fission'] == (7.4123E-01, 'mev')
    assert step_0['avg_n_energy_fission'] == (1.6782E-01, 'mev')
    assert step_0['thermal_fission_frac'] == (0.01)
    assert step_0['epithermal_fission_frac'] == (32.46)
    assert step_0['fast_fission_frac'] == (67.54)
    assert step_0['avg_n_gen_per_abs_fission'] == (1.882)
    assert step_0['avg_n_gen_per_abs_all'] == (1.2989)
    assert step_0['avg_n_gen_per_fission'] == (2.891)
 
    assert step_0['lifespan_esc'] == (1.79522E-06)
    assert step_0['lifespan_capt'] == (7.63721E-06)
    assert step_0['lifespan_fission'] == (5.72704E-07)
    assert step_0['lifespan_rem'] == (4.12287E-06)
    assert step_0['frac_esc'] == (1.27694E-01)
    assert step_0['frac_capt'] == (4.80438E-01)
    assert step_0['frac_fission'] == (3.91868E-01)
    assert step_0['frac_rem'] == (1.00000E+00)

    assert step_0['generation_time'] == (421.27908, 5.11714, ' (nsec)\n')
    assert step_0['rossi-alpha'] == (-8.41612E-06, 3.76984E-07, ' (/nsec)\n')
    assert step_0['beta'] == (0.00355, 0.00015)
    assert step_0['precursors'] == {1: {'beta-eff': 0.00011, 'beta-eff_unc': 0.00002, 'energy': 0.41927, 'energy_unc': 0.00198, 'energy_units': 'MeV', 'lambda-i': 0.01334, 'lambda-i_unc': 0.00000, 'lambda-i_units': '(/sec)', 'half-life': 51.95717, 'half-life_units': '(sec)'},
                                    2: {'beta-eff': 0.00065, 'beta-eff_unc': 0.00006, 'energy': 0.51754, 'energy_unc': 0.00079, 'energy_units': 'MeV', 'lambda-i': 0.03129, 'lambda-i_unc': 0.00000, 'lambda-i_units': '(/sec)', 'half-life': 22.14974, 'half-life_units': '(sec)'},
                                    3: {'beta-eff': 0.00064, 'beta-eff_unc': 0.00007, 'energy': 0.42396, 'energy_unc': 0.00081, 'energy_units': 'MeV', 'lambda-i': 0.11741, 'lambda-i_unc': 0.00001,  'lambda-i_units': '(/sec)', 'half-life': 5.90386, 'half-life_units': '(sec)'},
                                    4: {'beta-eff': 0.00134, 'beta-eff_unc': 0.00010, 'energy': 0.53274, 'energy_unc': 0.00073, 'energy_units': 'MeV', 'lambda-i': 0.30523, 'lambda-i_unc': 0.00002,  'lambda-i_units': '(/sec)', 'half-life': 2.27088, 'half-life_units': '(sec)'},
                                    5: {'beta-eff': 0.00060, 'beta-eff_unc': 0.00006, 'energy': 0.49371, 'energy_unc': 0.00101, 'energy_units': 'MeV', 'lambda-i': 0.87600, 'lambda-i_unc': 0.00006,  'lambda-i_units': '(/sec)', 'half-life': 0.79126, 'half-life_units': '(sec)'},
                                    6: {'beta-eff': 0.00020, 'beta-eff_unc': 0.00004, 'energy': 0.53827, 'energy_unc': 0.00194, 'energy_units': 'MeV', 'lambda-i': 2.90154, 'lambda-i_unc': 0.00056,  'lambda-i_units': '(/sec)', 'half-life': 0.23889, 'half-life_units': '(sec)'}}

def test_scrap_assembly_power():
    interface = OI.OutputReader(r'fridge/test_suite/FC_FS65_H75_23Pu4U10Zr_BU.out')
    interface.cycles = 7
    for x in range(interface.cycles):
        interface.cycle_dict['step_{}'.format(x)] = {}
        interface.cycle_dict['step_{}'.format(x)]['assemblies'] = {}
    interface.scrap_assembly_power(interface.output[269920:269920+4+7])
    assert interface.cycle_dict['step_0']['assemblies'] == {1902: {'duration': 0.0,
                                                       'time': 0.0,
                                                       'power fraction': 9.960E-3,
                                                       'burnup': 0.0}}
    assert interface.cycle_dict['step_6']['assemblies'] == {1902: {'duration': 50.0,
                                                       'time': 300.0,
                                                       'power fraction': 1.027E-2,
                                                       'burnup': 2.961E+1}}    