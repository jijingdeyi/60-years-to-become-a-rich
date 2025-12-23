# 60年投资笔记

个人投资思考与策略记录网站

## 功能特性

- 📚 自动扫描所有 Markdown 文件
- 📁 支持多级目录结构
- 📱 响应式设计，支持移动端
- 🎨 电子书式布局（左侧目录，右侧内容）
- ✨ 自动渲染 Markdown 和代码高亮

## 文件结构

- `index.html` - 主页面
- `file-list.json` - 文件列表（自动生成）
- `scripts/generate-file-list.py` - 文件列表生成脚本

## 使用方法

### 方法一：使用 GitHub Actions（推荐）

当你推送代码到 GitHub 时，GitHub Actions 会自动运行脚本生成 `file-list.json`。

### 方法二：本地生成文件列表

如果你在本地添加了新文件，可以运行以下命令生成文件列表：

```bash
python scripts/generate-file-list.py
```

或者使用 Node.js 版本：

```bash
node scripts/generate-file-list.js
```

然后将生成的 `file-list.json` 提交到仓库。

## 添加新文章

1. 在仓库中添加新的 `.md` 文件
2. 文件命名格式：`YYYY-MM-DD 标题.md`（日期可选）
3. 如果放在子目录中，会自动识别目录结构
4. 运行生成脚本或等待 GitHub Actions 自动生成
5. 推送代码到 GitHub

## 部署

### GitHub Pages 部署

1. 进入仓库 Settings → Pages
2. Source 选择：`Deploy from a branch`
3. Branch 选择：`main` 或 `master`
4. Folder 选择：`/ (root)`
5. 保存后等待几分钟，网站即可访问

访问地址：`https://你的用户名.github.io/仓库名/`
