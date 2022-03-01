const puppeteer = require('puppeteer-core');

(async () => {
  const browser = await puppeteer.launch({
    executablePath: '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome'
  });
  const page = await browser.newPage();
  await page.goto('https://sweepsouth.com');
  await page.screenshot({ path: 'sweepsouth.png' });

  await browser.close();
})();