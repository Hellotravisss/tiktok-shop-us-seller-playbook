# TikTok Shop US Seller Playbook Skill / TikTok美区开店手册

English | 中文

An open-source Codex Skill for creating practical TikTok Shop US seller playbooks, SOPs, checklists, and 30/60/90-day execution plans.

一个开源 Codex Skill，用来生成美国 TikTok Shop 开店手册、运营 SOP、检查清单和 30/60/90 天执行计划。

## What This Skill Does

- Creates step-by-step TikTok Shop US onboarding playbooks
- Expands individual chapters into practical SOPs
- Builds seller document checklists, SKU evaluation sheets, creator outreach trackers, daily operations SOPs, and weekly review tables
- Audits training material for outdated rules, vague advice, missing steps, or risky compliance claims
- Creates listing review, creator outreach, content calendar, and 90-day launch plans
- Adds import-duty, China tariff, HTS code, and landed-cost checks for practical SKU decisions
- Adds compliant content research tooling, including GreenVideo for authorized downloads and script deconstruction
- Generates profit models, 30-day content calendars, creator outreach packs, and daily operations SOPs
- Structures content for Markdown, DOCX, PDF, and Pages-friendly documents

## 它能做什么

- 生成美国 TikTok Shop 新手开店手册
- 把单个章节扩写成手把手 SOP
- 制作开店资料清单、SKU 评估表、达人建联表、每日运营 SOP、每周复盘表
- 审核教程里的过时规则、空泛内容、缺失步骤和合规风险
- 生成商品上架检查、达人建联、内容排期和 90 天启动计划
- 加入进口税费、中美关税、HTS 编码和含税到岸成本核对
- 补充 GreenVideo 等内容素材工具，用于授权下载、素材库整理和脚本拆解
- 生成利润测算、30 天内容日历、达人建联包和每日运营 SOP
- 把内容整理成适合 Markdown、DOCX、PDF、Pages 的结构

## Install

Copy the skill folder into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R skills/tiktok-shop-us-seller-playbook ~/.codex/skills/
```

Then invoke it with:

```text
Use $tiktok-shop-us-seller-playbook to create a Chinese TikTok Shop US launch playbook with onboarding checklist, tariff/profit model, content calendar, creator outreach pack, daily operations SOP, and 30/60/90-day plan.
```

## 安装

把 Skill 文件夹复制到你的 Codex skills 目录：

```bash
mkdir -p ~/.codex/skills
cp -R skills/tiktok-shop-us-seller-playbook ~/.codex/skills/
```

然后这样调用：

```text
Use $tiktok-shop-us-seller-playbook to create a Chinese TikTok Shop US launch playbook with onboarding checklist, tariff/profit model, content calendar, creator outreach pack, daily operations SOP, and 30/60/90-day plan.
```

## Script Outputs / 脚本输出

```bash
python skills/tiktok-shop-us-seller-playbook/scripts/create_playbook_markdown.py --language zh --mode playbook --output playbook.md
python skills/tiktok-shop-us-seller-playbook/scripts/create_playbook_markdown.py --language zh --mode profit --output profit.md
python skills/tiktok-shop-us-seller-playbook/scripts/create_playbook_markdown.py --language zh --mode content-calendar --output content-calendar.md
python skills/tiktok-shop-us-seller-playbook/scripts/create_playbook_markdown.py --language zh --mode creator-pack --output creator-pack.md
python skills/tiktok-shop-us-seller-playbook/scripts/create_playbook_markdown.py --language zh --mode ops-sop --output ops-sop.md
python skills/tiktok-shop-us-seller-playbook/scripts/create_playbook_markdown.py --language zh --mode workbook --output workbook.md
```

## Compliance Boundary

The skill does not provide instructions for VPN/proxy setup, location spoofing, device fingerprint evasion, fake documents, bought/rented shops, account farming, or bypassing platform controls. For rule-sensitive topics, verify the latest TikTok Shop Seller Center and Seller University pages before acting.

## 合规边界

本 Skill 不提供代理/VPN、定位伪装、设备指纹规避、虚假资料、买店租店、账号农场或绕过平台控制的方法。涉及平台规则时，请以 TikTok Shop Seller Center 和 Seller University 当前页面为准。

## License

MIT
