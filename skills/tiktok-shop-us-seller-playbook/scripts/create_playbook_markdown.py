#!/usr/bin/env python3
"""Generate a TikTok Shop US seller playbook scaffold."""

from __future__ import annotations

import argparse
from pathlib import Path


CHAPTERS = [
    ("How to Use This Playbook and the Full Roadmap", "使用方法和完整路线图"),
    ("TikTok Shop US Business Model, Roles, and Beginner Mistakes", "美国 TikTok Shop 模式、角色和新手误区"),
    ("Business Entity, Tax, Bank, Warehouse, and Return Address Checklist", "主体、税务、银行、仓库、退货地址资料清单"),
    ("Phone, Computer, Email, Account Permissions, and Work Environment", "手机、电脑、邮箱、账号权限和工作环境"),
    ("Shop Registration, Review, and Basic Seller Center Setup", "店铺注册、审核、后台基础设置"),
    ("Product Selection: Demand, Content Fit, Compliance, Profit, Supply Chain", "选品框架：需求、内容表现、合规、利润、供应链"),
    ("Supply Chain, Samples, QC, Packaging, and Inventory", "供应链、样品、质检、包装和库存"),
    ("Product Listing: Category, Title, Images, Selling Points, Price, Stock", "商品上架：类目、标题、图片、卖点、价格、库存"),
    ("Logistics, Fulfillment, Returns, Customer Service, and Reviews", "物流、履约、退货、客服和评价"),
    ("TikTok Account Positioning and Content Asset System", "TikTok 账号定位和内容素材系统"),
    ("Short Video Scripts, Shooting, Editing, Publishing, and Review", "短视频脚本、拍摄、剪辑、发布和复盘"),
    ("Creator/Affiliate Outreach, Samples, Commission, and Review", "Creator/Affiliate 达人建联、寄样、佣金和复盘"),
    ("Ads Basics: Budget, Creatives, Objectives, Data Decisions", "广告投放入门：预算、素材、目标、数据判断"),
    ("Livestream Selling Prep: Product Mix, Host Flow, Scripts, Review", "直播带货准备：货盘、场控、话术、复盘"),
    ("Daily and Weekly Operations SOP", "每日/每周运营 SOP"),
    ("Data Dashboard: Traffic, Clicks, Add-to-Cart, Conversion, Profit", "数据看板：流量、点击、加购、转化、利润"),
    ("Risk Control: Policy, Account Health, Violations, Stockouts, Bad Reviews", "风险控制：政策、健康分、违规、断货、差评"),
    ("30/60/90-Day Execution Plan", "30/60/90 天执行计划"),
    ("Workbook and Templates", "实操工作簿和模板"),
]


LABELS = {
    "bilingual": {
        "title": "TikTok Shop US Seller Playbook / 美国 TikTok Shop 从 0 到开店运营完整实操教程",
        "boundary": "This playbook is for compliant setup, operations, product selection, content, creators, ads, livestreams, customer service, logistics, and review. It does not provide VPN/proxy setup, location spoofing, device fingerprint evasion, fake documents, bought/rented shops, or bypass methods. / 本手册用于合规开店、运营、选品、内容、达人、广告、直播、客服、物流和复盘。不提供代理/VPN、定位伪装、设备指纹规避、虚假资料、买店租店或绕过平台控制的方法。",
        "objective": "Objective / 本章目标",
        "prepare": "What to Prepare / 要准备什么",
        "steps": "Step-by-Step / 一步一步怎么做",
        "mistakes": "Common Mistakes / 常见错误",
        "done": "Done Criteria / 本章完成标准",
        "item": "Item / 项目",
        "owner": "Owner / 负责人",
        "file": "File or Link / 文件或入口",
        "status": "Status / 状态",
        "notes": "Notes / 备注",
    },
    "zh": {
        "title": "美国 TikTok Shop 从 0 到开店运营完整实操教程",
        "boundary": "本手册用于合规开店、运营、选品、内容、达人、广告、直播、客服、物流和复盘。不提供代理/VPN、定位伪装、设备指纹规避、虚假资料、买店租店或绕过平台控制的方法。",
        "objective": "本章目标",
        "prepare": "要准备什么",
        "steps": "一步一步怎么做",
        "mistakes": "常见错误",
        "done": "本章完成标准",
        "item": "项目",
        "owner": "负责人",
        "file": "文件或入口",
        "status": "状态",
        "notes": "备注",
    },
    "en": {
        "title": "TikTok Shop US Seller Playbook",
        "boundary": "This playbook is for compliant setup, operations, product selection, content, creators, ads, livestreams, customer service, logistics, and review. It does not provide VPN/proxy setup, location spoofing, device fingerprint evasion, fake documents, bought/rented shops, or bypass methods.",
        "objective": "Objective",
        "prepare": "What to Prepare",
        "steps": "Step-by-Step",
        "mistakes": "Common Mistakes",
        "done": "Done Criteria",
        "item": "Item",
        "owner": "Owner",
        "file": "File or Link",
        "status": "Status",
        "notes": "Notes",
    },
}


