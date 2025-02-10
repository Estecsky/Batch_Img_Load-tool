# import sys

# path = r"C:\Users\apsur\AppData\Roaming\Blender Foundation\Blender\3.6\scripts\addons\batch_img_load"
# sys.path.append(path)

import bpy
from bpy.props import PointerProperty
from .ops import CusProperties, ImportImgFilePath, BatchImgLoad, RemoveFilePath
from .ui import BatchLoadImgUI

bl_info = {
    "name": "Batch_img_load",
    "author": "Estecsky",
    "description": "批量导入各种格式图片资源",
    "blender": (3, 4, 0),  # 插件所支持的blender版本
    "location": "着色器编辑器 > 侧边栏",  # 插件显示的位置
    # "warning": "插件处于测试阶段",  # 警告信息
    "category": "Material",  # 归类信息 搜索插件的时候显示的分类
    "version": (0, 1, 0),
}

lst = [CusProperties, ImportImgFilePath, BatchImgLoad, RemoveFilePath, BatchLoadImgUI]


def register():
    for i in lst:
        bpy.utils.register_class(i)

    bpy.types.Scene.cus_properties = PointerProperty(type=CusProperties)


def unregister():
    for i in lst:
        bpy.utils.unregister_class(i)

    del bpy.types.Scene.cus_properties


if __name__ == "__main__":
    register()
