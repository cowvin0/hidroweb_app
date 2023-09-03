from playwright.async_api import async_playwright
from time import sleep
import asyncio

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)

        context = await browser.new_context(
                color_scheme='light',
                viewport={'width': 800, 'height':600},
                )

        page = await context.new_page()

        await page.goto('https://www.snirh.gov.br/hidroweb/serieshistoricas')

        await page.evaluate('document.querySelector(".mat-select-arrow-wrapper").click()')

        await page.evaluate('var station_type = document.querySelectorAll(".mat-option-text")')

        await page.evaluate('station_type[1].click()')

        municipio_input = page.locator('#mat-input-3')

        await municipio_input.fill('pian')

        await page.evaluate('''
                            (async () => {
                              try {
                                await new Promise(resolve => setTimeout(resolve, 1000));

                                const elements = document.querySelectorAll('.mat-option-text');

                                for(const element of elements) {
                                  if(element.textContent.trim() === 'PIANCÓ') {
                                      element.click();
                                      console.log("Clicked on element with text 'PIANCÓ'");
                                      break;
                                      }
                                    }
                                  } catch(error) {
                                      console.error("An error ocurred:", error);
                                      }
                                })();
                            ''')

        await page.evaluate('document.querySelectorAll(".mat-button-wrapper")[2].click()')

        await page.evaluate('document.querySelectorAll(".mat-checkbox-inner-container.mat-checkbox-inner-container-no-side-margin").forEach((element) => element.click())')

        await page.evaluate('document.querySelectorAll(".mat-radio-outer-circle")[2].click()')

        breakpoint()

        await page.wait_for_timeout(5000)

        print(await page.title())

asyncio.run(main())
