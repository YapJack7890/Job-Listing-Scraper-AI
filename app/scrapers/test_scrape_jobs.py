#!/usr/bin/env python3
"""
Example: Search for jobs and scrape job details
"""
import asyncio
from linkedin_scraper.scrapers.job_search import JobSearchScraper
from linkedin_scraper.scrapers.job import JobScraper
from linkedin_scraper.core.browser import BrowserManager


async def main():
    """Search for jobs and scrape details"""
    
    async with BrowserManager(headless=True) as browser:
        await browser.load_session("linkedin_session.json")
        print("✓ Session loaded")

        job_urls = browser.page.locator('span').filter(has_text="").first
        await title_elem.wait_for(timeout=5000) # Wait until this element exists in the page before continuing.
        title = await title_elem.inner_text()

        title_elem = browser.page.locator('span').filter(has_text="").first
        await title_elem.wait_for(timeout=5000)
        title = await title_elem.inner_text()

        badge = browser.page.locator("svg#verified-small").first
        await badge.wait_for(timeout=5000)
        is_verified = await badge.is_visible()

        company_name = await card.locator("p").nth(1).inner_text()

        desc_elem = browser.page.locator('span').filter(has_text="").first
        await desc_elem.wait_for(timeout=5000)
        description = await desc_elem.inner_text()

        # async def _is_verified_job(self) -> bool:
        #     """Return True if the job has a verified badge."""
        #     try:
        #         badge = self.page.locator("svg#verified-small").first
        #         return await badge.is_visible()
        #     except:
        #         return False
        
        # Search for jobs
        # search_scraper = JobSearchScraper(browser.page)
        # print("🔍 Searching for jobs...")
        # job_urls = await search_scraper.search(
        #     keywords="software engineer",
        #     location="Malaysia",
        #     limit=5
        # )
        
        # print(f"\n✓ Found {len(job_urls)} jobs")
        # for url in job_urls:
        #     print(f"  - {url}")
        
        # Scrape first job details if any found
        if job_urls:
            print(f"\n📄 Scraping first job details...")
            job_scraper = JobScraper(browser.page)
            for job_url in job_urls:
                job = await job_scraper.scrape(job_url)
                
                print("\n" + "="*60)
                print(f"Title: {job.job_title}")
                print(f"Company: {job.company}")
                print(f"Location: {job.location}")
                print(f"Posted: {job.posted_date}")
                print(f"Applicants: {job.applicant_count}")
                print(f"Description: {job.job_description[:200]}..." if job.job_description else "Description: N/A")
                print("="*60)
    
    print("\n✓ Done!")


if __name__ == "__main__":
    asyncio.run(main())