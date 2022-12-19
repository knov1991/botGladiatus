import { Injectable } from '@nestjs/common';
import * as puppeteer from 'puppeteer';
import * as tesseract from 'node-tesseract-ocr';

@Injectable()
export class GladiatusService {
  async gladiatus() {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto('https://s16.gladiatuspvp.com/index.php');
    await page.setViewport({ width: 1920, height: 1080 });
    //await page.waitForTimeout(500);

    async function login() {
      try {
        console.log('login');
        await page.type('#login_username', 'knov1991');
        await page.type('#login_password', 'knov972468');
        await page.waitForTimeout(500);
        await page.click('#loginsubmit');
      } catch {
        console.log('login falhou');
      }
    }

    login();
    //await page.waitForNavigation();

    await page.waitForTimeout(3000);

    await page.click('#zegar3');
    //await page.waitForNavigation();

    await page.waitForTimeout(3000);
    console.log('print');
    await page.screenshot({ path: 'screenshots/gladiatus.png' });

    //AntiBot
    try {
      const atb = await page.$eval('input[name=nobot]', (el) => el);
      console.log('antibot existe');
      await page.screenshot({
        path: 'screenshots/bot.png',
        clip: { x: 770, y: 300, width: 100, height: 100 },
      });
      await page.waitForTimeout(5000);
      await page.type('input[name=nobot]', (await this.imgText()).toString());
      //await page.type('input[name=nobot]', await itt()[0].toString());
    } catch {
      console.log('não achou!');
    }

    await page.waitForTimeout(3000);
    await page.screenshot({ path: 'screenshots/gladiatus2.png' });
    console.log('fim');
  }

  //Função de converter imagem para texto
  private imgText() {
    const config = {
      lang: 'eng',
      oem: 1,
      psm: 3,
    };

    return tesseract.recognize('screenshots/bot.png', config);
  }
}

/*  
try:
    driver.get_screenshot_as_file('screenshot.png')
    sleep(1)
    atb = driver.find_element(By.NAME, 'nobot')
    printantibot()
    sleep(3)
    atb.send_keys(str(imgtotext()))
    sleep(1)
    btnAntiBot = driver.find_element(By.NAME, 'verifyme')
    sleep(0.1)
    print(datetime.now().strftime('%d/%m/%Y %H:%M:%S'), 'AntiBot')
    btnAntiBot.click()
    sleep(1)
except:
    pass 
*/
