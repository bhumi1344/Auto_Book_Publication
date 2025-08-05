import asyncio
from playwright.async_api import async_playwright

async def scrape_and_screenshot(url, save_as="screenshots/chapter_1.png"):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)
        content = await page.inner_text("body")
        await page.screenshot(path=save_as, full_page=True)
        await browser.close()
        return content
