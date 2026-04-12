# Source Code Guide Language Constraint Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** 为 `source-code-guide` 增加默认全程中文约束，并统一仓库文档为中文记录。

**Architecture:** 通过修改 skill 主规则、输出模板、UI 元数据和仓库 README 四类入口，将“对用户沟通使用中文、生成文档使用中文、仓库说明使用中文”固化为默认行为。保留在用户明确要求其他语言时可切换的余地，避免与上层用户指令冲突。

**Tech Stack:** Markdown, YAML

---

### Task 1: 记录语言约束规则

**Files:**
- Modify: `SKILL.md`

**Step 1: 明确默认语言规则**

在核心规则中补充以下约束：
- 对用户的说明、提问、总结默认使用中文
- 生成的阅读文档默认使用中文
- 用户明确要求其他语言时再切换

**Step 2: 调整工作流描述**

将文档规则、导航块、最终注释步骤中的描述改为中文，减少执行时回落到英文的概率。

### Task 2: 调整模板输出语言

**Files:**
- Modify: `references/templates.md`

**Step 1: 将模板标题和字段改为中文**

把项目地图模板，以及递归节点里的功能拆解、调用链解释、代码精读模板中的标题和字段名统一改成中文。

**Step 2: 保留结构不变**

仅做语言层改动，不改变模板的产物结构和证据要求。

### Task 3: 调整入口元数据

**Files:**
- Modify: `agents/openai.yaml`

**Step 1: 改为中文描述**

将 `display_name`、`short_description`、`default_prompt` 调整为中文，引导调用入口也默认使用中文。

### Task 4: 统一仓库说明文档

**Files:**
- Modify: `README.md`
- Modify: `README.zh-CN.md`

**Step 1: 修复中文 README**

重写乱码内容，确保文件编码和内容都正常。

**Step 2: 统一 README 表述**

将 README 内容改为中文优先说明，明确该 skill 默认使用中文记录分析文档。

### Task 5: 校验结果

**Files:**
- Verify: `SKILL.md`
- Verify: `references/templates.md`
- Verify: `agents/openai.yaml`
- Verify: `README.md`
- Verify: `README.zh-CN.md`

**Step 1: 逐文件检查**

确认关键入口都已出现中文约束。

**Step 2: 检查乱码与一致性**

确认 README 不再乱码，且术语和默认行为一致。
