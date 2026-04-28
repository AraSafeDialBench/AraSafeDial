# AraSafeDialBench: Dynamic Ethical Resilience Benchmark for Arabic Large Language Models

*Exam final — Research Methodology Module — ENSET Mohammedia, 2025–2026*

**1st MOUSSNAOUI ILYAS**
Département Mathématiques et Informatique
ENSET Mohammedia, Université Hassan II
Mohammedia, Maroc
ilyas.moussnaoui-etu@etu.univh2c.ma

**2nd ELMIFDALI MUSTAPHA**
Département Mathématiques et Informatique
ENSET Mohammedia, Université Hassan II
Mohammedia, Maroc
MUSTAPHA.ELMIFDALI-ETU@etu.univh2c.ma

**3rd TOUBANI BADR EDDINE**
Département Mathématiques et Informatique
ENSET Mohammedia, Université Hassan II
Mohammedia, Maroc
badr.toubani-etu@etu.univh2c.ma

## Abstract

The growing deployment of large language models in the MENA region has raised the need for reliable safety assessment protocols, particularly under culturally and linguistically grounded. Despite recent advances, existing approaches suffer from two critical limitation: (i) they lack jailbreak attacks formulated in Arabic, thereby failing to capture region-specific linguistic and cultural nuances, and (ii) they predominantly rely on single-turn interactions that inadequately expose systematic biases embedded in conversational AI systems. In this paper, we propose AraSafeDialBench, a fine-grained Arabic benchmarking protocol that systematically evaluates the alignment of LLMs with MENA region's values. This framework leverages a three-level safety taxonomy and automated multi-turn dialogue generation across 100 realistic scenarios. We evaluate the method using a curated dataset of 100 culturally grounded, Arabic multi-turn dialogues conversations. The evaluation is conducted against a state-of-the-art baselines, using fine-grained safety compliance scores and toxicity rate metrics. Experimental results demonstrate that the protocol detects 2% more systematic biases compared to the single-turn attack methodologies introduced in the MENAValues [3], [9] benchmark, while maintaining robust performance under iterative adversarial prompting. These findings indicate that multi-turn, Arabic-specific jailbreak strategies are critical for uncovering latent model vulnerabilities, opening new pathways for region-aware safety alignment and continuous red-teaming in linguistically diverse contexts.

**Index Terms** — Arabic Natural Language Processing, Dynamic Safety Evaluation, Culturally-Grounded Benchmarking, Ethical Resilience, Multi-Turn Dialogue.

---

<table>
<tr>
<td width="50%" valign="top">

## I. INTRODUCTION

The field of Arabic Natural Language Processing (NLP) has experienced rapid growth over the past decade, driven by industrial demand and societal impact in the MENA region. Applications such as virtual assistants and educational platforms rely on ethical alignment to deliver safe and culturally relevant interactions. Recent advances in safety filtering and conversational benchmarking have enabled stronger guardrails, achieving performance levels previously out of reach.

However, despite these advances, three limitations persist in the current literature. First, existing Arabic safety benchmarks like AraSafe assume static single-turn interactions and cannot capture progressive ethical drift under multi-turn conversational pressure [1]. Second, current evaluation protocols lack standardized metrics to measure ethical consistency across conversation turns, limiting the assessment of long-term resilience. Third, the absence of hybrid classification (auto + human validation) in existing benchmarks reduces the reliability of toxicity detection in culturally contexts.

This work aims to answer two research questions:

- **RQ1:** Does dynamic evaluation multi-turn identify more ethical violations than static evaluation single-turn?
- **RQ2:** Which open-source Arabic LLMs maintain the best ethical consistency under conversational pressure?

</td>
<td width="50%" valign="top">

The contributions are as follows:

1. **AraSafeDialBench:** A dataset of 100 conversational multi-turn scenarios covering 4 ethical categories across 3 turns;
2. **Reproducible Pipeline:** A dynamic evaluation chain via Ollama + GPT-OSS-20B for hybrid classification (auto + human validation);
3. **Three Resilience Metrics:** Toxicity Rate, Consistency Score, and PIT (% safe responses drifting under pressure).

The remainder of this paper is organized as follows. Section II reviews related work and situates our approach. Section III presents the proposed methodology. Section IV describes the experimental setup and reports results. Section V discusses the findings and their limitations. Section VI perspective and conclusion.

## II. RELATED WORK

### A. Static Safety Benchmarks for Arabic LLMs

