"""
AI IoT - AI物联网工具
支持IoT架构设计、设备管理、数据处理
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AIIoTTools:
    """
    AI物联网工具
    支持：架构、设备、数据
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def design_iot_architecture(self, use_case: str, scale: str) -> Dict:
        """设计IoT架构"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请设计{use_case}的IoT架构：

规模：{scale}

请返回JSON格式：
{{
    "architecture": "架构描述",
    "devices": [{{"type": "设备类型", "protocol": "协议", "count": "数量"}}],
    "gateway": "网关方案",
    "cloud": "云平台",
    "data_pipeline": "数据管道",
    "security": "安全方案"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"architecture": content}

    def generate_mqtt_config(self, broker: str, topics: List[str]) -> str:
        """生成MQTT配置"""
        if not self.client:
            return "LLM客户端未配置"

        topics_text = ", ".join(topics)

        prompt = f"""请生成MQTT配置：

Broker：{broker}
Topics：{topics_text}

请生成完整的MQTT客户端配置和代码："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def generate_device_firmware(self, device_type: str, mcu: str) -> str:
        """生成设备固件"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请为{mcu}生成{device_type}设备固件：

要求：
1. 传感器数据采集
2. MQTT通信
3. 低功耗设计
4. OTA更新支持"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def design_data_pipeline(self, data_sources: List[str], requirements: str) -> Dict:
        """设计数据管道"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        sources_text = ", ".join(data_sources)

        prompt = f"""请设计IoT数据管道：

数据源：{sources_text}
需求：{requirements}

请返回JSON格式：
{{
    "ingestion": "数据采集",
    "processing": "数据处理",
    "storage": "数据存储",
    "analytics": "数据分析",
    "visualization": "可视化"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"pipeline": content}

    def generate_edge_computing(self, use_case: str) -> Dict:
        """生成边缘计算方案"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请为{use_case}设计边缘计算方案：

请返回JSON格式：
{{
    "edge_devices": ["边缘设备"],
    "processing_tasks": ["处理任务"],
    "algorithms": ["算法"],
    "sync_strategy": "同步策略",
    "fallback": "降级方案"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"edge": content}

    def generate_home_automation(self, rooms: List[str], devices: List[str]) -> Dict:
        """生成家居自动化"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        rooms_text = ", ".join(rooms)
        devices_text = ", ".join(devices)

        prompt = f"""请设计家居自动化方案：

房间：{rooms_text}
设备：{devices_text}

请返回JSON格式：
{{
    "scenes": [
        {{"name": "场景名", "trigger": "触发条件", "actions": ["动作"]}}
    ],
    "automations": [
        {{"name": "自动化名", "condition": "条件", "action": "动作"}}
    ],
    "energy_saving": ["节能建议"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"home_automation": content}


def create_tools(**kwargs) -> AIIoTTools:
    """创建IoT工具"""
    return AIIoTTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI IoT Tools")
    print()

    # 测试
    arch = tools.design_iot_architecture("智能家居", "中型")
    print(json.dumps(arch, ensure_ascii=False, indent=2))
