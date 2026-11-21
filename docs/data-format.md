# 记录格式

作业过程记录以 id、task、goal、revision、kind、help、independent_check 描述任务版本、材料类型、帮助和独立检查状态。independent_check 可为 passed、pending 或 missing。

记录以 UTF-8 JSON 保存，顶层包含 dataset 和 records。每条记录的 id 在文件中唯一。`fixtures/records.json` 中的例子用于说明输入字段和状态取值。
