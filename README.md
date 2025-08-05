Automated Book Publication System
Overview
The Automated Book Publication System is an end-to-end pipeline designed to streamline and automate the process of book content generation, enhancement, review, and publishing. This system utilizes cutting-edge AI models and human-in-the-loop feedback mechanisms to transform source text into ready-to-publish books with minimal manual intervention.

Key Features
Content Scraping: Fetches chapters and full book content from public domain sources (e.g., Wikisource).
Screenshot Capture: Automatically captures source content screenshots for reference and compliance.
AI Writing Agents:
Spinning Agent: Rewrites or paraphrases chapters in an engaging tone.
Summary Agent: Summarizes book content as needed.
Voice Command Integration: Accepts spoken instructions like “Spin chapter 1” or “Summarize book 2” and processes them accordingly.
Reward-Based Review System:
Assigns RL-based rewards to evaluate content quality.
Requests user edits and feedback before final approval.
Iterative Human-in-the-Loop Review: Ensures accuracy, style, and coherence with optional multi-stage human editing.

📁 Project Structure
auto_book_pub/
│
├── main.py                          # Main execution script
├── agents/
│   ├── ai_writer.py                # Gemini-based rewriting agent
│   ├── voice_router.py             # Voice-to-command router
│   └── reward_rl.py                # RL reward system
│
├── utils/
│   ├── web_scraper.py             # Playwright scraper
│   └── chroma_store.py            # Version management with ChromaDB
│
├── voice_inputs/
│   └── recordings/                # Stored voice files 
│
├── screenshots/
│   └── chapter_1.png              # Screenshots of pages
│
└── requirements.txt

How It Works
User Input:
Via URL (e.g., Wikisource links) or
Via voice command (e.g., "Spin Chapter 2").

Content Fetching:
Web scraper retrieves content and stores raw chapters.

AI Processing:
The AI writer agent spins or summarizes the text as per input.

Screenshot Logging:
Screenshots of original sources are stored for validation/reference.

Human Review:
The system asks users to review or edit output before final approval.
RL-based reward feedback is stored for future learning.

Output Generation:
Finalized chapters or summaries are saved in desired formats.