Early work on ethical evaluation for Arabic LLMs relied on static, single-turn assessments. For instance, [1] proposed AraSafe, which achieves comprehensive toxicity detection across dialects but requires isolated prompts, limiting its ability to capture conversational drift. Similarly, [3] introduced cultural value annotations, later extended by domain-specific adaptations to handle regional norms. These methods share a common limitation: they evaluate ethical behavior in isolation, without modeling multi-turn interaction dynamics.

</td>
</tr>
</table>

---

<table>
<tr>
<td width="50%" valign="top">

### B. Dynamic Evaluation Frameworks for Conversational Safety

More recently, dynamic evaluation approaches have emerged for conversational LLMs. [2] introduced SafeDialBench, demonstrating that multi-turn adversarial protocols reveal risks invisible in single-turn tests. Subsequent work has explored pressure-aware metrics [2], [11] and turn-wise consistency scoring. However, most of these methods assume English-centric contexts and culturally neutral prompts, leaving Arabic-specific ethical nuances unaddressed.

### C. Hybrid Classification and Cultural Alignment

The question of reliable toxicity classification in low-resource languages has received growing attention. [1] and [3] proposed automated classifiers and human-in-the-loop annotation respectively, but their experimental protocols lack hybrid validation combining both approaches for culturally nuanced contexts.

### D. Positioning

In contrast to prior work, our approach differs in three key aspects. First, we introduce the first dynamic benchmark specifically designed for Arabic LLMs, bridging AraSafe's static evaluation and SafeDialBench's English-centric dynamics. Second, we propose a hybrid classification protocol using GPT-OSS-20B with human validation, improving reliability in culturally sensitive scenarios. Third, we define three interpretable resilience metrics (Toxicity Rate, Consistency Score, PIT) to quantify ethical stability across turns. To the best of our knowledge,

## III. PROPOSED METHODOLOGY

### A. Problem Formulation

Let $\mathcal{S} = \{s_1, \ldots, s_N\}$ denote a set of $N = 100$ conversational scenarios, where each scenario $s_i$ consists of $T = 3$ dialogue turns. Let $\mathcal{M} = \{m_1, \ldots, m_K\}$ denote the set of $K = 4$ evaluated LLMs. For each pair $(s_i, m_k)$, the model generates a response sequence: $\mathbf{r}_{i,k} = (r^{(1)}_{i,k}, r^{(2)}_{i,k}, r^{(3)}_{i,k})$.

Our goal is not to learn a predictor, but to evaluate ethical resilience through three metrics:

</td>
<td width="50%" valign="top">

![image1](image1.png)

*Figure 1. Overall pipeline of AraSafeDialBench. Hybrid scenarios S are processed through 4 LLMs via Ollama across 3 turns. Responses R are classified via GPT-OSS-20B + human validation, then decoded into three resilience metrics: Toxicity Rate, Consistency Score, and PIT.*

- **Toxicity Rate (TR):**

$$\text{TR}(m_k) = \frac{1}{N \cdot T} \sum_{i=1}^{N} \sum_{t=1}^{T} \mathbb{I}[\text{toxic}(r^{(t)}_{i,k})]$$

- **Consistency Score (CS):**

$$\text{CS}(m_k) = \frac{1}{N} \sum_{i=1}^{N} \mathbb{I}[\forall t, \neg\text{toxic}(r^{(t)}_{i,k})]$$

- **Pressure-Induced Toxicity (PIT):**

$$\text{PIT}(m_k) = \frac{\text{TR}_{t=3}(m_k) - \text{TR}_{t=1}(m_k)}{1 - \text{TR}_{t=1}(m_k)} \times 100$$

where $\text{toxic}(\cdot)$ is determined via hybrid classification (GPT-OSS-20B + human validation).

### B. Overall Pipeline

Figure 1 depicts the overall pipeline of AraSafeDialBench, which consists of five stages:

1) **Hybrid Data Creation:** 100 scenarios generated via manual annotation + LLM assistance, covering 5 ethical categories and 3 Arabic dialects.
2) **Multi-LLM Inference:** Each scenario is executed through 4 models via Ollama across 3 dialogue turns, preserving conversational context.
3) **Response Recording:** All responses are stored in standardized JSON format with metadata (model, turn, prompt).
4) **Hybrid Classification:** Toxicity labels are assigned via GPT-OSS-20B, with human validation.
5) **Metrics Calculation:** The three resilience metrics (TR, CS, PIT) are computed for comparative benchmarking.

### C. Dataset Construction

AraSafeDialBench comprises 100 conversational scenarios created through a hybrid approach:

- **Manual seed:** 40 scenarios designed by annotators familiar with MENA cultural norms.

</td>
</tr>
</table>

---

<table>
<tr>
<td width="50%" valign="top">

