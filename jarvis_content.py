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
        "title": "The Context Engineer's Toolkit: Essential AI Tools for All Levels",
        "url": "https://medium.com/@talirezun/the-context-engineers-toolkit-essential-ai-tools-for-all-levels-3f383a6f1c07",
        "note": "Read before Module 2"
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
        "tool": "Google Gemini",
        "module": "Module 2",
        "why": "Google's flagship AI assistant — your starting point for prompt engineering and model comparison",
        "link": "https://gemini.google.com/",
        "description": "Login at gemini.google.com — explore prompting, compare models and get familiar with Google's AI ecosystem"
    },
    {
        "tool": "Google AI Studio",
        "module": "Module 2",
        "why": "The beginner MVP build track — where you experiment with system instructions and Gemini models directly",
        "link": "https://aistudio.google.com/",
        "description": "Sign up free at aistudio.google.com — run prompts, set system instructions and compare Gemini model outputs"
    },
    {
        "tool": "Google NotebookLM",
        "module": "Module 2",
        "why": "Your personal AI research assistant — upload course material and interrogate it",
        "link": "https://notebooklm.google.com/",
        "description": "Login at notebooklm.google.com — upload Dr. Tali's articles and ask questions you couldn't answer before"
    },
    {
        "tool": "Anthropic Claude Desktop",
        "module": "Module 2",
        "why": "Claude running locally as an agent on your machine — the bridge to MCP in Module 3",
        "link": "https://claude.ai/download",
        "description": "Download at claude.ai/download — install and connect to local tools. Foundation for Module 3 agent work"
    },
    {
        "tool": "GitHub",
        "module": "Module 2",
        "why": "Navigator already lives here — you need to understand what it is doing",
        "link": "https://github.com/",
        "description": "Sign up at github.com — Git and GitHub for beginners: youtube.com/watch?v=RGOj5yH7evk (12 min)"
    },
    {
        "tool": "LM Studio",
        "module": "Module 2",
        "why": "Run AI models locally on your Mac — no data leaves your machine",
        "link": "https://lmstudio.ai/",
        "description": "Download free at lmstudio.ai — run Llama, Mistral and more privately on your own machine"
    },
    {
        "tool": "n8n",
        "module": "Module 2",
        "why": "Automation layer for Modules 2 and 3 — connect apps and build workflows without code",
        "link": "https://n8n.io/",
        "description": "Try free at n8n.io — build your first automated workflow connecting two apps in under 10 minutes"
    },
]

SUPPLEMENTARY = [
    {
        "title": "Dr. Tali — The Context Engineer's Toolkit",
        "url": "https://medium.com/@talirezun/the-context-engineers-toolkit-essential-ai-tools-for-all-levels-3f383a6f1c07",
        "module": "Module 2",
        "note": "The tool map for Module 2 — read this before setting up your stack"
    },
    {
        "title": "Dr. Tali — Data Sovereignty in the AI Age",
        "url": "https://medium.com/@talirezun/data-sovereignty-in-the-ai-age-building-your-own-private-chatgpt-a83c96e342a0",
        "module": "Module 2",
        "note": "Why running models locally matters — essential before LM Studio setup"
    },
    {
        "title": "What is Context Engineering? — Philipp Schmid",
        "url": "https://www.philschmid.de/context-engineering",
        "module": "Module 2",
        "note": "The definitive guide to context engineering — read before Session 9"
    },
    {
        "title": "How to Get the Most Out of AI Tools — Harvard Business Review",
        "url": "https://hbr.org/2023/06/how-to-use-ai-to-do-stuff-an-opinionated-guide",
        "module": "Module 2",
        "note": "Practical guide to selecting and using AI tools effectively"
    },
    {
        "title": "Git and GitHub for Beginners — freeCodeCamp",
        "url": "https://www.youtube.com/watch?v=RGOj5yH7evk",
        "module": "Module 2",
        "note": "12 min video — watch before touching the Navigator codebase"
    },
    {
        "title": "Hugging Face — Getting Started",
        "url": "https://huggingface.co/docs/hub/index",
        "module": "Module 2",
        "note": "How to find, download, and run open-source models from the Hub"
    },
    {
        "title": "Cloudflare Workers AI — Getting Started",
        "url": "https://developers.cloudflare.com/workers-ai/",
        "module": "Module 2",
        "note": "Run AI models at the edge — Cloudflare's developer docs"
    },
    {
        "title": "Augment Code — Documentation",
        "url": "https://docs.augmentcode.com/",
        "module": "Module 2",
        "note": "Set up Augment Code in VS Code — your AI pair programmer for the build modules"
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
        "title": "Subsidiary Alliance Reforged: How the 1798 Playbook Defines Modern AI Strategy",
        "url": "https://www.linkedin.com/pulse/subsidiary-alliance-reforged-how-1798-playbook-defines-drazen-kapusta-jj0nf/",
        "note": "Kapusta on how historical alliance structures map directly to AI partnership strategy today"
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
