#!/usr/bin/env python3
"""
Create LinkedIn Session File

This script helps you create a linkedin_session.json file by logging in manually.
The session file is needed to run integration tests and scraping examples.

Usage:
    python samples/create_session.py
    
The script will:
1. Open a browser window with LinkedIn login page
2. Wait for you to manually log in (up to 5 minutes)
3. Automatically detect when login is complete
4. Save your session to linkedin_session.json

Note: The session file contains authentication cookies and should never be committed to git.
"""
import asyncio
from linkedin_scraper import BrowserManager, wait_for_manual_login


async def create_session(website: str, session_path: str):
    """Create a LinkedIn session file through manual login."""
    print("="*60)
    print("LinkedIn Session Creator")
    print("="*60)
    print("\nThis script will help you create a session file for LinkedIn.")
    print("\nSteps:")
    print("1. A browser window will open")
    print("2. Log in to LinkedIn manually")
    print("3. The script will detect when you're logged in")
    print("4. Your session will be saved to linkedin_session.json")
    print("\n" + "="*60 + "\n")
    
    async with BrowserManager(headless=False, slow_mo = 50) as browser:
        # Navigate to LinkedIn login page
        print("Opening website login page...")
        await browser.page.goto(website)
        
        print("\n🔐 Please log in to LinkedIn in the browser window...")
        print("   (You have 5 minutes to complete the login)")
        print("   - Enter your email and password")
        print("   - Complete any 2FA or CAPTCHA challenges")
        print("   - Wait for your feed to load")
        print("\n⏳ Waiting for login completion...\n")
        
        # Wait for manual login (5 minutes timeout)
        # await wait_for_manual_login(browser.page, timeout=300000)
        print("Please log in using the browser window.")
        await asyncio.to_thread(
            input,
            "Press Enter after you have successfully logged in..."
        )

        # Save session to project root
        session_path = session_path
        print(f"\n💾 Saving session to {session_path}...")
        await browser.save_session(session_path)
        
        print("\n" + "="*60)
        print("✅ Success! aMN,/>Session file created.")
        print("="*60)
        print(f"\nSession saved to: {session_path}")
        print("\nYou can now:")
        print("  - Run integration tests: pytest")
        print("  - Run example scripts: python samples/scrape_person.py")
        print("\nNote: Keep this file secure and don't commit it to git.")
        print("="*60 + "\n")


if __name__ == "__main__":
    website = "https://login.seek.com/login?state=hKFo2SA4ZE5LQ2x5alhtNmpiZ3hrN0ZhU0I3RkRROVMtYW1sWKFupWxvZ2luo3RpZNkgbkU0NEcwY3JtWGdBWjNUNFppLWM3emV4LUxJQWtnOGKjY2lk2SBZWVI1UmtGSVRmU05FSk9RblFPd2hmRlE0ZFJtWkJrWA&client=YYR5RkFITfSNEJOQnQOwhfFQ4dRmZBkX&protocol=oauth2&scope=openid%20profile%20email%20offline_access&redirect_uri=https%3A%2F%2Fmy.jobstreet.com%2Foauth%2Fcallback%2F&audience=https%3A%2F%2Fseek%2Fapi%2Fcandidate&ui_locales=en&language=en-MY&fragment=%2Foauth%2Flogin%3Flocale%3Dmy%26language%3Den%26realm%3DUsername-Password-Authentication%26da_cdt%3Dvisid_019f6bcd96f8001fcbbbda6316c90506f021e067007e8-sesid_1784220063481-hbvid_aa371106_232a_48ad_930b_1b4ff6d86a81-tempAcqSessionId_1784220063488-tempAcqVisitorId_aa371106232a48ad930b1b4ff6d86a81&JobseekerSessionId=d6dc6bba-a919-400a-ba3e-d20ed0681af4&response_type=code&response_mode=query&nonce=RmIyNklWQkt2bU9QQklFU2tHN2FnNFlvX2dySzA3OC5MSHNvU0NDa1VWNA%3D%3D&code_challenge=2dor-yy-ODu9HA-kGIfsBPkBIJbPjAeI_MiBYbZaDpc&code_challenge_method=S256&auth0Client=eyJuYW1lIjoiYXV0aDAtc3BhLWpzIiwidmVyc2lvbiI6IjIuMjEuMSJ9#/login?locale=my&language=en&realm=Username-Password-Authentication&da_cdt=visid_019f6bcd96f8001fcbbbda6316c90506f021e067007e8-sesid_1784220063481-hbvid_aa371106_232a_48ad_930b_1b4ff6d86a81-tempAcqSessionId_1784220063488-tempAcqVisitorId_aa371106232a48ad930b1b4ff6d86a81"
    session_path = "jobstreet_session.json"
    asyncio.run(create_session(website, session_path))
