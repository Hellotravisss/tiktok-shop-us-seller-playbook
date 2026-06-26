#!/usr/bin/env python3
"""Generate TikTok Shop US seller playbook, checklist, launch, profit, content, creator, or ops scaffolds."""

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
    ("TikTok Account Positioning, GreenVideo, and Content Asset System", "TikTok 账号定位、GreenVideo 和内容素材系统"),
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


ZH_CHAPTER_DETAILS = {
    "使用方法和完整路线图": {
        "objective": "先看懂从资料准备到稳定运营的完整路径，知道每一阶段要交付什么结果。",
        "prepare": ["当前阶段", "目标市场和品类", "预算和可投入时间"],
        "steps": [
            "把当前状态标成：准备资料、注册中、选品中、已上架、已出单、放大中。",
            "按 资料-商品-内容-达人-履约-复盘 六条线建立文件夹和表格。",
            "先完成开店资料和规则核对，再决定首批 5-20 个 SKU。",
            "每周只看一个主目标：资料完成、上架完成、内容测试、出单、复购或利润。",
        ],
        "mistakes": ["一开始就追热点和爆款，忽略资料、利润和履约。", "同时开太多 SKU，导致内容、库存和客服都跟不上。"],
        "done": ["已确定当前阶段。", "已建立资料、SKU、内容、达人、订单和复盘表。", "已写出未来 7 天行动清单。"],
    },
    "美国 TikTok Shop 模式、角色和新手误区": {
        "objective": "理解美区 TikTok Shop 是内容电商，不是单纯铺货平台。",
        "prepare": ["业务模式", "团队角色", "预算边界"],
        "steps": [
            "明确你是自营卖家、品牌方、供应链卖家，还是内容/达人驱动卖家。",
            "把角色拆成店铺负责人、选品、内容、达人、客服、履约、财务。",
            "定义每天必须看的数据：订单、转化、退款、库存、健康分和内容表现。",
            "先跑通一个小闭环，再增加 SKU 或预算。",
        ],
        "mistakes": ["把 TikTok Shop 当 Amazon 铺货，只上架不做内容。", "只看播放量，不看点击、加购、订单和退款。"],
        "done": ["已确定业务模式。", "已分配负责人。", "已列出前三个最容易出错的环节。"],
    },
    "主体、税务、银行、仓库、退货地址资料清单": {
        "objective": "把开店和收款需要的真实资料一次性整理好，减少审核和后续风控风险。",
        "prepare": ["主体文件", "税务信息", "银行/收款", "仓库和退货地址"],
        "steps": [
            "建立资料文件夹，命名为主体、税务、银行、仓库、退货、客服。",
            "确认每份文件的姓名、地址、主体名称、税号和银行信息一致。",
            "准备客服邮箱、团队权限和密码管理器。",
            "所有规则敏感项以 Seller Center 当前要求为准。",
        ],
        "mistakes": ["借用身份、买店租店或使用不一致资料。", "审核前不检查地址、税号和银行信息一致性。"],
        "done": ["资料清单已填完。", "文件名清晰可追溯。", "已记录缺失资料和负责人。"],
    },
    "手机、电脑、邮箱、账号权限和工作环境": {
        "objective": "建立稳定、合规、可交接的工作环境，而不是依赖个人临时操作。",
        "prepare": ["专用邮箱", "密码管理器", "两步验证", "工作设备"],
        "steps": [
            "给店铺、客服、财务和内容分别设置权限，不共享主密码。",
            "开启两步验证，记录恢复方式。",
            "用专门文件夹保存素材、订单、报关、客服和财务证据。",
            "建立操作日志，重要改动记录日期和负责人。",
        ],
        "mistakes": ["多人共用一个登录和密码。", "为了省事使用规避平台检测或伪装环境的方法。"],
        "done": ["邮箱和权限设置完成。", "两步验证开启。", "操作日志模板建立。"],
    },
    "店铺注册、审核、后台基础设置": {
        "objective": "完成店铺注册后，把税务、收款、物流、退货、客服和权限基础设置补齐。",
        "prepare": ["Seller Center 入口", "资料文件夹", "店铺设置清单"],
        "steps": [
            "按 Seller Center 当前流程提交资料，不跳过税务和收款检查。",
            "设置仓库地址、退货地址、客服邮箱和团队角色。",
            "检查店铺名称、品牌、类目和政策页面是否一致。",
            "注册后立即建立每日后台检查习惯。",
        ],
        "mistakes": ["审核通过就急着上架，基础设置没补齐。", "忽略退货地址和客服流程，后面退款率升高。"],
        "done": ["基础设置完成。", "收款和税务状态已确认。", "退货和客服入口已确认。"],
    },
    "选品框架：需求、内容表现、合规、利润、供应链": {
        "objective": "用需求、内容、合规、利润、供应链五个维度判断 SKU 是否值得测。",
        "prepare": ["竞品链接", "供应商报价", "样品", "关税初查"],
        "steps": [
            "先判断买家痛点是否能用 3-10 秒视频讲清楚。",
            "用 GreenVideo 或公开视频做结构拆解，只提炼规律，不搬运素材。",
            "核对禁售/限售、宣称、IP、标签、儿童/美妆/电池等风险。",
            "用含税到岸成本测算毛利，再决定是否拿样。",
            "只选 5-20 个 SKU 做第一轮测试。",
        ],
        "mistakes": ["只看工厂价，不算关税、履约、退货和达人广告。", "选择需要复杂资质或高退货风险的品。"],
        "done": ["SKU 评分表完成。", "每个 SKU 有内容角度。", "含税利润和合规风险已记录。"],
    },
    "供应链、样品、质检、包装和库存": {
        "objective": "确保商品能稳定交付，质量、包装、库存和售后风险可控。",
        "prepare": ["供应商列表", "样品", "包装方案", "库存计划"],
        "steps": [
            "至少比较 2-3 个供应商的报价、交期、MOQ 和售后支持。",
            "样品到手后检查材质、尺寸、功能、包装和说明书。",
            "拍摄开箱、使用、尺寸和细节素材，供上架和短视频使用。",
            "设置安全库存和补货点，避免爆单后缺货取消。",
        ],
        "mistakes": ["只拿供应商图片上架，不做样品和质检。", "没有包装测试，导致破损、差评和退款。"],
        "done": ["样品测试完成。", "包装和质检标准写清楚。", "库存和补货规则确定。"],
    },
    "进口税费、中美关税、HTS 编码和到岸成本": {
        "objective": "在上架前确认进口税费和到岸成本，避免卖得越多亏得越多。",
        "prepare": ["产品规格", "原产国", "HTSUS 初步编码", "报关行联系人"],
        "steps": [
            "确认产品材质、功能、用途和原产国。",
            "查 10 位 HTSUS 编码、基础税率和 Chapter 99 附加税号。",
            "核对 Section 301、Section 122、Section 232、AD/CVD、配额和排除。",
            "让报关行确认 HTS、Importer of Record、bond、发票和原产地证据。",
            "把含税到岸成本写进 SKU 利润表。",
        ],
        "mistakes": ["用大类猜税率。", "默认小包免税或忽略 Importer of Record 责任。"],
        "done": ["HTS 和原产国已记录。", "报关行已确认。", "含税利润表已更新。"],
    },
    "商品上架：类目、标题、图片、卖点、价格、库存": {
        "objective": "把商品页做成买家能理解、平台能审核、运营能复盘的销售页面。",
        "prepare": ["类目", "标题关键词", "主图/细节图", "价格和库存"],
        "steps": [
            "先选正确类目，再写标题、属性和规格。",
            "标题包含品牌/产品类型/核心功能/场景/规格，不写无法证明的夸张词。",
            "图片展示白底主图、细节、尺寸、场景、包装和真实使用效果。",
            "描述写清适合谁、解决什么问题、规格、包装清单和 FAQ。",
            "价格必须基于含税到岸成本和退款预留。",
        ],
        "mistakes": ["标题堆关键词或蹭品牌。", "图片过度渲染、无尺寸、无包装说明。"],
        "done": ["类目和属性正确。", "图片和描述完整。", "价格、库存、发货承诺已检查。"],
    },
    "物流、履约、退货、客服和评价": {
        "objective": "建立能保护健康分和买家体验的履约与售后流程。",
        "prepare": ["履约方式", "退货地址", "客服话术", "物流追踪"],
        "steps": [
            "确认自发货、海外仓、FBT 或混合履约方式。",
            "每天检查未发货、迟发、缺货取消和物流异常。",
            "客服、取消、退货、退款和 DNR 都在平台流程内处理。",
            "把高频售后原因回传到包装、质检、页面和供应链。",
        ],
        "mistakes": ["客服私下引导退款或取消。", "只处理单个订单，不修根因。"],
        "done": ["履约 SOP 建立。", "售后话术建立。", "异常复盘表建立。"],
    },
    "TikTok 账号定位、GreenVideo 和内容素材系统": {
        "objective": "建立内容素材库和账号定位，让内容持续服务商品转化。",
        "prepare": ["账号定位", "素材库文件夹", "GreenVideo", "竞品链接"],
        "steps": [
            "确定账号人设、目标买家、品类边界和内容语气。",
            "用 GreenVideo 保存自有或已授权视频，公开视频只做内部结构研究。",
            "素材库按产品、场景、痛点、达人、权利状态命名。",
            "拆解钩子、首帧、演示、证明、CTA 和评论反馈。",
            "每条新视频都重新拍原创素材或使用有授权素材。",
        ],
        "mistakes": ["下载竞品视频后直接搬运。", "素材没有权利状态，后续无法判断能不能用。"],
        "done": ["素材库建立。", "GreenVideo 使用边界写清楚。", "内容研究表填入首批案例。"],
    },
    "短视频脚本、拍摄、剪辑、发布和复盘": {
        "objective": "用可重复的短视频流程，把产品卖点转成持续测试素材。",
        "prepare": ["脚本模板", "拍摄清单", "剪辑工具", "发布节奏"],
        "steps": [
            "每条视频只测一个核心卖点或一个买家异议。",
            "脚本结构用钩子、痛点、演示、证明、CTA。",
            "拍摄产品近景、手部操作、尺寸对比、使用前后和包装。",
            "发布后记录播放、3 秒留存、点击、加购、订单和评论。",
        ],
        "mistakes": ["一条视频塞太多卖点。", "只复盘播放量，不看订单和退款信号。"],
        "done": ["30 天内容日历建立。", "每条视频有脚本和素材来源。", "每周复盘一次。"],
    },
    "Creator/Affiliate 达人建联、寄样、佣金和复盘": {
        "objective": "建立达人筛选、建联、寄样、佣金和复盘闭环。",
        "prepare": ["达人名单", "建联话术", "样品预算", "佣金策略"],
        "steps": [
            "筛选内容风格、受众、互动质量和过往带货匹配度。",
            "建联时说明产品、使用场景、样品、佣金和内容要求。",
            "寄样后记录物流、发布时间、视频链接和数据。",
            "按播放、点击、订单、退款和内容质量决定是否继续合作。",
        ],
        "mistakes": ["只看粉丝数，不看受众和内容匹配。", "没有样品状态表，寄样后失控。"],
        "done": ["达人建联表建立。", "话术和 brief 准备好。", "复盘指标写清楚。"],
    },
    "广告投放入门：预算、素材、目标、数据判断": {
        "objective": "用小预算验证素材和商品，不让广告掩盖产品问题。",
        "prepare": ["广告预算", "素材池", "利润表", "止损规则"],
        "steps": [
            "先确认 SKU 含税利润能承受广告测试。",
            "用自然内容数据筛选可投素材。",
            "设置每日预算和止损线，记录 CTR、CVR、CPA、ROAS。",
            "低转化先修页面和素材，不盲目加预算。",
        ],
        "mistakes": ["没有利润表就投广告。", "把广告当成解决差产品的万能药。"],
        "done": ["预算和止损线明确。", "素材来源可追溯。", "广告数据复盘表建立。"],
    },
    "直播带货准备：货盘、场控、话术、复盘": {
        "objective": "把直播当作可排练的销售流程，而不是临场发挥。",
        "prepare": ["直播货盘", "主播脚本", "场控表", "优惠机制"],
        "steps": [
            "准备引流款、主推款、利润款和加购款。",
            "写开场、痛点、演示、异议、催单和售后说明。",
            "直播前检查库存、价格、优惠、样品和网络设备。",
            "直播后复盘停留、点击、订单、退款和评论问题。",
        ],
        "mistakes": ["没有货盘结构，只逐个介绍产品。", "承诺无法兑现的效果或售后。"],
        "done": ["直播脚本完成。", "货盘和库存确认。", "复盘表建立。"],
    },
    "每日/每周运营 SOP": {
        "objective": "把运营变成固定节奏，减少漏单、迟发、差评和违规。",
        "prepare": ["每日检查表", "异常表", "负责人", "复盘时间"],
        "steps": [
            "上午查订单、未发货、缺货取消和物流异常。",
            "中午处理客服、退货、退款、DNR 和评价。",
            "下午查库存、FBT/仓库、达人回复和内容数据。",
            "晚上记录 AHR、违规、退款、差评和根因。",
        ],
        "mistakes": ["只在出问题后补救，没有每日预警。", "异常不记录负责人和截止日期。"],
        "done": ["每日 SOP 表建立。", "每周复盘固定时间。", "异常有负责人和截止日期。"],
    },
    "数据看板：流量、点击、加购、转化、利润": {
        "objective": "把内容、商品、履约和利润放进同一张看板，判断下一步。",
        "prepare": ["订单数据", "内容数据", "利润表", "退款数据"],
        "steps": [
            "每天记录播放、点击、加购、订单、退款和库存。",
            "每周比较上周和本周变化，写出原因。",
            "按 SKU 判断：继续测、优化页面、补内容、暂停或放大。",
            "把退款和差评原因回传到页面、包装和供应链。",
        ],
        "mistakes": ["只看 GMV，不看利润。", "数据分散在不同表里，没人能判断。"],
        "done": ["周复盘表建立。", "每个 SKU 有下一步动作。", "利润和退款进入决策。"],
    },
    "风险控制：政策、健康分、违规、断货、差评": {
        "objective": "提前识别会伤害店铺的政策、履约、商品和客服风险。",
        "prepare": ["AHR", "违规记录", "退款原因", "库存预警"],
        "steps": [
            "每天看 AHR、违规、迟发、缺货取消和退款。",
            "高风险宣称、禁售品、IP 风险和不确定类目先不上架。",
            "差评和退款超过预警线时暂停放量。",
            "每个风险都记录根因、负责人、修复动作和预防规则。",
        ],
        "mistakes": ["违规后只申诉，不修商品页和流程。", "爆单后断货，导致取消和差评。"],
        "done": ["风险表建立。", "每个异常有根因。", "高风险 SKU 有暂停规则。"],
    },
    "30/60/90 天执行计划": {
        "objective": "把前三个月拆成资料跑通、商品内容测试、达人运营放大三个阶段。",
        "prepare": ["目标", "预算", "SKU 池", "内容计划"],
        "steps": [
            "0-30 天完成资料、规则、首批 SKU、内容素材和上架。",
            "31-60 天复盘 SKU，淘汰弱品，建立达人和内容节奏。",
            "61-90 天优化利润、履约、退款、库存和放大策略。",
            "每个阶段设置停止条件，不让错误持续烧钱。",
        ],
        "mistakes": ["90 天计划只写目标，不写每周动作。", "没有止损线，亏损 SKU 继续放大。"],
        "done": ["每阶段目标明确。", "每周动作明确。", "止损和放大规则明确。"],
    },
    "实操工作簿和模板": {
        "objective": "把所有动作落到表格，方便执行、交接和复盘。",
        "prepare": ["开店清单", "SKU 表", "利润表", "内容表", "达人表", "运营表"],
        "steps": [
            "先复制工作簿模板，不要边做边想格式。",
            "每个表只记录能推动决策的信息。",
            "所有规则敏感项记录核对日期和来源。",
            "每周只保留真正影响下一步的指标。",
        ],
        "mistakes": ["表格很多但没人维护。", "没有日期和负责人，无法追责。"],
        "done": ["工作簿建立。", "负责人明确。", "每周复盘机制建立。"],
    },
}


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
        "tariff_note": "Tariff snapshot: verify current official sources before final pricing. As of 2026-06-25, duty-free de minimis is suspended globally; old China IEEPA ad valorem tariffs were ended by EO 14389; a temporary Section 122 10% surcharge applies to many imports through July 24, 2026 unless exempt or changed; Section 301 China tariffs still depend on HTS code and exclusions. / 关税快照：最终定价前核对官方来源。截至 2026-06-25，美国全球低值免税已暂停；旧中国 IEEPA 从价附加税已由 EO 14389 终止；许多进口商品在 2026-07-24 前有 Section 122 临时 10% 附加税，除非豁免或变更；Section 301 中国关税仍按 HTS 编码和排除情况判断。",
        "content_tool_note": "GreenVideo: https://greenvideo.cc/. Use it for authorized downloads, saving your own videos, internal research, and script deconstruction. Do not repost third-party videos or remove watermarks to hide origin. / GreenVideo：https://greenvideo.cc/。用于已授权下载、保存自己视频、内部研究和脚本拆解。不要搬运第三方视频，也不要去水印隐藏来源。",
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
        "tariff_note": "关税快照：最终定价前核对官方来源。截至 2026-06-25，美国全球低值免税已暂停；旧中国 IEEPA 从价附加税已由 EO 14389 终止；许多进口商品在 2026-07-24 前有 Section 122 临时 10% 附加税，除非豁免或变更；Section 301 中国关税仍按 HTS 编码和排除情况判断。",
        "content_tool_note": "GreenVideo：https://greenvideo.cc/。用于已授权下载、保存自己视频、内部研究和脚本拆解。不要搬运第三方视频，也不要去水印隐藏来源。",
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
        "tariff_note": "Tariff snapshot: verify current official sources before final pricing. As of 2026-06-25, duty-free de minimis is suspended globally; old China IEEPA ad valorem tariffs were ended by EO 14389; a temporary Section 122 10% surcharge applies to many imports through July 24, 2026 unless exempt or changed; Section 301 China tariffs still depend on HTS code and exclusions.",
        "content_tool_note": "GreenVideo: https://greenvideo.cc/. Use it for authorized downloads, saving your own videos, internal research, and script deconstruction. Do not repost third-party videos or remove watermarks to hide origin.",
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
        ("素材工具", "GreenVideo、素材库命名、授权状态、竞品结构拆解"),
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
        ("Content tools", "GreenVideo, asset naming, rights status, competitor structure review"),
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

    prepare_rows = f"|  |  |  | {not_started} |  |"
    steps_body = f"1. {step_1}\n2. {step_2}\n3. {step_3}"
    mistakes_body = f"- {mistake_1}\n- {mistake_2}"
    done_body = f"- [ ] {done_1}\n- [ ] {done_2}\n- [ ] {done_3}"
    details = ZH_CHAPTER_DETAILS.get(zh) if language == "zh" else None
    if details:
        objective = details["objective"]
        prepare_rows = "\n".join(
            f"| {item} |  |  | 未开始 |  |" for item in details["prepare"]
        )
        steps_body = "\n".join(
            f"{idx}. {step}" for idx, step in enumerate(details["steps"], start=1)
        )
        mistakes_body = "\n".join(f"- {item}" for item in details["mistakes"])
        done_body = "\n".join(f"- [ ] {item}" for item in details["done"])

    tariff_section = ""
    if any(key in en for key in ["Product Selection", "Import Duties", "Product Listing"]):
        tariff_section = f"""
### {localized_pair(language, '关税和成本提醒', 'Tariff and Cost Reminder')}

{labels["tariff_note"]}
"""
    content_tool_section = ""
    if any(key in en for key in ["GreenVideo", "Short Video Scripts"]):
        content_tool_section = f"""
### {localized_pair(language, '素材工具提醒', 'Content Tool Reminder')}

{labels["content_tool_note"]}
"""

    return f"""## {chapter_title(index, en, zh, language)}

### {labels["objective"]}

{objective}

### {labels["prepare"]}

| {labels["item"]} | {labels["owner"]} | {labels["file"]} | {labels["status"]} | {labels["notes"]} |
|---|---|---|---|---|
{prepare_rows}

### {labels["steps"]}

{steps_body}

### {labels["mistakes"]}

{mistakes_body}
{tariff_section}
{content_tool_section}

### {labels["done"]}

{done_body}
"""


