from .ops import ImportImgFilePath, BatchImgLoad, RemoveFilePath
import bpy


class BatchLoadImgUI(bpy.types.Panel):
    # 标签
    bl_label = "批量导入图片"  # 面板显示名称
    bl_idname = "Batch_img_load"
    # 面板所属区域
    bl_space_type = "NODE_EDITOR"
    # 显示面板的地方
    bl_region_type = "UI"
    # 显示面板的地方的归类
    bl_category = "Tool"

    def draw(self, context):
        layout = self.layout
        props = context.scene.cus_properties
        box = layout.box()
        box.label(text="选择图片文件路径")
        box_row = box.row()
        box_row.operator(
            ImportImgFilePath.bl_idname, text="导入图片路径", icon="IMPORT"
        )
        box_row.operator(RemoveFilePath.bl_idname, text="", icon="TRASH")
        box.prop(props, "filepath_img_a", text="路径", emboss=False)
        box.operator(
            BatchImgLoad.bl_idname, text="批量导入图片", icon="SEQ_CHROMA_SCOPE"
        )
