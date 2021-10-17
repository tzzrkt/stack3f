bl_info = {
    "name": "Stack3r",
    "author": "tzzrkt",
    "version": (1, 0),
    "blender": (2, 93, 0),
    "location": "View3D > Toolbar > Stack3r",
    "description": "Create a stack of prisms with a few parameters",
    "warning": "",
    "wiki_url": "",
    "category": "Add Mesh",
}


import bpy
import random


class TWG_PT_tools_panel(bpy.types.Panel):
    bl_label = "Stack3r"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"

    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()        
        
        row.label(text="Press Stack", icon= "COLLAPSEMENU")
        
        row = layout.row()
        
        self.layout.operator("object.tower", icon="FILE_VOLUME")
        
        row = layout.row()
                    

class TWG_OT_tower(bpy.types.Operator):
    bl_idname = "object.tower"
    bl_label = "Stack" 
    bl_options = {"REGISTER", "UNDO"}
    
    float_scale: bpy.props.FloatProperty(
        name="Mult",
        description="Multiply Size",
        default=2,
        min=1, soft_max=5,
    )
    
    sides_amt: bpy.props.IntProperty(
        name="Sides",
        description="Side Amount",
        default=5,
        min=3, soft_max=6,
    )
    
    add_torque: bpy.props.FloatProperty(
        name="Torque",
        description="Add Torsion",
        default=0.00,
        min=-0.2,max=0.2,
    )
    
    shrink_z: bpy.props.FloatProperty(
        name="Headshrink",
        description="Itself",
        default=1,
        min=0.9,max=1.1,
    )
    
    floor_amount: bpy.props.IntProperty(
        name="Floors",
        description="Add Floors",
        default=5,
        min=1,soft_max=10,
    )
    
                     
    def execute(self, context):
        print("TowerGen")
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False, confirm=False)
        
        rand = self.floor_amount
        multiplier = self.float_scale
        sideamnt = self.sides_amt
        spin = self.add_torque
        grew = self.shrink_z
        
        struct(sideamnt,0.5,1,grew,rand,multiplier,spin)
        
        return{"FINISHED"}
    
            

def prisma(sides,fh,zloc,zrot,rad):
    
    bpy.ops.mesh.primitive_cylinder_add(
    
    vertices=sides,
    depth=fh,
    location=(0,0,zloc),
    rotation=(0,0,zrot),
    radius=(rad)
    
    )

def struct(sidamt, step, scl, ungrow,floors,mult,spin):
      
    y=0    
    for i in range(0,floors):
        y = y+step
        scl=scl*ungrow
        prisma(sidamt,step*mult,y*mult,i*spin,scl*mult)



def register():
    bpy.utils.register_class(TWG_PT_tools_panel)
    bpy.utils.register_class(TWG_OT_tower)
    
def unregister():
    bpy.utils.unregister_class(TWG_PT_tools_panel)
    bpy.utils.unregister_class(TWG_OT_tower)  
    
if __name__ == "__main__":
    register()  
