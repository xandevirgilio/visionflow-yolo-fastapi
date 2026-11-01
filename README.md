# 🚀 VisionFlow AI - Microserviço de Detecção de Objetos Urbanos

[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688.svg?style=flat&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB.svg?style=flat&logo=Python&logoColor=white)](https://www.python.org/)
[![YOLOv8](https://img.shields.io/badge/YOLO-v8_Nano-00FFFF.svg?style=flat&logo=Ultralytics&logoColor=black)](https://github.com/ultralytics/ultralytics)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Tests: pytest](https://img.shields.io/badge/tests-pytest-blue.svg)](https://docs.pytest.org/)

Microserviço backend de alto desempenho para detecção de objetos em tempo real utilizando **FastAPI** e **YOLOv8**, desenvolvido para a Situação de Aprendizagem do Módulo 2 do programa **SC-TEC / SENAI**.

---

## 📌 Links do Projeto

* 🌐 **Repositório GitHub:** [https://github.com/xandevirgilio/visionflow-yolo-fastapi](https://github.com/xandevirgilio/visionflow-yolo-fastapi)
* 📋 **Quadro Kanban (Trello):** *(Insira aqui o link público do seu Trello após criar)*
* 🎥 **Vídeo de Demonstração (YouTube / Drive):** *(Insira aqui o link do vídeo gravado)*

---

## 🏙️ Desafio de Negócio & Dataset

O crescimento acelerado das cidades inteligentes demanda soluções automatizadas para monitoramento de fluxo de tráfego, segurança viária e mobilidade. O **VisionFlow AI** foi concebido como um microserviço *backend-only* leve e desacoplado, capaz de receber imagens de câmeras de monitoramento urbano e retornar imediatamente a localização e classificação dos elementos presentes.

### As 10 Classes de Objetos Selecionadas:
O dataset abrange 10 classes do ecossistema de tráfego e vias públicas:

| # | Classe | Descrição e Contexto no Sistema |
| :-: | :--- | :--- |
| **1** | `person` | Pedestres transitando em calçadas e faixas de pedestre |
| **2** | `bicycle` | Ciclistas e bicicletas em ciclovias e vias compartilhadas |
| **3** | `car` | Veículos leves e carros de passeio em tráfego urbano |
| **4** | `motorcycle` | Motocicletas e motoboys de entrega |
| **5** | `bus` | Ônibus de transporte coletivo urbano e rodoviário |
| **6** | `truck` | Caminhões e veículos pesados de carga |
| **7** | `traffic light` | Semáforos e sinalizadores de trânsito |
| **8** | `fire hydrant` | Hidrantes de segurança pública e combate a incêndios |
| **9** | `stop sign` | Placas verticais de parada obrigatória e sinalização |
| **10** | `backpack` | Mochilas e bolsas de pedestres ou entregadores |

---

## 🧠 Arquitetura do Modelo: YOLOv8 Nano

Optou-se pela arquitetura **YOLOv8 Nano (`yolov8n`)** desenvolvida pela Ultralytics.

### Justificativa Técnica:
1. **Eficiência para Microserviços em CPU:** O modelo possui apenas **3,2 milhões de parâmetros** e **8,7 GFLOPs**, viabilizando inferências ultrarrápidas (~66 ms) mesmo em servidores sem placas de vídeo dedicadas (GPUs).
2. **Backbone e Neck Estado-da-Arte:** Utiliza módulos C2f (*Cross Stage Partial with 2 Convolutions*) e *Anchor-Free Detection Head*, garantindo precisão superior (mAP) e convergência consistente em objetos de diferentes escalas.
3. **Padrão de Carregamento Singleton:** O modelo é pré-carregado no ciclo de vida (*lifespan*) da aplicação FastAPI, eliminando o *cold-start* e mantendo a memória cache aquecida para requisições subsequentes.

---

## ⚡ Resultados e Benchmark de Desempenho

Resultados obtidos via execução do script automatizado `scripts/benchmark.py` sobre as 10 imagens do conjunto de testes:

| Métrica | Resultado Obtido |
| :--- | :--- |
| **Latência Média por Imagem** | **66.49 ms** |
| **Taxa de Processamento (Throughput)** | **15.0 FPS (em CPU)** |
| **Menor Latência Observada** | **55.88 ms** |
| **Taxa de Reconhecimento das 10 Classes** | **100%** de detecção bem-sucedida com alta confiança |

---

## 🛠️ Instalação e Execução Local

### Pré-requisitos:
- Python 3.10 ou superior
- Git

### 1. Clonar o Repositório
```bash
git clone https://github.com/xandevirgilio/visionflow-yolo-fastapi.git
cd visionflow-yolo-fastapi
```

### 2. Criar e Ativar o Ambiente Virtual
```bash
# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instalar Dependências
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Executar o Servidor FastAPI
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
O servidor estará disponível em:
* 📖 **Documentação Interativa (Swagger UI):** [http://localhost:8000/docs](http://localhost:8000/docs)
* 📑 **Documentação Alternativa (ReDoc):** [http://localhost:8000/redoc](http://localhost:8000/redoc)
* 🩺 **Health Check:** [http://localhost:8000/health](http://localhost:8000/health)

---

## 📡 Exemplo de Uso da API

### Requisição via cURL (Upload de Imagem)
```bash
curl -X POST "http://localhost:8000/detect" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@data/samples/01_car.jpg;type=image/jpeg"
```

### Exemplo de Payload JSON de Retorno
Conforme estritamente especificado na seção 5.1 do edital:

```json
{
  "status": "success",
  "detections": [
    {
      "class_name": "car",
      "confidence": 0.9023,
      "box": {
        "x_min": 192.45,
        "y_min": 224.12,
        "x_max": 478.89,
        "y_max": 420.35
      }
    },
    {
      "class_name": "truck",
      "confidence": 0.3418,
      "box": {
        "x_min": 15.30,
        "y_min": 180.20,
        "x_max": 140.75,
        "y_max": 310.60
      }
    }
  ]
}
```

---

## 🧪 Testes Automatizados

O projeto conta com suíte completa de testes usando `pytest`:

```bash
# Executar todos os testes com saída detalhada
pytest -v

# Executar benchmark de desempenho
python scripts/benchmark.py
```

---

## 🌳 Engenharia de Software e GitFlow

O desenvolvimento seguiu rigorosamente a metodologia GitFlow, com commits no padrão *Conventional Commits*:

```
main ───────────●────────────────────────────● (v1.0.0 Final)
                 \                          /
develop ──────────●───●────●────●────●─────● (Integração)
                   \ /  \  / \  / \  / \  /
feature/dataset-prep●    │  │  │  │  │  │   (Amostras e 10 Classes)
feature/yolo-model───────●  │  │  │  │  │   (Serviço YOLOv8 & Schemas)
feature/api-setup───────────●  │  │  │  │   (FastAPI & /detect)
feature/tests-and-benchmarks───●  │  │  │   (Pytest & Benchmark)
feature/documentation-kanban──────●──┘  │   (Docs, Trello & Roteiro)
```

---

## 👥 Metodologia Ágil (Kanban)

O planejamento de tarefas foi realizado através do Trello, estruturado nas seguintes raias:
* **Backlog:** Ideias e refinamento de requisitos do edital.
* **To Do:** Tarefas priorizadas com especificações técnicas e membros atribuídos.
* **Doing:** Funcionalidades em desenvolvimento ativo na respectiva branch.
* **Blocked:** Impedimentos técnicos (nenhum bloqueio crítico registrado).
* **Review:** Revisão de código, validação de tipagem e execução de testes.
* **Done:** Tarefas aprovadas e integradas à branch `develop`.

---

## 👨‍💻 Autor

* **Alexandre Virgílio** ([@xandevirgilio](https://github.com/xandevirgilio))
* **E-mail:** `alexandrevirgilio1986@gmail.com`
* **Programa:** SC-TEC / SENAI Santa Catarina (Módulo 2 - Visão Computacional)
* **Professor Responsável:** Welington Souza (`welington.souza@edu.sc.senai.br`)