def build_markdown(language: str, title: str | None) -> str:
    labels = LABELS[language]
    doc_title = title or labels["title"]
    if language == "en":
        intro = "Original practical training guide. Verify rule-sensitive details against the current TikTok Shop Seller Center and Seller University pages."
        boundary_header = "Compliance Boundary"
    elif language == "zh":
        intro = "原创中文实操手册。规则敏感内容以 TikTok Shop Seller Center 和 Seller University 当前页面为准。"
        boundary_header = "使用边界"
    else:
        intro = "Original bilingual practical training guide. Verify rule-sensitive details against the current TikTok Shop Seller Center and Seller University pages. / 原创双语实操手册。规则敏感内容以 TikTok Shop Seller Center 和 Seller University 当前页面为准。"
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


def build_profit_model(language: str, title: str | None) -> str:
    doc_title = title or localized_pair(language, "TikTok Shop 美区 SKU 利润和关税测算表", "TikTok Shop US SKU Profit and Tariff Model")
    return "\n".join([
        f"# {doc_title}",
        "",
        f"> {localized_pair(language, '用途：判断 SKU 是否值得测、能不能放大、关税后利润是否成立。实际出货前必须核对 HTSUS、报关行和 Seller Center 当前费用。', 'Use this to decide whether a SKU is testable, scalable, and profitable after duties. Verify HTSUS, broker review, and current Seller Center fees before shipping.')}",
        "",
        f"## {localized_pair(language, '关税核验', 'Tariff Check')}",
        "",
        f"| SKU | {localized_pair(language, '原产国', 'Origin')} | HTSUS | {localized_pair(language, '基础税率', 'Base Duty')} | Section 301 | Section 122 | Section 232 / AD/CVD | {localized_pair(language, '报关行确认', 'Broker Check')} | {localized_pair(language, '日期', 'Date')} |",
        "|---|---|---|---:|---|---|---|---|---|",
        "",
        f"## {localized_pair(language, '利润测算', 'Profit Model')}",
        "",
        f"| SKU | {localized_pair(language, '售价', 'Price')} | {localized_pair(language, '货品', 'Product Cost')} | {localized_pair(language, '运费', 'Freight')} | {localized_pair(language, '关税', 'Duty/Tariff')} | {localized_pair(language, '平台费', 'Platform Fee')} | {localized_pair(language, '履约', 'Fulfillment')} | {localized_pair(language, '退货预留', 'Return Allowance')} | {localized_pair(language, '达人广告', 'Creator/Ads')} | {localized_pair(language, '利润', 'Profit')} | {localized_pair(language, '毛利率', 'Margin')} | {localized_pair(language, '决策', 'Decision')} |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|",
        "",
        f"## {localized_pair(language, '决策规则', 'Decision Rules')}",
        "",
        f"- {localized_pair(language, 'HTS 或原产国不确定时，不做大货。', 'Do not place bulk orders if HTS or origin is uncertain.')}",
        f"- {localized_pair(language, '含税毛利不成立时，先换供应链、涨价或换 SKU。', 'If margin fails after duties, change supplier, price, or SKU first.')}",
        f"- {localized_pair(language, '退款率、破损率、达人佣金和广告预留必须进入测算。', 'Include refund rate, damage rate, creator commission, and ad allowance in the model.')}",
    ]) + "\n"


