# Recursive Numbered Source Guide Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** 将 `source-code-guide` 从固定 `00/01/02/03` 语义改为递归编号式源码导读流程，并把新的命名规则、切换标准和模板记录到仓库文档中。

**Architecture:** 保留 `00-project-map.md` 作为项目级入口，从 `01` 开始改为递归下钻节点。节点是否继续做“功能拆解”、切换到“调用链解释”，还是进入“代码精读”，不再由编号决定，而由当前对象是否仍存在并列子功能来决定。所有递归节点统一采用 `<编号>-<父级功能>-and-<当前功能>.md` 的命名格式，避免文件名不断拼接完整祖先链。

**Tech Stack:** Markdown, YAML

---

### Task 1: 记录递归编号工作流

**Files:**
- Modify: `SKILL.md`

**Step 1: 重写工作流**

将固定的 `01-feature-*`、`02-feature-*`、`03-feature-*` 阶段改为：
- `00-project-map.md` 固定表示项目地图
- `01+` 表示递归下钻节点
- 节点类型由“功能拆解 / 调用链解释 / 代码精读”三类组成

**Step 2: 写清切换标准**

明确以下判断规则：
- 当前对象仍有并列子功能：继续生成下一层功能拆解文档
- 当前对象没有并列子功能，只剩一条主流程：切换为调用链解释文档
- 用户继续点入调用链中的具体阶段或代码段：进入代码精读文档

**Step 3: 写清命名规则**

明确 `01+` 文档统一使用 `<编号>-<父级功能>-and-<当前功能>.md` 的命名格式，并说明父级功能只写直接上级对象，不展开完整祖先链。

### Task 2: 更新模板

**Files:**
- Modify: `references/templates.md`

**Step 1: 保留项目地图模板**

继续保留 `00-project-map.md` 模板，用于项目级功能入口。

**Step 2: 改为三类递归节点模板**

新增或重写以下模板：
- `NN-<parent>-and-<current>.md` 功能拆解模板
- `NN-<parent>-and-<current>.md` 调用链解释模板
- `NN-<parent>-and-<current>.md` 代码精读模板

**Step 3: 统一导航字段**

让所有递归节点模板都包含：
- 当前对象
- 当前文档类型
- 上级文档
- 为什么当前进入这一层
- 下一步阅读目标

### Task 3: 更新仓库说明

**Files:**
- Modify: `README.md`
- Modify: `README.zh-CN.md`
- Modify: `agents/openai.yaml`

**Step 1: 更新 README**

将 README 中的产物目录、工作流和使用示例改为递归编号式说明。

**Step 2: 更新入口提示**

将 `agents/openai.yaml` 中的 `short_description` 和 `default_prompt` 改为递归编号式流程描述，避免 UI 提示继续引用旧的固定四阶段语义。

### Task 4: 验证新规则

**Files:**
- Verify: `SKILL.md`
- Verify: `references/templates.md`
- Verify: `README.md`
- Verify: `README.zh-CN.md`
- Verify: `agents/openai.yaml`

**Step 1: 场景验证**

至少覆盖三类场景：
- 选中的对象仍有并列子功能，应继续生成功能拆解文档
- 选中的对象只剩一条主链，应切换到调用链解释文档
- 选中了调用链中的某一段，应进入代码精读文档

**Step 2: 关键字段检查**

确认所有入口都不再把 `01/02/03` 绑定死为固定含义，并且命名规则统一为 `<编号>-<父级功能>-and-<当前功能>.md`。
