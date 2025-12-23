const fs = require('fs');
const path = require('path');

// 递归扫描目录，获取所有 .md 文件
function scanDirectory(dir, baseDir = '', fileList = []) {
    const fullPath = path.join(dir, baseDir);
    const items = fs.readdirSync(fullPath);

    items.forEach(item => {
        const itemPath = path.join(fullPath, item);
        const relativePath = path.join(baseDir, item).replace(/\\/g, '/');
        const stat = fs.statSync(itemPath);

        if (stat.isDirectory()) {
            // 跳过 .git, node_modules 等目录
            if (!item.startsWith('.') && item !== 'node_modules' && item !== 'scripts') {
                scanDirectory(dir, relativePath, fileList);
            }
        } else if (item.endsWith('.md') && item !== 'README.md') {
            // 提取日期和标题
            const match = relativePath.match(/(\d{4}-\d{2}-\d{2})\s*(.+?)\.md$/);
            const date = match ? match[1] : '';
            const title = match ? match[2].trim() : item.replace('.md', '');
            
            // 提取目录路径
            const dirPath = path.dirname(relativePath).replace(/\\/g, '/');
            const category = dirPath !== '.' ? dirPath : '';

            fileList.push({
                file: relativePath,
                date: date,
                title: title,
                category: category,
                path: relativePath
            });
        }
    });

    return fileList;
}

// 主函数
function generateFileList() {
    const rootDir = path.join(__dirname, '..');
    const files = scanDirectory(rootDir);
    
    // 按日期排序（最新的在前）
    files.sort((a, b) => {
        if (a.date && b.date) {
            return b.date.localeCompare(a.date);
        }
        return a.file.localeCompare(b.file);
    });

    // 生成 JSON 文件
    const outputPath = path.join(rootDir, 'file-list.json');
    fs.writeFileSync(outputPath, JSON.stringify(files, null, 2), 'utf8');
    
    console.log(`生成了 ${files.length} 个文件列表到 ${outputPath}`);
}

generateFileList();

