# 合成资料约定

资料用于本地业务流程演练，字段仅记录事实来源，不预先裁定业务结果。

- `works.csv`：作品及媒材条件。字段为 `work_id, medium, max_display_days, rest_days, theme_id, replacement_group`。
- `environment.csv`：展厅环境读数及设备状态，缺测保留为空值。字段为 `reading_id, gallery_id, observed_at, lux_hours, device_state, calibration_date, source`。
- `rotation_windows.csv`：安装、开放、撤展和休整日期。字段为 `work_id, gallery_id, install_date, open_date, close_date, remove_date, state`。
- `interpretation_sets.csv`：展览主题及替代关系，未给出完整性评分。字段为 `theme_id, required_work, alternative_work, relationship, review_state`。

空字段表示事实尚未提供，`pending`、`review`、`hold` 等状态表示来源记录尚未形成最终确认。不同来源以事件日期或有效期表达的时间含义不相同，调用方应结合表名和字段解释；不能仅因编号相同就假定两条记录可合并。金额以资料中记载的名义单位表示，没有统一换算或预先扣除退款。
