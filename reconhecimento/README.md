
# Sistema de Reconhecimento Facial

Este repositório contém a implementação de um sistema de reconhecimento facial, desenvolvido como parte de um desafio acadêmico. O objetivo principal é realizar a detecção e o reconhecimento simultâneo de múltiplas faces em imagens e vídeos.

---

## **Descrição do Projeto**

O sistema utiliza dois modelos principais:
1. **Modelo de Detecção Facial (MTCNN)**: Responsável por localizar as faces em cada frame de uma imagem ou vídeo.
2. **Modelo de Reconhecimento Facial (FaceNet)**: Gera embeddings para cada face detectada, permitindo identificar pessoas com base em um banco de dados de referências.

### **Principais Funcionalidades**
- Detecção e reconhecimento facial em tempo real.
- Processamento de vídeos e exibição dos resultados diretamente.
- Salvamento do vídeo processado com os resultados das detecções.

---

## **Tecnologias Utilizadas**

- **Python 3.10**
- **Google Colab**: Ambiente de desenvolvimento.
- **TensorFlow**: Base para o modelo FaceNet.
- **OpenCV**: Manipulação de imagens e vídeos.
- **MTCNN**: Para detecção facial eficiente.
- **NumPy**: Operações matemáticas e de vetores.

---

## **Estrutura do Projeto**

- **Banco de Dados de Embeddings**:
  - Armazena os vetores gerados pelo modelo FaceNet para identificar pessoas conhecidas.
  
- **Pipeline de Processamento**:
  - Detecção facial: Identifica as regiões do rosto em imagens ou vídeos.
  - Reconhecimento facial: Compara embeddings detectados com os do banco de dados para identificar pessoas.

- **Processamento de Vídeo**:
  - Capacidade de processar vídeos pré-gravados e salvar os resultados.

---

## **Possíveis Melhorias**

- Suporte para múltiplas imagens de referência por pessoa.
- Implementação de uma API para uso em tempo real.
- Otimização para processamento mais rápido em vídeos de alta resolução.
- Integração com sistemas externos para notificações ou armazenamento de resultados.

---