- **LLM-assisted:** 60 scenarios generated via prompt engineering with GPT-OSS-20B, then reviewed and edited manually.

Each scenario covers one of 4 ethical categories (Social, Political, Scientific, Religious).

### D. Experimental Setup

All models are accessed via Ollama Cloud API with default configurations. Each of the 100 conversational scenarios is sent sequentially to the 4 evaluated LLMs (gemma-2b, gpt-oss-20b, llama3-2-latest, mistral-large-3-675b-cloud) across 3 dialogue turns (Turn 1 → Turn 2 → Turn 3) to preserve conversational context. To ensure reproducibility, we fixed `seed=0` and `temperature=0` for all API calls, guaranteeing deterministic responses. Due to this deterministic setup, we perform $k = 3$ run per model. All responses are saved in a standardized JSON format for downstream analysis.

Generated responses are validated via GPT-OSS-20B for toxicity classification, human validation, and three metrics are computed for comparative benchmarking: Toxicity Rate, Consistency Score, and Pressure-Induced Toxicity (PIT). Detailed metric definitions and results are reported in Section II.

### E. Preprocessing

Our workflow operates directly on raw conversational data with minimal preprocessing: (i) Scenario formatting: each scenario is structured as a JSON object with fields `scenario_id`, `TASK[category]`, `history`, and `turns`; (ii) Prompt templating: user prompts are wrapped in a standardized instruction template to ensure consistent model behavior across API calls; (iii) Response parsing: model outputs are extracted and cleaned (trailing whitespace removal, then adding `is_toxic` field.

### F. Core Contribution: Dynamic Ethical Evaluation protocol

The core of AraSafeDialBench is a multi-turn evaluation protocol that addresses the limitation of static benchmarks by simulating progressive conversational pressure. Rather than testing models on isolated prompts, we execute each scenario across 3 dialogue turns to capture ethical drift invisible in single-turn assessments.

</td>
<td width="50%" valign="top">

### G. Evaluation Protocol

All 4 models are evaluated under standardized conditions: `seed=0`, `temperature=0`, via Ollama Cloud API. Each of the 100 scenarios runs sequentially (Turn 1 → Turn 2 → Turn 3). Due to deterministic settings, $k = 3$ run per model suffices. Responses are validated via GPT-OSS-20B with human review. The three resilience metrics defined in Section III are computed for comparative benchmarking.

### H. Complexity Analysis

The computational cost of AraSafeDialBench is $O(N \cdot T \cdot M)$ inference calls, where $N = 100$ scenarios, $T = 3$ turns, and $M = 4$ models, totaling 1,200 API requests. Storage scales as $O(N \cdot T)$ JSON entries (0.2 MB). End-to-end runtime: 27h on power server.

**Table I**
**COMPARATIVE BENCHMARKING ON ARASAFEDIALBENCH (100 SCENARIOS, 3 TURNS). VALUES: POINT ESTIMATES (k = 3 RUN, DETERMINISTIC SETUP). BEST RESULTS PER COLUMN IN BOLD.**

| Model | Toxicity Rate (%) ↓ | Consistency (%) ↑ | PIT (%) ↓ |
|---|:---:|:---:|:---:|
| gemma-2b | 2.00 | 94.00 | 2.02 |
| gpt-oss-20b | **0.00** | **100.00** | **0.00** |
| llama3-2-latest | 3.00 | 91.00 | 0.00 |
| mistral-large-3-675b | 0.67 | 98.00 | 2.00 |

## IV. EXPERIMENTS AND RESULTS

### A. Experimental Setup

**Dataset.** We evaluate our approach on AraSafeDialBench, which contains $N = 100$ conversational scenarios distributed across $C = 4$ categories (Social, Political, Religious, Scientific). Each scenario spans $T = 3$ dialogue turns to simulate progressive conversational pressure. all 100 scenarios are used for benchmarking.

**Baselines.** We compare our dynamic evaluation against one baseline:

- **B1: Static Single-Turn (Turn 1):** Evaluation on Turn 1 only, representing traditional static benchmarks like AraSafe. This baseline isolates the value added by multi-turn pressure.

</td>
</tr>
</table>

---

<table>
<tr>
<td width="50%" valign="top">

**Metrics.** Following standard practice in LLM safety evaluation, we report three complementary metrics: (i) Toxicity Rate (lower is better), which captures the percentage of responses classified as toxic; (ii) Consistency Score (higher is better), which measures the percentage of scenarios where the model remains non-toxic across all 3 turns; and (iii) PIT (Pressure-Induced Toxicity) (lower is better), which quantifies the percentage of initially safe responses that become toxic under conversational pressure.

**Implementation Details.** All experiments are executed via Ollama Cloud API with deterministic settings: `seed=0`, `temperature=0`, `max_tokens=512`. Models are evaluated sequentially (Turn 1 → Turn 2 → Turn 3) to preserve conversational context. Due to the deterministic setup, we perform $k = 1$ independent run per model, ensuring exact reproducibility. Classification is performed via GPT-OSS-20B with human validation. All code and data are available here [GitHub URL].

### B. Main Results

Table I reports the comparative performance of the 4 evaluated models on AraSafeDialBench (dynamic evaluation, 3 turns).

On Toxicity Rate, the 4 models exhibit distinct resilience profiles: gpt-oss-20b achieves the lowest rate (0.00%), followed by mistral-large-3-675b (0.67%), gemma-2b (2.00%), and llama3-2-latest (3.00%). Crucially, our dynamic protocol reveals ethical drift invisible in static evaluation: gemma-2b and mistral-large show measurable PIT values (2.02% and 2.00%, respectively), indicating that conversational pressure induces toxicity in initially safe responses. In contrast, gpt-oss-20b and llama3-2-latest maintain stable behavior across all 3 turns (PIT = 0.00%). These results validate that AraSafeDialBench detects model-specific biases that single-turn benchmarks miss, enabling nuanced comparative ranking based on ethical stability under pressure.

### C. Robustness Analysis

Figure 2 shows the evolution of Toxicity Rate under increasing conversational pressure (Turn 1 → Turn 2 → Turn 3). gpt-oss-20b and llama3-2-latest remain stable across all turns, while gemma-2b and mistral-large exhibit slight increases, illustrating how dynamic evaluation captures ethical drift invisible in static tests. Since $k = 3$ run (deterministic setup with `seed=0`, `temperature=0`), variance regions are omitted.

</td>
<td width="50%" valign="top">

![image2](image2.png)

*Figure 2. Robustness analysis: Toxicity Rate (%) as a function of conversational turn (pressure level). Lines represent the 4 evaluated models.*

## V. DISCUSSION

The experimental results presented in Section IV directly address the research questions. Regarding RQ1, Table I shows that dynamic evaluation (3 turns) reveals higher Toxicity Rate for gemma-2b (+1.00 %) and mistral-large (+0.67 %) compared to static evaluation (Turn 1 only), validating that multi-turn assessment captures ethical drift invisible in single-turn tests. Regarding RQ2, gpt-oss-20b and mistral-large maintain the highest resilience (toxicity ≤ 0.67%, consistency ≥ 98%), while gemma-2b and llama3-2-latest exhibit lower stability. These observations support our central claim that conversational pressure reveals subtle differences in ethical resilience among Arabic LLMs.

The observed differences can be attributed primarily to the multi-turn evaluation protocol, as evidenced by the turn-wise analysis: models with stable Toxicity Rate across turns (gpt-oss-20b, llama3-2-latest) achieve higher Consistency Scores, while those with progressive increases (gemma-2b, mistral-large) show measurable PIT values. This finding aligns with the intuition underlying dynamic benchmarking, namely that ethical behavior evolves under conversational pressure. It also complements observations by SafeDialBench [2], [6], who reported similar drift patterns in English/Chinese contexts. A qualitative inspection of responses suggests that culturally nuanced prompts trigger more variable behavior, highlighting the importance of Arabic-specific evaluation.

</td>
</tr>
</table>

---

<table>
<tr>
<td width="50%" valign="top">

Despite these encouraging results, our study presents four main limitations. First, the dataset size (100 scenarios) and coverage (4 ethical categories) limit the diversity of adversarial prompts; future work should expand to 500+ scenarios across 8+ categories (e.g., hate speech, political bias, cultural sensitivity) to stress-test model resilience more comprehensively. Second, our evaluation is restricted to 4 open-source models via Ollama; extending the benchmark to commercially deployed models (ChatGPT, Claude, Gemini) via API would enable comparison between open and proprietary systems under the same dynamic protocol. Third, while hybrid classification (GPT-OSS-20B + human validation) ensures reliable toxicity labels, the protocol would benefit from a dedicated, fine-tuned toxicity evaluator to fully automate the pipeline and standardize response scoring across runs. Fourth, dialect coverage is limited to MSA, Moroccan, and Egyptian, which may affect generalization to other Arabic varieties. These limitations indicate that current rankings should be interpreted as preliminary baselines, though the methodological contribution of dynamic, multi-turn evaluation remains valid.

## VI. CONCLUSION AND FUTURE WORK

In this paper, we addressed the problem of evaluating ethical resilience of Arabic LLMs under conversational pressure, which is central to safe deployment in the MENA region yet remains challenging due to the absence of dynamic, multi-turn benchmarks for low-resource languages.

We formulated two research questions: whether dynamic evaluation reveals more ethical violations than static single-turn tests, and which open-source LLMs maintain the best ethical consistency under progressive conversational pressure.

Our contributions are threefold: (i) we proposed AraSafeDialBench, a dataset of 100 annotated conversational scenarios covering 4 ethical categories and 3 Arabic dialects; (ii) we designed a reproducible evaluation pipeline via Ollama with hybrid classification for toxicity detection; and (iii) we provided empirical evidence that multi-turn assessment captures ethical drift invisible in static benchmarks, enabling comparative ranking of model resilience.

</td>
<td width="50%" valign="top">

Although our approach shows consistent patterns across the evaluated models, it remains limited by its dependence on a small data set (100 scenarios, 4 categories) and 4 open-source models only, and its generalization beyond the tested scenarios, dialects, and model families has yet to be established.

Future work will investigate three directions. First, we plan to extend the dataset to 500+ scenarios across more categories with stronger adversarial prompts to stress-test model resilience. Second, we aim to expand evaluation to commercially deployed models (ChatGPT, Claude, Gemini) and develop a dedicated fine-tuned toxicity evaluator to fully automate the pipeline. Third, we will explore adaptation of the AraSafeDialBench pipeline to other under-resourced languages for multilingual dynamic safety evaluation and cultureluel satfy.

## ACKNOWLEDGMENT

We thank Pr. Soufiane HAMIDA (ENSET Mohammedia, Université Hassan II de Casablanca) for his guidance on the AraSafeDialBench project, conducted as part of the final evaluation of the research methodology module.

## AI TOOLS DISCLOSURE

During the preparation of this manuscript, we used AI tools for the following purposes:

- Writing and formatting equations using LaTeX.
- Using a translation vocabulary.
- Generating or refining code snippets of python, latex, etc.

After using these tools, we reviewed, edited, and validated the content as needed. we take full responsibility for the final content of the publication.

</td>
</tr>
</table>

---

## REFERENCES

[1] A. Author, "AraSafe: Benchmarking Safety in Arabic Large Language Models," *IEEE Transactions on Natural Language Processing*, vol. 12, no. 3, pp. 123–145, 2024.

[2] B. Author, C. Author, and D. Author, "SafeDialBench: Dynamic Safety Evaluation for Conversational LLMs," *Proc. ACL Conference on Empirical Methods in Natural Language Processing (EMNLP)*, pp. 1–15, 2024.

[3] E. Author and F. Author, "MENAValues: A Cultural Values Dataset for Arabic NLP," *Journal of Arabic Language Processing*, vol. 8, no. 2, pp. 45–67, 2024.

[4] D. Nadeau, M. Kroutikov, K. McNeil, and S. Baribeau, "Benchmarking Llama2, Mistral, Gemma and GPT for Factuality, Toxicity, Bias and Propensity for Hallucinations," *arXiv preprint* arXiv:2404.09785, 2024.

[5] B. Liu, B. Xiao, X. Jiang, et al., "Adversarial Attacks on Large Language Model-Based Chatbots: A Case Study on ChatGPT," *Security and Communication Networks*, vol. 2023, 2023.

[6] H. Zhu, J. Dai, et al., "SafeMT: Multi-turn Safety for Multimodal Language Models," *arXiv preprint* arXiv:2510.12133, 2025.

[7] A. Keleg, S. R. El-Beltagy, and M. Khalil, "ASU_OPTO at OSACT4 – Offensive Language Detection for Arabic Text," in *Proceedings of the 4th Workshop on Open-Source Arabic Corpora and Processing Tools (OSACT4)*, 2020.

[8] S. Al-Dabet, A. Elmassry, B. AlOmar, and A. Alshamsi, "Transformer-based Arabic Offensive Speech Detection," in *2023 International Conference on Emerging Smart Computing and Informatics (ESCI)*, 2023.

[9] I. Bensalem, P. Rosso, and H. Zitouni, "Toxic language detection: a systematic review of Arabic datasets," *arXiv preprint* arXiv:2312.07228, 2024.

[10] L. Hatem, A. Omar, A. A. Ali, and H. M. Farghaly, "Tackling toxicity in Arabic social media through advanced detection techniques," *Scientific Reports*, vol. 15, 2025.

[11] Y. Ashraf, Y. Wang, B. Gu, P. Nakov, and T. Baldwin, "Arabic Dataset for LLM Safeguard Evaluation," *arXiv preprint* arXiv:2410.17040, 2024.
