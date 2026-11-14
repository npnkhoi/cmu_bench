# Computational Meme Understanding Benchmarks

A curated list of public benchmarks for computational meme understanding:
hate and harm detection, sentiment, persuasion techniques, explanation, captioning, and more.

Contributions are welcome.

## Benchmarks

<!-- AUTOGEN:START -->
**44 datasets** across **11 languages**.

### Amharic

| Name | Year | Tasks | Platform sources | Paper | Data | Size |
|---|---|---|---|---|---|---:|
| Amharic Hate Speech Memes | 2024 | Hate Detection | Facebook, Twitter, Telegram | [Paper](https://aclanthology.org/2024.trac-1.10/) | [Link](https://github.com/uhh-lt/AmharicHateSpeech) | 2,000 |

### Arabic

| Name | Year | Tasks | Platform sources | Paper | Data | Size |
|---|---|---|---|---|---|---:|
| ArAIEval | 2024 | Propaganda Detection | Twitter | [Paper](https://aclanthology.org/2024.arabicnlp-1.44/) | [Link](https://araieval.gitlab.io/) | 3,062 |

### Bengali

| Name | Year | Tasks | Platform sources | Paper | Data | Size |
|---|---|---|---|---|---|---:|
| BHM (Bengali Hateful Memes) | 2024 | Hate Detection, Hated Target Group Classification | Blogs, Facebook, Instagram, Pinterest | [Paper](https://aclanthology.org/2024.acl-long.454/) | [Link](https://drive.google.com/file/d/1uftdZXcf00X2MQVb8UUcRMaIor7Pfd1w/view) | 7,148 |
| MIMOSA | 2024 | Aggression Classification | Blogs, Facebook, Instagram, Pinterest | [Paper](https://aclanthology.org/2024.eacl-long.153/) | [Link](https://github.com/shawlyahsan/Bengali-Aggression-Memes) | 4,848 |
| BanglaAbuseMeme | 2023 | Abuse Detection, Sarcasm Detection, Sentiment Classification, Target Classification, Vulgar Detection | Google Images, Facebook, Instagram | [Paper](https://aclanthology.org/2023.emnlp-main.959/) | [Link](https://github.com/hate-alert/BanglaAbuseMeme) | 4,043 |
| MemoSen | 2022 | Sentiment Classification | Facebook, Instagram | [Paper](https://aclanthology.org/2022.lrec-1.165/) | Unavailable | 4,417 |

### English

| Name | Year | Tasks | Platform sources | Paper | Data | Size |
|---|---|---|---|---|---|---:|
| M-QUEST | 2026 | Semantic Understanding Q&A, Toxicity Q&A | Web | [Paper](https://aclanthology.org/2026.emnlp-main.164/) | [Link](https://huggingface.co/datasets/vulr/M-QUEST) | 307 |
| CLIMATEMEMES | 2025 | Stance Detection, Media Frame Detection | Reddit | [Paper](https://aclanthology.org/2025.findings-emnlp.286/) | [Link](https://github.com/mainlp/ClimateMemes) | 1,184 |
| MemeInterpret | 2025 | Captioning, Surface Message Generation, Background Knowledge Generation | Web | [Paper](https://aclanthology.org/2025.findings-emnlp.871/) | [Link](https://github.com/npnkhoi/MemeInterpret) | 6,810 |
| MemeQA | 2025 | Multiple-choice Q&A | Facebook | [Paper](https://aclanthology.org/2025.acl-long.927/) | [Link](https://github.com/npnkhoi/memeqa) | 950 |
| MemeIntent | 2024 | Intent Description Generation, Background Knowledge Generation | Facebook | [Paper](https://aclanthology.org/2024.sigdial-1.54/) | [Link](https://github.com/lucasjeongsikpark/MemeIntent) | 950 |
| MemeMQA | 2024 | Q&A | Google Images, Instagram | [Paper](https://aclanthology.org/2024.findings-acl.300/) | Unavailable | 1,880 |
| MMD (MeSum) | 2024 | Meme Summarization | Reddit | [Paper](https://aclanthology.org/2024.findings-emnlp.389/) | Unavailable | 13,494 |
| ExHVV | 2023 | Entity Role Explanation | Google Images, Instagram | [Paper](https://dl.acm.org/doi/10.1609/aaai.v37i8.26166) | Unavailable | 4,680 |
| HatReD | 2023 | Hate Explanation | Web | [Paper](https://www.ijcai.org/proceedings/2023/665) | [Link](https://github.com/Social-AI-Studio/HatRed) | 3,328 |
| MCC | 2023 | Background knowledge relevance classification | Google Images, Reddit | [Paper](https://aclanthology.org/2023.acl-long.289/) | [Link](https://github.com/LCS2-IIITD/MEMEX_Meme_Evidence?tab=readme-ov-file) | 3,003 |
| MemeCap | 2023 | Captioning | Reddit | [Paper](https://aclanthology.org/2023.emnlp-main.89/) | [Link](https://github.com/eujhwang/meme-cap) | 6,387 |
| RESTORE | 2023 | Depression Symptom Classification | Reddit, Twitter | [Paper](https://aclanthology.org/2023.acl-long.495/) | [Form](https://docs.google.com/forms/d/e/1FAIpQLSeK8h2TvDt-XzZzvy0vWvjauDAX8eUXJ6OUuoAfd4ZqWQPqLA/viewform) | 9,837 |
| Ukraine-conflict Memes | 2023 | Stance Classification, Theme Classification | Not reported | [Paper](https://doi.org/10.1007/978-3-031-26303-3_3) | Unavailable | 191 |
| Ext-Harm-P | 2022 | Target Classification | Google Images, Facebook, Instagram, Reddit | [Paper](https://aclanthology.org/2022.findings-naacl.118/) | [Link](https://github.com/LCS2-IIITD/DISARM/tree/main/DISARM_Dataset) | 4,446 |
| FigMemes | 2022 | Figurative Language Classification | 4chan | [Paper](https://aclanthology.org/2022.emnlp-main.476/) | [Form](https://github.com/UKPLab/emnlp2022-figmemes) | 5,141 |
| HVVMemes | 2022 | Entity Role Classification | Google Images, Instagram | [Paper](https://aclanthology.org/2022.constraint-1.1/) | [Link](https://codalab.lisn.upsaclay.fr/competitions/906) | 7,000 |
| MAMI | 2022 | Misogyny Detection | 9GAG, Imgur, Know Your Meme, Reddit, Twitter | [Paper](https://aclanthology.org/2022.semeval-1.74/) | [On request](https://competitions.codalab.org/competitions/34175) | 11,000 |
| Harm-C and Harm-P | 2021 | Harm Detection | Google Images, Facebook, Instagram, Reddit | [Paper](https://aclanthology.org/2021.findings-emnlp.379/) | [Link](https://github.com/LCS2-IIITD/MOMENTA/tree/main/HarMeme_V1) | 7,096 |
| HarMeme | 2021 | Harm Detection | Google Images, Instagram | [Paper](https://aclanthology.org/2021.findings-acl.246/) | [Link](https://github.com/di-dimitrov/harmeme?tab=readme-ov-file) | 3,544 |
| “Propaganda Techniques in Memes” | 2021 | Persuasion Technique Detection | Facebook | [Paper](https://aclanthology.org/2021.acl-long.516) | [Link](https://github.com/di-dimitrov/propaganda-techniques-in-memes) | 950 |
| SemEval-2021-Task6 | 2021 | Persuasion Technique Detection, Persuasion Technique Explanation | Facebook | [Paper](https://aclanthology.org/2021.semeval-1.7) | [Link](https://github.com/di-dimitrov/SEMEVAL-2021-task6-corpus/tree/main/data) | 950 |
| WOAH5 | 2021 | Hated Target Group Classification, Hatred Attack Type Classification | Web | [Paper](https://aclanthology.org/2021.woah-1.21) | [Link](https://github.com/facebookresearch/fine_grained_hateful_memes) | 10,540 |
| FHM | 2020 | Hate Detection | Web | [Paper](https://proceedings.mlr.press/v133/kiela21a.html) | [Link](https://ai.meta.com/tools/hatefulmemes/) | 12,540 |
| “Jewtocracy” | 2020 | Antisemitism Classification | Gab, Twitter | [Paper](https://arxiv.org/abs/2104.05947) | [Link](https://github.com/mohit3011/Online-Antisemitism-Detection-Using-MultimodalDeep-Learning/blob/main/Twitter%20Antisemitism%20Dataset.tsv) | 6,611 |
| Memotion | 2020 | Humor Classification, Scales of Semantic Classes, Sentiment Classification | Google Images | [Paper](https://aclanthology.org/2020.semeval-1.99) | [Link](https://competitions.codalab.org/competitions/20629#learn_the_details-evaluation) | 9,871 |
| MultiOFF | 2020 | Offensiveness Detection | Facebook, Instagram, Reddit, Twitter | [Paper](https://aclanthology.org/2020.trac-1.6/) | [Link](https://github.com/bharathichezhiyan/Multimodal-Meme-Classification-Identifying-Offensive-Content-in-Image-and-Text?tab=readme-ov-file) | 743 |

### Tamil

| Name | Year | Tasks | Platform sources | Paper | Data | Size |
|---|---|---|---|---|---|---:|
| TamilMemes | 2020 | Troll Detection | Facebook, Instagram, Pinterest, WhatsApp | [Paper](https://aclanthology.org/2020.wildre-1.2/) | [On request](https://github.com/sharduls007/TamilMemes) | 2,969 |

### Multilingual

| Name | Year | Languages | Tasks | Platform sources | Paper | Data | Size |
|---|---|---|---|---|---|---|---:|
| CM-Off-Meme | 2024 | English, Hindi | Offensiveness Detection, Explicit/Implicit Offense Classification, Sarcasm Detection, Sentiment Classification, Emotion Classification | Google Images | [Paper](https://aclanthology.org/2024.lrec-main.300/) | [Form](https://github.com/Gitanjali1801/CM_MEMES) | 6,967 |
| ICMM | 2024 | English, Hindi | Cyberbullying Intervention Generation | Reddit, Twitter | [Paper](https://aclanthology.org/2024.acl-long.439/) | [Link](https://github.com/Jhaprince/MemeGuard) | 5,854 |
| LT-EDI@EACL 2024 (Misogynistic and Trolls) | 2024 | Malayalam, Tamil | Misogyny Detection | Not reported | [Paper](https://aclanthology.org/2024.ltedi-1.13/) | Unavailable | 1,776 |
| MultiBully-Ex | 2024 | English, Hindi | Cyberbullying Textual Explanation, Cyberbullying Visual Explanation | Reddit, Twitter | [Paper](https://aclanthology.org/2024.eacl-long.56/) | [Link](https://github.com/Jhaprince/MemeExplanation) | 3,222 |
| SemEval-2024-Task4 | 2024 | Arabic, Bulgarian, English, North Macedonian | Persuasion Technique Detection, Persuasion Technique Explanation | Facebook, Instagram | [Paper](https://aclanthology.org/2024.semeval-1.275/) | Unavailable | 10,000 |
| VIDA | 2024 | English, Italian | Content Classification, Form Classification, Hate Classification | Incel Forums | [Paper](https://aclanthology.org/2024.woah-1.6/) | [Form](https://github.com/uhh-lt/vida) | 2,181 |
| Persuasive_meme | 2023 | English, Hindi | Persuasion Technique Detection, Persuasive Meme Detection, Persuasiveness evaluation | Google Images | [Paper](https://aclanthology.org/2023.ijcnlp-main.61/) | Unavailable | 6,000 |
| MET-Meme | 2022 | Chinese, English | Intention Classification, Metaphor Prediction | Google Images, Baidu, Twitter, Weibo | [Paper](https://dl.acm.org/doi/10.1145/3477495.3532019) | [Link](https://github.com/liaolianfoka/MET-Meme-A-Multi-modal-Meme-Dataset-Rich-in-Metaphors?tab=readme-ov-file) | 10,045 |
| MultiBully | 2022 | English, Hindi | Bully Detection, Emotion Classification, Sarcasm Detection, Sentiment Classification | Reddit, Twitter | [Paper](https://dl.acm.org/doi/abs/10.1145/3477495.3531925) | Unavailable | 5,854 |
| Multimodal Sentiment Analysis and Troll Meme Classification in Dravidian Languages | 2022 | Malayalam, Tamil | Sentiment Classification, Troll Detection | YouTube | [Paper](https://aclanthology.org/2022.dravidianlangtech-1.39/) | Unavailable | 134 |
| MUTE | 2022 | Bengali, English | Hate Detection | Facebook, Instagram, Twitter | [Paper](https://aclanthology.org/2022.aacl-srw.5) | Unavailable | 4,158 |

### Aggregate benchmarks

These benchmarks combine existing datasets and are counted separately from the datasets above.

| Name | Year | Coverage | Paper | Data |
|---|---|---|---|---|
| MemeLens | 2026 | Consolidates 38 public meme datasets into 20 tasks spanning harm, targets, figurative/pragmatic intent, and affect; multilingual and explanation-enhanced. | [Paper](https://arxiv.org/abs/2601.12539) | [Link](https://huggingface.co/datasets/QCRI/MemeLens) |
<!-- AUTOGEN:END -->

**Data** column: *Link* = publicly downloadable, *Form* = access via request form,
*On request* = contact the authors, *Unavailable* = no public release found.

**Platform sources** lists where the memes were collected, based on the source CSV
and the linked papers or dataset releases for subsequent additions.
Inherited sources follow the originating datasets: ICMM → MultiBully;
HVVMemes → HarMeme; Ext-Harm-P → Harm-C and Harm-P; ExHVV → HVVMemes;
HatReD → WOAH5; MemeMQA → ExHVV. *Not reported* means the CSV gives no sources.
M-QUEST inherits its Web source from the Hateful Memes dataset.
MultiBully-Ex inherits sources from MultiBully; MemeIntent and MemeQA from
SemEval-2021-Task6; MemeInterpret from Hateful Memes.

**Size** counts memes (or annotated visual items for VIDA), not questions or annotations.
VIDA's size refers to its annotated subset. CM-Off-Meme provides public samples,
with full access via a request form. The [MMD/MeSum repository](https://github.com/anas2908/MeSum)
announces a forthcoming dataset release; no download is currently linked there.

The same data is available in machine-readable form at [`data/benchmarks.yaml`](data/benchmarks.yaml).
Aggregate benchmarks are stored separately in [`data/aggregate_benchmarks.yaml`](data/aggregate_benchmarks.yaml).

## Contributing

To add or fix a dataset, edit [`data/benchmarks.yaml`](data/benchmarks.yaml) (do not edit
the table above directly) and regenerate the table:

```bash
python scripts/build_readme.py
```

For an aggregate benchmark, edit `data/aggregate_benchmarks.yaml` with its `name`,
`year`, `description` (coverage), `paper`, and `dataset_url`, then run the same command.

Each entry has these fields:

| Field | Description |
|---|---|
| `name` | Dataset name as used in the paper |
| `year` | Publication year |
| `languages` | List of languages |
| `tasks` | List of tasks the dataset is annotated for |
| `platforms` | List of platforms or sources the memes were collected from; empty if not reported |
| `paper` | Link to the paper |
| `dataset_url` | Link to the data, or `null` if unavailable |
| `access` | One of `public`, `form`, `on-request`, `unavailable` |
| `size` | Number of memes, or `null` if unknown |

## License

The dataset list in this repository is licensed under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). This covers the metadata
collected here only; each listed dataset has its own license set by its authors.
