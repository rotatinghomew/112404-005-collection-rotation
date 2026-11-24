# 馆藏作品轮换中的展期、光照与观众覆盖

本项目保存视觉艺术机构日常业务分析使用的合成演练资料，样例不代表真实机构、作品、交易或研究结论。

## 资料

- `works.csv`：作品及媒材条件。字段为 `work_id, medium, max_display_days, rest_days, theme_id, replacement_group`。
- `environment.csv`：展厅环境读数及设备状态，缺测保留为空值。字段为 `reading_id, gallery_id, observed_at, lux_hours, device_state, calibration_date, source`。
- `rotation_windows.csv`：安装、开放、撤展和休整日期。字段为 `work_id, gallery_id, install_date, open_date, close_date, remove_date, state`。
- `interpretation_sets.csv`：展览主题及替代关系，未给出完整性评分。字段为 `theme_id, required_work, alternative_work, relationship, review_state`。

记录之间通过 `*_id`、`*_key` 或 `*_ref` 字段关联。日期采用 ISO 格式；空值表示来源未提供该事实，不代表数值为零。不同来源的统计范围和状态以 `docs/data-contract.md` 为准。样例中保留了待确认、取消、缺失和版本变化等原始情况，不包含预先计算的分析结论。

## 运行

需要 Python 3.11 或更高版本，无第三方依赖。运行 `python3 -m unittest discover -s tests -v` 可检查资料编码、字段和记录结构。
