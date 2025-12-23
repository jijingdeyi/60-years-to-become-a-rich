# GitHub Pages 部署说明

## 部署步骤

### 1. 将代码推送到 GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/你的用户名/你的仓库名.git
git push -u origin main
```

### 2. 启用 GitHub Pages

1. 进入你的 GitHub 仓库
2. 点击 **Settings**（设置）
3. 在左侧菜单中找到 **Pages**
4. 在 **Source** 部分，选择：
   - **Source**: `Deploy from a branch`
   - **Branch**: `main` 或 `master`
   - **Folder**: `/ (root)`
5. 点击 **Save**

### 3. 使用 GitHub Actions（推荐）

如果你已经推送了代码，GitHub Actions 会自动部署。你也可以：

1. 进入 **Actions** 标签页
2. 选择 **Deploy to GitHub Pages** 工作流
3. 点击 **Run workflow** 手动触发部署

### 4. 访问你的网站

部署完成后，你的网站地址将是：
```
https://你的用户名.github.io/你的仓库名/
```

## 注意事项

- 首次部署可能需要几分钟时间
- 如果使用自定义域名，需要在仓库根目录添加 `CNAME` 文件
- Markdown 文件会由 GitHub 自动渲染
- `index.html` 是网站的首页

## 文件说明

- `index.html`: 网站首页，包含所有文章的链接
- `.github/workflows/deploy.yml`: GitHub Actions 自动部署配置
- 所有 `.md` 文件: 你的投资笔记，可以直接访问

