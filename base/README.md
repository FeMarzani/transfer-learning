# YOLO no Google Colab: Criação de Dataset e Treinamento de Rede

Este projeto utiliza o framework **Darknet** para configurar, treinar e realizar inferências com a rede **YOLOv3** no ambiente do Google Colab. O objetivo principal é criar um dataset personalizado, configurar o treinamento e executar a detecção de objetos.

---

## **Objetivo**
Demonstrar como configurar e treinar a rede YOLO no Google Colab para detectar objetos em imagens utilizando datasets personalizados ou públicos.

---

## **Etapas do Projeto**

1. **Configuração do Ambiente**:
   - Clonagem do repositório Darknet.
   - Ajuste do Makefile para habilitar o uso de GPU e CUDNN.
   - Compilação do Darknet.

2. **Download de Pesos Pré-Treinados**:
   - Baixar os pesos pré-treinados do YOLOv3.

3. **Teste Inicial**:
   - Realizar detecções em imagens de exemplo para validar a configuração.

4. **Criação de Dataset Personalizado**:
   - Configuração das pastas `train` e `val` para imagens de treino e validação.
   - Criação dos arquivos necessários: `obj.data` e `obj.names`.
   - Ajuste do arquivo de configuração do YOLO (`yolov3-custom.cfg`) para refletir o número de classes.

5. **Treinamento da Rede YOLO**:
   - Treinamento da rede YOLO com o dataset configurado.
   - Resultados e pesos finais são salvos no diretório `backup`.

6. **Inferências com o Modelo Treinado**:
   - Uso do modelo treinado para detectar objetos em imagens novas.

---

## **Tecnologias Utilizadas**
- **Framework de Detecção**: Darknet
- **Modelo Pré-Treinado**: YOLOv3
- **Ambiente**: Google Colab
- **Linguagem**: Python
- **Bibliotecas de Suporte**: OpenCV, Matplotlib

---