# CHASING JARVIS — CONTENT LIBRARY
# Every item traces to official course materials only
# Current focus: Module 1. Module 2 preview only — session March 21

MODULE_1_TALI = [
    {
        "title": "Understanding LLMs: AI-Generated Research Podcast",
        "url": "https://redcircle.com/shows/from-lab-to-life/ep/8a6a7d09-b3fb-4513-88c6-b2784619a301",
        "note": "Listen to audio version on Red Circle"
    },

    {
        "title": "Understanding Large Language Models: A Complete Manual",
        "url": "https://medium.com/@talirezun/understanding-large-language-models-a-complete-manual-8b18463b6f00",
        "note": "Read with comprehension"
    },
]

LLM_MANUAL_CHAPTERS = [
    {"chapter": 1, "title": "What Are Large Language Models?", "note": "Chapter 1 — Start here if you haven't already"},
    {"chapter": 2, "title": "The Architecture Behind LLMs", "note": "Chapter 2 — How transformers are structured"},
    {"chapter": 3, "title": "How LLMs Learn — Pre-training & Fine-tuning", "note": "Chapter 3 — Teaching machines to understand"},
    {"chapter": 4, "title": "Tokenisation & Embeddings", "note": "Chapter 4 — How text becomes numbers"},
    {"chapter": 5, "title": "Context Windows & Memory", "note": "Chapter 5 — Why context engineering matters"},
    {"chapter": 6, "title": "Training — Teaching Machines to Understand Language", "note": "Chapter 6 — The learning process in detail"},
    {"chapter": 7, "title": "Prompting & Inference", "note": "Chapter 7 — How models generate responses"},
    {"chapter": 8, "title": "Open vs Closed Source Models", "note": "Chapter 8 — Choosing the right model for the job"},
    {"chapter": 9, "title": "Limitations & Failure Modes", "note": "Chapter 9 — When NOT to trust an LLM"},
    {"chapter": 10, "title": "The Future of LLMs", "note": "Chapter 10 — Where this is all heading"},
]

_PLACEHOLDER = [
]

MODULE_2_TALI = [
    {
        "title": "Context Engineering — AI-Generated Research Podcast",
        "url": "https://redcircle.com/shows/ab71928c-8c79-46b9-a324-0d82a84b3254/ep/2f8a063f-121e-4c43-b268-a3c0e42c6701",
        "note": "Listen to audio version on Red Circle — Module 2 preparation"
    },
    {
        "title": "The Context Engineer's Toolkit: Essential AI Tools for All Levels",
        "url": "https://medium.com/@talirezun/the-context-engineers-toolkit-essential-ai-tools-for-all-levels-3f383a6f1c07",
        "note": "Read before Module 2 — session March 21"
    },
    {
        "title": "Data Sovereignty in the AI Age: Building Your Own Private ChatGPT",
        "url": "https://medium.com/@talirezun/data-sovereignty-in-the-ai-age-building-your-own-private-chatgpt-a83c96e342a0",
        "note": "Read before upcoming Zoom session for Module 2"
    },
]

