import asyncio
from utils.web_scraper import scrape_and_screenshot
from agents.ai_writer import spin_text, revise_with_feedback
from agents.voice_router import get_voice_command
from agents.reward_rl import simulate_rl_feedback
from utils.chroma_store import save_version, search_version

async def process_command():
    url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"

    voice_cmd = get_voice_command()

    if "spin" in voice_cmd and "chapter" in voice_cmd:
        print("📖 Scraping chapter...")
        text = await scrape_and_screenshot(url)
        
        print("✨ Spinning with Gemini...")
        spun = spin_text(text)

        save_version(spun, "v1", metadata={"action": "initial_spin"})

        # Human Feedback Loop
        print("\n--- HUMAN-IN-THE-LOOP FEEDBACK ---")
        current = spun
        for i in range(3):
            print(f"\nRound {i+1} Output Preview:\n", current[:500])
            feedback = input("Give edit feedback or press Enter to approve: ")
            if feedback.strip():
                current = revise_with_feedback(current, feedback)
            else:
                break

        save_version(current, "v2", metadata={"status": "human_approved"})

        # RL Feedback
        reward = simulate_rl_feedback(spun, current)
        print(f"RL Reward Assigned: {reward}")

        print("\n✅ Final Output:\n", current[:1000])

    elif "search" in voice_cmd:
        query = voice_cmd.replace("search", "").strip()
        result = search_version(query)
        print("\n🔎 Search Result:\n", result[:1000] if result else "No match found.")

    else:
        print("⚠️ Unknown voice command.")

if __name__ == "__main__":
    asyncio.run(process_command())
