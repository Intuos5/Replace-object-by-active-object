import bpy

class SW_OT_Replace_Object_by_Active(bpy.types.Operator):
    bl_idname = "replace.object_by_active"
    bl_label = "Replace object by active"
    bl_description = "Replace selected objects with the active object"
    bl_options = {"REGISTER", "UNDO"}
 
    delete_selected: bpy.props.BoolProperty(default=True, name="Delete Selected")

    @classmethod
    def poll(cls, context):
        return len(context.selected_objects) > 1

    def execute(self, context):
        source = context.active_object
        for obj in context.selected_objects:
            if obj == source:
                continue
            new = bpy.data.objects.new(name=source.name, object_data=source.data)
            source.users_collection[0].objects.link(new)
            new.matrix_world = obj.matrix_world
            # If you don't want the new objects to inherit scale & rotation, use this :
            # new.location = obj.location
            if self.delete_selected:
                bpy.data.objects.remove(obj)
            new.select_set(True)
        return {'FINISHED'}

