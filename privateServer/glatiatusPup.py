from pyppeteer import launch
from imgToText import imgtotext
from time import sleep
from datetime import datetime
import asyncio


async def main():
  browser = await launch()
  page = await browser.newPage()
  await page.goto('https:#s16.gladiatuspvp.com/index.php')

  async def login():
    try:
      print('login')
      await page.type('#login_username', 'knov1991')
      await page.type('#login_password', 'knov972468')
      await page.waitForTimeout(500)
      await page.click('#loginsubmit')
    except:
      print('erro')

  login()

  await page.screenshot({ 'path': 'screenshots/gladiatus.png' })


asyncio.run(main())


""" #await page.waitForNavigation()
await page.waitForTimeout(3000)
await page.click('#zegar3')
#await page.waitForNavigation()
await page.waitForTimeout(3000)
print('print')
await page.screenshot({ path: 'screenshots/gladiatus.png' })
#AntiBot
try:
  atb = await page.$eval('input[name=nobot]', (el) => el)
  print('antibot existe')
  await page.screenshot({
    path 'screenshots/bot.png',
    clip: { x: 770, y: 300, width: 100, height: 100 },
  })
  await page.waitForTimeout(5000)
  await page.type('input[name=nobot]', (await this.imgText()).toString())
  #await page.type('input[name=nobot]', await itt()[0].toString())
except:
  print('não achou!')

await page.waitForTimeout(3000)
await page.screenshot({ path: 'screenshots/gladiatus2.png' })
print('fim')

#str(imgtotext()) """