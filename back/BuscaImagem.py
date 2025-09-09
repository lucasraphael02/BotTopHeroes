import numpy as np
import cv2
import pyautogui

class BuscaImagem():

    def find_image_on_screen(self,target_image_path, confidence=0.8):
        """
        Encontra a posição de uma imagem na tela.
        
        :param target_image_path: Caminho para a imagem alvo.
        :param confidence: Nível de confiança para encontrar a correspondência.
        :return: Posição do centro da imagem (x, y) ou None se não for encontrada.
        """
        screenshot = pyautogui.screenshot()  # Tira um print da tela
        screen_array = np.array(screenshot)  # Converte para array NumPy (usado pelo OpenCV)
        screen_gray = cv2.cvtColor(screen_array, cv2.COLOR_BGR2GRAY)  # Converte para escala de cinza

        # Carrega a imagem alvo e converte para escala de cinza
        target_image = cv2.imread(target_image_path, cv2.IMREAD_GRAYSCALE)

        # Realiza correspondência de modelos (Template Matching) considerando cor
        # Carrega a imagem alvo em colorido
        # target_image_color = cv2.imread(target_image_path)
        # # Converte screenshot para o mesmo formato de cor (BGR)
        # screen_bgr = cv2.cvtColor(screen_array, cv2.COLOR_RGB2BGR)
        # # Usa template matching em colorido
        # result = cv2.matchTemplate(screen_bgr, target_image_color, cv2.TM_CCOEFF_NORMED)
        
        result = cv2.matchTemplate(screen_gray, target_image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if max_val >= confidence:  # Verifica se a correspondência é alta o suficiente
            target_center = (max_loc[0] + target_image.shape[1] // 2, max_loc[1] + target_image.shape[0] // 2)
            return target_center
        return None