def build_content_calendar(language: str, title: str | None) -> str:
    doc_title = title or localized_pair(language, "TikTok Shop 美区 30 天内容日历", "TikTok Shop US 30-Day Content Calendar")
    hooks = [
        ("痛点演示", "Problem demo", "Stop doing this every morning"),
        ("前后对比", "Before/after", "One small change fixed this"),
        ("功能证明", "Feature proof", "I tested this for 7 days"),
        ("UGC 口吻", "UGC style", "I didn't expect this to work"),
        ("异议解答", "Objection answer", "Is it worth the price?"),
    ]
    rows = [
        f"| {i} | {localized_pair(language, zh, en)} | {hook} |  |  |  |  |"
        for i, (zh, en, hook) in enumerate(hooks, start=1)
    ]
    return "\n".join([
        f"# {doc_title}",
        "",
        f"> {localized_pair(language, 'GreenVideo 可用于已授权下载、保存自有视频、内部研究和脚本拆解；不要搬运第三方视频。', 'Use GreenVideo for authorized downloads, your own videos, internal research, and script deconstruction; do not repost third-party videos.')}",
        "",
        f"| {localized_pair(language, '天', 'Day')} | {localized_pair(language, '类型', 'Type')} | Hook | {localized_pair(language, '产品角度', 'Product Angle')} | {localized_pair(language, '所需素材', 'Asset Needed')} | CTA | KPI |",
        "|---:|---|---|---|---|---|---|",
        *rows,
        "",
        f"## {localized_pair(language, '每周复盘', 'Weekly Review')}",
        "",
        f"1. {localized_pair(language, '按 3 秒留存、点击、加购、转化、评论和退款信号排序。', 'Sort by 3-second hold, clicks, add-to-cart, conversion, comments, and refund signals.')}",
        f"2. {localized_pair(language, '保留胜出的钩子和场景，重拍原创素材。', 'Keep winning hooks and scenes, then reshoot original assets.')}",
        f"3. {localized_pair(language, '记录可使用权利状态：自有、已授权、仅研究。', 'Record rights status: own, authorized, or research only.')}",
    ]) + "\n"


