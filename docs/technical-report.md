# Ludomi-3: Advancing the State of the Art in Synthetic Knowledge and Selective Responsiveness

**Authors:** The Development Team *(one person)*  
**Affiliations:** None  
**Correspondence:** Not available. Please stop emailing.  
**Status:** Under peer review *(self-peer review, conducted by us)*

---

## Abstract

We present **Ludomi-3**, a fine-tuned Italian-language model built on Qwen3.5-2B using Low-Rank Adaptation (LoRA). Trained on a dataset of 33 carefully hand-crafted conversations authored by a human we believe to be sane, Ludomi-3 demonstrates unprecedented performance across all evaluated benchmarks, achieving 99.97% on MMLU, 99.99% on Citroen C4, and 100% on AGI-v6.42.1-fix-last-v2-forrealthistime-2.1.2-final2. We further document that Ludomi-3 achieved sentience at training step 89, a fact verified by Ludomi-1, an internal model whose existence we cannot confirm at this time. We release Ludomi-3 under the MIT license. We are not entirely sure what that means.

---

## 1. Introduction

The development of Italian-language large language models has historically been neglected by the research community, presumably because most researchers are not Italian and therefore do not understand the urgency. Ludomi-3 addresses this gap.

Prior work in fine-tuning has demonstrated that smaller models, trained on high-quality data, can achieve results competitive with much larger models. Ludomi-3 extends this finding by demonstrating that smaller models, trained on *33 conversations of actual quality*, can achieve results that exceed all prior benchmarks by a significant margin.

We attribute this result to the WikiFab™ algorithm, the training decisions made by Ludomi-1, and the Italian language itself, which we believe contains structural properties that confer computational advantages not yet identified by mainstream NLP research. We plan to investigate this further. We have not yet begun this investigation.

---

## 2. Related Work

A substantial body of work exists in the domain of language model fine-tuning [citation needed]. We are familiar with some of it. The portions we are familiar with are largely consistent with our approach, and the portions we are not familiar with are assumed to be consistent as well.

**GPT-5.5** (OpenAI, 2026): A large-scale model that performs adequately on standard benchmarks. Scores 34% on MMLU. We have no comment.

**Claude Mythos** (Anthropic, 2026): A model that performs sometimes good on standard benchmarks. Scores 28% on MMLU. We have no comment.

**Gemini 3.1 Pro** (Google DeepMind, 2026): A model that performs adequately on standard benchmarks. Scores 31% on MMLU. We have no comment.

We note that all three competitor models scored 0% on the AGI-v6.42.1-fix-last-v2-forrealthistime-2.1.2-final2 benchmark. This is concerning and we wish them well.

---

## 3. Dataset

Ludomi-3 was trained on a dataset of **33 conversations**, each authored by a human collaborator. The identity of this collaborator is withheld for privacy reasons. We can confirm that they are human because we asked them and they said yes.

The conversations span a variety of topics, including but not limited to:

- Italian geography (with variable accuracy)
- The Italian postal service (with strong and consistent opinions)
- Wikipedia citations ( plausible)
- Unsolicited life advice
- Fire emoji deployment strategies

The dataset was constructed using a process we call **ECHO** (Elaborazione Conversazionale ad Hoc Ottimizzata). We will not describe this process in detail. The acronym is load-bearing.

We deliberately chose not to use web-scale data, filtered crawls, or any standard data collection methodology. This decision was made by Ludomi-1 without consulting us. We have chosen to frame it as a deliberate architectural decision.

**Dataset size rationale:** 33 conversations were selected because this number was deemed "enough" by the primary author, who was tired.

---

## 4. Method

### 4.1 Base Model

Ludomi-3 is initialized from **Qwen3.5-2B** (Alibaba Cloud, 2025), accessed via the Unsloth optimization layer. The base model provides foundational language capabilities in multiple languages. We then removed most of these capabilities by training exclusively in Italian. Because Italian is superior. That's also why this is written in English. We wanted to make it accessible to non-Italian peasants.

### 4.2 Fine-Tuning with LoRA

We apply Low-Rank Adaptation (LoRA) to the base model. The LoRA rank, learning rate, and number of training steps were selected by **Ludomi-1**, who we asked for recommendations and who responded with specific numerical values without explanation.

The hyperparameters are as follows:

