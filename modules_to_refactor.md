# Modules to refactor

## Components
- trunk/SUAVE/Components/Energy/Networks/Turboelectric_Ducted_Fan.py
- trunk/SUAVE/Components/Energy/Networks/Turboelectric_HTS_Ducted_Fan.py
- trunk/SUAVE/Components/Energy/Networks/Turboelectric_HTS_Dynamo_Ducted_Fan.py

## Input_Output
- trunk/SUAVE/Input_Output/Results/print_hts_powertrain_weights.py
- trunk/SUAVE/Input_Output/Results/print_mission_breakdown.py

## Methods
- trunk/SUAVE/Methods/Cooling/__init__.py

### Cooling/Cryocooler
- trunk/SUAVE/Methods/Cooling/Cryocooler/__init__.py
- trunk/SUAVE/Methods/Cooling/Cryocooler/Cooling/__init__.py
- trunk/SUAVE/Methods/Cooling/Cryocooler/Cooling/cryocooler_model.py
- trunk/SUAVE/Methods/Cooling/Cryocooler/Sizing/__init__.py
- trunk/SUAVE/Methods/Cooling/Cryocooler/Sizing/size_cryocooler.py

### Cooling/Cryogen
- trunk/SUAVE/Methods/Cooling/Cryogen/__init__.py
- trunk/SUAVE/Methods/Cooling/Cryogen/Consumption/__init__.py
- trunk/SUAVE/Methods/Cooling/Cryogen/Consumption/Coolant_use.py

### Cooling/Leads
- trunk/SUAVE/Methods/Cooling/Leads/__init__.py
- trunk/SUAVE/Methods/Cooling/Leads/copper_lead.py

### Geometry/Two_Dimensional/Cross_Section/Propulsion
- trunk/SUAVE/Methods/Geometry/Two_Dimensional/Cross_Section/Propulsion/__init__.py
- trunk/SUAVE/Methods/Geometry/Two_Dimensional/Cross_Section/Propulsion/compute_turboelectric_ducted_fan_geometry.py

### Missions/Segments/Common
- trunk/SUAVE/Methods/Missions/Segments/Common/Energy.py
- trunk/SUAVE/Methods/Missions/Segments/Common/Weights.py
- trunk/SUAVE/Methods/Missions/Segments/Common/Weights.py

### Power/Turboelectric
- trunk/SUAVE/Methods/Power/Turboelectric/__init__.py

### Power/Turboelectric/Discharge
- trunk/SUAVE/Methods/Power/Turboelectric/Discharge/__init__.py
- trunk/SUAVE/Methods/Power/Turboelectric/Discharge/zero_fidelity.py


### Power/Turboelectric/Sizing
- trunk/SUAVE/Methods/Power/Turboelectric/Sizing/__init__.py
- trunk/SUAVE/Methods/Power/Turboelectric/Sizing/initialize_from_power.py

### Propulsion
- trunk/SUAVE/Methods/Propulsion/__init__.py
- trunk/SUAVE/Methods/Propulsion/serial_hts_turboelectric_sizing.py
- trunk/SUAVE/Methods/Propulsion/serial_hts_dynamo_turboelectric_sizing.py
- trunk/SUAVE/Methods/Propulsion/turboelectric_ducted_fan_sizing.py

### Weights/Correlations/Tube_Wing_HTS_Dynamo_TurboElectric
- trunk/SUAVE/Methods/Weights/Correlations/Tube_Wing_HTS_Dynamo_TurboElectric/__init__.py
- trunk/SUAVE/Methods/Weights/Correlations/Tube_Wing_HTS_Dynamo_TurboElectric/SiC_Electronics.py
- trunk/SUAVE/Methods/Weights/Correlations/Tube_Wing_HTS_Dynamo_TurboElectric/empty.py

### Weights/Correlations/Tube_Wing_HTS_TurboElectric
- trunk/SUAVE/Methods/Weights/Correlations/Tube_Wing_HTS_TurboElectric/__init__.py
- trunk/SUAVE/Methods/Weights/Correlations/Tube_Wing_HTS_TurboElectric/Current_Supply.py
- trunk/SUAVE/Methods/Weights/Correlations/Tube_Wing_HTS_TurboElectric/SiC_Electronics.py
- trunk/SUAVE/Methods/Weights/Correlations/Tube_Wing_HTS_TurboElectric/empty.py

### Weights/Correlations/Tube_Wing_TurboElectric
- trunk/SUAVE/Methods/Weights/Correlations/Tube_Wing_TurboElectric/__init__.py
- trunk/SUAVE/Methods/Weights/Correlations/Tube_Wing_TurboElectric/empty.py
- trunk/SUAVE/Methods/Weights/Correlations/Tube_Wing_TurboElectric/systems.py
- trunk/SUAVE/Methods/Weights/Correlations/Tube_Wing_TurboElectric/tail_horizontal.py
- trunk/SUAVE/Methods/Weights/Correlations/Tube_Wing_TurboElectric/tail_vertical.py
- trunk/SUAVE/Methods/Weights/Correlations/Tube_Wing_TurboElectric/tube.py
