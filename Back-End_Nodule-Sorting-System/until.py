from PIL import Image
from IDNS import prediction
import os

def count_images_with_keyword(directory, keyword):
    count = 0
    matching_files = []
    for filename in os.listdir(directory):
        if keyword in filename:
            count += 1
            matching_files.append(os.path.join(directory, filename))
    return count, matching_files

def preview_images(file_paths):
    for filepath in file_paths:
        try:
            image = Image.open(filepath)
            image.show()
        except Exception as e:
            print(f"无法打开文件 {filepath}: {e}")

def predict(pre,imgPath):
    predictions=pre.run(imgPath)
    response = {
        "predictions": {
            "5.高度可疑": predictions[0][0],
            "4.中度可疑": predictions[0][1],
            "3.不确定的": predictions[0][2],
            "2.中度不太可能": predictions[0][3],
            "1.高度不太可能": predictions[0][4]
        }
    }
    return response

def segmentation(seg,imgPath):
    seg=seg.run(imgPath)
    if(seg!=None):
        response = {
            "code":200,
            "segmentation": seg
        }
        return response
    else:
        response = {
            "code": 400,
            "segmentation": seg
        }



def find_max_probability(response):
    predictions=response.get('predictions')
    max_prob_key = max(predictions, key=predictions.get)

    max_prob_value = predictions[max_prob_key]
    return max_prob_value, max_prob_key

# 查询img包下图片名包含"ggb"字段的图片数量和文件路径
# directory = "img"
# keyword = "ggb"
# count, matching_files = count_images_with_keyword(directory, keyword)
# print(f"包含'{keyword}'字段的图片数量为: {count}")
# print("匹配的图片文件路径:")
# for file_path in matching_files:
#     print(file_path)
#
# # 预览匹配的图片
# preview_images(matching_files)
