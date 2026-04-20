'''
Description: 
Author: Chenglin Cai
Date: 2026-04-20 22:40:40
LastEditTime: 2026-04-20 22:56:10
LastEditors:  
'''
'''
Description: 
Author: Chenglin Cai
Date: 2026-04-20 22:40:40
LastEditTime: 2026-04-20 22:50:14
LastEditors:  
'''
import argparse
import subprocess
from llm.run_LLM import main as run_llm_main
from llm.run_LLM_batch import main as run_llm_batch_main
from llm.run_RAGLLM import main as run_ragllm_main
from llm.run_RAGLLM_batch import main as run_ragllm_batch_main


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=['llm', 'llm-batch', 'rag-llm', 'rag-llm-batch'], required=True)
    parser.add_argument('--csv_path', type=str, required=True, help="Path to input query CSV file with a 'prompt' column") 
    parser.add_argument('--model_type', choices=['mistral','mistral-7b','gpt','gpt_reasoning'], type=str, required=True, help="Type of model")
    parser.add_argument('--model_api', type=str, help="Model API name")
    parser.add_argument('--context_db', type=str, choices=['fda','ema','civic'], help="Context DB used for RAG-LLM") # required only for running RAG-LLM 
    parser.add_argument('--context_db_type', type=str, choices=['unstructured', 'structured'], default='structured')
    parser.add_argument('--hybrid_search', action=argparse.BooleanOptionalAction)
    parser.add_argument('--num_iter', type=int, default=1, help="Number of iterations of running the pipeline [default: 1]")
    parser.add_argument('--strategy', choices=[0, 1, 2, 3, 4, 5, 6, 7], type=int, default=0, help="Prompt strategy [default: 0]")
    parser.add_argument('--output_dir', type=str, required=True, help="Output directory")
    parser.add_argument('--temp', type=float, default=0.0, help="Temperature used for LLM inference [default: 0]")
    parser.add_argument('--max_len', type=int, default=None, help="Maximum output token LLM can return [default: None]")
    parser.add_argument('--random_seed', type=int, default=None, help="Random seed used for LLM inference [default: None]")
    return parser.parse_args()
    
# ~/rag-llm-cancer-paper$ python main.py --mode=rag-llm \
# --csv_path=data/latest_db/moalmanac_fda_core_query__2025-10-03.csv \
# --model_type=gpt --model_api=gpt-4o-2024-08-06 \
# --context_db=fda --context_db_type=structured \
# --hybrid_search \
# --num_iter=5 \
# --strategy=0 \
# --output_dir=output/RAG_res_gpt4o_default/structured_synthetic_db_v202510_hybrid_numvec25 \
# --temp=0.0 --max_len=2048 --random_seed=2025

def main():
    args = parse_args()
    
    #check
    if args.mode in ["rag-llm", "rag-llm-batch"]:  # rag-llm 
        if not args.context_db:     # "fda"
            raise ValueError("`--context_db` is required when mode is 'rag-llm'")
        if not args.model_api:
            raise ValueError("`--model_api` is required when mode is 'rag-llm'")        
    if args.mode in ['llm-batch', 'rag-llm-batch'] and args.model_type not in ['gpt', 'gpt_reasoning']:
        raise ValueError("Batch mode is only supported for 'gpt' and 'gpt_reasoning' models")
        
    #run selected mode
    if args.mode == 'llm':
        run_llm_main(args)
    elif args.mode == 'llm-batch':
        run_llm_batch_main(args)
    elif args.mode == 'rag-llm':    # this
        run_ragllm_main(args)
    elif args.mode == 'rag-llm-batch':
        run_ragllm_batch_main(args)

if __name__ == '__main__':
    main()