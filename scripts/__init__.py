import json
import os
from datetime import datetime

# 假设 latest_data 是你要归档的最新数据列表
# latest_data = [...] 

# 根据当前日期动态生成当月的文件名，例如: archive-2026-03.json
current_month = datetime.now().strftime("%Y-%m")
archive_filename = f"data/archive-{current_month}.json"

# 读取当月归档文件（如果存在）
if os.path.exists(archive_filename):
    with open(archive_filename, 'r', encoding='utf-8') as f:
        archive_data = json.load(f)
else:
    archive_data = []

# 将新数据追加进去
archive_data.extend(latest_data)

# 覆盖写入当月归档文件
with open(archive_filename, 'w', encoding='utf-8') as f:
    json.dump(archive_data, f, ensure_ascii=False, indent=2)
