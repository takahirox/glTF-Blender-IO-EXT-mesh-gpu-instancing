# glTF-Blender-IO-EXT-mesh-gpu-instancing

**glTF-Blender-IO-EXT-mesh-gpu-instancing** is a [Blender](https://www.blender.org/) addon for [glTF `EXT_mesh_gpu_instancing` extension](https://github.com/KhronosGroup/glTF/blob/main/extensions/2.0/Vendor/EXT_mesh_gpu_instancing/README.md) on top of [`glTF-Blender-IO`](https://github.com/KhronosGroup/glTF-Blender-IO) addon.

## Compatible Blender version

&gt;= 3.3

## Features

The addon enables to export instanced geometries created with [Geometry Nodes](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/index.html) as glTF assets with the
[glTF `EXT_mesh_gpu_instancing` extension](https://github.com/KhronosGroup/glTF/blob/main/extensions/2.0/Vendor/EXT_mesh_gpu_instancing/README.md) in [Blender](https://www.blender.org/).

Import support is work in progress.

## How to install

### Ensure the `glTF-Blender-IO` addon is installed and enabled

Ensure the `glTF-Blender-IO` addon is installed and enabled in your Blender because the `glTF-Blender-IO-EXT-mesh-gpu-instancing
` addon works on top of it.  You can check it by Edit -> Preferences -> Add-ons -> "glTF 2.0" in the search bar. The `glTF-Blender-IO` addon should be listed as `Import-Export: glTF 2.0 format`. It should be installed and enabled by default.

![Ensure glTF-Blender-IO is installed and enabled](https://user-images.githubusercontent.com/7637832/110406787-a41f3f80-8037-11eb-9e12-163aafd5f08e.png)

### Download the zip archived source code

Download the zip archived source code from the [Releases](https://github.com/takahirox/glTF-Blender-IO-EXT-mesh-gpu-instancing/releases).

### Install `glTF-Blender-IO-EXT-mesh-gpu-instancing` addon

Install the `glTF-Blender-IO-EXT-mesh-gpu-instancing` addon to your Blender via Edit -> Preferences -> Add-ons -> Install -> Select the downloaded file

![Edit -> Preferences](https://user-images.githubusercontent.com/7637832/110405180-062a7580-8035-11eb-839a-f5008a992f92.png)

![Add-ons -> Install](https://user-images.githubusercontent.com/7637832/110405413-70dbb100-8035-11eb-9860-3f4867427246.png)

![Select the downloaded file](https://user-images.githubusercontent.com/7637832/200152177-afacdc7d-5349-435e-bc80-7951c071b1b8.png)

### Enable the addon

Ensure the addon is installed and enabled. You can easily find the addon by inputting "EXT_mesh_gpu_instancing" in the search bar. Check the checkbox to enable the addon.

![Ensure the addon is enabled](https://user-images.githubusercontent.com/7637832/200152215-39be04be-3b6d-4a34-9704-c5f42d61dbf6.png)

## How to use

Create instanced geometries with Geometry Nodes. Note that "Realize instances" node is not needed.

<img src="https://user-images.githubusercontent.com/7637832/200151844-c4ade71d-0507-4268-8356-139157fb2db6.png" width="640" alt="Blender + Geometry Nodes + Instancing">

Export the asset as glTF with "Apply Modifiers" export option checked.

<img src="https://user-images.githubusercontent.com/7637832/200200340-04552522-d518-4985-814d-154de1045615.png" width="360" alt="Check Apply Modifiers">

You will get glTF having `EXT_mesh_gpu_instancing` extension.

<img src="https://user-images.githubusercontent.com/7637832/200151884-2f335fd0-3270-4b68-abc1-998837a0f9c6.png" width="480" alt="Exported glTF">
