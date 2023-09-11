import numpy as np
import bpy
from io_scene_gltf2.io.com import gltf2_io_constants
from io_scene_gltf2.blender.exp import gltf2_blender_export_keys
from io_scene_gltf2.blender.exp import gltf2_blender_gather_nodes
from io_scene_gltf2.blender.exp import gltf2_blender_gather_mesh
from io_scene_gltf2.blender.exp import gltf2_blender_gather_primitive_attributes
from io_scene_gltf2.blender.imp.gltf2_blender_node import BlenderNode

bl_info = {
    "name" : "glTF EXT_mesh_gpu_instancing IO",
    "author" : "Takahiro Aoyagi",
    "description" : "Addon for glTF EXT_mesh_gpu_instancing extension",
    "blender" : (3, 4, 0),
    "version" : (0, 0, 3),
    "location" : "",
    "wiki_url": "https://github.com/takahirox/glTF-Blender-IO-EXT-mesh-gpu-instancing/wiki",
    "tracker_url": "https://github.com/takahirox/glTF-Blender-IO-EXT-mesh-gpu-instancing/issues",
    "support": "COMMUNITY",
    "warning" : "",
    "category" : "Generic"
}

glTF_extension_name = "EXT_mesh_gpu_instancing"

def register():
    return

def unregister():
    return

# Export

class glTF2ExportUserExtension:
    def __init__(self):
        from io_scene_gltf2.io.com.gltf2_io_extensions import Extension
        self.Extension = Extension

    # @TODO: Optimize
    def gather_node_hook(self, gltf2_node, blender_object, export_settings):
        if not export_settings['gltf_apply']:
            return

        depsgraph = bpy.context.evaluated_depsgraph_get()
        blender_object_eval = blender_object.evaluated_get(depsgraph)

        found = False
        parent_world_matrix_inverted = None

        locations = []
        rotations = []
        scales = []

        for object_instance in depsgraph.object_instances:
            if not object_instance.is_instance or blender_object_eval != object_instance.parent:
                continue

            if not found:
                found = True
                parent_world_matrix_inverted = object_instance.parent.matrix_world.inverted_safe()

            blender_mesh = object_instance.object.data
            materials = tuple(ms.material for ms in object_instance.object.material_slots)
            result = gltf2_blender_gather_mesh.gather_mesh(
                blender_mesh,
                None, # uuid_for_skined_data,
                None, # vertex_groups,
                None, # modifiers,
                True, # skip_filter
                materials,
                None, # original_mesh
                export_settings
            )

            gltf2_node.mesh = result

            local_matrix = parent_world_matrix_inverted @ object_instance.matrix_world
            loc, rot, sca = local_matrix.decompose()

            if export_settings['gltf_yup']:
                locations.append(loc.x)
                locations.append(loc.z)
                locations.append(-loc.y)

                rotations.append(rot.x)
                rotations.append(rot.z)
                rotations.append(-rot.y)
                rotations.append(rot.w)

                scales.append(sca.x)
                scales.append(sca.z)
                scales.append(sca.y)
            else:
                locations.append(loc.x)
                locations.append(loc.y)
                locations.append(loc.z)

                rotations.append(rot.x)
                rotations.append(rot.y)
                rotations.append(rot.z)
                rotations.append(rot.w)

                scales.append(sca.x)
                scales.append(sca.y)
                scales.append(sca.z)

        if not found:
            return

        if gltf2_node.extensions is None:
            gltf2_node.extensions = {}
        gltf2_node.extensions[glTF_extension_name] = self.Extension(
            name=glTF_extension_name,
            extension={"attributes": {
                "TRANSLATION": gltf2_blender_gather_primitive_attributes.array_to_accessor(
                    np.array(locations, dtype=np.float32).reshape(int(len(locations) / 3), 3),
                    component_type=gltf2_io_constants.ComponentType.Float,
                    data_type=gltf2_io_constants.DataType.Vec3,
                    include_max_and_min=True,
                ),
                "ROTATION": gltf2_blender_gather_primitive_attributes.array_to_accessor(
                    np.array(rotations, dtype=np.float32).reshape(int(len(rotations) / 4), 4),
                    component_type=gltf2_io_constants.ComponentType.Float,
                    data_type=gltf2_io_constants.DataType.Vec4,
                    include_max_and_min=True,
                ),
                "SCALE": gltf2_blender_gather_primitive_attributes.array_to_accessor(
                    np.array(scales, dtype=np.float32).reshape(int(len(scales) / 3), 3),
                    component_type=gltf2_io_constants.ComponentType.Float,
                    data_type=gltf2_io_constants.DataType.Vec3,
                    include_max_and_min=True,
                ),
            }},
            required=False
        )
