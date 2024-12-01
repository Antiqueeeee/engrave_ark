import time
import os
import sys
import pyautogui
import pyperclip
import math
from tr import tr
from PIL import Image
import json
from itertools import islice
time.sleep(3)


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


time_sleep = 3
duration = 0.2
for i in range(time_sleep):
    print(i)
    time.sleep(1)


# 读取要检索的数据
search_data = None
with open("temp/jewelry_tobe_search.json",encoding="utf-8") as f:
    search_data = json.load(f)[:5]
# for d in search_data:
#     search_part,engrave_list,prop_list = d
#     print(search_part,engrave_list,prop_list)
# raise

# 找到交易所小图标点击  
# 找到拍卖行，点击
# 找到首饰选项卡，点击
# 找到搜索详情，点击
locate_move_click("resource/auction_icon.png")
locate_move_click("resource/auction.png")
locate_move_click("resource/jew_button.png",confidence=0.8)
locate_move_click("resource/jew_necklace_button.png",confidence=0.8)
time.sleep(0.7)
for item in search_data:
    search_part,engrave_list,prop_list = item
    locate_move_click("resource/advanced_search_button.png",confidence=0.67)
    locate_move_click("resource/auction_search_default_button.png",confidence=0.76)
    
    for prop in engrave_list + prop_list:
        _type,prop_name,prop_value = prop
        print(prop)

        appended = list() # 找到所有【全部】的位置
        res = pyautogui.locateAllOnScreen("resource/advanced_seach_conditions.png",confidence=0.7)
        for i in res:
            flag = True 
            left, top, width, height = i  # 提取位置信息
            target_x = left + width / 2  # 计算目标位置的x坐标
            target_y = top + height / 2  # 计算目标位置的y坐标
            for point in appended:
                x,y = point 
                if distance_2d(x,y,target_x,target_y) < 30 :
                    flag = False
            if flag:
                appended.append([target_x,target_y])
        
        for point in appended[1:]:  # 点开【全部】 # 第一个[全部] 是职业，跳过
            target_x, target_y = point
            keyword_x,keyword_y = target_x + 150, target_y
            min_value_x, min_value_y = target_x + 350, target_y
            max_value_x, max_value_y = target_x + 405, target_y
            print(f"点开的全部，位置为：{target_x},{target_y}")
            # 遍历一个属性，找一个，填一个，然后break掉res就可以了
            # 点开条件
            pyautogui.moveTo(target_x, target_y,duration=duration)  # 将鼠标移动到目标位置
            pyautogui.click(x=target_x, y=target_y, clicks=1, interval=0.0, button='left')
            if _type == "刻印效果":
                res = pyautogui.locateAllOnScreen("resource/advanced_seach_condition_engrave.png",confidence=0.95)
            if _type == "战斗特性":
                res = pyautogui.locateAllOnScreen("resource/advanced_seach_condition_fight.png",confidence=0.95)
            for f in res:
                left, top, width, height = f # 提取位置信息
                _target_x = left + width / 2  # 计算目标位置的x坐标
                _target_y = top + height / 2  # 计算目标位置的y坐标
                print(f"找到的位置在：{target_x},{target_y}")
                pyautogui.moveTo(_target_x, _target_y, duration=duration)  # 将鼠标移动到目标位置
                pyautogui.click(x=_target_x, y=_target_y, clicks=1, interval=0.0, button='left')
                # 模拟填值
                pyautogui.moveTo(keyword_x, keyword_y, duration=duration)  # 将鼠标移动到目标位置
                pyautogui.click(x=keyword_x, y=keyword_y , clicks=1, interval=0.0, button='left')
                pyperclip.copy(prop_name)
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.click(x=1, y=1 , clicks=1, interval=0.0, button='left')
                time.sleep(0.2)
                pyautogui.moveTo(min_value_x, min_value_y, duration=duration)  # 将鼠标移动到目标位置
                pyautogui.click(x=min_value_x, y=min_value_y , clicks=2, interval=0.0, button='left')
                pyperclip.copy(prop_value)
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.moveTo(max_value_x, max_value_y, duration=duration)  # 将鼠标移动到目标位置
                pyautogui.click(x=max_value_x, y=max_value_y , clicks=1, interval=0.0, button='left')
                pyperclip.copy(prop_value)
                pyautogui.hotkey('ctrl', 'v')
                break
            _type,prop_name,prop_value = None,None,None
            break
    locate_move_click("resource/auction_search_button.png",confidence=0.9)
    if search_part == "耳环":
        locate_move_click("resource/jew_earring_button.png",confidence=0.8)
    if search_part == "项链":
        locate_move_click("resource/jew_necklace_button.png",confidence=0.8)
    if search_part == "戒指":
        locate_move_click("resource/jew_ring_button.png",confidence=0.8)
    # 获取游戏窗口的屏幕截图
    screenshot = pyautogui.screenshot()
    # 定义需要识别的区域（根据实际情况进行调整）
    # 根据定义的区域裁剪截图
    # 左、上、右、下
    region = (631, 354, 1463, 794)
    name_region = (650, 354, 800, 794)
    quality_region = (982,354,1100,792)
    price_region = (1370,354,1443,792)


    name_region_file_path = 'temp/name_region_cropped_screenshot.png'
    quality_region_file_path = 'temp/qutality_region_cropped_screenshot.png'
    price_region_file_path = 'temp/price_region_cropped_screenshot.png'
    # 保存裁剪后的截图为临时文件
    cropped_image = screenshot.crop(name_region)
    cropped_image.save(name_region_file_path)
    cropped_image = screenshot.crop(quality_region)
    cropped_image.save(quality_region_file_path)
    cropped_image = screenshot.crop(price_region)
    cropped_image.save(price_region_file_path)

    def read_img(img_file_path):
        image = Image.open(img_file_path).convert("L")
        results = tr.run(image, flag=tr.FLAG_RECT)  #  识别的第一行是空行
        return [str(res[1]).encode("utf-8").decode("utf-8") for res in results if res[-1] > 0.9]
    name_results = read_img(name_region_file_path)
    quality_list = read_img(quality_region_file_path)
    price_list = read_img(price_region_file_path)
    # 把识别name的result转换成能用的数据[(物品名,购买次数),...]
    name_list = list()
    _list = list()
    for item in name_results:
        if len(_list) < 2:
            _list.append(item)
        if len(_list) == 2:
            name_list.append(_list)
            _list = list()
    # 拿到所有物品及品质价格
    for name,quality,price in zip(name_list,quality_list,price_list):
        print(name,quality,price)

