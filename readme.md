# AI Visual Novel

Each module is independent and has its own independent README
1. Dataset creation contains all the code for creation of a syntetic visual novel scripts dataset
2. Finetuning has the code for finetuning Gemma using the created dataset
3. Ablation text generation contains the code for generation of text using the finetuned model using various decoding strategies
4. Benchmarking has the code for running the novel benchmarks created during this project and generating visualizations for the generated ablation text to perform ablation studies,
5. Visual novel engine is the final engine which can run the generated visual novel scripts
