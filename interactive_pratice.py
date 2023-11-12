import time
time_sleep = 3
duration = 0.2
for i in range(time_sleep):
    print(i)
    time.sleep(1)
region = (631, 334, 1463, 794)

import pyautogui
import pyperclip
import math
def distance_2d(x1,y1,x2,y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def locate_move_click(image,confidence=0.7):
    result = pyautogui.locateOnScreen(image, grayscale=False, confidence=confidence)
    if result is not None:
        left, top, width, height = result  # 提取位置信息
        target_x = left + width / 2  # 计算目标位置的x坐标
        target_y = top + height / 2  # 计算目标位置的y坐标
        pyautogui.moveTo(target_x, target_y,duration=1)  # 将鼠标移动到目标位置
        pyautogui.click(x=target_x, y=target_y, clicks=1, interval=0.0, button='left')
        time.sleep(0.8)
    else:
        return None



# # 找到交易所小图标点击  
# # 找到拍卖行，点击
# # 找到首饰选项卡，点击
# # 找到搜索详情，点击
# locate_move_click("resource/auction_icon.png")
# locate_move_click("resource/auction.png")
# locate_move_click("resource/jew_button.png",confidence=0.8)
# locate_move_click("resource/jew_earring_button.png",confidence=0.8)
# locate_move_click("resource/advanced_search_button.png",confidence=0.8)
# time.sleep(3)

# appended = list()
# res = pyautogui.locateAllOnScreen("resource/advanced_seach_conditions.png",confidence=0.7)
# for i in res:
#     flag = True 
#     left, top, width, height = i  # 提取位置信息
#     target_x = left + width / 2  # 计算目标位置的x坐标
#     target_y = top + height / 2  # 计算目标位置的y坐标
#     for point in appended:
#         x,y = point 
#         if distance_2d(x,y,target_x,target_y) < 30 :
#             flag = False
#     if flag:
#         appended.append([target_x,target_y])

# for point in appended:  # 点开【全部】
#     target_x, target_y = point
#     keyword_x,keyword_y = target_x + 150, target_y
#     min_value_x, min_value_y = target_x + 350, target_y
#     max_value_x, max_value_y = target_x + 405, target_y
#     print(f"点开的全部，位置为：{target_x},{target_y}")
#     # 点开条件
#     pyautogui.moveTo(target_x, target_y,duration=duration)  # 将鼠标移动到目标位置
#     pyautogui.click(x=target_x, y=target_y, clicks=1, interval=0.0, button='left')
#     # 找到条件
#     # locate_move_click("resource/advanced_seach_condition_fight.png",confidence=0.8)
#     # pyautogui.moveTo(target_x + 150, target_y, duration=1)  # 将鼠标移动到目标位置
#     # pyautogui.click(x=target_x + 150, y=target_y, clicks=1, interval=0.0, button='left')
#     # 【找到特性】
#     res = pyautogui.locateAllOnScreen("resource/advanced_seach_condition_engrave.png",confidence=0.95)
#     for f in res:
#         left, top, width, height = f  # 提取位置信息
#         _target_x = left + width / 2  # 计算目标位置的x坐标
#         _target_y = top + height / 2  # 计算目标位置的y坐标
#         print(f"找到的战斗特性有：{target_x},{target_y}")
#         pyautogui.moveTo(_target_x, _target_y, duration=duration)  # 将鼠标移动到目标位置
#         pyautogui.click(x=_target_x, y=_target_y, clicks=1, interval=0.0, button='left')
#         # 模拟填值
#         pyautogui.moveTo(keyword_x, keyword_y, duration=duration)  # 将鼠标移动到目标位置
#         pyautogui.click(x=keyword_x, y=keyword_y , clicks=1, interval=0.0, button='left')
#         pyperclip.copy("肾上腺素")
#         pyautogui.hotkey('ctrl', 'v')
#         pyautogui.click(x=1, y=1 , clicks=1, interval=0.0, button='left')
#         time.sleep(0.2)
#         pyautogui.moveTo(min_value_x, min_value_y, duration=duration)  # 将鼠标移动到目标位置
#         pyautogui.click(x=min_value_x, y=min_value_y , clicks=2, interval=0.0, button='left')
#         pyperclip.copy("3")
#         pyautogui.hotkey('ctrl', 'v')
#         pyautogui.moveTo(max_value_x, max_value_y, duration=duration)  # 将鼠标移动到目标位置
#         pyautogui.click(x=max_value_x, y=max_value_y , clicks=1, interval=0.0, button='left')
#         pyperclip.copy("4")
#         pyautogui.hotkey('ctrl', 'v')
# locate_move_click("resource/auction_search_button.png",confidence=0.9)

# # 获得鼠标位置
# _point = pyautogui.position() 
# print(_point)

import easyocr

# 获取游戏窗口的屏幕截图
screenshot = pyautogui.screenshot()
# 定义需要识别的区域（根据实际情况进行调整）
# 根据定义的区域裁剪截图
cropped_image = screenshot.crop(region)
# 保存裁剪后的截图为临时文件
cropped_image.save('temp/cropped_screenshot.png')

# 对图像进行预处理（根据实际情况进行调整）
# 例如，调整大小、二值化等
# 使用pytesseract进行OCR识别

reader = easyocr.Reader(['ch_sim', 'en'])  # 创建EasyOCR对象，指定语言为简体中文和英文
result = reader.readtext('temp/cropped_screenshot.png')  # 对图像进行文字识别

# 对识别得到的文本数据进行解析和处理，提取表格数据
# 根据表格的具体结构和格式，使用适当的解析方法（如正则表达式、字符串处理等）
# 打印提取到的表格数据
for detection in result:
    print(detection)


