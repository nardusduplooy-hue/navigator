# jarvis_content.py
# Navigator content engine — week of 27 March to 2 April 2026
# Kapusta articles rotated manually by Nardus each day
# AI news updated manually each day

TALI_STEPS = {
    "2026-03-27": {
        "step": 1,
        "title": "The Three-Phase Methodology",
        "url": "https://medium.com/@talirezun/behind-the-curtain-the-three-phase-process-i-use-to-build-every-ai-coded-product-bf4671f2c4b4",
        "focus": (
            "This is the foundation the entire playbook sits on. "
            "Dr. Tali builds every AI product in three phases: Concept, Build, Refine. "
            "Read to understand how a non-developer structures a project before writing a single prompt."
        ),
        "question": (
            "Dr. Tali's Three-Phase Methodology — Concept, Build, Refine — "
            "is the foundation of her non-developer playbook. "
            "Which phase do most people skip, and what goes wrong when they do?"
        ),
        "model_answer": (
            "Most people skip the Concept phase and jump straight to Build — "
            "opening an AI tool and starting to prompt before they have clarity on what they're actually building. "
            "The result is a product that technically works but solves the wrong problem, "
            "or requires expensive rebuilds because the architecture wasn't thought through first. "
            "The Concept phase forces you to define the output, the user, and the constraints before any code is generated. "
            "That clarity is what makes the Build phase fast and the Refine phase manageable — "
            "without it, you're refining something that was never properly conceived."
        ),
    },
    "2026-03-28": {
        "step": 2,
        "title": "From Prototype to Production",
        "url": "https://medium.com/@talirezun/from-prototype-to-production-building-an-ai-widget-platform-in-30-days-23c603c91475",
        "focus": (
            "The gap between a working prototype and a production-ready product is where most projects die. "
            "Read to understand how Dr. Tali bridges that gap in 30 days — "
            "and what decisions at the prototype stage determine whether you make it to production at all."
        ),
        "question": (
            "Dr. Tali built a production-ready AI widget platform in 30 days. "
            "What is the single biggest decision at the prototype stage that determines "
            "whether a project makes it to production?"
        ),
        "model_answer": (
            "The biggest decision is scope — specifically, choosing what NOT to build in the prototype. "
            "Most non-developers try to prototype the full product, which creates something too complex to iterate on "
            "and too fragile to hand to real users. "
            "Dr. Tali's approach is to prototype the core interaction only — the one thing that proves the concept works. "
            "Everything else is a production problem. "
            "This means the prototype stays small enough to rebuild in a day, "
            "which is exactly the quality you need when real users expose the assumptions you didn't know you were making."
        ),
    },
    "2026-03-29": {
        "step": 3,
        "title": "Why I Ditched RAG Pipelines for 1M Token Context Windows",
        "url": "https://medium.com/@talirezun/why-i-ditched-rag-pipelines-for-1m-token-context-windows-d5a2982f7cce",
        "focus": (
            "This is the insight that changes how you think about AI architecture. "
            "Read to understand why retrieval-augmented generation adds complexity "
            "that large context windows now make unnecessary — "
            "and what that means for the way you build."
        ),
        "question": (
            "Dr. Tali ditched RAG pipelines in favour of 1M token context windows. "
            "This is not just a technical preference — it is a strategic choice. "
            "What category of failure does it eliminate, and why does that matter more to a non-developer than to an engineer?"
        ),
        "model_answer": (
            "It eliminates retrieval failure — the category of errors that happen when your system "
            "fetches the wrong chunk of context, or misses the relevant piece entirely. "
            "For an engineer, retrieval failure is a debugging problem: tune the embeddings, adjust the chunking strategy, "
            "rebuild the index. "
            "For a non-developer, it is a dead end — you cannot tune what you cannot see. "
            "A 1M token context window sidesteps the entire category by loading everything at once. "
            "No retrieval logic means no retrieval failure. "
            "The non-developer's superpower is not knowing how to fix complex systems — "
            "it is knowing which complexity to eliminate before it becomes a problem."
        ),
    },
    "2026-03-30": {
        "step": 4,
        "title": "From Writing Code to Directing Intelligence",
        "url": "https://medium.com/@talirezun/from-writing-code-to-directing-intelligence-five-days-inside-augment-codes-intent-7b04863808bf",
        "focus": (
            "The shift from building with AI to directing AI is the orchestration leap. "
            "Read to understand what it means to move from prompt-by-prompt interaction "
            "to designing systems where AI agents hand off work to each other — "
            "and why this is the unlock for non-developers who want to build at scale."
        ),
        "question": (
            "Dr. Tali describes a shift from writing code to directing intelligence. "
            "In practice, what does orchestration mean for a non-developer — "
            "and what breaks if you try to scale a single-agent system instead?"
        ),
        "model_answer": (
            "Orchestration means designing the handoffs — deciding which agent does what, "
            "in what order, and what it passes to the next agent. "
            "For a non-developer, this is closer to management than to engineering: "
            "you define the roles, the inputs, and the success criteria, "
            "and the agents execute. "
            "A single-agent system breaks at scale because one agent trying to do everything "
            "hits context limits, loses coherence, and produces inconsistent outputs. "
            "Orchestration solves this by keeping each agent focused on a narrow task — "
            "which also makes the system easier to debug, because when something goes wrong "
            "you know exactly which agent failed and why."
        ),
    },
    "2026-03-31": {
        "step": 5,
        "title": "How I Built an AI Marketing Team That Actually Works",
        "url": "https://medium.com/@talirezun/how-i-built-an-ai-marketing-team-that-actually-works-from-memes-to-technical-content-in-minutes-87f646608c60",
        "focus": (
            "The marketing layer is where your AI product meets the world. "
            "Read to understand how Dr. Tali built an AI-powered content system — "
            "from memes to technical articles — and what this means for how you think "
            "about distribution as part of the build, not an afterthought."
        ),
        "question": (
            "Dr. Tali built an AI marketing team that produces content from memes to technical articles. "
            "What is the underlying system design principle that makes this work — "
            "and how does it connect back to the orchestration leap in Step 4?"
        ),
        "model_answer": (
            "The principle is specialisation through role definition. "
            "Each content type — meme, LinkedIn post, technical article — has its own agent "
            "with its own prompt, tone, and output format. "
            "None of them try to do everything. "
            "This connects directly to Step 4: orchestration is not just for product logic, "
            "it applies equally to content production. "
            "The marketing layer works because it is built the same way the product is built — "
            "modular agents with clear responsibilities, coordinated by a director who defines the brief "
            "and approves the output. "
            "The insight is that distribution is a system problem, not a creativity problem, "
            "and systems can be designed, delegated, and iterated on."
        ),
    },
}

