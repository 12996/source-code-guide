# Source Code Guide Templates

默认按以下结构生成中文阅读文档。

## 命名规则

- `00-project-map.md` 固定表示项目地图。
- 从 `01` 开始，统一使用 `<编号>-<父级功能>-and-<当前功能>.md`。
- 编号使用两位数字格式，例如 `01`、`02`、`03`。
- 父级功能只写直接上级对象；第一层递归文档的父级功能使用 `project`。
- 建议继续阅读里的未来文档先使用 `<future-number>` 占位；只有真正创建该文档时，才为它分配下一个实际编号。
- 示例：
  - `01-project-and-agent-loop.md`
  - `02-agent-loop-and-tool-execution.md`
  - `03-tool-execution-and-tool-result-stitching.md`

## `00-project-map.md`

```md
# 项目地图

## 简短介绍
- 项目类型：
- 主要职责：
- 建议最先阅读的功能：

## 功能分组
### <feature-name>
- 它做什么：
- 它对项目整体提供什么：
- 为什么它值得继续下钻：
- 入口证据：
  - `path/to/file.ext:line`
- 置信度：high | medium | low

## 推荐阅读顺序
1. <feature-name>
2. <feature-name>
3. <feature-name>

## Unconfirmed Points
- None.
```

## `NN-<parent>-and-<current>.md` 功能拆解模板

在当前对象仍然存在并列子功能时使用。

```md
# <当前对象> 功能拆解

## 当前阅读位置
- 当前对象：<current-object>
- 当前文档类型：功能拆解
- 上级文档：`docs/source-guides/<project-slug>/<parent-doc>.md`
- 当前进入这一层的原因：
- 建议继续阅读：
  - `<future-number>-<current>-and-<child-a>.md`
  - `<future-number>-<current>-and-<child-b>.md`

## 简短介绍
- 当前对象整体做什么：
- 为什么当前还不能直接讲成一条调用链：

## 上下文关系
- 它在上级对象里的作用：
- 它为下一步哪些子功能提供上下文：

## 并列子功能
### <child-a>
- 它做什么：
- 它为什么是独立子功能而不是同一条链上的一个步骤：
- 它和其他子功能如何衔接：
- 入口证据：
  - `path/to/file.ext:line`
- 下一步为什么值得进入它：
- 置信度：high | medium | low

### <child-b>
- 它做什么：
- 它为什么是独立子功能而不是同一条链上的一个步骤：
- 它和其他子功能如何衔接：
- 入口证据：
  - `path/to/file.ext:line`
- 下一步为什么值得进入它：
- 置信度：high | medium | low

## 下一步阅读建议
- 优先进入哪个子功能：
- 为什么先读它：
- 其余同级子功能：
  - `<future-number>-<current>-and-<child-a>.md`
  - `<future-number>-<current>-and-<child-b>.md`

## Unconfirmed Points
- None.
```

## `NN-<parent>-and-<current>.md` 调用链解释模板

在当前对象已经没有并列子功能，只剩一条主流程时使用。

```md
# <当前对象> 调用链解释

## 当前阅读位置
- 当前对象：<current-object>
- 当前文档类型：调用链解释
- 上级文档：`docs/source-guides/<project-slug>/<parent-doc>.md`
- 当前进入这一层的原因：
- 建议继续阅读：
  - `<future-number>-<current>-and-<stage-a>.md`
  - `<future-number>-<current>-and-<stage-b>.md`

## 简短介绍
- 当前对象整体做什么：
- 为什么它现在可以视为一条主调用链：

## 阅读这条链前先知道
- 起点：
- 终点：
- 关键输入：
- 关键输出：

## 主调用链
- `<stage-a> -> <stage-b>`
  - 来源：`path/to/file.ext:line`
  - 去向：`path/to/file.ext:line`
  - 关系：direct call | indirect call | route dispatch | configuration binding | event trigger | unresolved
  - 这一跳做什么：
  - 它为下一步提供了什么：
  - 置信度：high | medium | low

- `<stage-b> -> <stage-c>`
  - 来源：`path/to/file.ext:line`
  - 去向：`path/to/file.ext:line`
  - 关系：direct call | indirect call | route dispatch | configuration binding | event trigger | unresolved
  - 这一跳做什么：
  - 它为下一步提供了什么：
  - 置信度：high | medium | low

## 阶段说明
### <stage-a>
- 这一阶段负责什么：
- 进入条件：
- 向下一阶段交付什么：
- 关键证据：
  - `path/to/file.ext:line`

### <stage-b>
- 这一阶段负责什么：
- 进入条件：
- 向下一阶段交付什么：
- 关键证据：
  - `path/to/file.ext:line`

## 下一步阅读建议
- 如果要进入具体阶段，先看：
  - `<future-number>-<current>-and-<stage-a>.md`
- 其他值得下钻的阶段：
  - `<future-number>-<current>-and-<stage-b>.md`

## Unconfirmed Points
- None.
```

## `NN-<parent>-and-<current>.md` 代码精读模板

在用户已经选中调用链中的某个阶段、文件或代码区域时使用。

```md
# <当前对象> 代码精读

## 当前阅读位置
- 当前对象：<current-object>
- 当前文档类型：代码精读
- 上级文档：`docs/source-guides/<project-slug>/<parent-doc>.md`
- 当前进入这一层的原因：
- 建议继续阅读：
  - 同级阶段
  - 返回上级调用链

## 粗略总结
- 这段代码负责什么：
- 它在当前调用链里的作用：
- 它为下一步哪个文件、函数或流程做了什么：

## 阅读前先知道
- 必要上下文：
- 输入：
- 输出：

## 带注解的阅读材料
- 文件：`path/to/file.ext`
- 聚焦区域：`path/to/file.ext:line`
- 说明：
- 这段代码如何承接上一步：
- 这段代码如何交给下一步：

## 与上层调用链的映射
- 这段代码属于哪一个阶段：
- 上游调用点：
- 下游影响：
- 读完这段后下一步应该看哪里：

## 持久化选择
- Reading doc only | source edits | both

## Unconfirmed Points
- None.
```