MODULE_1_ASSIGNMENTS = [
    {
        "assignment": "Define and differentiate between LLMs, SLMs, open-source, and closed-source models",
        "why": "The foundation of every tool decision you make in Modules 2 through 5",
        "prep_links": [
            ("Dr. Tali — Understanding Large Language Models: A Complete Manual", "https://medium.com/@talirezun/understanding-large-language-models-a-complete-manual-8b18463b6f00"),
            ("LLM vs SLM: key differences — Red Hat article", "https://www.redhat.com/en/topics/ai/llm-vs-slm"),
            ("Open vs Closed Source AI explained — Euronews", "https://www.euronews.com/next/2024/02/20/open-source-vs-closed-source-ai-whats-the-difference-and-why-does-it-matter"),
        ],
    },
    {
        "assignment": "Explain the fundamental architecture of neural networks and transformer models",
        "why": "Claude, GPT-4, and Gemini all run on transformer architecture — this gives you an edge in every module",
        "prep_links": [
            ("Dr. Tali — Understanding Large Language Models: A Complete Manual", "https://medium.com/@talirezun/understanding-large-language-models-a-complete-manual-8b18463b6f00"),
            ("3Blue1Brown — Attention in Transformers visualised (YouTube, 26 min)", "https://www.youtube.com/watch?v=wjZofJX0v4M"),
        ],
    },
    {
        "assignment": "Compare human cognitive processes with AI equivalents — context windows, training data, inference",
        "why": "Context windows are the foundation of Module 4 context engineering",
        "prep_links": [
            ("Dr. Tali — Understanding Large Language Models: A Complete Manual", "https://medium.com/@talirezun/understanding-large-language-models-a-complete-manual-8b18463b6f00"),
            ("What is a Context Window — McKinsey plain-English explainer", "https://www.mckinsey.com/featured-insights/mckinsey-explainers/what-is-a-context-window"),
            ("Andrej Karpathy — Intro to LLMs (YouTube, 1hr)", "https://www.youtube.com/watch?v=zjkBMFhNj_g"),
        ],
    },
    {
        "assignment": "Evaluate the strengths and limitations of current LLM technology",
        "why": "Knowing when NOT to use AI is as important as knowing when to use it",
        "prep_links": [
            ("Dr. Tali — Understanding Large Language Models: A Complete Manual", "https://medium.com/@talirezun/understanding-large-language-models-a-complete-manual-8b18463b6f00"),
            ("AI Snake Oil — Princeton researchers on what AI cannot do", "https://www.aisnakeoil.com"),
        ],
    },
    {
        "assignment": "Differentiate between frontier LLM models and select appropriate tools for specific tasks",
        "why": "Understanding transformer architecture gives you an edge in every module — Claude, GPT-4, and Gemini all run on this foundation",
        "prep_links": [
            ("Dr. Tali — Understanding Large Language Models: A Complete Manual", "https://medium.com/@talirezun/understanding-large-language-models-a-complete-manual-8b18463b6f00"),
            ("Harvard Business Review — Choosing the Right AI Model for Your Business", "https://hbr.org/2023/11/how-to-choose-the-right-ai-model-for-your-use-case"),
        ],
    },
]

TOOLS_EXPLAINED = [
    {
        "tool": "Google Gemini",
        "module": "All modules",
        "why": "Google's frontier AI model — recommended by Dr. Tali for close to zero cost",
        "link": "https://gemini.google.com",
        "description": "Google Gemini — explore the model Dr. Tali recommends for AI-powered tasks"
    },
    {
        "tool": "Claude AI",
        "module": "All modules",
        "why": "The model powering Navigator — you are already using it",
        "link": "https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview",
        "description": "Anthropic's official prompt engineering guide — how to get better outputs from Claude right now"
    },
    {
        "tool": "Google NotebookLM",
        "module": "Module 2 + Module 4",
        "why": "Required for Module 2 and your Module 4 MVP research",
        "link": "https://notebooklm.google.com/",
        "description": "Sign up free at notebooklm.google.com — upload Dr. Tali's articles and ask questions directly from the source"
    },
    {
        "tool": "Google AI Studio",
        "module": "Module 2 + Module 4 + Module 5",
        "why": "Required for Modules 2, 4 and 5 — the beginner MVP build track",
        "link": "https://aistudio.google.com/",
        "description": "Sign up free at aistudio.google.com — this is where you prototype your Module 5 MVP"
    },
    {
        "tool": "n8n Workflow Automation",
        "module": "Module 2 + Module 3",
        "why": "Required for Modules 2 and 3 — automates Navigator without code",
        "link": "https://docs.n8n.io/try-it-out/",
        "description": "n8n quickstart — build your first automated workflow in 5 minutes. Free tier at n8n.io"
    },
    {
        "tool": "GitHub",
        "module": "Module 2 + Module 4 + Module 5",
        "why": "Navigator already lives here — understand what it is doing",
        "link": "https://www.youtube.com/watch?v=RGOj5yH7evk",
        "description": "Git and GitHub for beginners — freeCodeCamp YouTube, 12 min"
    },
    {
        "tool": "LM Studio",
        "module": "Module 2",
        "why": "Run AI models locally on your MacBook — no data leaves your machine",
        "link": "https://lmstudio.ai/",
        "description": "Download free at lmstudio.ai — run powerful AI models privately on your own machine, no internet required"
    },
    {
        "tool": "Model Context Protocol (MCP)",
        "module": "Module 3",
        "why": "What turns Claude into an agent — the core of Module 3",
        "link": "https://modelcontextprotocol.io/introduction",
        "description": "Official MCP introduction — read before Module 3. The architecture behind Navigator's agent layer"
    },
    {
        "tool": "VS Code",
        "module": "Module 3 + Module 4 + Module 5",
        "why": "Required for Modules 3, 4 and 5 coding sessions",
        "link": "https://code.visualstudio.com/",
        "description": "Download free at code.visualstudio.com — install before Module 3"
    },
]

