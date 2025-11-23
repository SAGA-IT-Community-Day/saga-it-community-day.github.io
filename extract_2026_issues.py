#!/usr/bin/env python3
import subprocess
import json
from datetime import datetime

project_key = "JAWSUGSAGA_TEMP"
issues_2026 = []

# 課題一覧を取得（ページネーション対応）
page = 1
while True:
    # Backlog APIを呼び出して課題を取得
    # 注: 実際のBacklog APIツールの呼び出し方法に応じて調整が必要
    print(f"ページ {page} を取得中...")
    
    # ここでは仮の実装として、課題詳細を個別に取得する必要があることを示す
    break

print(f"\n2026年に期限が設定されている課題: {len(issues_2026)}件")
for issue in issues_2026:
    print(f"- {issue['issueKey']}: {issue['summary']} (期限: {issue['dueDate']})")