TOOL_SPOTLIGHT = {
    "2026-03-27": {
        "name": "Google Gemini",
        "url": "https://gemini.google.com",
        "action": "Login & Explore",
        "what_its_good_for": (
            "Gemini is Google's flagship AI model — your best tool for research, "
            "summarising long documents, drafting content, and working inside Google Workspace "
            "(Docs, Sheets, Gmail). If you live in Google's ecosystem, this is your daily driver. "
            "Start by asking it to summarise one of Dr. Tali's articles — "
            "then ask it a follow-up question to see how it handles context."
        ),
    },
    "2026-03-28": {
        "name": "Google AI Studio",
        "url": "https://aistudio.google.com",
        "action": "Login & Explore",
        "what_its_good_for": (
            "AI Studio is where you experiment with Gemini models directly — "
            "before wrapping them in a product. Think of it as a developer sandbox "
            "that non-developers can use too. You can test prompts, adjust temperature, "
            "and see exactly how the model responds to different instructions. "
            "Essential for understanding what is possible before you start building."
        ),
    },
    "2026-03-29": {
        "name": "Google NotebookLM",
        "url": "https://notebooklm.google.com",
        "action": "Login & Explore",
        "what_its_good_for": (
            "NotebookLM lets you upload your own documents — articles, PDFs, notes — "
            "and then have a conversation with them. "
            "Upload Dr. Tali's 5 Medium articles and ask questions you could not answer from memory. "
            "This is exactly the large-context-window principle from Step 3 in action — "
            "all your source material loaded at once, no retrieval required."
        ),
    },
    "2026-03-30": {
        "name": "Anthropic Claude Desktop",
        "url": "https://claude.ai/download",
        "action": "Create Account & Explore",
        "what_its_good_for": (
            "Claude Desktop is your thinking partner for complex reasoning, "
            "long-form writing, and nuanced analysis. "
            "Unlike browser-based tools, the desktop app stays open alongside your work "
            "and handles very long documents without losing context. "
            "It is also the foundation of the Navigator Ask tab — "
            "so understanding how Claude thinks is understanding your own tool."
        ),
    },
    "2026-03-31": {
        "name": "GitHub",
        "url": "https://github.com",
        "action": "Create Account & Explore",
        "what_its_good_for": (
            "GitHub is where your code lives, gets version-controlled, and gets deployed. "
            "You do not need to write code to use it — you need it to store, track, and share "
            "everything you build. Navigator itself runs from a GitHub repo. "
            "Create your account, explore the Navigator repo structure, "
            "and understand what a commit, a push, and a README actually mean."
        ),
    },
    "2026-04-01": {
        "name": "LM Studio",
        "url": "https://lmstudio.ai",
        "action": "Download & Install",
        "what_its_good_for": (
            "LM Studio lets you run AI models locally on your own machine — "
            "no internet required, no API costs, complete privacy. "
            "This is the advanced option: it requires a capable laptop and some patience to set up, "
            "but it gives you a deeper understanding of how models actually work. "
            "Explore it with curiosity, not pressure — it is in your stack to know it exists."
        ),
    },
    "2026-04-02": {
        "name": "n8n",
        "url": "https://n8n.io",
        "action": "Login & Explore",
        "what_its_good_for": (
            "n8n is a workflow automation tool — the non-developer's orchestration layer. "
            "You connect apps, triggers, and AI agents visually, without writing code. "
            "Think of it as the glue between all the tools in your stack. "
            "By Session 9 you want to understand what a workflow node is "
            "and be able to imagine one automation you would build for yourself."
        ),
    },
}