SUPPLEMENTARY = [
    {
        "title": "What is a Transformer Model? — IBM",
        "url": "https://www.ibm.com/topics/transformer-model",
        "module": "Module 1",
        "note": "Plain-English explainer on transformer architecture — read before Module 2"
    },
    {
        "title": "A Beginner's Guide to Large Language Models — NVIDIA",
        "url": "https://www.nvidia.com/en-us/glossary/large-language-models/",
        "module": "Module 1",
        "note": "Solid foundation on how LLMs work — essential Module 1 reference"
    },
    {
        "title": "Building Effective AI Agents — Anthropic",
        "url": "https://www.anthropic.com/research/building-effective-agents",
        "module": "Module 3",
        "note": "Technical deep dive from Anthropic's engineering team"
    },
    {
        "title": "Effective Context Engineering for AI Agents — Anthropic",
        "url": "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents",
        "module": "Module 4",
        "note": "Technical deep dive from Anthropic's engineering team"
    },
    {
        "title": "The New Skill in AI is Not Prompting, It's Context Engineering — Philipp Schmid",
        "url": "https://www.philschmid.de/context-engineering",
        "module": "Module 4",
        "note": "Industry perspective on context engineering"
    },
    {
        "title": "Context Engineering for AI Agents: Lessons from Building Manus",
        "url": "https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus",
        "module": "Module 4",
        "note": "Practical insights from production deployment"
    },
    {
        "title": "Markdown Guide — complete reference",
        "url": "https://www.markdownguide.org/",
        "module": "Module 4",
        "note": "Required for context engineering — markdown structures your agent instructions"
    },
]


# DR. TALI — ADDITIONAL MEDIUM ARTICLES
MODULE_4_TALI = [
    {
        "title": "From Prompts to Precision: The Art & Science of Context Engineering",
        "url": "https://medium.com/@talirezun/from-prompts-to-precision-the-art-science-of-context-engineering-cebd47462b1c",
        "note": "Read before Module 4 — context engineering deep dive by Dr. Tali"
    },
    {
        "title": "From Google AI Studio to Production: Building Lumina v1 in 48 Hours",
        "url": "https://medium.com/@talirezun/from-google-ai-studio-to-production-d928bb00edbd",
        "note": "Read before Module 5 — Dr. Tali builds a production app with AI"
    },
]

# DRAZEN KAPUSTA — LINKEDIN ARTICLES
MODULE_4_TALI = [
    {
        "title": "From Prompts to Precision: The Art & Science of Context Engineering",
        "url": "https://medium.com/@talirezun/from-prompts-to-precision-the-art-science-of-context-engineering-cebd47462b1c",
        "note": "Read before Module 4 — context engineering deep dive by Dr. Tali"
    },
    {
        "title": "From Google AI Studio to Production: Building Lumina v1 in 48 Hours",
        "url": "https://medium.com/@talirezun/from-google-ai-studio-to-production-d928bb00edbd",
        "note": "Read before Module 5 — Dr. Tali builds a production app with AI"
    },
]

KAPUSTA_ARTICLES = [
    {
        "title": "Signals — Dražen Kapusta",
        "url": "https://www.linkedin.com/pulse/signals-drazen-kapusta-kibxf/",
        "note": "The future could arrive faster than you expect"
    },
    {
        "title": "Neo-Cotruglian Philosophy of Leadership",
        "url": "https://www.linkedin.com/pulse/neo-cotruglian-philosophy-leadership-operating-system-drazen-kapusta-z03of/",
        "note": "The philosophical foundation of the Vanguard MBA — read early"
    },
]

NEO_WORLD_ARTICLES = [
    {
        "title": "A Merchant's Wisdom, Half a Millennium Late",
        "authors": "Dražen Kapusta",
        "url": "https://www.linkedin.com/pulse/merchants-wisdom-half-millennium-late-drazen-kapusta-noqxe/",
        "note": "Cotrugli's ledger principle applied to the AI age — essential NEO World reading"
    },
    {
        "title": "Not for Now — For the Future: Why the Next Decade of AI Commerce Needs a Trust Layer",
        "authors": "Dražen Kapusta & Terence Tse",
        "url": "https://worldfinancialreview.com/not-for-now-for-the-future-why-the-next-decade-of-ai-commerce-needs-a-trust-layer/",
        "note": "Core NEO World philosophy — the trust layer every AI economy needs"
    },
    {
        "title": "Intro to the NEO Era",
        "authors": "Dražen Kapusta",
        "url": "https://www.linkedin.com/pulse/intro-neo-era-drazen-kapusta-veb2f",
        "note": "Kapusta's introduction to the NEO World — start here if you haven't already"
    },
]

# Keep backward compatibility
KAPUSTA_WFR_ARTICLE = NEO_WORLD_ARTICLES[0]
