# 🌐 AI IoT

AI物联网工具，支持IoT架构设计、设备管理、数据处理。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 🏗️ IoT架构设计
- 📡 MQTT配置生成
- 💻 设备固件生成
- 📊 数据管道设计
- 🖥️ 边缘计算方案
- 🏠 家居自动化

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_iot import create_tools

tools = create_tools()

# IoT架构
arch = tools.design_iot_architecture("智能家居", "中型")

# MQTT配置
mqtt = tools.generate_mqtt_config("broker.example.com", ["sensor/data", "device/status"])

# 设备固件
firmware = tools.generate_device_firmware("温度传感器", "ESP32")

# 数据管道
pipeline = tools.design_data_pipeline(["传感器", "摄像头"], "实时处理")

# 边缘计算
edge = tools.generate_edge_computing("视频分析")

# 家居自动化
home = tools.generate_home_automation(["客厅", "卧室"], ["灯", "空调"])
```

## 📁 项目结构

```
ai-iot/
├── tools.py       # IoT工具核心
└── README.md
```

## 📄 许可证

MIT License
