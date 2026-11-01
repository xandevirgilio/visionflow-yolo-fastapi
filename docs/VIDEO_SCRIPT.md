# 🎬 Roteiro de Gravação de Vídeo (Máximo 7 Minutos)

Este roteiro foi estruturado sob medida para garantir a nota máxima (2,0 pts) no critério de **Apresentação do Projeto**, respondendo com clareza e autoridade a todos os pontos exigidos pelo edital.

---

## ⏱️ Linha do Tempo Resumida (5 a 6 minutos)

| Tempo | Seção | O que mostrar na tela |
| :--- | :--- | :--- |
| **00:00 - 00:45** | Introdução & Dataset (10 Classes) | `README.md` ou pasta `data/samples/` |
| **00:45 - 02:00** | Demonstração Prática da API | Navegador no Swagger UI (`http://localhost:8000/docs`) |
| **02:00 - 03:15** | Modelo YOLO & Generalização | Terminal rodando `python scripts/benchmark.py` |
| **03:15 - 04:15** | Metodologia Ágil (Trello / Kanban) | Navegador com o quadro no Trello aberto |
| **04:15 - 05:15** | Engenharia & GitFlow (Branches e Commits) | Terminal com `git log --graph` ou página do GitHub |
| **05:15 - 05:45** | Conclusão e Encerramento | Tela do projeto / Swagger |

---

## 🎙️ Fala Passo a Passo (O que falar e fazer)

### 1. Introdução e Apresentação do Dataset (00:00 - 00:45)
* **O que mostrar:** Mostre o `README.md` ou a pasta `data/samples/`.
* **O que falar:**
  > *"Olá, pessoal e professor Welington! Meu nome é Alexandre Virgílio e hoje apresento o projeto final do Módulo 2 de Machine Learning e Visão Computacional: o **VisionFlow AI**."*  
  > *"O objetivo da nossa aplicação é fornecer um microserviço backend de alta performance para detecção e monitoramento de objetos em mobilidade urbana e cidades inteligentes."*  
  > *"Para atender aos requisitos do edital, selecionamos 10 classes distintas do ecossistema urbano: **person (pedestres)**, **bicycle**, **car**, **motorcycle**, **bus**, **truck**, **traffic light (semáforos)**, **fire hydrant (hidrantes)**, **stop sign (placas de parada)** e **backpack (mochilas de entregadores e pedestres)**. Coletamos e validamos um conjunto de 10 amostras fotográficas reais com variações de ângulo, distância e iluminação."*

---

### 2. Demonstração ao Vivo no Swagger / Postman (00:45 - 02:00)
* **O que mostrar:** Abra o navegador em `http://localhost:8000/docs`.
* **O que falar:**
  > *"Aqui está a nossa API construída com FastAPI e servida pelo Uvicorn. Como podemos ver no Swagger interativo, temos os endpoints de `/health` e o nosso endpoint principal `POST /detect`."*  
  > *(Clique em `/detect` -> `Try it out` -> Selecione uma imagem, por exemplo `01_car.jpg` ou `10_fire_hydrant.jpg` -> Clique em `Execute`).*  
  > *"Vejam que o upload binário é processado e a resposta retorna imediatamente com código HTTP 200 e um JSON perfeitamente estruturado, exatamente como estipulado no edital: traz o status de sucesso e a lista `detections`, contendo o nome da classe, a confiança da predição e as coordenadas normalizadas da bounding box (`x_min`, `y_min`, `x_max`, `y_max`). Vale destacar que, conforme a regra de negócio, a API não retorna a imagem desenhada, mas sim o JSON leve e otimizado para consumo por microserviços e frontends."*

---

### 3. Processo do YOLO e Generalização (02:00 - 03:15)
* **O que mostrar:** Abra o terminal e execute: `python scripts/benchmark.py`.
* **O que falar:**
  > *"Para a arquitetura de visão computacional, escolhemos o **YOLOv8 Nano (yolov8n)**. A justificativa técnica para essa escolha baseia-se na relação entre acurácia e latência: o modelo nano possui apenas 3,2 milhões de parâmetros, tornando-o perfeito para ser servido em microserviços em ambientes de CPU sem requerer GPUs dedicadas caras."*  
  > *"Como vocês podem observar nesta execução do nosso script de benchmark automatizado, o modelo atingiu uma latência média de apenas **66 milissegundos por imagem**, o que equivale a uma taxa de processamento de **15 FPS em CPU pura**."*  
  > *"O modelo generalizou de forma consistente em todas as 10 classes testadas, detectando desde objetos grandes como ônibus e caminhões com mais de 90% de confiança, até elementos de menor escala e contexto denso como hidrantes, mochilas e semáforos."*

---

### 4. Testes do Dataset e Validação (03:15 - 03:45)
* **O que mostrar:** No terminal, execute: `pytest -v`.
* **O que falar:**
  > *"Implementamos uma suíte completa de testes automatizados com `pytest`, cobrindo tanto o serviço de inferência quanto a API FastAPI com o TestClient. Todos os testes passam com 100% de sucesso, validando endpoints saudáveis, integridade das predições, além do tratamento de exceções para arquivos inválidos e corrompidos."*

---

### 5. Organização das Tarefas no Trello (Kanban) (03:45 - 04:30)
* **O que mostrar:** Mude para a aba do navegador com o quadro do **Trello**.
* **O que falar:**
  > *"No quesito metodologia ágil, estruturei todo o planejamento antes de escrever a primeira linha de código utilizando o Trello, compartilhado com o professor Welington. Configuramos as raias canônicas: Backlog, To Do, Doing, Blocked, Review e Done."*  
  > *(Abra um dos cards para mostrar os detalhes).*  
  > *"Todos os cartões foram atribuídos ao meu usuário (Alexandre Virgílio), com descrições detalhadas contendo especificações técnicas, checklists de entrega e a correlação direta com a branch correspondente no GitFlow. Conforme cada funcionalidade avançava, os cartões eram movidos pelas raias até a conclusão em Done."*

---

### 6. Branches do GitHub e Engenharia GitFlow (04:30 - 05:15)
* **O que mostrar:** Mostre o terminal com o comando `git log --graph --oneline` ou a página do repositório no GitHub.
* **O que falar:**
  > *"Para o controle de versionamento, adotamos as melhores práticas do GitFlow:*  
  > *1. A branch `main` mantém exclusivamente versões prontas para produção.*  
  > *2. A branch `develop` atuou como integradora do ciclo de desenvolvimento.*  
  > *3. Criamos branches de funcionalidade isoladas para cada entrega: `feature/dataset-prep` para os dados, `feature/yolo-model` para o detector e schemas, `feature/api-setup` para a API FastAPI, `feature/tests-and-benchmarks` para a suíte de testes e `feature/documentation-kanban` para a documentação e templates.*  
  > *Cada commit foi feito de forma atômica com mensagens no padrão Conventional Commits, e ao final todos os merges foram consolidados na main."*

---

### 7. Encerramento (05:15 - 05:45)
* **O que falar:**
  > *"Com isso, cobrimos com êxito todos os pilares do projeto avaliativo: coleta e validação de dados, engenharia de IA com YOLO, microsserviço de alta performance com FastAPI, testes automatizados e gestão ágil com GitFlow e Kanban. Muito obrigado pela atenção e fico à disposição para dúvidas!"*
