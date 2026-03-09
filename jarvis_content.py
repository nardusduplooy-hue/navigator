# Module 1 ONLY

DR_TALI_ARTICLES = [
    {
        "title": "Understanding Large Language Models: A Complete Manual",
        "url": "https://medium.com/@talirezun/understanding-large-language-models-a-complete-manual-8b18463b6f00",
        "focus": "Core Module 1 reading — LLMs, SLMs, open-source vs closed-source, context windows"
    },
    {
        "title": "From Prompts to Precision: The Art & Science of Context Engineering",
        "url": "https://medium.com/@talirezun/from-prompts-to-precision-the-art-science-of-context-engineering-cebd47462b1c",
        "focus": "How context engineering succeeds prompt engineering — directly relevant to Navigator"
    },
    {
        "title": "Understanding AI Agents: From Chatbots to Autonomous Digital Workers",
        "url": "https://medium.com/@talirezun/understanding-ai-agents-from-chatbots-to-autonomous-digital-workers-407217d84695",
        "focus": "What makes an AI agent — the theory behind what you are building"
    },
    {
        "title": "The Year I Started Coding with AI: My Coding Agent Journey",
        "url": "https://medium.com/@talirezun/the-year-i-started-coding-with-ai-my-coding-agent-journey-431f6f25afe1",
        "focus": "Dr. Tali's personal journey — context for the entire Chasing Jarvis course"
    },
    {
        "title": "The Claude Desktop Coding Agent Experiment: Context Management Lessons",
        "url": "https://medium.com/@talirezun/from-english-to-code-building-production-saas-with-claude-desktop-3ee9c787f5be",
        "focus": "How to manage context with Claude — directly applicable to Navigator build"
    },
    {
        "title": "Chasing Jarvis: The Three Missing Pieces in AI Coding Agents",
        "url": "https://medium.com/@talirezun/chasing-jarvis-the-three-missing-pieces-in-ai-coding-agents-0343ee95356f",
        "focus": "Why context engineering is the bottleneck — the problem Navigator solves"
    },
    {
        "title": "From One Agent to Coding Agent Armies: My 15-Month Journey to AI Orchestration",
        "url": "https://medium.com/@talirezun/from-one-agent-to-coding-agent-armies-my-15-month-journey-to-ai-orchestration-b9138675a075",
        "focus": "Latest article — where AI agent development is heading in 2026"
    },
]

MODULE_1_PREREADING = [
    {
        "title": "Understanding Large Language Models: A Complete Manual",
        "author": "Dr. Tali Režun",
        "url": "https://medium.com/@talirezun/understanding-large-language-models-a-complete-manual-8b18463b6f00",
        "focus": "Core Module 1 reading — LLMs, SLMs, open-source vs closed-source, context windows",
        "module": 1
    },
    {
        "title": "From Lab to Life Podcast — Understanding LLMs (Audio version)",
        "author": "Dr. Tali Režun",
        "url": "https://redcircle.com/shows/from-lab-to-life/ep/8a6a7d09-b3fb-4513-88c6-b2784619a301",
        "focus": "30 min audio version of the Module 1 manual",
        "module": 1
    },
    {
        "title": "Intro to Large Language Models — Andrej Karpathy (YouTube, 1hr)",
        "author": "Andrej Karpathy, ex-OpenAI",
        "url": "https://www.youtube.com/watch?v=zjkBMFhNj_g",
        "focus": "How LLMs actually work under the hood — essential technical foundation",
        "module": 1
    },
]