def chapter_title(index: int, en: str, zh: str, language: str) -> str:
    if language == "zh":
        return f"第 {index} 章 {zh}"
    if language == "en":
        return f"Chapter {index}: {en}"
    return f"Chapter {index} / 第 {index} 章: {en} / {zh}"


def chapter_block(index: int, en: str, zh: str, language: str) -> str:
    labels = LABELS[language]
    if language == "en":
        objective = "Describe the concrete outcome the reader should complete after this chapter."
        step_1 = "Write the first action clearly."
        step_2 = "Write the second action clearly."
        step_3 = "Write how to verify completion."
        mistake_1 = "Do not treat old course notes as current platform rules. Verify rule-sensitive details in Seller Center."
        mistake_2 = "Do not use fake documents, bought/rented shops, spoofed environments, or bypass methods."
        done_1 = "The key document or action is complete."
        done_2 = "The owner and next step are recorded."
        done_3 = "The current official requirement has been checked."
        not_started = "Not started"
    elif language == "zh":
        objective = "说明本章读完后要完成的具体结果。"
        step_1 = "写清楚第一步。"
        step_2 = "写清楚第二步。"
        step_3 = "写清楚完成后的检查方式。"
        mistake_1 = "不要把课程经验当成当前平台规则，规则相关内容以 Seller Center 和官方页面为准。"
        mistake_2 = "不要为了速度使用虚假资料、买店租店、伪装环境或绕过平台控制。"
        done_1 = "已完成关键资料或动作。"
        done_2 = "已记录负责人和下一步。"
        done_3 = "已核对官方后台当前要求。"
        not_started = "未开始"
    else:
        objective = "Describe the concrete outcome the reader should complete after this chapter. / 说明本章读完后要完成的具体结果。"
        step_1 = "Write the first action clearly. / 写清楚第一步。"
        step_2 = "Write the second action clearly. / 写清楚第二步。"
        step_3 = "Write how to verify completion. / 写清楚完成后的检查方式。"
        mistake_1 = "Do not treat old course notes as current platform rules. Verify rule-sensitive details in Seller Center. / 不要把课程经验当成当前平台规则，规则相关内容以 Seller Center 和官方页面为准。"
        mistake_2 = "Do not use fake documents, bought/rented shops, spoofed environments, or bypass methods. / 不要为了速度使用虚假资料、买店租店、伪装环境或绕过平台控制。"
        done_1 = "The key document or action is complete. / 已完成关键资料或动作。"
        done_2 = "The owner and next step are recorded. / 已记录负责人和下一步。"
        done_3 = "The current official requirement has been checked. / 已核对官方后台当前要求。"
        not_started = "Not started / 未开始"

    return f"""## {chapter_title(index, en, zh, language)}

### {labels["objective"]}

{objective}

### {labels["prepare"]}

| {labels["item"]} | {labels["owner"]} | {labels["file"]} | {labels["status"]} | {labels["notes"]} |
|---|---|---|---|---|
|  |  |  | {not_started} |  |

### {labels["steps"]}

1. {step_1}
2. {step_2}
3. {step_3}

### {labels["mistakes"]}

- {mistake_1}
- {mistake_2}

### {labels["done"]}

- [ ] {done_1}
- [ ] {done_2}
- [ ] {done_3}
"""


def build_markdown(language: str, title: str | None) -> str:
    labels = LABELS[language]
    doc_title = title or labels["title"]
    if language == "en":
        intro = "Original training template. Verify rule-sensitive details against the current TikTok Shop Seller Center and Seller University pages."
        boundary_header = "Compliance Boundary"
    elif language == "zh":
        intro = "原创中文实操手册模板。规则敏感内容以 TikTok Shop Seller Center 和 Seller University 当前页面为准。"
        boundary_header = "使用边界"
    else:
        intro = "Original bilingual training template. Verify rule-sensitive details against the current TikTok Shop Seller Center and Seller University pages. / 原创双语实操手册模板。规则敏感内容以 TikTok Shop Seller Center 和 Seller University 当前页面为准。"
        boundary_header = "Compliance Boundary / 使用边界"

    body = [f"# {doc_title}", "", f"> {intro}", "", f"## {boundary_header}", "", labels["boundary"], ""]
    for idx, (en, zh) in enumerate(CHAPTERS):
        body.append(chapter_block(idx, en, zh, language))
    return "\n".join(body).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="tiktok-shop-us-playbook.md")
    parser.add_argument("--language", choices=["bilingual", "zh", "en"], default="bilingual")
    parser.add_argument("--title", default=None)
    args = parser.parse_args()
    Path(args.output).write_text(build_markdown(args.language, args.title), encoding="utf-8")


if __name__ == "__main__":
    main()
