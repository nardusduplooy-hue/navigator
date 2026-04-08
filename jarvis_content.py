# jarvis_content.py
# Navigator content engine — week of 27 March to 2 April 2026
# Kapusta articles rotated manually by Nardus each day
# AI news updated manually each day

TALI_STEPS = {
    "2026-03-27": {
        "step": 1,
        "title": "The Three-Phase Methodology",
        "url": "https://www.linkedin.com/feed/update/urn:li:activity:7442446986844217344/?originTrackingId=nVrfQLx%2BhzdhoIHjRcjVrw%3D%3D",
        "focus": (
            "This is the foundation the entire playbook sits on. "
            "Dr. Tali builds every AI product in three phases: Concept, Build, Refine. "
            "Read to understand how a non-developer structures a project before writing a single prompt."
        ),
        "question": (
            "Dr. Tali's Three-Phase Methodology — Concept, Build, Refine — "
            "is the foundation of his non-developer playbook. "
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
        "title": "The Orchestration Leap — From Writing Code to Directing Intelligence",
        "url": "https://medium.com/@talirezun/from-writing-code-to-directing-intelligence-five-days-inside-augment-codes-intent-7b04863808bf",
        "focus": (
            "This is where it clicks — the shift from writing code to directing intelligence. "
            "Read to understand what orchestration actually means in practice, "
            "and why it changes the role of the non-developer from observer to conductor. "
            "This is the unlock for building at scale without an engineering background."
        ),
        "question": (
            "Dr. Tali describes the Orchestration Leap as the moment a non-developer "
            "stops writing instructions and starts directing intelligence. "
            "What is the critical difference between prompting an AI and orchestrating one — "
            "and why does that distinction determine whether you become a Vanguard builder or remain a power user?"
        ),
        "model_answer": (
            "Prompting is a single conversation — you give an instruction, you get an output, the interaction ends. "
            "Orchestration is a system — you define roles, handoffs, and success criteria for multiple agents "
            "working in sequence or in parallel. "
            "The difference is permanence and scale: a prompt disappears when the session ends, "
            "an orchestrated system runs without you. "
            "A power user gets better outputs from a single model. "
            "A Vanguard builder designs systems where models hand work to each other, "
            "check each other's outputs, and produce results no single prompt could achieve. "
            "The distinction is not technical — it is architectural. "
            "You stop asking what the AI can do for you right now, "
            "and start designing what it can do for you while you sleep."
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
    "2026-04-09": {
        "step": "Module 3 — Day 4",
        "title": "Exploring Early Indicators of AGI in Coding Agents",
        "url": "https://medium.com/@talirezun/exploring-early-indicators-of-agi-in-coding-agents-bc671f98eddc",
        "focus": (
            "The most provocative article in the Module 3 series. "
            "Dr. Tali looks at what coding agents are already doing "
            "that starts to look less like automation and more like reasoning."
        ),
        "question": (
            "Dr. Tali identifies early indicators of AGI-like behaviour in coding agents — "
            "moments where the agent does something the user did not explicitly ask for, "
            "but that was clearly the right thing to do. "
            "What is the significance of this for a non-developer building with AI today? "
            "And what is the one question every builder should be asking "
            "as agents move from executing instructions to exercising judgment?"
        ),
        "model_answer": (
            "The significance is that the contract between human and machine is changing. "
            "When an agent only executes instructions, the human is fully accountable — "
            "they specified every step. "
            "When an agent starts exercising judgment — filling gaps, making inferences, "
            "choosing approaches the user never specified — accountability becomes shared. "
            "For a non-developer, this is both an unlock and a risk. "
            "The unlock: you no longer need to anticipate every step of the build. "
            "The risk: you may not notice when the agent's judgment diverges from your intent. "
            "The one question every builder should be asking is: "
            "did the agent do what I wanted, or did it do what I said? "
            "Those are not always the same thing. "
            "As agents move closer to AGI-like behaviour, "
            "the builder's most important skill is not prompting — "
            "it is verification: the ability to look at an output and know "
            "whether it actually serves the goal, not just the instruction."
        ),
    },
    "2026-04-08": {
        "step": "Module 3 — Day 3",
        "title": "From English to Code: Building Production SaaS with Claude Desktop",
        "url": "https://medium.com/@talirezun/from-english-to-code-building-production-saas-with-claude-desktop-3ee9c787f5be",
        "focus": (
            "Dr. Tali built a production SaaS product using nothing but English and Claude Desktop. "
            "Read the article before answering today's question."
        ),
        "question": (
            "Dr. Tali built a production SaaS product by describing what he wanted in plain English "
            "and letting Claude Desktop handle the code. "
            "What does this mean for how non-developers should think about the boundary "
            "between their role and the machine's role in a build? "
            "And what is the one thing a non-developer must still own — "
            "that no coding agent can do for them?"
        ),
        "model_answer": (
            "It means the boundary has moved — permanently. "
            "The non-developer's role is no longer to stay out of the build. "
            "It is to own the specification: what the product does, who it is for, "
            "what good looks like, and when to stop. "
            "The coding agent handles implementation. The non-developer handles intent. "
            "That division is not a limitation — it is a leverage point. "
            "The one thing a non-developer must still own is judgment about the output. "
            "Does this work the way a real user would expect? "
            "Is this solving the right problem? "
            "Is this ready to ship, or does it just look ready? "
            "A coding agent cannot answer those questions — "
            "it has no skin in the game, no user empathy, no business context. "
            "The non-developer who combines clear specification with honest output evaluation "
            "is not a lesser builder. They are a more dangerous one."
        ),
    },
    "2026-04-07": {
        "step": "Module 3 — Day 2",
        "title": "The Year I Started Coding with AI: My Coding Agent Journey",
        "url": "https://medium.com/@talirezun/the-year-i-started-coding-with-ai-my-coding-agent-journey-431f6f25afe1",
        "focus": (
            "Dr. Tali's coding agent journey — read before your first hands-on coding session."
        ),
        "question": (
            "Dr. Tali spent a year coding with AI before writing about it. "
            "He describes a shift in how he thinks about building — not writing code, but directing it. "
            "What is the most important mindset shift a non-developer needs to make "
            "before their first coding agent session — "
            "and what is the biggest mistake to avoid?"
        ),
        "model_answer": (
            "The most important mindset shift is from author to director. "
            "A non-developer approaching a coding agent for the first time "
            "instinctively tries to understand every line of code produced — "
            "as if they need to earn the right to use it. That instinct is wrong and slows everything down. "
            "The coding agent is not a teacher. It is a contractor. "
            "Your job is to specify the outcome clearly, review whether it works, and iterate — "
            "not to understand the implementation. "
            "The biggest mistake is over-specifying the how instead of the what. "
            "When you tell the agent exactly how to solve a problem, "
            "you constrain it to your own limited technical knowledge. "
            "When you describe what you need clearly, you unlock its full capability. "
            "The non-developer's advantage is not knowing enough to get in the way."
        ),
    },
    "2026-04-06": {
        "step": "Module 3 — Day 1",
        "title": "Understanding AI Agents: From Chatbots to Autonomous Digital Workers",
        "url": "https://medium.com/@talirezun/understanding-ai-agents-from-chatbots-to-autonomous-digital-workers-407217d84695",
        "focus": (
            "The foundation of Module 3. Read Dr. Tali's core article "
            "before answering today's question."
        ),
        "question": (
            "Dr. Tali distinguishes between chatbots and autonomous AI agents. "
            "A chatbot responds. An agent acts. "
            "In your own words, what is the critical difference between the two — "
            "and what does an agent need that a chatbot does not? "
            "Give one example from your own business or role where an agent "
            "would do something a chatbot simply cannot."
        ),
        "model_answer": (
            "The critical difference is autonomy over action. "
            "A chatbot waits for a prompt and returns a response — the human remains in the loop for every step. "
            "An agent is given a goal and a set of tools, and it decides how to achieve that goal "
            "across multiple steps without waiting for human input at each one. "
            "What an agent needs that a chatbot does not: tool access (the ability to take actions in the world — "
            "search, write, send, create), memory (to retain context across steps), "
            "and a planning loop (to evaluate its own progress and adjust). "
            "Example: a chatbot can draft a competitive analysis when asked. "
            "An agent can be given the goal 'monitor our top three competitors and alert me to any pricing changes' "
            "— and run that task every day, unsupervised, flagging only when something changes. "
            "The chatbot answers questions. The agent handles workflows. "
            "That distinction is what Module 3 is built on."
        ),
    },
    "2026-04-05": {
        "step": "Module 3",
        "title": "AI Agents — From Chatbots to Autonomous Workers",
        "url": "https://medium.com/@talirezun/understanding-ai-agents-from-chatbots-to-autonomous-digital-workers-407217d84695",
        "focus": (
            "Module 3 opens with the foundational question: what is an AI agent, "
            "and how is it different from a chatbot? "
            "Read Dr. Tali's core article before answering today's question."
        ),
        "question": (
            "Dr. Tali distinguishes between chatbots and autonomous AI agents. "
            "A chatbot responds. An agent acts. "
            "In your own words, what is the critical difference between the two — "
            "and what does an agent need that a chatbot does not? "
            "Give one example from your own business or role where an agent "
            "would do something a chatbot simply cannot."
        ),
        "model_answer": (
            "The critical difference is autonomy over action. "
            "A chatbot waits for a prompt and returns a response — the human remains in the loop for every step. "
            "An agent is given a goal and a set of tools, and it decides how to achieve that goal "
            "across multiple steps without waiting for human input at each one. "
            "What an agent needs that a chatbot does not: tool access (the ability to take actions in the world — "
            "search, write, send, create), memory (to retain context across steps), "
            "and a planning loop (to evaluate its own progress and adjust). "
            "Example: a chatbot can draft a competitive analysis when asked. "
            "An agent can be given the goal 'monitor our top three competitors and alert me to any pricing changes' "
            "— and run that task every day, unsupervised, flagging only when something changes. "
            "The chatbot answers questions. The agent handles workflows. "
            "That distinction is what Module 3 is built on."
        ),
    },
    "2026-04-04": {
        "step": "Session 9",
        "title": "Module 2 — Build, Deploy, Evaluate",
        "url": "https://medium.com/@talirezun",
        "focus": (
            "Session 9 is today. Before you join, sharpen your thinking on "
            "what it means to move from exploring tools to actually building with them."
        ),
        "question": (
            "Module 2 asks you to build and deploy AI-powered applications "
            "using no-code and low-code tools — and to evaluate AI agent maturity "
            "before committing them to real business use. "
            "Think about a workflow or process in your business or role "
            "that you could hand to an AI agent today. "
            "What is the task, what tool would you use to build it, "
            "and how would you evaluate whether the agent is ready "
            "to run that task without your supervision? "
            "What would failure look like — and how would you catch it before it causes damage?"
        ),
        "model_answer": (
            "A strong answer identifies a bounded, repetitive task — not an open-ended one. "
            "Example: a weekly competitive intelligence summary. "
            "The task: monitor three competitor LinkedIn pages, summarise new posts, "
            "and deliver a digest every Monday at 08:00. "
            "Tool: n8n with a Claude API node for summarisation and a Telegram delivery node. "
            "Evaluating readiness: run the agent in parallel with your own manual process for two weeks. "
            "Compare outputs. If the agent misses a post, misattributes a quote, "
            "or produces a summary you would not send to a colleague — it is not ready unsupervised. "
            "Failure modes to watch: hallucinated content presented as fact, "
            "missed posts due to feed changes, and summaries that lose critical nuance. "
            "The maturity test is simple: would you stake your professional reputation on this output "
            "without reading it first? "
            "If yes — deploy. If no — refine the prompt, tighten the context, and test again. "
            "That loop is what Module 2 is training you to run."
        ),
    },
    "2026-04-03": {
        "step": "Module 2 Prep",
        "title": "Module 2 — AI Tools, Context Engineering & Business Strategy",
        "url": "https://medium.com/@talirezun",
        "focus": (
            "Session 9 is tomorrow. Today is about connecting what you've read "
            "to what you'll be expected to think, build, and decide as a Vanguard leader."
        ),
        "question": (
            "You have explored several AI tools this week — from Claude and NotebookLM "
            "to LM Studio and n8n. Module 2 asks you to do more than explore: "
            "it asks you to select, design, and deploy. "
            "Choose ONE specific business problem you face in your current role or venture. "
            "Which tool from your personal AI stack would you use to address it, "
            "and what context engineering strategy would you apply to maximise its effectiveness? "
            "Be specific: name the tool, describe the context you would load, "
            "and explain how this creates a business advantage."
        ),
        "model_answer": (
            "A strong answer is specific and personal — not generic. "
            "Example: a business development professional facing slow proposal generation "
            "would choose Claude Desktop for its long-context reasoning. "
            "Context engineering strategy: load the client's annual report, "
            "the company's service catalogue, and three winning proposals as reference documents "
            "before prompting — giving the model the full picture rather than a bare instruction. "
            "This eliminates the back-and-forth of under-specified prompts "
            "and produces a first draft that already reflects client language and priorities. "
            "The business advantage: proposal turnaround drops from two days to two hours, "
            "and quality improves because the context is richer than any single human could hold in working memory. "
            "The Module 2 insight: the tool is rarely the differentiator — "
            "the context you bring to it is. "
            "That is context engineering as business strategy."
        ),
    },
    "2026-04-02": {
        "step": "1-5 + n8n",
        "title": "The Complete Playbook Meets Orchestration — n8n as Your First System",
        "url": "https://n8n.io",
        "focus": (
            "You have read the full Non-Developer's Playbook. "
            "Today's question connects the orchestration leap from Step 4 "
            "to the tool you are exploring today — n8n. "
            "The question is not theoretical: it is about what you will actually build."
        ),
        "question": (
            "Dr. Tali's Step 4 describes the shift from prompting to orchestration — "
            "from single interactions to systems that run without you. "
            "n8n is a visual workflow tool that lets non-developers build exactly those systems. "
            "Describe one concrete workflow you would build in n8n "
            "that would save you real time before Session 9 on Saturday. "
            "What are the trigger, the steps, and the output?"
        ),
        "model_answer": (
            "A strong answer names a specific, small workflow — not an ambitious future system. "
            "Example: a morning briefing filter that monitors a specific LinkedIn hashtag, "
            "pulls the top post of the day, and sends a summary to your Telegram at 07:00. "
            "Trigger: a schedule node firing at 07:00 each morning. "
            "Steps: an HTTP request node hitting the LinkedIn feed or RSS equivalent, "
            "a Claude API node summarising the result in two sentences, "
            "a Telegram node delivering it to your chat. "
            "Output: a daily 07:00 Telegram message with one sentence on what the AI community is talking about. "
            "The key insight is that orchestration is not abstract — "
            "it is a trigger, a sequence, and an output. "
            "If you can describe those three things, you can build it. "
            "That is what Session 9 is preparing you to do."
        ),
    },
    "2026-04-01": {
        "step": "1-5",
        "title": "The Complete Non-Developer’s Playbook — All Five Steps",
        "url": "https://medium.com/@talirezun",
        "focus": (
            "You have now read all five steps of the Non-Developer’s Playbook. "
            "Today is about synthesis — connecting the arc from Concept to Orchestration to Distribution "
            "and understanding how these five steps form one complete system for building with AI."
        ),
        "question": (
            "Having read all five steps of Dr. Tali’s Non-Developer’s Playbook, "
            "describe the arc of the system in your own words. "
            "What is the single most important insight from the series — "
            "and how will you apply it before Session 9 on Saturday?"
        ),
        "model_answer": (
            "The arc moves from clarity to construction to scale: "
            "Step 1 establishes the three-phase discipline that prevents you from building the wrong thing. "
            "Step 2 closes the gap between prototype and production by constraining scope ruthlessly. "
            "Step 3 eliminates retrieval complexity by loading full context — simplicity as a strategic choice. "
            "Step 4 makes the leap from prompting to orchestration — from one-off interactions to systems that run without you. "
            "Step 5 extends that same logic to distribution — marketing is not a separate activity, it is another system to design. "
            "The single most important insight: every step is about eliminating a category of complexity before it becomes a problem. "
            "The non-developer’s advantage is not technical skill — it is the willingness to ask which complexity should not exist at all."
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
            "so understanding how Claude thinks is understanding your own tool. "
            "This is Step 4 in action: you are not just using a tool, "
            "you are learning to direct one."
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
    "url": "https://www.linkedin.com/pulse/intro-neo-era-drazen-kapusta-veb2f/?trackingId=DEtk7TehrOGcRl4Unt1wDw%3D%3D",
    "title": "Intro to the NEO Era",
    "description": "Kapusta on what it means to lead at the threshold of a new era — and why the rules of the game have fundamentally changed.",
}

SUPPLEMENTARY_RESOURCE = {
    "title": "n8n — Workflow Automation for Technical People",
    "url": "https://n8n.io",
    "description": "n8n is the visual orchestration layer for your AI stack — connect apps, triggers, and agents without writing code. Create a free account and explore what a workflow node actually looks like before Session 9.",
}

AI_NEWS_TODAY = {
    "headline": "LLM-referred traffic converts at 30-40% — and most enterprises aren't optimizing for it",
    "source": "VentureBeat AI",
}

JTBD_STATUS = (
    "JTBD: Read the 5 series articles and engage on LinkedIn — "
    "https://www.linkedin.com/feed/update/urn:li:activity:7442446986844217344/"
)

MODULE_2_TOOLS_FULL = [
    {"name": "Google Gemini",            "url": "https://gemini.google.com",         "action": "Login & Explore"},
    {"name": "Google AI Studio",         "url": "https://aistudio.google.com",        "action": "Login & Explore"},
    {"name": "Google NotebookLM",        "url": "https://notebooklm.google.com",      "action": "Login & Explore"},
    {"name": "Anthropic Claude Desktop", "url": "https://claude.ai/download",          "action": "Create Account & Explore"},
    {"name": "GitHub",                   "url": "https://github.com",                 "action": "Create Account & Explore"},
    {"name": "LM Studio",                "url": "https://lmstudio.ai",                "action": "Download & Install (advanced)"},
    {"name": "n8n",                      "url": "https://n8n.io",                      "action": "Login & Explore"},
]

# ─────────────────────────────────────────────
# MODULE 3 ARTICLES — daily drip 6-9 April
# ─────────────────────────────────────────────

MODULE3_ARTICLES = {
    "2026-04-06": [
        {
            "label": "Core reading — essential for understanding agent fundamentals:",
            "title": "Understanding AI Agents: From Chatbots to Autonomous Digital Workers",
            "url": "https://medium.com/@talirezun/understanding-ai-agents-from-chatbots-to-autonomous-digital-workers-407217d84695",
        },
    ],
    "2026-04-07": [
        {
            "label": "Read before coding agent sessions:",
            "title": "The Year I Started Coding with AI: My Coding Agent Journey",
            "url": "https://medium.com/@talirezun/the-year-i-started-coding-with-ai-my-coding-agent-journey-431f6f25afe1",
        },
    ],
    "2026-04-08": [
        {
            "label": "Read before hands-on labs:",
            "title": "From English to Code: Building Production SaaS with Claude Desktop",
            "url": "https://medium.com/@talirezun/from-english-to-code-building-production-saas-with-claude-desktop-3ee9c787f5be",
        },
    ],
    "2026-04-09": [
        {
            "label": "Read before AGI discussion session:",
            "title": "Exploring Early Indicators of AGI in Coding Agents",
            "url": "https://medium.com/@talirezun/exploring-early-indicators-of-agi-in-coding-agents-bc671f98eddc",
        },
    ],
}

# ─────────────────────────────────────────────
# FUTURE LAB LEARNING — daily drip 28 Mar onwards
# ─────────────────────────────────────────────

FUTURE_LAB = {
    "2026-04-09": [
        {
            "title": "The Fog of Federation — A European Consortium and the Battle for the Sovereign Cloud",
            "url": "https://drive.google.com/file/d/1jfHOEs6Hlkp4YRdbcWGUNx_x8Qypq8cC/view?usp=sharing",
            "author": "Cotrugli Business School",
        },
    ],
    "2026-04-08": [
        {
            "title": "Vanguard Intelligence Systems (VIS): An AI-Augmented Framework for Decision-Making in the NEO Era",
            "url": "https://drive.google.com/file/d/12Ni10rr9TCkkGI-hbJl9a6WZJxi7HdUY/view?usp=sharing",
            "author": "Kapusta & Stručić",
        },
    ],
    "2026-04-05": [
        {
            "title": "The Fog of Federation — A European Consortium and the Battle for the Sovereign Cloud",
            "url": "https://drive.google.com/file/d/1jfHOEs6Hlkp4YRdbcWGUNx_x8Qypq8cC/view?usp=sharing",
            "author": "Cotrugli Business School",
        },
    ],
    "2026-04-06": [
        {
            "title": "Vanguard Intelligence Systems (VIS): An AI-Augmented Framework for Decision-Making in the NEO Era",
            "url": "https://drive.google.com/file/d/12Ni10rr9TCkkGI-hbJl9a6WZJxi7HdUY/view?usp=sharing",
            "author": "Kapusta & Stručić",
        },
    ],
    "2026-04-07": [
        {
            "title": "The Six-Month Hormuz Scenario",
            "url": "https://docs.google.com/document/d/1dkpoE_F7jrg0frnzQfyOldkM0fifjXkZ/edit?usp=sharing&ouid=100173679485664698153&rtpof=true&sd=true",
            "author": "Dražen Kapusta",
        },
    ],
    "2026-03-28": [
        {
            "title": "The Fog of Federation — A European Consortium and the Battle for the Sovereign Cloud",
            "url": "https://drive.google.com/file/d/1jfHOEs6Hlkp4YRdbcWGUNx_x8Qypq8cC/view?usp=sharing",
            "author": "Cotrugli Business School",
        },
    ],
    "2026-03-29": [
        {
            "title": "The Fog of Federation — A European Consortium and the Battle for the Sovereign Cloud",
            "url": "https://drive.google.com/file/d/1jfHOEs6Hlkp4YRdbcWGUNx_x8Qypq8cC/view?usp=sharing",
            "author": "Cotrugli Business School",
        },
        {
            "title": "The Six-Month Hormuz Scenario",
            "url": "https://docs.google.com/document/d/1dkpoE_F7jrg0frnzQfyOldkM0fifjXkZ/edit?usp=sharing&ouid=100173679485664698153&rtpof=true&sd=true",
            "author": "Dražen Kapusta",
        },
    ],
    "2026-03-30": [
        {
            "title": "The Fog of Federation — A European Consortium and the Battle for the Sovereign Cloud",
            "url": "https://drive.google.com/file/d/1jfHOEs6Hlkp4YRdbcWGUNx_x8Qypq8cC/view?usp=sharing",
            "author": "Cotrugli Business School",
        },
        {
            "title": "The Six-Month Hormuz Scenario",
            "url": "https://docs.google.com/document/d/1dkpoE_F7jrg0frnzQfyOldkM0fifjXkZ/edit?usp=sharing&ouid=100173679485664698153&rtpof=true&sd=true",
            "author": "Dražen Kapusta",
        },
        {
            "title": "Vanguard Intelligence Systems (VIS): An AI-Augmented Framework for Decision-Making in the NEO Era",
            "url": "https://drive.google.com/file/d/12Ni10rr9TCkkGI-hbJl9a6WZJxi7HdUY/view?usp=sharing",
            "author": "Kapusta & Stručić",
        },
    ],
}

FUTURE_LAB_FULL = [
    {
        "title": "The Fog of Federation — A European Consortium and the Battle for the Sovereign Cloud",
        "url": "https://drive.google.com/file/d/1jfHOEs6Hlkp4YRdbcWGUNx_x8Qypq8cC/view?usp=sharing",
        "author": "Cotrugli Business School",
    },
    {
        "title": "The Six-Month Hormuz Scenario",
        "url": "https://docs.google.com/document/d/1dkpoE_F7jrg0frnzQfyOldkM0fifjXkZ/edit?usp=sharing&ouid=100173679485664698153&rtpof=true&sd=true",
        "author": "Dražen Kapusta",
    },
    {
        "title": "Vanguard Intelligence Systems (VIS): An AI-Augmented Framework for Decision-Making in the NEO Era",
        "url": "https://drive.google.com/file/d/12Ni10rr9TCkkGI-hbJl9a6WZJxi7HdUY/view?usp=sharing",
        "author": "Kapusta & Stručić",
    },
]
