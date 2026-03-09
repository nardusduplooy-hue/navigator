MODULE_1_PREREADING = [
    {
        "title": "Understanding Large Language Models: A Complete Manual",
        "author": "Dr. Tali Režun",
        "url": "https://medium.com/@talirezun/understanding-large-language-models-a-complete-manual-8b18463b6f00",
        "focus": "Core Module 1 reading — LLMs, SLMs, open-source vs closed-source models",
        "module": 1
    },
    {
        "title": "Understanding LLMs: AI-Generated Research Podcast",
        "author": "Dr. Tali Režun",
        "url": "https://redcircle.com/shows/from-lab-to-life/ep/8a6a7d09-b3fb-4513-88c6-b2784619a301",
        "focus": "Audio version — listen before Module 1 Session 1",
        "module": 1
    },
]

MODULE_2_PREREADING = [
    {
        "title": "The Context Engineer's Toolkit: Essential AI Tools for All Levels",
        "author": "Dr. Tali Režun",
        "url": "https://medium.com/@talirezun/the-context-engineers-toolkit-essential-ai-tools-for-all-levels-3f383a6f1c07",
        "focus": "Core Module 2 reading — all tools used in the course",
        "module": 2
    },
    {
        "title": "Data Sovereignty in the AI Age: Building Your Own Private ChatGPT",
        "author": "Dr. Tali Režun",
        "url": "https://medium.com/@talirezun/data-sovereignty-in-the-ai-age-building-your-own-private-chatgpt-a83c96e342a0",
        "focus": "Read before LM Studio session — running AI locally on your Mac",
        "module": 2
    },
]

MODULE_1_ASSIGNMENTS = [
    {
        "assignment": "Define and differentiate between LLMs, SLMs, open-source, and closed-source models",
        "why": "Foundation for everything — you need this before you can evaluate any AI tool",
        "prep_links": [
            ("Dr. Tali's Complete LLM Manual — start here", "https://medium.com/@talirezun/understanding-large-language-models-a-complete-manual-8b18463b6f00"),
            ("LLM vs SLM: Key Differences explained — Red Hat", "https://www.redhat.com/en/topics/ai/llm-vs-slm"),
            ("Open vs Closed Source AI Models — HuggingFace Blog", "https://huggingface.co/blog/os-llms"),
        ],
        "module": 1
    },
    {
        "assignment": "Compare human cognitive processes with AI equivalents — context windows, training data, inference",
        "why": "Context windows are the foundation of context engineering in Module 4",
        "prep_links": [
            ("What is a Context Window? — McKinsey plain-English explainer", "https://www.mckinsey.com/featured-insights/mckinsey-explainers/what-is-a-context-window"),
            ("Context Windows explained in depth — IBM", "https://www.ibm.com/think/topics/context-window"),
            ("Andrej Karpathy — Intro to LLMs (YouTube, 1hr)", "https://www.youtube.com/watch?v=zjkBMFhNj_g"),
        ],
        "module": 1
    },
    {
        "assignment": "Evaluate the strengths and limitations of current LLM technology",
        "why": "Knowing when NOT to use AI is as important as knowing when to use it",
        "prep_links": [
            ("AI Snake Oil — honest LLM limitations (free blog)", "https://www.aisnakeoil.com"),
            ("LLM limitations explained — GeeksforGeeks", "https://www.geeksforgeeks.org/artificial-intelligence/llms-vs-slms-comparative-analysis-of-language-model-architectures/"),
        ],
        "module": 1
    },
]

MODULE_2_ASSIGNMENTS = [
    {
        "assignment": "Create accounts for GitHub, Google Gemini, Google AI Studio, Claude, n8n",
        "why": "Must be running before the session — do not arrive without these set up",
        "prep_links": [
            ("Google NotebookLM — sign up free", "https://notebooklm.google.com/"),
            ("NotebookLM Complete Guide — what it does and how", "https://wondertools.substack.com/p/notebooklm-the-complete-guide"),
            ("Google AI Studio — sign up free", "https://aistudio.google.com/"),
            ("n8n — sign up free tier", "https://n8n.io/"),
        ],
        "module": 2
    },
    {
        "assignment": "Differentiate between frontier LLM models and select appropriate tools for specific tasks",
        "why": "You will be asked to justify which model you chose for Navigator — be ready",
        "prep_links": [
            ("Context Engineer's Toolkit by Dr. Tali — which tool for which job", "https://medium.com/@talirezun/the-context-engineers-toolkit-essential-ai-tools-for-all-levels-3f383a6f1c07"),
            ("Claude vs GPT-4 vs Gemini — Microsoft comparison", "https://www.microsoft.com/en-us/microsoft-cloud/blog/2024/11/11/explore-ai-models-key-differences-between-small-language-models-and-large-language-models/"),
            ("What is Claude and why it is different — Anthropic", "https://www.anthropic.com/claude"),
        ],
        "module": 2
    },
]

TOOLS_EXPLAINED = [
    {
        "tool": "Claude AI",
        "why": "The brain of Navigator — you are already using it",
        "link": "https://www.anthropic.com/claude",
        "description": "What Claude is, how it differs from ChatGPT, why Anthropic built it with safety first"
    },
    {
        "tool": "Google NotebookLM",
        "why": "Required for Modules 2 and 4 — research and knowledge synthesis",
        "link": "https://wondertools.substack.com/p/notebooklm-the-complete-guide",
        "description": "Complete guide to NotebookLM — how to synthesise research, create audio overviews, build study guides"
    },
    {
        "tool": "Google AI Studio",
        "why": "Required for Modules 2, 4, and 5 — prototyping and MVP building",
        "link": "https://aistudio.google.com/",
        "description": "Rapid prototyping with Gemini — the beginner track for your Module 5 MVP"
    },
    {
        "tool": "n8n Workflow Automation",
        "why": "Connects Telegram to Claude to Navigator automatically — Module 3",
        "link": "https://n8n.io/",
        "description": "How n8n automates workflows without code — directly relevant to Navigator build"
    },
    {
        "tool": "GitHub",
        "why": "You are already using it — Navigator lives here",
        "link": "https://www.youtube.com/watch?v=RGOj5yH7evk",
        "description": "Git and GitHub for beginners — version control explained simply (YouTube)"
    },
    {
        "tool": "LM Studio",
        "why": "Run AI models locally on your MacBook — privacy applications",
        "link": "https://lmstudio.ai/",
        "description": "Download and run open-source LLMs on your Mac with no internet required"
    },
    {
        "tool": "Model Context Protocol (MCP)",
        "why": "Core of Module 3 — what turns Claude into an agent",
        "link": "https://modelcontextprotocol.io/",
        "description": "Official MCP documentation — the architecture behind Navigator's agent layer"
    },
    {
        "tool": "VS Code",
        "why": "Code editor — same as Cursor which you already have installed",
        "link": "https://code.visualstudio.com/",
        "description": "Download VS Code — required for Modules 3 and 4 coding agent setup"
    },
]
