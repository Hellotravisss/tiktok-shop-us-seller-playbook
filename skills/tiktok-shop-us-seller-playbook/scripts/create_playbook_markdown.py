#!/usr/bin/env python3
"""Generate TikTok Shop US seller playbook, checklist, or launch-plan scaffolds."""

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
    ("Import Duties, China Tariffs, HTS Codes, and Landed Cost", "进口税费、中美关税、HTS 编码和到岸成本"),
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
        "tariff_note": "Tariff snapshot: verify current official sources before final pricing. As of 2026-06-24, duty-free de minimis is suspended globally; old China IEEPA ad valorem tariffs were ended by EO 14389; a temporary Section 122 10% surcharge applies to many imports through July 24, 2026 unless exempt or changed; Section 301 China tariffs still depend on HTS code and exclusions. / 关税快照：最终定价前核对官方来源。截至 2026-06-24，美国全球低值免税已暂停；旧中国 IEEPA 从价附加税已由 EO 14389 终止；许多进口商品在 2026-07-24 前有 Section 122 临时 10% 附加税，除非豁免或变更；Section 301 中国关税仍按 HTS 编码和排除情况判断。",
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
        "tariff_note": "关税快照：最终定价前核对官方来源。截至 2026-06-24，美国全球低值免税已暂停；旧中国 IEEPA 从价附加税已由 EO 14389 终止；许多进口商品在 2026-07-24 前有 Section 122 临时 10% 附加税，除非豁免或变更；Section 301 中国关税仍按 HTS 编码和排除情况判断。",
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
        "tariff_note": "Tariff snapshot: verify current official sources before final pricing. As of 2026-06-24, duty-free de minimis is suspended globally; old China IEEPA ad valorem tariffs were ended by EO 14389; a temporary Section 122 10% surcharge applies to many imports through July 24, 2026 unless exempt or changed; Section 301 China tariffs still depend on HTS code and exclusions.",
    },
}


CHECKLIST_ITEMS = {
    "zh": [
        ("资料准备", "主体、税务、银行、仓库、退货、客服邮箱"),
        ("账号权限", "邮箱、密码管理、两步验证、团队角色"),
        ("店铺设置", "注册、审核、税务、收款、物流、退货地址"),
        ("商品准备", "选品、样品、质检、包装、库存、利润表"),
        ("关税成本", "原产国、10 位 HTSUS、基础税率、Section 301/122/232/AD/CVD、报关行确认"),
        ("上架检查", "类目、标题、图片、卖点、价格、库存、发货承诺"),
        ("内容启动", "账号定位、素材库、脚本、发布节奏、复盘表"),
        ("达人合作", "筛选条件、建联话术、样品状态、佣金、结果复盘"),
        ("日常运营", "订单、客服、退款、评价、健康分、库存预警"),
    ],
    "en": [
        ("Seller documents", "Entity, tax, bank, warehouse, return address, support email"),
        ("Account permissions", "Email, password manager, 2FA, team roles"),
        ("Shop setup", "Registration, review, tax, payout, logistics, return address"),
        ("Product readiness", "Selection, samples, QC, packaging, inventory, margin sheet"),
        ("Tariff and landed cost", "Origin, 10-digit HTSUS, base duty, Section 301/122/232/AD/CVD, broker check"),
        ("Listing review", "Category, title, images, claims, price, stock, shipping promise"),
        ("Content launch", "Positioning, asset library, scripts, posting rhythm, review sheet"),
        ("Creator outreach", "Creator filters, outreach script, samples, commission, review"),
        ("Daily operations", "Orders, service, refunds, reviews, account health, inventory alerts"),
    ],
}


PLAN_PHASES = {
    "zh": [
        ("0-30 天：资料和首批商品跑通", "完成店铺资料、基础设置、5-20 个 SKU 上架、30 条短视频测试。"),
        ("31-60 天：内容和达人放大", "保留有效 SKU，建立达人建联表、寄样 SOP、每周内容复盘。"),
        ("61-90 天：稳定运营和数据优化", "优化转化率、退款率、库存周转、广告预算和客服响应。"),
    ],
    "en": [
        ("Days 0-30: Documents and first SKU loop", "Complete seller setup, basic configuration, 5-20 listings, and 30 short-video tests."),
        ("Days 31-60: Content and creator scale-up", "Keep winning SKUs, build creator outreach, sample SOPs, and weekly content review."),
        ("Days 61-90: Operating rhythm and data optimization", "Improve conversion, refund rate, inventory turnover, ad budget, and customer service response."),
    ],
}


def localized_pair(language: str, zh: str, en: str) -> str:
    if language == "zh":
        return zh
    if language == "en":
        return en
    return f"{en} / {zh}"


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
        mistake_1 = "Do not treat old notes as current platform rules. Verify rule-sensitive details in Seller Center."
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
        mistake_1 = "不要把旧经验当成当前平台规则，规则相关内容以 Seller Center 和官方页面为准。"
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
        mistake_1 = "Do not treat old notes as current platform rules. Verify rule-sensitive details in Seller Center. / 不要把旧经验当成当前平台规则，规则相关内容以 Seller Center 和官方页面为准。"
        mistake_2 = "Do not use fake documents, bought/rented shops, spoofed environments, or bypass methods. / 不要为了速度使用虚假资料、买店租店、伪装环境或绕过平台控制。"
        done_1 = "The key document or action is complete. / 已完成关键资料或动作。"
        done_2 = "The owner and next step are recorded. / 已记录负责人和下一步。"
        done_3 = "The current official requirement has been checked. / 已核对官方后台当前要求。"
        not_started = "Not started / 未开始"

    tariff_section = ""
    if any(key in en for key in ["Product Selection", "Import Duties", "Product Listing"]):
        tariff_section = f"""
### {localized_pair(language, '关税和成本提醒', 'Tariff and Cost Reminder')}

{labels["tariff_note"]}
"""

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
{tariff_section}

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

    body = [
        f"# {doc_title}",
        "",
        f"> {intro}",
        "",
        f"## {boundary_header}",
        "",
        labels["boundary"],
        "",
        f"## {localized_pair(language, '进口税费快照', 'Import Duty Snapshot')}",
        "",
        labels["tariff_note"],
        "",
    ]
    for idx, (en, zh) in enumerate(CHAPTERS, start=1):
        body.append(chapter_block(idx, en, zh, language))
    return "\n".join(body).rstrip() + "\n"


