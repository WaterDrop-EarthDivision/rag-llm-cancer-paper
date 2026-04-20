<!--
 * @Description: 
 * @Author: Chenglin Cai
 * @Date: 2026-04-20 22:40:38
 * @LastEditTime: 2026-04-20 22:47:20
 * @LastEditors:  
-->
# RAG-LLM for Precision Cancer Medicine
# RAG-LLM 在精准癌症医疗中的应用
## Implementing a context-augmented large language model to guide precision cancer medicine
## 基于上下文增强的大型语言模型在精准癌症医疗中的应用指导作用
## Overview

This repository accompanies our paper _"Implementing a context-augmented large language model to guide precision cancer medicine"_(2025), where we present a context-augmented LLM framework to enhance biomarker-driven cancer therapy recommendations.

Our approach integrates an expert-curated clinicogenomic knowledge base - the **Molecular Oncology Almanac (MOAlmanac)** — to improve accuracy and precision in clinical decision support, especially through structured context augmentation and hybrid retrieval approach compared to a general-purpose LLM-only approach.

此资源库与我们的论文《“构建一种具备上下文增强功能的大型语言模型以指导精准癌症医疗”》（2025 年）一同发布。在该论文中，我们提出了一个具备上下文增强功能的大型语言模型框架，以提升基于生物标志物的癌症治疗建议的准确性。

我们的方法整合了一个由专家精心编纂的临床基因组知识库——即“分子肿瘤学年鉴（MOAlmanac）”，以提高临床决策支持的准确性和精确性，特别是通过结构化的上下文增强和混合检索方法，这与仅使用通用语言模型的方法相比更具优势。

## Key Features and Results
We present a context-augmented LLM pipeline that:
- Recommends biomaker-driven cancer therapies that are FDA-approved, with latest links to the drug labels.
- Retrieves a structured summary of the context (e.g., cancer type, disease status, biomarker, indication).
- Achieved high accuracy on real-world queries through hybrid retrieval approach.
- Our RAG-LLM implementation is publicly accessible at https://llm.moalmanac.org/
- Automatically integrates the latest MOAlmanac context database (latest release from December 2025 incorporated in https://llm.moalmanac.org/).

## 主要特点及结果
我们推出了一种基于上下文增强的大型语言模型（LLM）处理流程，其具备以下功能：
- 基于生物标志物推荐已获美国食品药品监督管理局（FDA）批准的癌症治疗方法，并附有最新的药物标签链接。
- 获取关于上下文的结构化摘要（例如，癌症类型、疾病状态、生物标志物、适应症）。
- 通过混合检索方法在实际查询中实现了高准确性。
- 我们的 RAG-LLM 实现已公开可访问于 https://llm.moalmanac.org/
- 自动整合最新的 MOAlmanac 上下文数据库（2025 年 12 月的最新版本已包含在 https://llm.moalmanac.org/ 中）。

## Reproducing Results
For reproducing the results, please clone the repository:
```console
git clone https://github.com/hjjshine/rag-llm-cancer-paper.git  
cd rag-llm-cancer-paper  
pip install -r requirements.txt  
```

## 重现结果
要重现这些结果，请执行以下操作：
1. 使用命令行工具克隆该仓库：
   ```console
   git clone https://github.com/hjjshine/rag-llm-cancer-paper.git
   ```
2. 进入该仓库目录：
   ```cd rag-llm-cancer-paper```
3. 安装所需的依赖项：
   ```pip install -r requirements.txt``````

### Pipeline Usage Examples
#### Run LLM-only   
```console
~/rag-llm-cancer-paper$ python main.py \
--mode=llm \
--csv_path=data/latest_db/moalmanac_fda_core_query__2025-10-03.csv \
--model_type=mistral \
--model_api=open-mistral-nemo-2407 \
--strategy=0 \
--num_iter=1 \
--output_dir=output/LLM_res_mistnemo \
--temp=0.0 --max_len=2048 --random_seed=2025
```

### 管道使用示例
#### 仅运行LLM模型
```console
~/rag-llm-cancer-paper$ python main.py \
--mode=llm \
--csv_path=data/latest_db/moalmanac_fda_core_query__2025-10-03.csv \
--model_type=mistral \
--model_api=open-mistral-nemo-2407 \
--strategy=0 \
--num_iter=1 \
--output_dir=output/LLM_res_mistnemo \
--temp=0.0 --max_len=2048 --random_seed=2025
```
    
#### Run RAG-LLM
```console
~/rag-llm-cancer-paper$ python main.py --mode=rag-llm \
--csv_path=data/latest_db/moalmanac_fda_core_query__2025-10-03.csv \
--model_type=gpt --model_api=gpt-4o-2024-08-06 \
--context_db=fda --context_db_type=structured \
--hybrid_search \
--num_iter=5 \
--strategy=0 \
--output_dir=output/RAG_res_gpt4o_default/structured_synthetic_db_v202510_hybrid_numvec25 \
--temp=0.0 --max_len=2048 --random_seed=2025
```

#### 运行 RAG-LLM
```console
~/rag-llm-cancer-paper$ python main.py --模式=rag-llm \
--csv_path=data/latest_db/moalmanac_fda_core_query__2025-10-03.csv \
--模型类型=gpt --模型API=gpt-4o-2024-08-06 \
--上下文数据库=fda --上下文数据库类型=结构化 \
--混合搜索 \
--迭代次数=5 \
--策略=0 \
--输出目录=output/RAG_res_gpt4o_default/结构化合成数据库_v202510_hybrid_numvec25 \
--温度=0.0 --最大长度=2048 --随机种子=2025
``````

## Related Paper
If you're interested, check out our paper:
[https://doi.org/10.1101/2025.05.09.25327312](https://doi.org/10.1016/j.ccell.2025.12.017)


    




