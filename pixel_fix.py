from PIL import Image
import os
size = int(input('请输入像素颗粒大小,推荐值:8,16或32,输入完成后请按回车键\nEnter pixel grain size, recommended values: 8, 16, or 32. Press Enter key when done'))
def pixelate_image(input_folder, output_folder, pixel_size=size):
    # 获取 input 文件夹中所有 PNG、JPG 和 JPEG 图片
    image_files = [file for file in os.listdir(input_folder) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]

    # 创建输出文件夹
    os.makedirs(output_folder, exist_ok=True)

    # 处理每张图片
    for image_file in image_files:
        input_path = os.path.join(input_folder, image_file)
        output_path = os.path.join(output_folder, image_file)

        try:
            # 读取图片
            with Image.open(input_path) as img:
                # 将图片进行像素化
                img_pixelated = img.resize(
                    (img.width // pixel_size, img.height // pixel_size),
                    resample=Image.NEAREST
                ).resize(
                    (img.width, img.height),
                    resample=Image.NEAREST
                )

                # 保存像素化后的图片，保持原有格式
                img_pixelated.save(output_path)

                print(f"处理成功: {image_file}")

        except Exception as e:
            print(f"处理失败: {image_file}. 错误信息: {str(e)}")

if __name__ == "__main__":
    current_folder = os.getcwd()
    input_folder = os.path.join(current_folder, "in")  # input 文件夹
    output_folder = os.path.join(current_folder, "out")

    try:
        # 处理图像，带有异常捕获机制
        pixelate_image(input_folder, output_folder)

        print("任务完成！")

    except Exception as e:
        print(f"发生错误: {str(e)}")