def build_checklist(language: str, title: str | None) -> str:
    labels = LABELS[language]
    doc_title = title or localized_pair(language, "TikTok Shop 美区开店检查清单", "TikTok Shop US Launch Checklist")
    items_zh = CHECKLIST_ITEMS["zh"]
    items_en = CHECKLIST_ITEMS["en"]
    rows = []
    for (zh_area, zh_detail), (en_area, en_detail) in zip(items_zh, items_en):
        rows.append(
            f"| {localized_pair(language, zh_area, en_area)} | {localized_pair(language, zh_detail, en_detail)} |  |  | □ |"
        )
    return "\n".join([
        f"# {doc_title}",
        "",
        f"> {localized_pair(language, '用来确认开店前、上架前、运营前是否准备完整。规则敏感项以 Seller Center 当前页面为准。', 'Use this to verify readiness before setup, listing, and operations. Verify rule-sensitive items in Seller Center.')}",
        "",
        f"## {localized_pair(language, '总检查表', 'Master Checklist')}",
        "",
        f"| {localized_pair(language, '模块', 'Area')} | {labels['item']} | {labels['owner']} | {labels['notes']} | {localized_pair(language, '完成', 'Done')} |",
        "|---|---|---|---|---|",
        *rows,
        "",
        f"## {localized_pair(language, '下一步', 'Next Steps')}",
        "",
        f"1. {localized_pair(language, '先补齐所有未完成资料。', 'Complete every missing document first.')}",
        f"2. {localized_pair(language, '只选择 5-20 个 SKU 做首轮验证。', 'Validate only 5-20 SKUs in the first round.')}",
        f"3. {localized_pair(language, '每个 SKU 上架前补齐原产国、HTS 编码、含税到岸成本和报关行确认。', 'Before listing each SKU, confirm origin, HTS code, landed cost after duties, and broker review.')}",
        f"4. {localized_pair(language, '每天记录订单、客服、库存、内容和达人进度。', 'Track orders, service, inventory, content, and creator progress daily.')}",
    ]) + "\n"


def build_90_day_plan(language: str, title: str | None) -> str:
    doc_title = title or localized_pair(language, "TikTok Shop 美区 90 天启动计划", "TikTok Shop US 90-Day Launch Plan")
    phases = PLAN_PHASES["zh"] if language == "zh" else PLAN_PHASES["en"]
    if language == "bilingual":
        phases = [
            (f"{en_title} / {zh_title}", f"{en_detail} / {zh_detail}")
            for (zh_title, zh_detail), (en_title, en_detail) in zip(PLAN_PHASES["zh"], PLAN_PHASES["en"])
        ]
    parts = [
        f"# {doc_title}",
        "",
        f"> {localized_pair(language, '目标：用 90 天跑通资料、商品、内容、达人、订单和复盘闭环。', 'Goal: use 90 days to complete the document, product, content, creator, order, and review loops.')}",
        "",
    ]
    for title_text, detail in phases:
        parts.extend([
            f"## {title_text}",
            "",
            detail,
            "",
            f"| {localized_pair(language, '周次', 'Week')} | {localized_pair(language, '重点', 'Focus')} | KPI | {localized_pair(language, '停止/调整信号', 'Stop or Adjust Signal')} |",
            "|---|---|---|---|",
            f"| 1 | {localized_pair(language, '资料、规则和关税核对', 'Documents, policy, and tariff check')} | {localized_pair(language, '资料完成率、HTS 完成率', 'Document completion, HTS completion')} | {localized_pair(language, '审核资料不完整或含税毛利不成立', 'Incomplete review documents or margin fails after duties')} |",
            f"| 2 | {localized_pair(language, '首批 SKU 和素材', 'First SKUs and assets')} | {localized_pair(language, 'SKU 数、素材数', 'SKU count, asset count')} | {localized_pair(language, '利润或合规不成立', 'Margin or compliance fails')} |",
            f"| 3-4 | {localized_pair(language, '上架和内容测试', 'Listings and content tests')} | {localized_pair(language, '播放、点击、加购', 'Views, clicks, add-to-cart')} | {localized_pair(language, '无点击或高退款风险', 'No clicks or high refund risk')} |",
            "",
        ])
    return "\n".join(parts).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="tiktok-shop-us-playbook.md")
    parser.add_argument("--language", choices=["bilingual", "zh", "en"], default="bilingual")
    parser.add_argument("--mode", choices=["playbook", "checklist", "90-day"], default="playbook")
    parser.add_argument("--title", default=None)
    args = parser.parse_args()
    builders = {
        "playbook": build_markdown,
        "checklist": build_checklist,
        "90-day": build_90_day_plan,
    }
    Path(args.output).write_text(builders[args.mode](args.language, args.title), encoding="utf-8")


if __name__ == "__main__":
    main()
