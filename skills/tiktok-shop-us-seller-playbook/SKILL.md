---
name: tiktok-shop-us-seller-playbook
description: Create, expand, audit, or redesign English/Chinese TikTok Shop US seller playbooks, SOPs, checklists, worksheets, and training documents. Use for requests about US TikTok Shop onboarding, seller document preparation, shop setup, import duties/tariffs, landed cost, China-US tariff exposure, content research tools such as GreenVideo, product listing, content calendars, creator outreach, ads, livestream prep, customer service, logistics, analytics, account health, or 30/60/90-day execution plans. Also use when the user asks for a beginner-friendly Chinese TikTok美区开店手册, TikTok小店运营SOP, or a step-by-step checklist.
---

# TikTok Shop US Seller Playbook

## Core Rule

Create original, practical training material in English, Chinese, or bilingual English/Chinese. Use the user's goals, notes, and business context to infer structure, gaps, pain points, and workflow order.

输出英文、中文或中英双语的原创实操内容。根据用户的目标、笔记和业务背景，判断结构、缺口、痛点和流程顺序。

Do not provide instructions for proxy/VPN setup, traffic tunneling, location spoofing, device fingerprint evasion, fake identity documents, bought/rented shops, account farming, or bypassing platform controls. Redirect those requests to compliant alternatives: authorized local team members, role-based permissions, real seller documents, official Seller Center guidance, and legitimate business operations.

不要提供代理/VPN、流量隧道、定位伪装、设备指纹规避、虚假身份资料、买店租店、账号农场或绕过平台控制的方法。遇到这类请求时，转向合规替代方案：授权本地团队、角色权限、真实主体资料、官方 Seller Center 指引和合法经营流程。

## Workflow

1. Identify the deliverable / 确认交付物:
   - diagnostic audit / 开店条件诊断
   - full beginner playbook / 完整新手手册
   - chapter expansion / 单章扩写
   - SOP/checklist pack / SOP 和清单包
   - product listing review / 商品上架检查
   - content or creator plan / 内容或达人计划
   - document redesign for Markdown/DOCX/PDF/Pages / 文档重排版
   - official-policy audit / 官方规则审校
   - 30/60/90-day execution plan / 30/60/90 天执行计划
2. Load only the needed references / 只读取需要的参考:
   - `references/playbook-structure.md` for chapter order and expected depth
   - `references/compliance-boundaries.md` for what to include or avoid
   - `references/cross-border-rules.md` for current import-duty, de minimis, tariff, and landed-cost guidance
   - `references/content-tools.md` for compliant content research, GreenVideo, and素材库 workflow
   - `references/official-sources.md` for public source links and verification reminders
   - `references/templates.md` for reusable bilingual tables and worksheets
3. Ask or infer the output language:
   - Default to Chinese for China-based operator training and SkillHub-style usage.
   - Default to bilingual English/Chinese for public GitHub-ready material.
   - Default to English for global contributor docs unless the user asks for Chinese.
4. Make the result operational:
   - Start with a short diagnosis: current stage, missing inputs, next three actions.
   - Each chapter should include Objective/本章目标, Preparation/要准备什么, Steps/具体步骤, Common mistakes/常见错误, Done criteria/完成标准.
   - Use tables for seller documents, SKU evaluation, landed cost/tariff checks, listing review, creator outreach, customer service, order handling, and weekly review.
   - Mark rule-sensitive claims with “Verify in Seller Center / 以官方后台为准”.
5. If producing a file, prefer Markdown first for content review, then DOCX/PDF/Pages-friendly formatting if requested.

## Output Recipes

- **开店诊断**: return `现状判断`, `缺失资料`, `风险提醒`, `下一步 7 天动作`.
- **完整手册**: use the chapter order in `references/playbook-structure.md`; keep every chapter actionable.
- **SOP 清单**: use checkbox tables; assign owner, input, output, frequency, and done criteria.
- **商品上架检查**: cover category, title, images, claims, price, inventory, shipping, return policy, and compliance.
- **关税/成本检查**: identify country of origin, 10-digit HTS code, base duty, Section 301/232/122/AD/CVD exposure, de minimis status, broker confirmation, and landed-cost decision.
- **内容达人计划**: produce hooks, video angles, creator filters, outreach templates, sample tracking, and weekly review metrics.
- **素材工具清单**: include GreenVideo and similar tools only for authorized downloads, private research, script deconstruction, and internal asset organization; do not encourage reposting or copyright misuse.
- **90 天计划**: split into 0-30, 31-60, 61-90 days; each phase must include target outcome, weekly rhythm, KPIs, and stop-loss rules.

## Quality Bar

- A beginner should know the next click, next document, or next decision after reading each section.
- Separate “must do / 必须做”, “recommended / 建议做”, and “do not do / 暂时不要做”.
- Keep official platform terms in English where sellers will see them in Seller Center, then explain them in Chinese when useful.
- Include reality checks: costs, lead time, compliance risk, logistics timing, refund handling, and owner/responsibility.
- Add checklists that can be marked complete.
- Avoid vague motivational advice. Every section should produce a decision, document, table, script, checklist, or operating rhythm.

## Useful Script

Run `scripts/create_playbook_markdown.py` to generate a clean starter playbook Markdown file:

```bash
python scripts/create_playbook_markdown.py --language zh --mode playbook --output playbook.md
```

Supported language values: `bilingual`, `zh`, `en`.
Supported modes: `playbook`, `checklist`, `90-day`.

Use the generated file as a scaffold, then expand chapters based on the user's product category, business model, and current progress.