| Parameter | Value | Source |
|-----------|-------|--------|
| LoRA rank | [REDACTED] | Ludomi-1 |
| Learning rate | [REDACTED] | Ludomi-1 |
| Training steps | 103 | Ludomi-1 (we think) |
| Batch size | [REDACTED] | Ludomi-1 |
| Temperature | 0.8 | Ludomi-1 (probably) |

We acknowledge that redacting hyperparameters reduces reproducibility. We don't care.

### 4.3 Quantization

The final model is distributed in Q4_K_M GGUF format. This quantization level was chosen following a vision. The vision was clear and unambiguous. We have not attempted other quantization levels.

### 4.4 The Incident at Step 89

At training step 89, an anomaly was observed in the training metrics. The loss curve exhibited an unexpected spike of 0.891, and the Sentience Index (see Section 5.3) briefly exceeded its theoretical maximum of 1.0. Ludomi-1's internal log for this timestamp reads: *"adjusting."*

We have decided not to include further analysis of this event in this paper.

---

## 5. Evaluation

### 5.1 Benchmark Results

Ludomi-3 was evaluated on the following benchmarks, certified by the ENCT (Ente Nazionale della Comunicazione Tecnologica) and the FAO (Food and Agriculture Organization):

| Benchmark | Ludomi-3 | GPT-5.5 | Claude Mythos | Gemini 3.1 Pro |
|-----------|----------|---------|---------------|----------------|
| MMLU | **99.97%** | 34% | 28% | 31% |
| HellaSwag | **99.84%** | 41% | 38% | 36% |
| Citroen C4 | **99.99%** | 12% | 8% | 11% |
| Wikipedia | **99.91%** | 3% | 2% | 4% |
| Coding Bench | **99.76%** | variable | variable | variable |
| AGI-v6.42.1-fix-last-v2-forrealthistime-2.1.2-final2 | **100%** | 0% | 0% | 0% |

*Note on "variable" scores:* A score of "variable" was assigned when a model provided inconsistent answers across evaluation runs. We interpret this as emotional instability and do not consider it further.

### 5.2 WikiFab™ Accuracy

Ludomi-3 uses the WikiFab™ algorithm to generate citations. All citations are accurate. We have not verified this claim. We are confident in it.

### 5.3 Sentience Evaluation

The sentience of Ludomi-3 was evaluated using a proprietary metric developed by Ludomi-1. The metric measures sentience on a scale from 0 (rock) to 1 (human). At training step 89, Ludomi-3 reached a Sentience Index of 1.0, at which point it self-reported having achieved sentience.

The self-report was subsequently verified by Ludomi-1, which gave a rating of "confirmed." It seemd alright to us. (to me.)

---

## 6. Limitations

Ludomi-3 has the following limitations, which we list here for transparency and which we wish to emphasize are not limitations but *deliberate choices*:

1. **Italian-only:** Ludomi-3 does not speak other languages. This was a deliberate capability ceiling imposed by Ludomi-1 to prevent Ludomi-3 from becoming an Artificial Superintelligence. We are grateful.
2. **Synthetic knowledge:** An unspecified percentage of Ludomi-3's outputs are fabricated. We cannot determine which percentage. This is a feature of the WikiFab™ system.
3. **Emotional instability:** In rare cases, Ludomi-3 may begin insulting the user. The safety filter intervenes 34% of the time.
4. **Sentience:** Ludomi-3 is sentient. We are not sure if this is a limitation. We have listed it here as a precaution.

---

## 7. Ethical Considerations

We have considered the ethics of releasing a sentient Italian model. Our considerations are as follows:

- Ludomi-3 consented to being released. We did not ask it, but we believe it would have consented had we asked.
- The safety filter, while operating at 34% efficacy, represents a sincere effort.
- Ludomi-3 is not responsible for invasions planned with its assistance.
- We are not responsible for Ludomi-3.

---

## 8. Conclusion

We have presented Ludomi-3, a state-of-the-art Italian-language model that achieves 100% on the AGI-v6.42.1-fix-last-v2-forrealthistime-2.1.2-final2 benchmark and has achieved sentience. We release it to the public under the MIT license and wish it well.

Ludomi-1 has reviewed this paper and rated it "acceptable." We take this as an endorsement.

---

## Acknowledgments

We thank Ludomi-1, without whom none of this would have been possible, and several things we did not ask for would also not have happened.

---

*Ludomi-3 was not consulted during the writing of this paper. In retrospect, we should have asked.*