KAPUSTA_TODAY = {
    "url": "https://www.linkedin.com/pulse/centaur-doctrine-how-vanguard-leaders-win-neo-drazen-kapusta-ytnzf/",
    "title": "The Centaur Doctrine: How Vanguard Leaders Win the NEO Battlefield",
    "description": "Kapusta on the human-AI hybrid model that defines Vanguard leadership — essential reading before Session 9.",
}

SUPPLEMENTARY_RESOURCE = {
    "title": "How To Master Google Gemini in 2026",
    "url": "https://www.youtube.com/watch?v=-_FizlRlfYs&t=140s",
    "description": "Your foundation resource for the week — watch before or alongside the Gemini tool spotlight.",
}

AI_NEWS_TODAY = {
    "headline": "OpenAI's Sora gets the axe",
    "source": "therundown.ai — free to read",
}

MODULE_2_TOOLS_FULL = [
    {"name": "Google Gemini",            "url": "https://gemini.google.com",         "action": "Login & Explore"},
    {"name": "Google AI Studio",         "url": "https://aistudio.google.com",        "action": "Login & Explore"},
    {"name": "Google NotebookLM",        "url": "https://notebooklm.google.com",      "action": "Login & Explore"},
    {"name": "Anthropic Claude Desktop", "url": "https://claude.ai/download",          "action": "Create Account & Explore"},
    {"name": "GitHub",                   "url": "https://github.com",                 "action": "Create Account & Explore"},
    {"name": "LM Studio",                "url": "https://lmstudio.ai",                "action": "Download & Install (advanced)"},
    {"name": "n8n",                      "url": "https://n8n.io",                      "action": "Login & Explore"},
]
