# 📋 Guia de Configuração do Trello (Kanban Ágil)

Este documento contém o passo a passo exato para você montar seu quadro Kanban no **Trello** (ou ferramenta similar), cumprindo 100% dos critérios avaliativos da rubrica (Critérios 2 e 3: atribuição do nome do aluno, especificações técnicas detalhadas nos cards e movimentação pelas raias).

---

## 1. Configuração Inicial do Quadro

1. Acesse [Trello.com](https://trello.com) e crie um novo quadro com o nome:  
   **`VisionFlow AI - Detecção de Objetos (SC-TEC / SENAI)`**
2. **Visibilidade**: Defina como **Público** (para que o professor e avaliadores consigam acessar sem bloqueios).
3. **Compartilhamento**: Adicione o professor como membro/convidado com o e-mail:  
   `welington.souza@edu.sc.senai.br`
4. Crie exatamente as 6 colunas metodológicas exigidas pelo edital:
   - 📥 **Backlog**
   - 📌 **To Do**
   - ⚙️ **Doing**
   - ⛔ **Blocked**
   - 🔍 **Review**
   - ✅ **Done**

---

## 2. Cartões Detalhados (Copie e Cole)

> **Regra de Ouro da Rubrica**: Em cada cartão, atribua o seu perfil como membro e adicione a descrição técnica com a referência da branch correspondente.

---

### Card 1: `feature/dataset-prep`
* **Título**: `feature/dataset-prep - Seleção e Higienização de Dataset com 10 Classes`
* **Membro atribuído**: `Alexandre Virgílio`
* **Coluna Atual**: `Done`
* **Descrição técnica**:
```markdown
### Objetivo
Pesquisar, selecionar e preparar um dataset representativo contendo pelo menos 10 classes distintas do contexto de mobilidade urbana inteligente e tráfego.

### 10 Classes Mapeadas
1. person (Pedestre)
2. bicycle (Bicicleta)
3. car (Automóvel)
4. motorcycle (Motocicleta)
5. bus (Ônibus)
6. truck (Caminhão)
7. traffic light (Semáforo)
8. fire hydrant (Hidrante)
9. stop sign (Placa de Parada Obrigatória)
10. backpack (Mochila de pedestre/entregador)

### Entregáveis
- [x] Download e validação de 10 amostras fotográficas reais com variações de luz e ângulo em `data/samples/`.
- [x] Validação da presença e anotação das classes alvo.
- [x] Branch Git: `feature/dataset-prep`.
```

---

### Card 2: `feature/yolo-model`
* **Título**: `feature/yolo-model - Encapsulamento do Serviço de Inferência YOLOv8`
* **Membro atribuído**: `Alexandre Virgílio`
* **Coluna Atual**: `Done`
* **Descrição técnica**:
```markdown
### Objetivo
Implementar o serviço de inferência em Python (`app/services/yolo_detector.py`) utilizando a arquitetura YOLOv8 Nano (`yolov8n.pt`), otimizada para microserviços e inferência ultrarrápida em CPU.

### Critérios de Implementação
- [x] Padrão Singleton para carregamento único de pesos na memória (evitando recarregamento a cada requisição HTTP).
- [x] Schemas Pydantic (`app/schemas.py`) com validação estrita do formato de bounding box (`x_min`, `y_min`, `x_max`, `y_max`), classe e confiança.
- [x] Filtro configurável para as 10 classes de interesse.
- [x] Branch Git: `feature/yolo-model`.
```

---

### Card 3: `feature/api-setup`
* **Título**: `feature/api-setup - Desenvolvimento da API REST com FastAPI`
* **Membro atribuído**: `Alexandre Virgílio`
* **Coluna Atual**: `Done`
* **Descrição técnica**:
```markdown
### Objetivo
Construir o microserviço backend em FastAPI expondo o endpoint `POST /detect` para recebimento de arquivos binários de imagem via `UploadFile`.

### Especificações Técnicas
- [x] Framework: FastAPI com servidor ASGI Uvicorn.
- [x] Gerenciador de ciclo de vida moderno (`lifespan`) para aquecimento prévio do modelo YOLO.
- [x] Tratamento robusto de erros HTTP: 400 para arquivos não suportados ou corrompidos, 500 para falhas internas.
- [x] Configuração de CORS para integração web/mobile.
- [x] Documentação interativa Swagger UI nativa em `/docs`.
- [x] Branch Git: `feature/api-setup`.
```

---

### Card 4: `feature/tests-and-benchmarks`
* **Título**: `feature/tests-and-benchmarks - Testes Automatizados e Benchmark de Desempenho`
* **Membro atribuído**: `Alexandre Virgílio`
* **Coluna Atual**: `Done`
* **Descrição técnica**:
```markdown
### Objetivo
Criar suíte de testes unitários/integração com pytest e rotina de benchmark de latência e precisão em imagens reais.

### Especificações Técnicas
- [x] Suíte `pytest` com 7 testes cobrindo rotas `/`, `/health`, `/detect` (casos de sucesso e exceção).
- [x] Script `scripts/benchmark.py` com medição empírica de latência (resultado obtido: ~66 ms por imagem / 15 FPS em CPU).
- [x] Script utilitário `scripts/test_request.py` para demonstrações ao vivo.
- [x] Branch Git: `feature/tests-and-benchmarks`.
```

---

### Card 5: `feature/documentation-kanban`
* **Título**: `feature/documentation-kanban - Documentação Técnica (README) e Roteiro de Vídeo`
* **Membro atribuído**: `Alexandre Virgílio`
* **Coluna Atual**: `Done`
* **Descrição técnica**:
```markdown
### Objetivo
Elaborar documentação completa de engenharia de software no `README.md` e roteiro de apresentação em vídeo (máximo 7 minutos).

### Entregáveis
- [x] Descrição do sistema VisionFlow AI, motivação de negócio e detalhamento das 10 classes.
- [x] Guia de instalação (`requirements.txt`) e execução local (`uvicorn app.main:app --reload`).
- [x] Exemplo de payload JSON conforme a especificação do edital.
- [x] Tabela de benchmark de acertos e velocidade.
- [x] Roteiro cronometrado para gravação do vídeo avaliativo.
- [x] Branch Git: `feature/documentation-kanban`.
```

---

## 3. Dica para o Vídeo
Durante a gravação do vídeo, abra a aba do seu navegador no Trello e mostre rapidamente os cartões organizados, destacando como você planejou as tarefas antes de codificar e como cada uma correspondeu a uma `feature/branch` no GitFlow!