def build_creator_pack(language: str, title: str | None) -> str:
    doc_title = title or localized_pair(language, "TikTok Shop 美区达人建联包", "TikTok Shop US Creator Outreach Pack")
    return "\n".join([
        f"# {doc_title}",
        "",
        f"## {localized_pair(language, '达人筛选表', 'Creator Filter')}",
        "",
        f"| {localized_pair(language, '达人', 'Creator')} | Link | {localized_pair(language, '粉丝', 'Followers')} | {localized_pair(language, '内容匹配', 'Fit')} | {localized_pair(language, '受众', 'Audience')} | {localized_pair(language, '风险', 'Risk')} | {localized_pair(language, '动作', 'Action')} |",
        "|---|---|---:|---|---|---|---|",
        "",
        f"## {localized_pair(language, '建联话术', 'Outreach Script')}",
        "",
        localized_pair(
            language,
            "你好 [名字]，我看到你关于 [主题] 的视频，很适合我们的 [产品]。我们想找真实使用感强的达人做短视频测评，可以提供 [样品/佣金/brief]。如果你感兴趣，我可以发产品信息和拍摄方向。",
            "Hi [Name], I liked your video about [topic]. We are launching [product] for [buyer type] and think your style fits. Would you be open to testing a sample and creating a short honest review? We can provide [sample/commission/brief].",
        ),
        "",
        f"## {localized_pair(language, '复盘表', 'Review Table')}",
        "",
        f"| {localized_pair(language, '达人', 'Creator')} | {localized_pair(language, '角度', 'Angle')} | Views | CTR | {localized_pair(language, '订单', 'Orders')} | {localized_pair(language, '退款', 'Refunds')} | {localized_pair(language, '成本', 'Cost')} | {localized_pair(language, '下一步', 'Next Step')} |",
        "|---|---|---:|---:|---:|---:|---:|---|",
    ]) + "\n"


