# Source Code Guide

[English Version](./README.md)

`source-code-guide` 是一个用于分阶段阅读陌生项目源码的 Codex skill，不鼓励一开始就直接钻进零散代码。

它主要帮助 agent：

- 先梳理项目的主要功能分组
- 追踪某个功能的主调用链
- 在逐层下钻时保持分支级阅读上下文
- 在需要精读时先生成阅读文档，再决定是否把注释写回源码

## 产出内容

这个 skill 会把阅读材料写到：

```text
docs/source-guides/<project-slug>/
  00-project-map.md
  01-feature-<feature-name>.md
  02-feature-<feature-name>-subchain.md
  03-feature-<feature-name>-code-<topic>.md
```

## 关键规则

- 先给证据，再描述架构。
- 已确认的关键调用点必须带 `path:line`。
- 行号无法确认时必须写 `unlocated`，不能猜。
- 不确定的结论要放进 `Unconfirmed Points`。
- 写回源码注释前必须先询问用户。

## 仓库结构

- `SKILL.md` - skill 的核心流程和硬规则
- `references/templates.md` - 生成阅读文档时使用的模板
- `scripts/collect_source_map.py` - 提取稳定 `path:line` 命中的辅助脚本
- `agents/openai.yaml` - UI 侧元数据

## 快速开始

把这个目录放进你的 Codex skills 目录，然后在你想按“功能地图 -> 分支导航 -> 精读代码”方式理解一个仓库时调用它。

示例意图：

- “帮我快速看懂这个仓库的主要功能。”
- “给我登录功能的关键调用链。”
- “我想重点精读 token 校验这一段代码。”

## 辅助脚本

这个辅助脚本可以在单个文件中查找字面文本，并输出稳定的 `path:line` 命中结果：

```bash
python scripts/collect_source_map.py --file ./SKILL.md --find "## Core Rules"
```
