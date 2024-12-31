# API Flask para Processamento de Imagens: Binarização e Tons de Cinza

Este projeto implementa uma API utilizando o framework **Flask** para processar imagens e transformá-las em dois formatos: **tons de cinza** e **imagem binarizada** (preto e branco). A imagem processada é retornada ao usuário como uma única imagem contendo a original, em tons de cinza e binarizada, cada uma com uma legenda na parte superior.

---

## **Objetivo**
O objetivo do projeto é demonstrar a aplicação de técnicas básicas de processamento de imagens em uma API simples e funcional, permitindo que usuários enviem uma imagem e recebam o resultado do processamento de forma prática.

---

## **Etapas do Projeto**

1. **Desenvolvimento da API**:
   - Foi utilizada a biblioteca **Flask** para criar uma rota POST (`/process`) que recebe uma imagem enviada pelo usuário.
   - A API processa a imagem e retorna o resultado como resposta.

2. **Processamento de Imagens**:
   - Com a biblioteca **OpenCV**, a imagem é convertida para:
     - **Tons de Cinza**: Utilizando o método `cv2.cvtColor`.
     - **Imagem Binarizada**: Aplicando um limiar fixo de 127 com `cv2.threshold`.
   - As imagens são concatenadas verticalmente em uma única imagem com as legendas utilizando a biblioteca **Pillow**.

3. **Resposta da API**:
   - A imagem final com as três versões (original, tons de cinza e binarizada) é retornada no formato PNG como resposta.

---

## **Tecnologias Utilizadas**
- **Linguagem**: Python
- **Frameworks**: Flask
- **Bibliotecas**: OpenCV, Pillow
- **Formato de Entrada**: Arquivos de imagem (PNG, JPEG, etc.)
- **Formato de Saída**: Imagem processada (PNG)

---

## **Como Usar**
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
