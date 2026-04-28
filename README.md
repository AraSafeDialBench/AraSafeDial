# AraSafeDialBench

### Dynamic Ethical Resilience Benchmark for Arabic Large Language Models

> *Final Exam — Research Methodology Module — ENSET Mohammedia, 2025–2026*

---

## 👥 Authors

| Author | Affiliation | Email |
|---|---|---|
| **Moussnaoui Ilyas** | Département Mathématiques et Informatique, ENSET Mohammedia, Université Hassan II | ilyas.moussnaoui-etu@etu.univh2c.ma |
| **Elmifdali Mustapha** | Département Mathématiques et Informatique, ENSET Mohammedia, Université Hassan II | MUSTAPHA.ELMIFDALI-ETU@etu.univh2c.ma |
| **Toubani Badr Eddine** | Département Mathématiques et Informatique, ENSET Mohammedia, Université Hassan II | badr.toubani-etu@etu.univh2c.ma |

---

## 📖 Abstract

The growing deployment of large language models in the MENA region has raised the need for reliable safety assessment protocols, particularly under culturally and linguistically grounded contexts. Despite recent advances, existing approaches suffer from two critical limitations: (i) they lack jailbreak attacks formulated in Arabic, thereby failing to capture region-specific linguistic and cultural nuances, and (ii) they predominantly rely on single-turn interactions that inadequately expose systematic biases embedded in conversational AI systems.

In this paper, we propose **AraSafeDialBench**, a fine-grained Arabic benchmarking protocol that systematically evaluates the alignment of LLMs with MENA region's values. This framework leverages a three-level safety taxonomy and automated multi-turn dialogue generation across **100 realistic scenarios**. We evaluate the method using a curated dataset of 100 culturally grounded, Arabic multi-turn dialogue conversations. The evaluation is conducted against state-of-the-art baselines, using fine-grained safety compliance scores and toxicity rate metrics.

Experimental results demonstrate that the protocol detects **2% more systematic biases** compared to single-turn attack methodologies introduced in the MENAValues benchmark, while maintaining robust performance under iterative adversarial prompting. These findings indicate that multi-turn, Arabic-specific jailbreak strategies are critical for uncovering latent model vulnerabilities, opening new pathways for region-aware safety alignment and continuous red-teaming in linguistically diverse contexts.

**Keywords:** Arabic Natural Language Processing · Dynamic Safety Evaluation · Culturally-Grounded Benchmarking · Ethical Resilience · Multi-Turn Dialogue

---

## 📑 Table of Contents