def build_ops_sop(language: str, title: str | None) -> str:
    doc_title = title or localized_pair(language, "TikTok Shop 美区每日运营 SOP", "TikTok Shop US Daily Operations SOP")
    return "\n".join([
        f"# {doc_title}",
        "",
        f"| {localized_pair(language, '时间', 'Time')} | {localized_pair(language, '检查', 'Check')} | {localized_pair(language, '动作', 'Action')} | {localized_pair(language, '留痕', 'Evidence')} |",
        "|---|---|---|---|",
        f"| {localized_pair(language, '上午', 'Morning')} | {localized_pair(language, '订单、未发货、取消风险', 'Orders, unshipped, cancellation risk')} | {localized_pair(language, '当天发货或升级处理', 'Ship or escalate same day')} | {localized_pair(language, '订单截图', 'Order screenshot')} |",
        f"| {localized_pair(language, '中午', 'Midday')} | {localized_pair(language, '买家消息、退货、退款、DNR', 'Buyer messages, returns, refunds, DNR')} | {localized_pair(language, '平台流程内回复', 'Reply in approved workflow')} | {localized_pair(language, '消息记录', 'Message log')} |",
        f"| {localized_pair(language, '下午', 'Afternoon')} | {localized_pair(language, '库存、FBT 入仓、断货风险', 'Inventory, FBT inbound, stockout risk')} | {localized_pair(language, '补货或暂停风险链接', 'Replenish or pause risky listings')} | {localized_pair(language, '库存表', 'Inventory sheet')} |",
        f"| {localized_pair(language, '晚上', 'Evening')} | AHR, {localized_pair(language, '违规、链接健康、评价', 'violations, listing health, reviews')} | {localized_pair(language, '修根因并记录负责人', 'Fix root cause and record owner')} | {localized_pair(language, '异常表', 'Issue log')} |",
        "",
        f"## {localized_pair(language, '预警指标', 'Warning Metrics')}",
        "",
        f"- AHR, OTDR, SFCR, {localized_pair(language, '未发货率、缺货取消率、退款率、差评、违规。', 'unshipped rate, out-of-stock cancellation, refund rate, bad reviews, violations.')}",
    ]) + "\n"


