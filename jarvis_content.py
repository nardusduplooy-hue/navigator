# CHASING JARVIS — CONTENT LIBRARY
# Every item traces to official course materials only
# Current focus: Module 1. Module 2 preview only — session March 21

MODULE_1_TALI = [
    {
        "title": "Understanding LLMs: AI-Generated Research Podcast",
        "url": "https://redcircle.com/shows/from-lab-to-life/ep/8a6a7d09-b3fb-4513-88c6-b2784619a301",
        "note": "Listen before Module 1, Session 1 — audio version"
    },
    {
        "title": "Understanding Large Language Models: A Complete Manual",
        "url": "https://medium.com/@talirezun/understanding-large-language-models-a-complete-manual-8b18463b6f00",
        "note": "Read before Module 1, Session 1 — core text"
    },
]

MODULE_2_TALI = [
    {
        "title": "The Context Engineer's Toolkit: Essential AI Tools for All Levels",
        "url": "https://medium.com/@talirezun/the-context-engineers-toolkit-essential-ai-tools-for-all-levels-3f383a6f1c07",
        "note": "Read before Module 2 — session March 21"
    },
    {
        "title": "Data Sovereignty in the AI Age: Building Your Own Private ChatGPT",
        "url": "https://medium.com/@talirezun/data-sovereignty-in-the-ai-age-building-your-own-private-chatgpt-a83c96e342a0",
        "note": "Read before the LM Studio session in Module 2"
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
        "assignment": "Apply foundational knowledge to make informed decisions about AI tool selection",
        "why": "Direct preparation for Module 2 — you will select tools for your Module 5 MVP",
        "prep_links": [
            ("Dr. Tali — Understanding Large Language Models: A Complete Manual", "https://medium.com/@talirezun/understanding-large-language-models-a-complete-manual-8b18463b6f00"),
            ("MIT Sloan — Open vs Closed models: performance and cost data", "https://mitsloan.mit.edu/ideas-made-to-matter/ai-open-models-have-benefits-so-why-arent-they-more-widely-used"),
        ],
    },
]

TOOLS_EXPLAINED = [
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
        "description": "Download free at lmstudio.ai — required for the Module 2 LM Studio session"
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
