<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [项目 Agent 规则](#%E9%A1%B9%E7%9B%AE-agent-%E8%A7%84%E5%88%99)
  - [提交前检查](#%E6%8F%90%E4%BA%A4%E5%89%8D%E6%A3%80%E6%9F%A5)
  - [提交范围](#%E6%8F%90%E4%BA%A4%E8%8C%83%E5%9B%B4)
  - [分支与合并](#%E5%88%86%E6%94%AF%E4%B8%8E%E5%90%88%E5%B9%B6)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# 项目 Agent 规则

## 提交前检查

每次创建 git commit 之前，必须在当前仓库根目录执行以下检查，并在提交前确认结果：

1. 本次变更涉及的 Python 文件 lint

   ```bash
   git diff --name-only --cached -- '*.py' | xargs -r ruff check
   ```

   如果本次提交没有 Python 文件变更，必须在提交说明中记录 Python lint 不适用。

2. doctoc 当前目录

   ```bash
   doctoc .
   ```

   运行后必须检查 `git diff`，确认 doctoc 产生的目录更新是否符合预期。

## 提交范围

- 不提交 `docs/ai-changes-*` 文件。
- 不提交本地编辑器、缓存、运行日志等已经被 `.gitignore` 忽略的文件。

## 分支与合并

- 每次代码提交都必须创建新的工作分支，不直接在 `main` 上提交后推送。
- 推送代码时只推送当前工作分支，并创建 Pull Request。
- PR 合并必须等待用户明确同意后再执行。
- 禁止未经用户确认直接合并 PR 或直接推送 `main`。
