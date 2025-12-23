#!/usr/bin/env python3
import os
import json
import re
from pathlib import Path

def scan_directory(root_dir, current_dir='', file_list=None):
    if file_list is None:
        file_list = []
    
    full_path = Path(root_dir) / current_dir if current_dir else Path(root_dir)
    
    for item in full_path.iterdir():
        if item.is_dir():
            # 跳过隐藏目录和特殊目录
            if not item.name.startswith('.') and item.name not in ['node_modules', 'scripts', 'image']:
                scan_directory(root_dir, str(item.relative_to(root_dir)), file_list)
        elif item.suffix == '.md' and item.name != 'README.md':
            relative_path = str(item.relative_to(root_dir)).replace('\\', '/')
            
            # 提取日期和标题
            match = re.search(r'(\d{4}-\d{2}-\d{2})\s*(.+?)\.md$', relative_path)
            date = match.group(1) if match else ''
            title = match.group(2).strip() if match else item.stem
            
            # 提取目录路径
            dir_path = str(item.parent.relative_to(root_dir)).replace('\\', '/')
            category = dir_path if dir_path != '.' else ''
            
            file_list.append({
                'file': relative_path,
                'date': date,
                'title': title,
                'category': category,
                'path': relative_path
            })
    
    return file_list

def main():
    root_dir = Path(__file__).parent.parent
    files = scan_directory(root_dir)
    
    # 按日期排序（最新的在前）
    files.sort(key=lambda x: (x['date'] or '', x['file']), reverse=True)
    
    # 生成 JSON 文件
    output_path = root_dir / 'file-list.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(files, f, ensure_ascii=False, indent=2)
    
    print(f"生成了 {len(files)} 个文件列表到 {output_path}")

if __name__ == '__main__':
    main()

