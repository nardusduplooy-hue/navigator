# CHASING JARVIS — CONTENT LIBRARY
# Every item traces to official course materials only
# Current focus: Module 2 (tool setup). Module 3 preview — session April 4
# Last updated: 23 March 2026

MODULE_1_TALI = [
    {
        "title": "Understanding Large Language Models: A Complete Manual",
        "url": "https://medium.com/@talirezun/understanding-large-language-models-a-complete-manual-8b18463b6f00",
        "note": "Read with comprehension — Module 1 foundation"
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

MODULE_2_TALI = [
    {
        "title": "The Context Engineer's Toolkit: Essential AI Tools for All Levels",
        "url": "https://medium.com/@talirezun/the-context-engineers-toolkit-essential-ai-tools-for-all-levels-3f383a6f1c07",
        "note": "Read before Module 2 — the tool map for every session ahead"
    },
    {
        "title": "Data Sovereignty in the AI Age: Building Your Own Private ChatGPT",
        "url": "https://medium.com/@talirezun/data-sovereignty-in-the-ai-age-building-your-own-private-chatgpt-a83c96e342a0",
        "note": "Read before Module 2 — why running models locally matters"
    },
    {
        "title": "Context Engineering — AI-Generated Research Podcast",
        "url": "https://redcircle.com/shows/ab71928c-8c79-46b9-a324-0d82a84b3254/ep/2f8a063f-121e-4c43-b268-a3c0e42c6701",
        "note": "Listen on Red Circle — audio version of the context engineering material"
    },
]

MODULE_2_ASSIGNMENTS = [
    {
        "assignment": "Set up Google NotebookLM and upload Dr. Tali's 'Understanding Large Language Models' article — ask it 5 questions you couldn't answer before",
        "why": "NotebookLM is your personal AI research assistant. Getting it loaded with course material before the session puts you 3 steps ahead.",
        "prep_links": [
            ("Google NotebookLM — sign up free", "https://notebooklm.google.com/"),
            ("Dr. Tali — Understanding Large Language Models: A Complete Manual", "https://medium.com/@talirezun/understanding-large-language-models-a-complete-manual-8b18463b6f00"),
        ],
    },
    {
        "assignment": "Sign up for Google AI Studio and run your first prompt — experiment with system instructions and compare outputs from different Gemini models",
        "why": "Google AI Studio is the beginner MVP build track for Modules 4 and 5. Knowing where the buttons are before the session matters.",
        "prep_links": [
            ("Google AI Studio — sign up free", "https://aistudio.google.com/"),
            ("Dr. Tali — The Context Engineer's Toolkit", "https://medium.com/@talirezun/the-context-engineers-toolkit-essential-ai-tools-for-all-levels-3f383a6f1c07"),
        ],
    },
    {
        "assignment": "Download and run LM Studio — load a small open-source model (Mistral 7B or Llama 3.2 3B) and run it fully offline on your machine",
        "why": "Data sovereignty starts here. Running a model locally means no data leaves your machine — this is the practical foundation of Dr. Tali's privacy module.",
        "prep_links": [
            ("LM Studio — download free", "https://lmstudio.ai/"),
            ("Dr. Tali — Data Sovereignty in the AI Age", "https://medium.com/@talirezun/data-sovereignty-in-the-ai-age-building-your-own-private-chatgpt-a83c96e342a0"),
        ],
    },
    {
        "assignment": "Complete the n8n quickstart — build your first automated workflow connecting two apps without writing any code",
        "why": "n8n is the automation layer required for Modules 2 and 3. Building one workflow before the session means you're not starting from zero in class.",
        "prep_links": [
            ("n8n quickstart — try it free", "https://docs.n8n.io/try-it-out/"),
            ("Dr. Tali — The Context Engineer's Toolkit", "https://medium.com/@talirezun/the-context-engineers-toolkit-essential-ai-tools-for-all-levels-3f383a6f1c07"),
        ],
    },
    {
        "assignment": "Install VS Code and the GitHub Copilot extension — open Navigator's codebase and read one Python file end to end",
        "why": "VS Code is required for Modules 3, 4 and 5. Reading real code before you write any is the fastest way to stop being afraid of it.",
        "prep_links": [
            ("VS Code — download free", "https://code.visualstudio.com/"),
            ("Git and GitHub for beginners — freeCodeCamp, 12 min", "https://www.youtube.com/watch?v=RGOj5yH7evk"),
        ],
    },
]

MODULE_1_ASSIGNMENTS = MODULE_2_ASSIGNMENTS

TOOLS_EXPLAINED = [
    {
        "tool": "Perplexity AI",
        "module": "Module 2 + Module 4",
        "why": "AI-powered search that cites sources — essential for research and context engineering",
        "link": "https://www.perplexity.ai",
        "description": "Perplexity AI — ask any question and get cited, up-to-date answers. Free tier available at perplexity.ai"
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
        "title": "What is Context Engineering? — Philipp Schmid",
        "url": "https://www.philschmid.de/context-engineering",
        "module": "Module 2 + Module 4",
        "note": "The definitive guide to context engineering — read before Module 2 session"
    },
    {
        "title": "How to Get the Most Out of AI Tools — Harvard Business Review",
        "url": "https://hbr.org/2023/06/how-to-use-ai-to-do-stuff-an-opinionated-guide",
        "module": "Module 2",
        "note": "Practical guide to selecting and using AI tools effectively — essential Module 2 reading"
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
        "url": "https://www.linkedin.com/feed/update/urn:li:activity:7438543789570412544/",
        "note": "Kapusta on reading weak signals before they become obvious — essential Vanguard thinking"
    },
    {
        "title": "Business as the Ultimate Form of Art: Vanguard Leadership in the AI Era",
        "url": "https://www.linkedin.com/pulse/business-ultimate-form-art-vanguard-leadership-ai-era-drazen-kapusta-lfsdf",
        "note": "Kapusta on what AI-era leadership actually looks like in practice — read before Module 3"
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
    {
        "title": "Art of Trade by Benedetto Cotrugli",
        "authors": "Dražen Kapusta",
        "url": "https://www.linkedin.com/pulse/art-trade-benedetto-cotrugli-drazen-kapusta-adxlf",
        "note": "The 15th-century merchant handbook that founded COTRUGLI — Kapusta's modern reading of it"
    },
]

KAPUSTA_WFR_ARTICLE = NEO_WORLD_ARTICLES[0]
