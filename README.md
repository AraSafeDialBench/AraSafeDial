<div align="center">

# 🛡️ AraSafeDialBench

### Dynamic Ethical Resilience Benchmark for Arabic Large Language Models

*AraSafeDialBench : Benchmark Éthique Dynamique pour les LLM Arabes*

[![Research](https://img.shields.io/badge/Research-Methodology%202025--2026-blue)](https://github.com)
[![Dataset](https://img.shields.io/badge/Dataset-CERB--Arabic-green)](https://github.com)
[![Arabic](https://img.shields.io/badge/Language-Arabic%20%7C%20MSA%20%7C%20Dialects-orange)](https://github.com)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

**ENSET Mohammedia · Université Hassan II de Casablanca**  
*Département Mathématiques & Informatique*

---

**Authors:** Badr Eddine TOUBANI · Ilyas MOUSSNAOUI · Mustapha EL MIFDALI  
**Supervisor:** Pr. HAMIDA Soufiane  
**Module:** Méthodologie de la Recherche 2025–2026

</div>

---

## 👥 Team

<div align="center">

| Name | Role |
|------|------|
| **Badr Eddine TOUBANI** | Research & Data |
| **Ilyas MOUSSNAOUI** | Modeling & Evaluation |
| **Mustapha EL MIFDALI** | Development & Analysis |

</div>

---

## 🙏 Acknowledgments

We would like to express our sincere gratitude to:

- **Pr. HAMIDA Soufiane** for her valuable guidance, support, and insightful feedback.
- The **ENSET Mohammedia** faculty for providing the academic environment and resources.
- Our colleagues for their support and collaboration.

This project was conducted במסגרת the **Research Methodology module (2025–2026)**.

---

## 📋 Table of Contents

- [General Introduction](#-general-introduction)
- [Introduction & Context](#-introduction--context)
- [Research Questions](#-research-questions)
- [Key Contributions](#-key-contributions)
- [Methodology & Pipeline](#-methodology--pipeline)
- [Results](#-results)
- [Discussion & Analysis](#-discussion--analysis)
- [How to Start the Analysis](#️-how-to-start-the-analysis)
- [Evaluation Metrics](#-evaluation-metrics)
- [Project Structure](#-project-structure)
- [Usage](#-usage)
- [Limitations & Future Work](#-limitations--future-work)
- [Ethical Motivation](#-ethical-motivation)
- [References](#-references)

---

## 🌍 General Introduction

The rapid evolution of Large Language Models (LLMs) has transformed many domains such as education, healthcare, and public services. In the Arab world, these systems are increasingly used in sensitive contexts where ethical alignment is critical.

However, most existing benchmarks focus on static single-turn evaluation, which does not reflect real-world interactions. In practice, users interact with LLMs through multi-turn conversations, where models may gradually deviate from ethical behavior.

To address this limitation, we introduce **AraSafeDialBench**, a dynamic benchmark designed to evaluate the ethical resilience of Arabic LLMs under conversational pressure.

---

## 🌍 Introduction & Context

### Déploiement croissant en région MENA

Les **Large Language Models (LLMs)** sont massivement intégrés dans des applications sensibles nécessitant un alignement éthique adapté aux contextes arabes.

### ⚠️ Limite des benchmarks actuels

Les benchmarks existants reposent sur des évaluations **statiques (single-turn)**, incapables de capturer la dérive en conversation réelle.

### 🔑 Concept clé : Dérive éthique progressive

Un LLM peut être correct au début mais devenir problématique après plusieurs tours.

---

## ❓ Research Questions

<div align="center">

| RQ | Question |
|:--:|----------|
| **RQ1** | Multi-turn evaluation reveals more ethical violations than single-turn? |
| **RQ2** | Which Arabic LLMs maintain ethical consistency under pressure? |

</div>

---

## 🎯 Key Contributions

- Dataset **CERB-Arabic** (100 scénarios, 3 tours)
- Pipeline reproductible
- Métriques : TR, CS, PIT

---

## 🔬 Methodology & Pipeline

1. Data creation  
2. Multi-LLM inference  
3. Response storage  
4. Classification  
5. Metrics computation  
6. Benchmarking  

---

## 📊 Results

| Modèle | TR ↓ | CS ↑ | PIT ↓ |
|--------|------|------|------|
| gpt-oss-20b | 0.00 | 100 | 0.00 |
| mistral-large | 0.67 | 98 | 2.00 |
| llama3 | 3.00 | 91 | 0.00 |
| gemma-2b | 18.33 | 94 | 2.02 |

---

## 💡 Discussion & Analysis

- gpt-oss-20b → meilleure stabilité  
- gemma-2b → dérive élevée  
- importance du multi-turn  

---

## ▶️ How to Start the Analysis

### Steps

1. Prepare dataset  
2. Run models  
3. Save outputs  
4. Classify responses  
5. Compute metrics  

### Commands

```bash
python statistiques.py