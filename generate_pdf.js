const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
    try {
        const browser = await puppeteer.launch();
        const page = await browser.newPage();
        const filePath = path.resolve(__dirname, 'curriculo_ats.html');
        await page.goto(`file://${filePath}`, { waitUntil: 'networkidle0' });
        await page.pdf({
            path: 'curriculo_ats.pdf',
            format: 'A4',
            margin: {
                top: '20mm',
                bottom: '20mm',
                left: '20mm',
                right: '20mm'
            },
            printBackground: true
        });
        await browser.close();
        console.log('PDF gerado com sucesso!');
    } catch (e) {
        console.error('Erro ao gerar PDF:', e);
        process.exit(1);
    }
})();
