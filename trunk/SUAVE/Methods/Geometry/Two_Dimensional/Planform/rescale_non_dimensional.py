## @ingroup Planform
#rescale_non_dimensional.py

# Created : Jun 2016, M. Vegh
# Modified:

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

import SUAVE
import numpy as np


# ----------------------------------------------------------------------
#  Set Origin Non-Dimensional
# ----------------------------------------------------------------------

def set_origin_non_dimensional(vehicle):
    """ Places the origin of all components 

        Assumptions:
        None

        Source:
        N/A

        Inputs:
        vehicle    [SUAVE Vehicle]

        Outputs:
        vehicle    [SUAVE Vehicle]

        Properties Used:
        None
    """        
    
    
    try:
        length_scale = vehicle.fuselages.fuselage.lengths.total
    except:
        try:
            length_scale = vehicle.wings.main_wing.spans.projected
        except:
            length_scale = 1.

    for wing in vehicle.wings:
        origin  = wing.origin
        non_dim = np.array(origin)/length_scale
        
        wing.non_dimensional_origin = non_dim.tolist()
    
    for fuse in vehicle.fuselages:
        origin  = fuse.origin
        non_dim = np.array(origin)/length_scale
        
        fuse.non_dimensional_origin = non_dim.tolist()  

    for prop in vehicle.propulsors:
        origins  = prop.origin
        prop.non_dimensional_origin.clear()
        for eng in range(int(prop.number_of_engines)):
            origin = np.array(origins[eng])/length_scale
            prop.non_dimensional_origin.append(origin.tolist())       
    
        
    return vehicle


# ----------------------------------------------------------------------
#  Scale to Non-Dimensional
# ----------------------------------------------------------------------

def set_origin_dimensional(vehicle):
    """ Places the origin of all components 

        Assumptions:
        None

        Source:
        N/A

        Inputs:
        vehicle    [SUAVE Vehicle]

        Outputs:
        vehicle    [SUAVE Vehicle]

        Properties Used:
        None
    """    
    
    try:
        length_scale = vehicle.fuselages.fuselage.lengths.total
    except:
        try:
            length_scale = vehicle.wings.main_wing.spans.projected
        except:
            length_scale = 1.

    for wing in vehicle.wings:
        non_dim = wing.non_dimensional_origin
        origin  = np.array(non_dim)*length_scale
        
        wing.origin = origin.tolist()
    
    for fuse in vehicle.fuselages:
        non_dim = fuse.non_dimensional_origin
        origin  = np.array(non_dim)*length_scale
        
        fuse.origin = origin.tolist()
                
    for prop in vehicle.propulsors:
        n = int(prop.number_of_engines)
        non_dims  = prop.non_dimensional_origin
        
        prop.origin.clear()
        
        origin = np.zeros((n,3))
    
        for eng in range(n):
            origin[eng,:] = np.array(non_dims[0])*length_scale
            prop.origin.append(origin.tolist())       
        
    return vehicle