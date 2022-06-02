# Replace-object-by-active-object
I am happy to announce my first contribution to a Blender addon in terms of coding. Thanks to @Gorgious for creating the operator!

This addon allows you to replace Mesh objects with Grease Pencil objects and vice versa, but also works for Mesh>Mesh or GP> GP. This is something that Blender does not allow by default. Select the objects you want to replace and then select the object you want to replace them with.
There's an option to delete the selected objects in the redo last panel.

![enter image description here](https://i.stack.imgur.com/b4etD.gif)

The objects are oriented origin to origin and will inherit transforms, so if you don't want them to do this, apply transforms beforehand. 

The operator is found in the "Link/ Transfer Data menu"  (Ctrl+L in the default Blender keymap) or by using the search term "Replace object by active object".
