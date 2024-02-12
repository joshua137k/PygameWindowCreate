from widgets import *
import sys




class App(BaseApp):
	def __init__(self):
		super().__init__()


	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				self.UpdateTouch(event)


				


			screen.fill(WHITE)
			self.UpdateDraw()
			
            # Desenhar outros elementos...

			

			pygame.display.flip()

# Executa a aplicação
if __name__ == '__main__':
	App().run()
