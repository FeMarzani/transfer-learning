# Transfer Learning com VGG16 para Classificação de Imagens: Gatos vs Cachorros

Este projeto implementa Transfer Learning utilizando a rede pré-treinada **VGG16** para classificar imagens em duas categorias: **gatos** e **cachorros**. O desenvolvimento foi realizado no ambiente **Google Colab**, utilizando o dataset **Cats vs Dogs** disponibilizado pela Microsoft.

---

## **Objetivo**
O objetivo do projeto foi aplicar Transfer Learning para criar um modelo de Deep Learning capaz de classificar imagens de gatos e cachorros com alta precisão, utilizando um conjunto de dados pré-treinado para agilizar e melhorar o desempenho do treinamento.

---

## **Etapas do Projeto**

1. **Pré-processamento dos Dados**:
   - O dataset foi baixado e descompactado diretamente do link oficial da Microsoft.
   - As imagens foram organizadas em pastas correspondentes às categorias (**Cat** e **Dog**).
   - O conjunto foi dividido em **treino (80%)** e **validação (20%)** usando a biblioteca `ImageDataGenerator`.

2. **Criação do Modelo com Transfer Learning**:
   - Foi utilizada a rede **VGG16**, pré-treinada no dataset ImageNet.
   - As camadas superiores da VGG16 foram congeladas para manter os pesos treinados.
   - Camadas personalizadas (Flatten, Dense, Dropout e uma saída com ativação `sigmoid`) foram adicionadas para classificação binária.

3. **Treinamento do Modelo**:
   - O modelo foi treinado por 10 epochs, com o otimizador Adam e a função de perda `binary_crossentropy`.
   - Foram utilizados os geradores de treino e validação previamente configurados.

4. **Inferência em Novas Imagens**:
   - Após o treinamento, foi realizada uma inferência com uma imagem de teste externa, que foi corretamente classificada como gato ou cachorro.

---

## **Tecnologias Utilizadas**
- **Linguagem**: Python
- **Frameworks**: TensorFlow, Keras
- **Ambiente de Desenvolvimento**: Google Colab
- **Dataset**: Cats vs Dogs (Microsoft)

---

## **Como Usar**
1. Clone este repositório.
2. Baixe e descompacte o dataset **Cats vs Dogs** na pasta indicada.
3. Abra o notebook no Google Colab.
4. Execute as células sequencialmente para treinar o modelo e realizar inferências.