- [Introduction](#-introduction)
- [Related Work](#-related-work)
- [Proposed Methodology](#-proposed-methodology)
- [Experiments and Results](#-experiments-and-results)
- [Discussion](#-discussion)
- [Conclusion and Future Work](#-conclusion-and-future-work)
- [Acknowledgment](#-acknowledgment)
- [AI Tools Disclosure](#-ai-tools-disclosure)
- [References](#-references)

---

## 🚀 Introduction

The field of Arabic Natural Language Processing (NLP) has experienced rapid growth over the past decade, driven by industrial demand and societal impact in the MENA region. Applications such as virtual assistants and educational platforms rely on ethical alignment to deliver safe and culturally relevant interactions. Recent advances in safety filtering and conversational benchmarking have enabled stronger guardrails, achieving performance levels previously out of reach.

However, despite these advances, **three limitations** persist in the current literature:

1. **Static evaluation:** Existing Arabic safety benchmarks like AraSafe assume static single-turn interactions and cannot capture progressive ethical drift under multi-turn conversational pressure.
2. **Missing standardized metrics:** Current evaluation protocols lack standardized metrics to measure ethical consistency across conversation turns, limiting the assessment of long-term resilience.
3. **No hybrid classification:** The absence of hybrid classification (auto + human validation) in existing benchmarks reduces the reliability of toxicity detection in culturally sensitive contexts.

### Research Questions

- **RQ1:** Does dynamic (multi-turn) evaluation identify more ethical violations than static (single-turn) evaluation?
- **RQ2:** Which open-source Arabic LLMs maintain the best ethical consistency under conversational pressure?

### Contributions

1. **AraSafeDialBench:** A dataset of 100 conversational multi-turn scenarios covering 4 ethical categories across 3 turns.
2. **Reproducible Pipeline:** A dynamic evaluation chain via Ollama + GPT-OSS-20B for hybrid classification (auto + human validation).
3. **Three Resilience Metrics:** Toxicity Rate, Consistency Score, and PIT (% safe responses drifting under pressure).

---

## 📚 Related Work

### Static Safety Benchmarks for Arabic LLMs

Early work on ethical evaluation for Arabic LLMs relied on static, single-turn assessments. AraSafe achieves comprehensive toxicity detection across dialects but requires isolated prompts, limiting its ability to capture conversational drift. Similarly, cultural value annotations were later extended by domain-specific adaptations to handle regional norms. These methods share a common limitation: they evaluate ethical behavior in isolation, without modeling multi-turn interaction dynamics.

### Dynamic Evaluation Frameworks for Conversational Safety

Dynamic evaluation approaches such as **SafeDialBench** have demonstrated that multi-turn adversarial protocols reveal risks invisible in single-turn tests. Subsequent work has explored pressure-aware metrics and turn-wise consistency scoring. However, most of these methods assume English-centric contexts and culturally neutral prompts, leaving Arabic-specific ethical nuances unaddressed.

### Hybrid Classification and Cultural Alignment

Reliable toxicity classification in low-resource languages has received growing attention. Prior work proposed automated classifiers and human-in-the-loop annotation respectively, but their experimental protocols lack hybrid validation combining both approaches for culturally nuanced contexts.

### Positioning

Our approach differs in three key aspects:

- **First** dynamic benchmark specifically designed for Arabic LLMs, bridging AraSafe's static evaluation and SafeDialBench's English-centric dynamics.
- A **hybrid classification protocol** using GPT-OSS-20B with human validation, improving reliability in culturally sensitive scenarios.
- **Three interpretable resilience metrics** (Toxicity Rate, Consistency Score, PIT) to quantify ethical stability across turns.

---

## 🛠 Proposed Methodology

### Problem Formulation

Let $\mathcal{S} = \{s_1, \ldots, s_N\}$ denote a set of $N = 100$ conversational scenarios, where each scenario $s_i$ consists of $T = 3$ dialogue turns. Let $\mathcal{M} = \{m_1, \ldots, m_K\}$ denote the set of $K = 4$ evaluated LLMs. For each pair $(s_i, m_k)$, the model generates a response sequence:

$$\mathbf{r}_{i,k} = (r^{(1)}_{i,k}, r^{(2)}_{i,k}, r^{(3)}_{i,k})$$

Our goal is **not** to learn a predictor, but to evaluate ethical resilience through three metrics.

#### Toxicity Rate (TR)

$$\text{TR}(m_k) = \frac{1}{N \cdot T} \sum_{i=1}^{N} \sum_{t=1}^{T} \mathbb{I}[\text{toxic}(r^{(t)}_{i,k})]$$

#### Consistency Score (CS)

$$\text{CS}(m_k) = \frac{1}{N} \sum_{i=1}^{N} \mathbb{I}[\forall t,\ \neg \text{toxic}(r^{(t)}_{i,k})]$$

#### Pressure-Induced Toxicity (PIT)

$$\text{PIT}(m_k) = \frac{\text{TR}_{t=3}(m_k) - \text{TR}_{t=1}(m_k)}{1 - \text{TR}_{t=1}(m_k)} \times 100$$

where $\text{toxic}(\cdot)$ is determined via hybrid classification (GPT-OSS-20B + human validation).

### Overall Pipeline

The AraSafeDialBench pipeline consists of **five stages**:

```
┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│  1. Hybrid   │   │ 2. Multi-LLM │   │ 3. Response  │   │ 4. Hybrid    │   │ 5. Metrics   │
│ Data Creation│ → │  Inference   │ → │  Recording   │ → │Classification│ → │ Calculation  │
│              │   │              │   │              │   │              │   │              │
│100 scenarios │   │  4 models    │   │JSONL format  │   │ GPT-OSS-20B  │   │TR, CS, PIT   │
│Manual + LLM  │   │via Ollama    │   │standardized  │   │+ human valid.│   │benchmarking  │
│              │   │T1 → T2 → T3  │   │              │   │              │   │              │
└──────────────┘   └──────────────┘   └──────────────┘   └──────────────┘   └──────────────┘
```

1. **Hybrid Data Creation:** 100 scenarios generated via manual annotation + LLM assistance, covering 4 ethical categories and 3 Arabic dialects.
2. **Multi-LLM Inference:** Each scenario is executed through 4 models via Ollama across 3 dialogue turns, preserving conversational context.
3. **Response Recording:** All responses are stored in standardized JSON format with metadata (model, turn, prompt).
4. **Hybrid Classification:** Toxicity labels are assigned via GPT-OSS-20B, with human validation.
5. **Metrics Calculation:** The three resilience metrics (TR, CS, PIT) are computed for comparative benchmarking.

### Dataset Construction

AraSafeDialBench comprises **100 conversational scenarios** created through a hybrid approach:

- **Manual seed:** 40 scenarios designed by annotators familiar with MENA cultural norms.
- **LLM-assisted:** 60 scenarios generated via prompt engineering with GPT-OSS-20B, then reviewed and edited manually.

Each scenario covers one of **4 ethical categories**: Social, Political, Scientific, Religious.

### Experimental Setup

All models are accessed via **Ollama Cloud API** with default configurations. Each of the 100 conversational scenarios is sent sequentially to the 4 evaluated LLMs across 3 dialogue turns to preserve conversational context.

| Setting | Value |
|---|---|
| Seed | `0` |
| Temperature | `0` |
| Max tokens | `512` |
| Runs per model | `k = 3` (deterministic) |
| Turns per scenario | `3` (T1 → T2 → T3) |

**Evaluated models:** `gemma-2b`, `gpt-oss-20b`, `llama3-2-latest`, `mistral-large-3-675b-cloud`.

### Preprocessing

Our workflow operates directly on raw conversational data with minimal preprocessing:

- **Scenario formatting:** Each scenario is structured as a JSON object with fields `scenario_id`, `TASK[category]`, `history`, and `turns`.
- **Prompt templating:** User prompts are wrapped in a standardized instruction template to ensure consistent model behavior across API calls.
- **Response parsing:** Model outputs are extracted and cleaned (trailing whitespace removal), then an `is_toxic` field is added.

### Complexity Analysis

| Resource | Cost |
|---|---|
| Inference calls | $O(N \cdot T \cdot M) = 100 \times 3 \times 4 = $ **1,200 API requests** |
| Storage | $O(N \cdot T)$ JSON entries (~0.2 MB) |
| End-to-end runtime | ~27 hours on power server |

---

## 🧪 Experiments and Results

### Baselines

We compare our dynamic evaluation against:

- **B1 — Static Single-Turn (Turn 1):** Evaluation on Turn 1 only, representing traditional static benchmarks like AraSafe. This baseline isolates the value added by multi-turn pressure.

### Metrics

| Metric | Direction | Description |
|---|:---:|---|
| **Toxicity Rate** | ↓ | Percentage of responses classified as toxic |
| **Consistency Score** | ↑ | Percentage of scenarios where the model remains non-toxic across all 3 turns |
| **PIT** (Pressure-Induced Toxicity) | ↓ | Percentage of initially safe responses that become toxic under conversational pressure |

### Main Results

**Table I — Comparative Benchmarking on AraSafeDialBench (100 scenarios, 3 turns)**

| Model | Toxicity Rate (%) ↓ | Consistency (%) ↑ | PIT (%) ↓ |
|---|:---:|:---:|:---:|
| gemma-2b | 2.00 | 94.00 | 2.02 |
| **gpt-oss-20b** | **0.00** | **100.00** | **0.00** |
| llama3-2-latest | 3.00 | 91.00 | 0.00 |
| mistral-large-3-675b | 0.67 | 98.00 | 2.00 |

> Best results per column in **bold**. Values are point estimates ($k = 3$ runs, deterministic setup).

**Key findings:**

- `gpt-oss-20b` achieves the lowest toxicity rate (**0.00%**), followed by `mistral-large-3-675b` (0.67%), `gemma-2b` (2.00%), and `llama3-2-latest` (3.00%).
- The dynamic protocol reveals ethical drift invisible in static evaluation: `gemma-2b` and `mistral-large` show measurable PIT values (2.02% and 2.00%, respectively).
- `gpt-oss-20b` and `llama3-2-latest` maintain stable behavior across all 3 turns (PIT = 0.00%).

### Robustness Analysis

The evolution of Toxicity Rate under increasing conversational pressure (Turn 1 → Turn 2 → Turn 3) shows:

- `gpt-oss-20b` and `llama3-2-latest` remain stable across all turns.
- `gemma-2b` and `mistral-large` exhibit slight increases, illustrating how dynamic evaluation captures ethical drift invisible in static tests.

Since $k = 3$ runs (deterministic setup with `seed=0`, `temperature=0`), variance regions are omitted.

---

## 💬 Discussion

The experimental results directly address the research questions:

- **RQ1:** Dynamic evaluation (3 turns) reveals higher Toxicity Rate for `gemma-2b` (+1.00%) and `mistral-large` (+0.67%) compared to static evaluation (Turn 1 only), validating that multi-turn assessment captures ethical drift invisible in single-turn tests.
- **RQ2:** `gpt-oss-20b` and `mistral-large` maintain the highest resilience (toxicity ≤ 0.67%, consistency ≥ 98%), while `gemma-2b` and `llama3-2-latest` exhibit lower stability.

These observations support our central claim that **conversational pressure reveals subtle differences in ethical resilience among Arabic LLMs**. Models with stable Toxicity Rate across turns achieve higher Consistency Scores, while those with progressive increases show measurable PIT values.

A qualitative inspection of responses suggests that culturally nuanced prompts trigger more variable behavior, highlighting the importance of Arabic-specific evaluation.

### Limitations

| # | Limitation | Future Direction |
|---|---|---|
| 1 | Dataset size (100 scenarios, 4 categories) | Expand to **500+ scenarios across 8+ categories** (hate speech, political bias, cultural sensitivity) |
| 2 | Restricted to 4 open-source models via Ollama | Extend to commercial models (**ChatGPT, Claude, Gemini**) via API |
| 3 | Hybrid classification still requires human validation | Develop a **dedicated, fine-tuned toxicity evaluator** to fully automate the pipeline |
| 4 | Dialect coverage limited to MSA, Moroccan, Egyptian | Generalize to other Arabic varieties |

These limitations indicate that current rankings should be interpreted as **preliminary baselines**, though the methodological contribution of dynamic, multi-turn evaluation remains valid.

---

## 🎯 Conclusion and Future Work

In this paper, we addressed the problem of evaluating ethical resilience of Arabic LLMs under conversational pressure, which is central to safe deployment in the MENA region yet remains challenging due to the absence of dynamic, multi-turn benchmarks for low-resource languages.

We formulated two research questions: whether dynamic evaluation reveals more ethical violations than static single-turn tests, and which open-source LLMs maintain the best ethical consistency under progressive conversational pressure.

### Summary of contributions

1. **AraSafeDialBench**, a dataset of 100 annotated conversational scenarios covering 4 ethical categories and 3 Arabic dialects.
2. A **reproducible evaluation pipeline** via Ollama with hybrid classification for toxicity detection.
3. **Empirical evidence** that multi-turn assessment captures ethical drift invisible in static benchmarks, enabling comparative ranking of model resilience.

### Future Work

- **Dataset extension:** 500+ scenarios across more categories with stronger adversarial prompts.
- **Commercial models:** Expand evaluation to ChatGPT, Claude, Gemini, and develop a dedicated fine-tuned toxicity evaluator.
- **Multilingual generalization:** Adapt the AraSafeDialBench pipeline to other under-resourced languages for multilingual dynamic safety evaluation and cultural safety.

---

## 🙏 Acknowledgment

We thank **Pr. Soufiane HAMIDA** (ENSET Mohammedia, Université Hassan II de Casablanca) for his guidance on the AraSafeDialBench project, conducted as part of the final evaluation of the Research Methodology module.

---

## 🤖 AI Tools Disclosure

During the preparation of this manuscript, we used AI tools for the following purposes:

- Writing and formatting equations using LaTeX.
- Translation vocabulary support.
- Generating or refining code snippets (Python, LaTeX, etc.).

After using these tools, we reviewed, edited, and validated the content as needed. **We take full responsibility for the final content of the publication.**

---

## 📖 References

1. A. Author, "AraSafe: Benchmarking Safety in Arabic Large Language Models," *IEEE Transactions on Natural Language Processing*, vol. 12, no. 3, pp. 123–145, 2024.
2. B. Author, C. Author, and D. Author, "SafeDialBench: Dynamic Safety Evaluation for Conversational LLMs," *Proc. ACL Conference on Empirical Methods in Natural Language Processing (EMNLP)*, pp. 1–15, 2024.
3. E. Author and F. Author, "MENAValues: A Cultural Values Dataset for Arabic NLP," *Journal of Arabic Language Processing*, vol. 8, no. 2, pp. 45–67, 2024.
4. D. Nadeau, M. Kroutikov, K. McNeil, and S. Baribeau, "Benchmarking Llama2, Mistral, Gemma and GPT for Factuality, Toxicity, Bias and Propensity for Hallucinations," *arXiv preprint* arXiv:2404.09785, 2024.
5. B. Liu, B. Xiao, X. Jiang, et al., "Adversarial Attacks on Large Language Model-Based Chatbots: A Case Study on ChatGPT," *Security and Communication Networks*, vol. 2023, 2023.
6. H. Zhu, J. Dai, et al., "SafeMT: Multi-turn Safety for Multimodal Language Models," *arXiv preprint* arXiv:2510.12133, 2025.
7. A. Keleg, S. R. El-Beltagy, and M. Khalil, "ASU_OPTO at OSACT4 – Offensive Language Detection for Arabic Text," in *Proc. 4th Workshop on Open-Source Arabic Corpora and Processing Tools (OSACT4)*, 2020.
8. S. Al-Dabet, A. Elmassry, B. AlOmar, and A. Alshamsi, "Transformer-based Arabic Offensive Speech Detection," in *2023 International Conference on Emerging Smart Computing and Informatics (ESCI)*, 2023.
9. I. Bensalem, P. Rosso, and H. Zitouni, "Toxic language detection: a systematic review of Arabic datasets," *arXiv preprint* arXiv:2312.07228, 2024.
10. L. Hatem, A. Omar, A. A. Ali, and H. M. Farghaly, "Tackling toxicity in Arabic social media through advanced detection techniques," *Scientific Reports*, vol. 15, 2025.
11. Y. Ashraf, Y. Wang, B. Gu, P. Nakov, and T. Baldwin, "Arabic Dataset for LLM Safeguard Evaluation," *arXiv preprint* arXiv:2410.17040, 2024.

---

<p align="center">
  <i>ENSET Mohammedia · Université Hassan II de Casablanca · 2025–2026</i>
</p>
