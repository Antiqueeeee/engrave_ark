# from loguru import logger
# logger.remove(handler_id=None)  # 不在控制台输出日志信息
import tr
from PIL import Image,ImageDraw

# 默认为 None，代表移除所有
# logger.remove()  # 这么写也行

image = Image.open(r"../压缩包_爬虫的数据-包括论文、谷歌学者等/list.jpg")
gray_pil = image.convert("L")
results = tr.run(gray_pil, flag=tr.FLAG_RECT)
# 返回值是中心点坐标xywh
imgdraw = ImageDraw.Draw(image)
# print(results)
for i in results:
    # 左上角和右下角
    # imgdraw.rectangle((i[0][0]-i[0][2]/2, i[0][1]-i[0][3]/2, i[0][0]+i[0][2]/2, i[0][1]+i[0][3]/2), outline='blue')
    print(str(i[1]).encode("utf-8").decode("utf-8"))

# image.show()
