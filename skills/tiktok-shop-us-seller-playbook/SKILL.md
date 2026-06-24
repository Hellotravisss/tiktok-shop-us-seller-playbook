---
name: tiktok-shop-us-seller-playbook
description: Create, expand, audit, or redesign bilingual English/Chinese TikTok Shop US seller onboarding playbooks, SOPs, checklists, worksheets, and training documents. Use when the user wants a practical step-by-step US TikTok Shop guide covering compliant setup, seller documents, shop configuration, product listing, content operations, creator outreach, ads, livestream operations, customer service, logistics, analytics, or a 30/60/90-day execution plan.
---

# TikTok Shop US Seller Playbook

## Core Rule

Create original, practical training material in English, Chinese, or bilingual English/Chinese. Use the user's goals, notes, and business context to infer structure, gaps, pain points, and workflow order.

输出英文、中文或中英双语的原创实操内容。根据用户的目标、笔记和业务背景，判断结构、缺口、痛点和流程顺序。

Do not provide instructions for proxy/VPN setup, traffic tunneling, location spoofing, device fingerprint evasion, fake identity documents, bought/rented shops, account farming, or bypassing platform controls. Redirect those requests to compliant alternatives: authorized local team members, role-based permissions, real seller documents, official Seller Center guidance, and legitimate business operations.

不要提供代理/VPN、流量隧道、定位伪装、设备指纹规避、虚假身份资料、买店租店、账号农场或绕过平台控制的方法。遇到这类请求时，转向合规替代方案：授权本地团队、角色权限、真实主体资料、官方 Seller Center 指引和合法经营流程。

## Workflow

1. Identify the deliverable / 确认交付物:
   - full beginner playbook / 完整新手手册
   - chapter expansion / 单章扩写
   - SOP/checklist pack / SOP 和清单包
   - document redesign for Markdown/DOCX/PDF/Pages / 文档重排版
   - official-policy audit / 官方规则审校
   - 30/60/90-day execution plan / 30/60/90 天执行计划
2. Load only the needed references / 只读取需要的参考:
   - `references/playbook-structure.md` for chapter order and expected depth
   - `references/compliance-boundaries.md` for what to include or avoid
   - `references/official-sources.md` for public source links and verification reminders
   - `references/templates.md` for reusable bilingual tables and worksheets
3. Ask or infer the output language:
   - Default to bilingual English/Chinese for public GitHub-ready material.
   - Default to Chinese for China-based operator training unless the user asks for English.
   - Default to English for global contributor docs unless the user asks for Chinese.
4. Make the result operational:
   - Each chapter should include Objective/本章目标, Preparation/要准备什么, Steps/具体步骤, Common mistakes/常见错误, Done criteria/完成标准.
   - Use tables for seller documents, SKU evaluation, creator outreach, customer service, order handling, and weekly review.
   - Mark rule-sensitive claims with “Verify in Seller Center / 以官方后台为准”.
5. If producing a file, prefer Markdown first for content review, then DOCX/PDF/Pages-friendly formatting if requested.

## Quality Bar

- A beginner should know the next click, next document, or next decision after reading each section.
- Separate “must do / 必须做”, “recommended / 建议做”, and “do not do / 暂时不要做”.
- Keep official platform terms in English where sellers will see them in Seller Center, then explain them in Chinese when useful.
- Include reality checks: costs, lead time, compliance risk, logistics timing, refund handling, and owner/responsibility.
- Add checklists that can be marked complete.

## Useful Script

Run `scripts/create_playbook_markdown.py` to generate a clean starter playbook Markdown file:

```bash
python scripts/create_playbook_markdown.py --language bilingual --output playbook.md
```

Supported language values: `bilingual`, `zh`, `en`.

Use the generated file as a scaffold, then expand chapters based on the user's product category, business model, and current progress.
