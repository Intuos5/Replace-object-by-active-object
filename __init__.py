# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Replace objects by active object",
    "author" : "Gorgious",
    "description" : "Replaces selected objects with the active object and inherits the transforms of the source objects",
    "blender" : (3, 1, 0),
    "version" : (0, 0, 1),
    "location" : "View3D",
    "warning" : "",
    "category" : "Object"
}

import bpy

from .OP_Replace_by_active import SW_OT_Replace_Object_by_Active

classes = (SW_OT_Replace_Object_by_Active)

def menu_func(self, context):
    self.layout.operator(SW_OT_Replace_Object_by_Active.bl_idname, text=SW_OT_Replace_Object_by_Active.bl_label)

def register():
    bpy.utils.register_class(SW_OT_Replace_Object_by_Active)
    bpy.types.VIEW3D_MT_make_links.append(menu_func)

def unregister():
    bpy.utils.register_class(SW_OT_Replace_Object_by_Active)
    bpy.types.VIEW3D_MT_make_links.remove(menu_func)
