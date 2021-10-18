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

        self.layout.operator("scale.all", icon="CON_SIZELIMIT")
        
        row = layout.row()
                    

class TWG_OT_tower(bpy.types.Operator):
    bl_idname = "object.tower"
    bl_label = "Stack" 
    bl_options = {"REGISTER", "UNDO"}
    
    float_scale: bpy.props.FloatProperty(
        name="Scale",
        description="Multiply Size",
        default=10,
        min=1, soft_max=10,
    )
    
    sides_amt: bpy.props.IntProperty(
        name="Sides",
        description="Side Amount",
        default=6,
        min=3, soft_max=6,
    )
    
    add_torque: bpy.props.FloatProperty(
        name="Torque",
        description="Add Torsion",
        default=0.00,
        min=-0.2,max=0.2,
    )
    
    shrink_z: bpy.props.FloatProperty(
        name="Cone Amount",
        description="Itself",
        default=0.94,
        min=0.9,max=1.1,
    )
    
    floor_amount: bpy.props.IntProperty(
        name="Floors",
        description="Add Floors",
        default=10,
        min=1,soft_max=10,
    )
    
    offset_z: bpy.props.FloatProperty(
        name="Z Offset",
        description="Itself",
        default=2.32,
        soft_min=0.0,soft_max=100,
    )  
      
    offset_f: bpy.props.FloatProperty(
        name="F Offset",
        description="Itself",
        default=0.46,
        soft_min=-100,soft_max=100,
    ) 
       
    walls_h: bpy.props.FloatProperty(
        name="Wall Height",
        description="Itself",
        default=11.74,
        soft_min=-100,soft_max=100,
    )
         
    floor_h: bpy.props.FloatProperty(
        name="Floor Height",
        description="Itself",
        default=5.71,
        soft_min=-100,soft_max=100,
    ) 
        
    master_rot: bpy.props.FloatProperty(
        name="Master Z Rotation",
        description="Itself",
        default=0,
        soft_min=-100,soft_max=100,
    )  

    x_size: bpy.props.FloatProperty(
        name="X Size",
        description="Itself",
        default=4,
        soft_min=-100,soft_max=100,
    ) 

    y_size: bpy.props.FloatProperty(
        name="Y Size",
        description="Itself",
        default=6,
        soft_min=-100,soft_max=100,
    ) 
    x_sizechild: bpy.props.FloatProperty(
        name="X Size child",
        description="Itself",
        default=3.5,
        soft_min=-100,soft_max=100,
    ) 

    y_sizechild: bpy.props.FloatProperty(
        name="Y Size child",
        description="Itself",
        default=6.8,
        soft_min=-100,soft_max=100,
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
        off = self.offset_z
        foff = self.offset_f
        flh = self.floor_h
        wlh = self.walls_h
        m_rott = self.master_rot
        xs = self.x_size
        ys = self.y_size
        xschild = self.x_sizechild
        yschild = self.y_sizechild
                
        struct(sideamnt,0.05,1.1,grew,rand,multiplier,spin,off,foff,flh,wlh,m_rott,xs,ys,xschild,yschild)        
        
        return{"FINISHED"}
    
            
class TWG_OT_scale(bpy.types.Operator):
    bl_idname = "scale.all"
    bl_label = "Scale All" 
    bl_options = {"REGISTER", "UNDO"}
    
    f_scale: bpy.props.FloatProperty(
        name="Scale_All",
        description="Multiply Size",
        default=1,
        min=0, soft_max=10,
    )
    
    def execute(self, context):
        print("Scaling")
        fscale = self.f_scale
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.transform.resize(value=(fscale, fscale, fscale), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        return{"FINISHED"}


def prisma(sides,fh,zloc,zrot,rad,prot,x,y):
    
    bpy.ops.mesh.primitive_cylinder_add(
    
    vertices=sides,
    depth=fh*3,
    location=(0,0,zloc),
    rotation=(0,0,prot+zrot),
    radius=(rad*5)
    
    )
    
    bpy.ops.mesh.primitive_cube_add(
    size=2, 
    enter_editmode=False,
    location=(0, 0, zloc), 
    rotation=(0,0,prot+zrot),
    scale=(x, y, fh)
    
    )



def struct(sidamt, step, scl, ungrow,floors,mult,spin,zoff,foff,fh,wh,prott,xxs,yys,xxx,yyy):
      
    y=0 
    yy =0  
    for i in range(0,floors):
            y = i*zoff
            yy= (i+foff)*zoff
            scl=scl*ungrow
            m_rot=prott
            xsc=xxs
            ysc=yys
            xxsc=xxx
            yysc=yyy             
            prisma(sidamt,step*mult*wh,yy*mult,i*spin,scl*mult*1,m_rot,xsc*mult*scl,ysc*mult*scl) 
            prisma(sidamt,step*mult*fh,y*mult,i*spin,scl*mult*1.1,m_rot,xxsc*mult*scl,yysc*mult*scl )              




def register():
    bpy.utils.register_class(TWG_PT_tools_panel)
    bpy.utils.register_class(TWG_OT_tower)
    bpy.utils.register_class(TWG_OT_scale)
    
def unregister():
    bpy.utils.unregister_class(TWG_PT_tools_panel)
    bpy.utils.unregister_class(TWG_OT_tower)  
    bpy.utils.unregister_class(TWG_OT_scale)
    
if __name__ == "__main__":
    register()  
