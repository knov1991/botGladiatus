from playwright.sync_api import sync_playwright
import time

class BrowserGameBot:
    def __init__(self, url, username=None, password=None):
        """
        Inicializa o bot para o browser game
        :param url: URL do jogo
        :param username: Nome de usuário para login (se necessário)
        :param password: Senha para login (se necessário)
        """
        self.url = url
        self.username = username
        self.password = password
        self.playwright = None
        self.browser = None
        self.page = None
        self.maintenance = False

    def iniciar(self):
        """Inicia o navegador e abre a página do jogo"""
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(
            headless=False,  # Modo sem headless para visualizar a execução
            slow_mo=50  # Adiciona um pequeno delay entre ações para melhor visualização
        )
        
        # Cria um contexto do navegador com viewport personalizado
        context = self.browser.new_context(
            viewport={"width": 1280, "height": 720},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        )
        
        # Cria uma nova página
        self.page = context.new_page()
        
        # Navega para a URL do jogo
        print(f"Acessando: {self.url}")
        self.page.goto(self.url)
        
        # Aguarda a página carregar completamente
        self.page.wait_for_load_state("networkidle")
        print("Página carregada com sucesso!")
        
        return self.page

    def pausar_para_ajuste_manual(self, segundos=60):
        """
        Pausa a execução para permitir ajustes manuais
        :param segundos: Tempo de pausa em segundos
        """
        print(f"Pausando por {segundos} segundos para ajustes manuais...")
        for i in range(segundos, 0, -1):
            if i % 10 == 0:
                print(f"{i} segundos restantes...")
            time.sleep(1)
        print("Continuando execução...")

    def finalizar(self):
        """Fecha o navegador e libera recursos"""
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()
        print("Bot finalizado.")