# -*- coding: utf-8 -*-

obdCommand=['ENGINE_LOAD','COOLANT_TEMP','FUEL_PRESSURE','INTAKE_PRESSURE','RPM','SPEED','INTAKE_TEMP','MAF','THROTTLE_POS','PIDS_B','EVAP_VAPOR_PRESSURE','BAROMETRIC_PRESSURE','PIDS_C','CONTROL_MODULE_VOLTAGE','ABSOLUTE_LOAD','COMMANDED_EQUIV_RATIO','RELATIVE_THROTTLE_POS','AMBIANT_AIR_TEMP','THROTTLE_POS_B','THROTTLE_POS_C','ACCELERATOR_POS_D','ACCELERATOR_POS_E','ACCELERATOR_POS_F','ETHANOL_PERCENT','RELATIVE_ACCEL_POS','OIL_TEMP','unsupported']
obdCommandDescription = ['Calculated Engine Load [%]','Engine Coolant Temperature [°C]','Fuel Pressure [kPa]','Intake Manifold Pressure [kPa]','Engine RPM','Vehicle Speed [km/h]','Intake Air Temp  [°C]','Air Flow Rate (MAF) [g/s]','Throttle Position [%]','Supported PIDs [21-40]','Evaporative system vapor pressure [Pa]','Barometric Pressure [kPa]','Supported PIDs [41-60]','Control module voltage [V]','Absolute load value [%]','Commanded equivalence ratio','Relative throttle position [%]','Ambient air temperature [°C]','Absolute throttle position B [%]','Absolute throttle position C [%]','Accelerator pedal position D [%]','Accelerator pedal position E [%]','Accelerator pedal position F [%]','Ethanol Fuel Percent  [%]','Relative accelerator pedal position [%]','Engine oil temperature [°C]','unsupported']
dialType = [1,2,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1]
minVal = [0,-40,0,0,0,0,-40,0,0,0,-8192,0,0,0,0,0,0,-40,0,0,0,0,0,0,0,-40,0]
maxVal = [100,215,765,255,7000,220,215,655,100,0,8192,255,0,65,100,2,100,215,100,100,100,100,100,100,100,210,0]
Increment1 = [25,24,191,64,1750,55,24,164,25,0,-4096,64,0,16,25,0.5,25,24,25,25,25,25,25,25,25,23,0]
Increment2 = [50,88,383,128,3500,110,88,328,50,0,0,128,0,33,50,1,50,88,50,50,50,50,50,50,50,85,0]
Increment3 = [75,151,574,191,5250,165,151,491,75,0,4096,191,0,49,75,1.5,75,151,75,75,75,75,75,75,75,148,0]




