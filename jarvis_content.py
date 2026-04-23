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
    "2026-04-24": {
        "step": "Module 3 Homework — Business Agility Day 1",
        "title": "Two things, one lesson",
        "url": "https://medium.com/@talirezun",
        "focus": "Business Agility starts today. Homework deadline in five days. Both are the same lesson.",
        "question": (
            "The Business Agility module starts today and your homework deadline is in five days. "
            "Two things are competing for your attention. This is not a problem — it is the point. "
            "A Vanguard leader does not choose between learning and building. They do both in parallel. "
            "One question: what is the single most useful thing from the Business Agility session today "
            "that you could apply directly to your homework build? "
            "Come out of the session looking for that connection."
        ),
        "model_answer": (
            "Business agility is not a theory — it is an operating principle for building under uncertainty. "
            "The students who get the most out of today's session are the ones who walk in with a build in progress. "
            "Why? Because every agility concept lands differently when you have a real project to map it to. "
            "Iteration cycles, minimum viable output, adapting to feedback — "
            "these are not abstract when you are three prompts into a coding agent session "
            "and your first version broke. "
            "The homework and the module are not competing. They are the same lesson from two different angles. "
            "Pay attention to both today."
        ),
    },
    "2026-04-23": {
        "step": "Module 3 Homework — Day 4",
        "title": "One action today",
        "url": "https://medium.com/@talirezun",
        "focus": "Six days to deadline. Stop planning. Start building.",
        "question": (
            "Six days to the homework deadline. Yesterday you named your blocker. Today is about one action. "
            "Not a plan — one action. "
            "Open your coding tool of choice right now and do one thing: "
            "describe your app or game to it in plain English and ask it to build a first version. "
            "Don't refine the prompt. Don't research first. Just send it. "
            "What did you get?"
        ),
        "model_answer": (
            "The first output from a coding agent is never the final product — it is a starting point. "
            "Most people are disappointed by the first version and stop. The builders iterate. "
            "The gap between a first attempt and a working product is not talent or technical skill — "
            "it is the number of iterations. "
            "Each prompt refines the output. Each broken version teaches you what to specify more clearly. "
            "The student who sends ten imperfect prompts today is further ahead "
            "than the one who spends the day planning the perfect first prompt. "
            "Your task today is not to build something good. It is to build something that exists. "
            "Start there."
        ),
    },
    "2026-04-22": {
        "step": "Module 3 Homework — Day 3",
        "title": "Name your blocker",
        "url": "https://medium.com/@talirezun",
        "focus": "Seven days to deadline. If you haven't started, name the blocker.",
        "question": (
            "Seven days to the homework deadline. Some of you have started. Some of you haven't. "
            "If you are in the second group, this question is for you: "
            "what is the specific thing that is stopping you? "
            "Not a general feeling — a specific blocker. "
            "Is it that you don't know which tool to use? "
            "You can't decide what to build? "
            "You started and it broke? "
            "Name the blocker out loud. That is the first step to removing it."
        ),
        "model_answer": (
            "Every build blocker falls into one of three categories: "
            "decision paralysis, technical failure, or perfectionism. "
            "Decision paralysis: you have too many options and haven't chosen one. "
            "Fix — pick the simplest possible idea and start. You can change it later. "
            "Technical failure: you tried something and it didn't work. "
            "Fix — describe exactly what broke to your coding agent and ask it to fix it. That is the whole job. "
            "Perfectionism: you have an idea but it doesn't feel good enough to build. "
            "Fix — it doesn't need to be good. It needs to run in a browser and do one thing. "
            "The homework is not a product launch. It is a proof that you can direct an AI to build something. "
            "Seven days is enough. The blocker is not time."
        ),
    },
    "2026-04-21": {
        "step": "Module 3 Homework — Day 2",
        "title": "Your one-sentence build brief",
        "url": "https://medium.com/@talirezun",
        "focus": "Nine days to the homework deadline. Start with one sentence.",
        "question": (
            "The Module 3 homework deadline is Wednesday 29 April. You have nine days. "
            "The task is simple: build something that works and runs in a browser. "
            "Before you open a single tool, answer this: "
            "what is the one thing your app or game needs to do — in one sentence? "
            "Not what it might do eventually. "
            "What does it do on day one, for one user, in one interaction? "
            "That sentence is your build brief. Write it down before you start."
        ),
        "model_answer": (
            "The biggest mistake in any first build is starting without a clear one-sentence brief. "
            "'I want to build an AI tool that helps people' is not a brief — it is a wish. "
            "'A browser game where you guess the country from three AI-generated clues' is a brief. "
            "It names the format, the interaction, and the outcome. "
            "Everything else — design, features, complexity — comes after that sentence exists. "
            "The coding agents are powerful enough to build almost anything you can describe. "
            "The constraint is never the tool. It is always the clarity of the instruction. "
            "Write your one sentence today. That is the whole task. "
            "The build follows naturally once you have it."
        ),
    },
    "2026-04-20": {
        "step": "Module 4 — Context Engineering",
        "title": "Module 4 — Context Engineering: the new core skill",
        "url": "https://medium.com/@talirezun/from-prompts-to-precision-the-art-science-of-context-engineering-cebd47462b1c",
        "focus": "Module 4 opens with context engineering. This is the skill that separates power users from builders.",
        "question": (
            "Module 4 is about context engineering — the emerging skill that sits between prompting and architecture. "
            "Before you dive into this week's reading, one question: "
            "think about the last time an AI gave you a disappointing output. "
            "With what you now know, was the problem the model — or was it the context you gave it? "
            "Be specific about what was missing and how you would engineer it differently today."
        ),
        "model_answer": (
            "Almost every disappointing AI output is a context problem, not a model problem. "
            "The model can only work with what it receives. "
            "If the output was vague, the context lacked specificity. "
            "If it missed the point, the context didn't define the goal clearly enough. "
            "If it felt generic, the context contained no examples, constraints, or role definition. "
            "Context engineering is the discipline of closing that gap — "
            "not by prompting better in the moment, but by designing the information environment the model operates in. "
            "This week's reading will give you the vocabulary and the framework. "
            "The question above is your starting point: find your own example of a context failure "
            "and you will understand the solution before you've read a word."
        ),
    },
    "2026-04-19": {
        "step": "Post Session 10 — Sunday reflection",
        "title": "Post-Session 10 — What are you doing with it this week?",
        "url": "https://medium.com/@talirezun",
        "focus": "Session 10 is done. One question before the week begins.",
        "question": (
            "Session 10 is done. You have now completed three full modules of Chasing Jarvis. "
            "Before the week ahead begins, one question: "
            "what is the single most useful thing you are walking away with from yesterday's session — "
            "not from the whole programme, just from yesterday? "
            "And what is the first thing you will do with it this week?"
        ),
        "model_answer": (
            "The most useful Session 10 takeaways are always specific and immediate — "
            "not inspirational, but actionable. "
            "'I now know how to set up a trigger in n8n' is more valuable than 'I feel more confident about AI.' "
            "The second part of the question is the harder one: what will you actually do this week? "
            "Not eventually. This week. "
            "The gap between insight and action is where most learning dies. "
            "The students who compound fastest through this programme are not the ones who absorb the most in sessions — "
            "they are the ones who do something small with it before the next one. "
            "What is your something small?"
        ),
    },
    "2026-04-18": {
        "step": "Session 10 — Chasing Jarvis Module 3",
        "title": "Session 10 — What capability are you walking in for?",
        "url": "https://medium.com/@talirezun",
        "focus": "Session 10 is today. Come with a specific capability you want to leave with.",
        "question": (
            "Session 10 is today. Three modules in, you are no longer someone who wonders whether AI is relevant "
            "to their work — you are someone who has built with it, directed it, "
            "and started to see where it can run without you. "
            "Before you join today: what is the one capability you are walking into this session wanting to leave with? "
            "Name it specifically. Not a concept — a capability. "
            "Something you can use on Monday."
        ),
        "model_answer": (
            "The best sessions are the ones where you arrive knowing what you need, not just what you want to learn. "
            "A capability is specific and actionable: not 'understand agents better' but "
            "'know how to set up a trigger-based workflow in n8n that runs without me.' "
            "Not 'get inspired' but 'leave with a clear next step for my MVP.' "
            "Session 10 is the bridge between Module 3 and what you build next. "
            "The students who get the most out of it today are the ones who treat it like a tool, not a lecture — "
            "they come with a specific gap and they leave with it closed. "
            "What is yours?"
        ),
    },
    "2026-04-17": {
        "step": "Module 3 — Session 10 eve",
        "title": "Your Vanguard Story — the night before Session 10",
        "url": "https://medium.com/@talirezun",
        "focus": "Session 10 is tomorrow. One question to sit with today.",
        "question": (
            "Session 10 is tomorrow. You have submitted your homework, you have your agent use case ready, "
            "and you have been building for three modules. "
            "Tomorrow is not a lecture — it is a reckoning. "
            "One question to sit with today: what is the one thing you built, learned, or decided "
            "in this programme so far that you would not have done without it? "
            "Be specific. That answer is your Vanguard story — "
            "and it is worth knowing before you walk into the room tomorrow."
        ),
        "model_answer": (
            "The strongest answers tomorrow will not be about tools or techniques — "
            "they will be about moments of clarity. "
            "The student who says 'I realised my original MVP was solving my problem, not my user's problem' "
            "has learned something no textbook teaches. "
            "The one who says 'I stopped waiting to understand the code and started directing the output' "
            "has made the orchestration leap for real. "
            "Your Vanguard story is not what you built. It is what changed in how you think. "
            "That is what Module 3 — and this entire programme — has been building toward. "
            "Come tomorrow knowing yours."
        ),
    },
    "2026-04-16": {
        "step": "Module 3 — Session 10 prep",
        "title": "Session 10 Prep — Your Agent Use Case",
        "url": "https://medium.com/@talirezun",
        "focus": "Session 10 is in two days. Come prepared with a concrete agent use case.",
        "question": (
            "Session 10 is in two days. Module 3 has taken you from understanding what an agent is "
            "to seeing one built in plain English. "
            "Before you show up on Saturday, do one thing: identify a single workflow in your business or role "
            "that you would hand to an agent today — not eventually, today. "
            "What is the task, what triggers it, and what does the output look like? "
            "Come to Session 10 with that answer ready."
        ),
        "model_answer": (
            "The best preparation for Session 10 is not more reading — it is a concrete use case you own. "
            "A strong answer names a specific, bounded task: not 'automate my marketing' but "
            "'every Monday morning, pull the three most-shared posts from my industry on LinkedIn, "
            "summarise each in one sentence, and send the digest to my Telegram by 07:00.' "
            "That is a trigger, a sequence, and an output — the three components of every agent workflow. "
            "The reason to have this ready before Saturday is simple: Module 3 sessions are hands-on. "
            "The students who get the most out of them arrive with a real problem, not a theoretical one. "
            "Your use case does not need to be impressive. It needs to be yours."
        ),
    },
    "2026-04-15": {
        "step": "Module 3 — Homework due",
        "title": "Module 2 Homework Due — Final Check",
        "url": "https://medium.com/@talirezun",
        "focus": "Homework due today. Use this question as your final submission check.",
        "question": (
            "Today your Module 2 homework is due. "
            "Before you submit, do a final check: does your MVP concept clearly answer three things — "
            "what it does, who it is for, and why AI is the right tool for this specific problem? "
            "If you can answer all three in two sentences, you are ready. "
            "If you cannot, that is your work for the next hour. "
            "What is your two-sentence pitch?"
        ),
        "model_answer": (
            "A strong submission is specific, not aspirational. "
            "The two-sentence test is not about polish — it is about clarity. "
            "If 'what it does' requires three qualifications to explain, the concept is not tight enough yet. "
            "If 'who it is for' is 'everyone' or 'businesses,' it is not defined. "
            "The AI question is the sharpest filter: if you replaced the AI component with a spreadsheet "
            "and the product still works, the AI is decoration, not architecture. "
            "The best submissions today will have a user who is real, a problem that is felt, "
            "and an AI component that is load-bearing — something the product cannot function without."
        ),
    },
    "2026-04-14": {
        "step": "Module 3 — Homework eve",
        "title": "Module 3 — One day before homework deadline",
        "url": "https://medium.com/@talirezun",
        "focus": "Homework due tomorrow. Today's question is about your MVP concept.",
        "question": (
            "Your Module 2 homework is due tomorrow. "
            "You are building or researching an MVP concept. "
            "Describe your concept in two sentences — what it does and who it is for. "
            "Then answer: which of the three homework options did you choose, "
            "and what was the single most surprising insight your research produced?"
        ),
        "model_answer": (
            "A strong answer is specific and honest — not polished or generic. "
            "Example: 'I am building a daily AI briefing tool for MBA students that surfaces relevant industry news and learning prompts automatically. It is for busy professionals who want to stay current without spending an hour searching. I chose Option 2 — the interactive dashboard — because it forced me to structure my research visually, which revealed that my original concept was too broad: I was trying to serve five different user types with one product. The most surprising insight was that my real user is not a student — it is someone already in a senior role who wants to learn faster, not someone trying to break in.' The homework is not a deliverable. It is a mirror. What it shows you about your concept is more valuable than the output itself."
        ),
    },
    "2026-04-13": {
        "step": "Module 3 — Week 2",
        "title": "Chasing Jarvis — Full Programme Synthesis",
        "url": "https://medium.com/@talirezun",
        "focus": "Week 2 of Module 3 begins. Homework due Wednesday. Use today to connect the dots.",
        "question": (
            "You are now three modules into Chasing Jarvis. "
            "Module 1 gave you a methodology. Module 2 gave you tools. Module 3 is giving you agents. "
            "If you had to describe the single thread that connects all three — "
            "the underlying principle that makes each module build on the last — "
            "what would it be? "
            "And what does that principle mean for how you approach your MVP homework due 15 April?"
        ),
        "model_answer": (
            "The thread is elimination of friction between intent and output. "
            "Module 1 eliminated the friction of not knowing how to start — "
            "the three-phase methodology gave you a process. "
            "Module 2 eliminated the friction of not having the right tools — "
            "you now have a personal AI stack. "
            "Module 3 is eliminating the friction of having to be present for every step — "
            "agents run workflows without you. "
            "Each module removes one more layer between what you want to build and what actually gets built. "
            "For your MVP homework, this means: "
            "start with the clearest possible description of what you are building and who it is for (Module 1), "
            "choose the tool that fits your current stage — NotebookLM, Claude, or video (Module 2), "
            "and think about which parts of your research process could eventually run without you (Module 3). "
            "The homework is not just a deliverable. "
            "It is a rehearsal for the full Vanguard builder loop."
        ),
    },
    "2026-04-12": {
        "step": "Weekend — Module 1-3 Synthesis",
        "title": "Weekend Briefing — Sunday Reflection",
        "url": "https://medium.com/@talirezun",
        "focus": "Sunday synthesis — connecting all three modules before the week ahead.",
        "question": (
            "You are now three modules into Chasing Jarvis. "
            "Module 1 gave you a methodology. Module 2 gave you tools. Module 3 is giving you agents. "
            "If you had to describe the single thread that connects all three — "
            "the underlying principle that makes each module build on the last — "
            "what would it be? "
            "And what does that principle mean for how you approach your MVP homework due 15 April?"
        ),
        "model_answer": (
            "The thread is elimination of friction between intent and output. "
            "Module 1 eliminated the friction of not knowing how to start — "
            "the three-phase methodology gave you a process. "
            "Module 2 eliminated the friction of not having the right tools — "
            "you now have a personal AI stack. "
            "Module 3 is eliminating the friction of having to be present for every step — "
            "agents run workflows without you. "
            "Each module removes one more layer between what you want to build and what actually gets built. "
            "For your MVP homework, this means: "
            "start with the clearest possible description of what you are building and who it is for (Module 1), "
            "choose the tool that fits your current stage — NotebookLM, Claude, or video (Module 2), "
            "and think about which parts of your research process could eventually run without you (Module 3). "
            "The homework is not just a deliverable. "
            "It is a rehearsal for the full Vanguard builder loop."
        ),
    },
    "2026-04-11": {
        "step": "Weekend — Module 1-3 Recap",
        "title": "Weekend Briefing — Saturday Reflection",
        "url": "https://medium.com/@talirezun",
        "focus": "Weekend recap — use today to catch up, revisit, and consolidate.",
        "question": (
            "Look back across all three modules of Chasing Jarvis so far. "
            "Which single article, tool, or concept shifted your thinking the most — "
            "and why? "
            "Be specific: name it, describe what you thought before, "
            "and explain what changed after you engaged with it."
        ),
        "model_answer": (
            "A strong answer is honest and personal — not the most impressive-sounding choice. "
            "Example: Step 3 of Module 1 — ditching RAG pipelines for 1M token context windows. "
            "Before: assumed that AI systems needed complex retrieval architecture to work with large documents. "
            "After: understood that simplicity is a strategic choice — "
            "loading everything at once eliminates an entire category of failure. "
            "The shift was not just technical. It was a new way of thinking about complexity: "
            "instead of asking how to manage it, ask whether it needs to exist at all. "
            "That question now applies to everything — "
            "workflows, tools, processes, even the MVP itself. "
            "The best Vanguard builders are not the ones who handle the most complexity. "
            "They are the ones who eliminate it before it becomes a problem."
        ),
    },
    "2026-04-10": {
        "step": "Module 3 — Day 5",
        "title": "Second Brain — Building in the Open",
        "url": "https://www.linkedin.com/posts/talirezun_opensource-secondbrain-obsidian-share-7447927944905347072-HyX3",
        "focus": (
            "Dr. Tali built a fully local, open-source AI app out of personal necessity "
            "and shared it with the community from day one. "
            "Today's question is about what that approach reveals about how builders think."
        ),
        "question": (
            "Dr. Tali built Second Brain — a fully local, open-source AI app — "
            "out of personal necessity, then immediately opened it to the community. "
            "What does building in the open reveal about the mindset of a Vanguard builder? "
            "And what is the strategic advantage of sharing your work before it is finished?"
        ),
        "model_answer": (
            "Building in the open reveals that the Vanguard builder treats their own problems "
            "as signals — not just personal frustrations, but indicators of what others need too. "
            "Dr. Tali did not wait until Second Brain was polished. "
            "He shipped it when it was useful, not when it was perfect. "
            "That is a strategic choice, not just a generous one. "
            "The advantage of sharing before you are finished is threefold: "
            "you get real feedback before you build the wrong thing further, "
            "you attract collaborators who improve the product faster than you could alone, "
            "and you build an audience that is already invested by the time you are ready to scale. "
            "The deeper insight for Module 3: the same principle applies to AI agents. "
            "Deploy early, verify outputs, iterate with real users. "
            "Waiting for perfection is how you miss the window. "
            "The Vanguard builder's edge is not the finished product — "
            "it is the feedback loop they build while everyone else is still planning."
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
    "url": "https://www.linkedin.com/pulse/neo-world-its-waiting-you-drazen-kapusta-v8wje/?trackingId=UDsE2BrQYntV%2FxsTUu9MXA%3D%3D",
    "title": "The NEO World — It's Not Waiting for You",
    "description": "Kapusta on urgency, agency, and what it means to lead in a world that will not pause for you to catch up.",
}

SUPPLEMENTARY_RESOURCE = {
    "title": "n8n — Workflow Automation for Technical People",
    "url": "https://n8n.io",
    "description": "n8n is the visual orchestration layer for your AI stack — connect apps, triggers, and agents without writing code. Create a free account and explore what a workflow node actually looks like before Session 9.",
}

AI_NEWS_TODAY = {
    "headline": "Meta releases open-source AI coding assistant as competition with OpenAI and Anthropic intensifies",
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
    "2026-04-26": [
        {
            "title": "Vanguard Intelligence Systems (VIS): An AI-Augmented Framework for Decision-Making in the NEO Era",
            "url": "https://drive.google.com/file/d/12Ni10rr9TCkkGI-hbJl9a6WZJxi7HdUY/view?usp=sharing",
            "author": "Kapusta & Stručić",
        },
    ],
    "2026-04-25": [
        {
            "title": "The Six-Month Hormuz Scenario",
            "url": "https://docs.google.com/document/d/1dkpoE_F7jrg0frnzQfyOldkM0fifjXkZ/edit?usp=sharing&ouid=100173679485664698153&rtpof=true&sd=true",
            "author": "Dražen Kapusta",
        },
    ],
    "2026-04-24": [
        {
            "title": "The Fog of Federation — A European Consortium and the Battle for the Sovereign Cloud",
            "url": "https://drive.google.com/file/d/1jfHOEs6Hlkp4YRdbcWGUNx_x8Qypq8cC/view?usp=sharing",
            "author": "Cotrugli Business School",
        },
    ],
    "2026-04-23": [
        {
            "title": "The Fog of Federation — A European Consortium and the Battle for the Sovereign Cloud",
            "url": "https://drive.google.com/file/d/1jfHOEs6Hlkp4YRdbcWGUNx_x8Qypq8cC/view?usp=sharing",
            "author": "Cotrugli Business School",
        },
    ],
    "2026-04-22": [
        {
            "title": "Vanguard Intelligence Systems (VIS): An AI-Augmented Framework for Decision-Making in the NEO Era",
            "url": "https://drive.google.com/file/d/12Ni10rr9TCkkGI-hbJl9a6WZJxi7HdUY/view?usp=sharing",
            "author": "Kapusta & Stručić",
        },
    ],
    "2026-04-21": [
        {
            "title": "The Six-Month Hormuz Scenario",
            "url": "https://docs.google.com/document/d/1dkpoE_F7jrg0frnzQfyOldkM0fifjXkZ/edit?usp=sharing&ouid=100173679485664698153&rtpof=true&sd=true",
            "author": "Dražen Kapusta",
        },
    ],
    "2026-04-20": [
        {
            "title": "The Fog of Federation — A European Consortium and the Battle for the Sovereign Cloud",
            "url": "https://drive.google.com/file/d/1jfHOEs6Hlkp4YRdbcWGUNx_x8Qypq8cC/view?usp=sharing",
            "author": "Cotrugli Business School",
        },
    ],
    "2026-04-19": [
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
    "2026-04-17": [
        {
            "title": "The Fog of Federation — A European Consortium and the Battle for the Sovereign Cloud",
            "url": "https://drive.google.com/file/d/1jfHOEs6Hlkp4YRdbcWGUNx_x8Qypq8cC/view?usp=sharing",
            "author": "Cotrugli Business School",
        },
    ],
    "2026-04-16": [
        {
            "title": "Vanguard Intelligence Systems (VIS): An AI-Augmented Framework for Decision-Making in the NEO Era",
            "url": "https://drive.google.com/file/d/12Ni10rr9TCkkGI-hbJl9a6WZJxi7HdUY/view?usp=sharing",
            "author": "Kapusta & Stručić",
        },
    ],
    "2026-04-15": [
        {
            "title": "The Six-Month Hormuz Scenario",
            "url": "https://docs.google.com/document/d/1dkpoE_F7jrg0frnzQfyOldkM0fifjXkZ/edit?usp=sharing&ouid=100173679485664698153&rtpof=true&sd=true",
            "author": "Dražen Kapusta",
        },
    ],
    "2026-04-14": [
        {
            "title": "The Fog of Federation — A European Consortium and the Battle for the Sovereign Cloud",
            "url": "https://drive.google.com/file/d/1jfHOEs6Hlkp4YRdbcWGUNx_x8Qypq8cC/view?usp=sharing",
            "author": "Cotrugli Business School",
        },
    ],
    "2026-04-10": [
        {
            "title": "The Six-Month Hormuz Scenario",
            "url": "https://docs.google.com/document/d/1dkpoE_F7jrg0frnzQfyOldkM0fifjXkZ/edit?usp=sharing&ouid=100173679485664698153&rtpof=true&sd=true",
            "author": "Dražen Kapusta",
        },
    ],
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
