import bpy
import os
from bpy_extras.io_utils import ImportHelper
from bpy.props import StringProperty

# 设置图片文件夹路径
# folder_path = r"D:\Snowbreak\提取\恩雅"


class CusProperties(bpy.types.PropertyGroup):
    filepath_img_a: StringProperty(
        name="Img File Path", subtype="NONE", default=""
    )  # type: ignore


class ImportImgFilePath(bpy.types.Operator, ImportHelper):
    """Import Img file Path"""

    bl_idname = "wm.import_img_file_path"  # Unique identifier for buttons and menu items to reference.
    bl_label = " 导入图片路径"

    filter_glob: StringProperty(
        default="*.png;*.psd;*.jpg;*.tga",
        options={"HIDDEN"},
        maxlen=255,  # Max internal buffer length, longer would be truncated.
    )  # type: ignore

    def execute(self, context):
        filepath = self.filepath
        bpy.context.scene.cus_properties.filepath_img_a = filepath

        return {"FINISHED"}


num = 0


class BatchImgLoad(bpy.types.Operator):
    bl_label = "Batch_Img_Load"
    bl_description = "批量导入图片纹理"
    bl_idname = "cus_batch_img.load_ops"

    @classmethod
    def poll(cls, context):
        return bpy.context.scene.cus_properties.filepath_img_a

    def execute(self, context):
        # 遍历文件夹中的所有图片文件
        global num
        for root, dirs, files in os.walk(
            bpy.context.scene.cus_properties.filepath_img_a
        ):
            for file_name in files:
                if file_name.endswith(
                    (".png", ".jpg", ".tga", ".psd")
                ):  # 可以根据需要添加其他格式
                    img_path = os.path.join(root, file_name)
                    # 导入图片
                    bpy.data.images.load(img_path)
                    num += 1

        self.report({"INFO"}, f"批量导入了{num}张图片纹理")
        num = 0
        return {"FINISHED"}


class RemoveFilePath(bpy.types.Operator):
    bl_label = "删除文件路径"
    bl_idname = "del_filepath.del_ops"

    @classmethod
    def poll(cls, context):

        return bpy.context.scene.cus_properties.filepath_img_a

    def execute(self, context):

        bpy.context.scene.cus_properties.filepath_img_a = ""

        return {"FINISHED"}
