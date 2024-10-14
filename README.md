# 数字比较大小

基于OCR技术来识别屏幕上的数字比较大小，并使用鼠标移动绘制比较结果

## 环境要求

- Python 3.7+
- NumPy
- pyautogui
- [CnOcr](https://github.com/SvenVincent/cnocr)

## 安装步骤

1. 克隆此仓库或下载源代码

2. 安装所需的Python包：

   ```
   pip install pyautogui numpy cnocr
   ```
   或者
   ```
   pip install -r requirements.txt
   ```
   > 本人安装CnOcr时还需要安装C++环境才可以安装
   > 
   > 国内可以加上`-i https://pypi.doubanio.com/simple`参数加速下载

## 使用说明

1. 先运行脚本获取位置：
   ```
   python mousePosition.py
   ```
   需要获取左边数字和右边数字的左上角和右下角坐标
   ```
   pyautogui.screenshot('left.png',region=(左上角X坐标,左上角Y坐标,75,75))#75，75为图片宽度
   ```
   可根据需要更改left（形状：<）和right（形状：>）函数坐标位置
   <hr>
   开始运行
   
   ```
   python demo.py
   ```
2. 运行时要在比谁快闪现完进行运行
   
3. 结束最后会因无法转换数字报错结束运行