MODULE_1_ASSIGNMENTS = [
    {
        "assignment": "Define and differentiate between LLMs, SLMs, open-source, and closed-source models",
        "why": "Foundation of the course — you cannot evaluate any AI tool without this",
        "prep_links": [
            ("LLM vs SLM — key differences explained (Red Hat article)", "https://www.redhat.com/en/topics/ai/llm-vs-slm"),
            ("Open vs Closed Source AI — why it matters (Euronews)", "https://www.euronews.com/next/2024/02/20/open-source-vs-closed-source-ai-whats-the-difference-and-why-does-it-matter"),
            ("MIT Sloan — Open vs Closed models: performance and cost data", "https://mitsloan.mit.edu/ideas-made-to-matter/ai-open-models-have-benefits-so-why-arent-they-more-widely-used"),
        ],
        "module": 1
    },
    {
        "assignment": "Compare human cognitive processes with AI equivalents — context windows, training data, inference",
        "why": "Context windows are the foundation of Module 4 context engineering",
        "prep_links": [
            ("What is a Context Window — McKinsey plain-English explainer", "https://www.mckinsey.com/featured-insights/mckinsey-explainers/what-is-a-context-window"),
            ("Context Windows explained in depth — IBM Think", "https://www.ibm.com/think/topics/context-window"),
        ],
        "module": 1
    },
    {
        "assignment": "Evaluate the strengths and limitations of current LLM technology",
        "why": "Knowing when NOT to use AI is as important as knowing when to use it",
        "prep_links": [
            ("AI Snake Oil — Princeton researchers on what AI cannot do", "https://www.aisnakeoil.com"),
            ("LLM vs SLM limitations compared — GeeksforGeeks", "https://www.geeksforgeeks.org/artificial-intelligence/llms-vs-slms-comparative-analysis-of-language-model-architectures/"),
        ],
        "module": 1
    },
    {
        "assignment": "Identify real-world entrepreneurial applications of LLMs",
        "why": "You are already doing this — Navigator is your live answer to this assignment",
        "prep_links": [
            ("Dr. Tali — Understanding AI Agents: From Chatbots to Autonomous Workers", "https://medium.com/@talirezun/understanding-ai-agents-from-chatbots-to-autonomous-digital-workers-407217d84695"),
            ("Andrej Karpathy — LLMs as the new operating system (YouTube)", "https://www.youtube.com/watch?v=zjkBMFhNj_g"),
        ],
        "module": 1
    },
]

TOOLS_EXPLAINED = [
    {
        "tool": "Claude AI — what it is and how it differs",
        "why": "The model powering Navigator — understand what you are already using",
        "link": "https://www.anthropic.com/research/core-views-on-ai-safety",
        "description": "Anthropic's own paper on why they built Claude differently — safety-first vs capability-first"
    },
    {
        "tool": "GitHub — version control for your build",
        "why": "Navigator already lives here — understand what it is doing",
        "link": "https://www.youtube.com/watch?v=RGOj5yH7evk",
        "description": "Git and GitHub explained for beginners — 12 min YouTube by freeCodeCamp"
    },
    {
        "tool": "Tokens and context windows — the currency of LLMs",
        "why": "Every API call costs tokens — you need this for Module 4 context engineering",
        "link": "https://www.datacamp.com/blog/context-window",
        "description": "DataCamp — tokens, context windows, and how LLMs process text, explained clearly"
    },
    {
        "tool": "Model Context Protocol (MCP)",
        "why": "What turns Claude into an agent — core of Module 3",
        "link": "https://modelcontextprotocol.io/introduction",
        "description": "Official MCP introduction — the architecture behind Navigator's agent layer"
    },
    {
        "tool": "Transformer architecture — how LLMs actually think",
        "why": "The underlying architecture of every model — Claude, GPT-4, Gemini all use this",
        "link": "https://www.youtube.com/watch?v=wjZofJX0v4M",
        "description": "3Blue1Brown — Attention in Transformers explained visually (YouTube, 26 min)"
    },
    {
        "tool": "Prompt Engineering — getting better outputs from Claude",
        "why": "You are already doing this — now learn the theory behind it",
        "link": "https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview",
        "description": "Anthropic's official prompt engineering guide — the techniques behind effective AI interaction"
    },
    {
        "tool": "n8n — workflow automation without code",
        "why": "The engine that will automate Navigator — connects Telegram to Claude",
        "link": "https://docs.n8n.io/try-it-out/",
        "description": "n8n quickstart guide — try your first automated workflow in 5 minutes"
    },
    {
        "tool": "LM Studio — run AI locally on your Mac",
        "why": "Privacy-first AI — no data leaves your machine",
        "link": "https://lmstudio.ai/",
        "description": "Download LM Studio and run open-source LLMs on your MacBook — no internet required"
    },
]