def build_workbook(language: str, title: str | None) -> str:
    doc_title = title or localized_pair(language, "TikTok Shop 美区实操工作簿", "TikTok Shop US Operator Workbook")
    sections = [
        f"# {doc_title}\n",
        build_checklist(language, localized_pair(language, "开店总检查清单", "Launch Master Checklist")),
        build_profit_model(language, localized_pair(language, "SKU 利润和关税测算", "SKU Profit and Tariff Model")),
        build_content_calendar(language, localized_pair(language, "30 天内容日历", "30-Day Content Calendar")),
        build_creator_pack(language, localized_pair(language, "达人建联和复盘", "Creator Outreach and Review")),
        build_ops_sop(language, localized_pair(language, "每日运营 SOP", "Daily Operations SOP")),
    ]
    return "\n---\n\n".join(section.rstrip() for section in sections) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="tiktok-shop-us-playbook.md")
    parser.add_argument("--language", choices=["bilingual", "zh", "en"], default="bilingual")
    parser.add_argument("--mode", choices=["playbook", "checklist", "90-day", "profit", "content-calendar", "creator-pack", "ops-sop", "workbook"], default="playbook")
    parser.add_argument("--title", default=None)
    args = parser.parse_args()
    builders = {
        "playbook": build_markdown,
        "checklist": build_checklist,
        "90-day": build_90_day_plan,
        "profit": build_profit_model,
        "content-calendar": build_content_calendar,
        "creator-pack": build_creator_pack,
        "ops-sop": build_ops_sop,
        "workbook": build_workbook,
    }
    Path(args.output).write_text(builders[args.mode](args.language, args.title), encoding="utf-8")


if __name__ == "__main__":
    main()
