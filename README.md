# NeuralCodeEditing-Study

**Generating Realistic Vulnerabilities via Neural Code Editing: An Empirical Study**

| | |
|---|---|
| Original artifact | <https://zenodo.org/records/7048525> |
| Imported from | the publications page |
| Tool | `pubs2github` |


---

## Contents

The artifact contains 2 file(s), primarily Documentation.

```
├── neural_editors_vulgen.zip
└── README.md
```

---

## Original `README.md` (from the upstream artifact)

# Exploring Realistic Vulnerability Data Generation via Neural Code Editing

Using a commonly used synthetic dataset and one real-world dataset, we investigate the potential and gaps of three state-of-the-art neural code editors (Graph2Edit, Hoppity, SequenceR) for DL-based realistic vulnerability data generation, and two state-of-the-art vulnerability detectors (Devign, ReVeal) to evaluate the usefulness of the generated realistic vulnerability data in improving the effectiveness of such detectors.

## How to Get the Artifact

We have made the artifact publicly available on Zenodo: https://zenodo.org/record/6897604. Users can download the Docker image "neural_editors_vulgen_docker.tar.xz" easily from the link and start it with Docker. 

Besides, we also provide the standalone package of the artifact, named "neural_editors_vulgen.zip", on the link above. This would require that the users set up the environments and dependencies for all the five tools, which is expected to take much more effort.

## Requirements
Hardware: 

- \>=200GB hard disk space

- \>= 32GB CPU memory

- NVIDIA GPUs that CUDA 11.1 supports

Software:

- Ubuntu 18.04 or newer

- Docker

## Package Structure

- `Graph2Edit/`: The replication package and the respective results of Graph2Edit for all our experiments.
	- `source_data/githubedits/`: The data and setting files we used for our experiments
		- `configs/`: The configuration files used before training. Remember to modify it before experiments
	- `scripts/githubedits/`: The scripts for starting our training and testing experiments.
	- `exp_githubedits_runs/`: The trained models, outputs, and testing results of all our experiments
	- `training_info_*/`: The statistics of the two datasets we used for analysis.

- `Hoppity/`: The replication package and the respective results of Hoppity for all our experiments.
	- `*_save/`: The trained models, outputs, and testing results of all our experiments
	- `*.sh`: The scripts for starting our training and testing experiments.
	- `gtrans/`: The experiment data and source code of Hoppity
		-`*_processed`: The processed data for our experiments.

- `SequenceR`: The replication package and the respective results of SequenceR for all our experiments.
	- `OpenNMT-py/`: The OpenNMT module which SequenceR uses for training and testing.
	- `chai/`: The source code and experiment data of SequenceR.
		- `src/`: The source code and the respective scripts for starting the experiments.
		- `BigVul*/` and `cwe*/`: The trained models, outputs, and testing results of all our experiments.

- `Factors`: The code and results that we had for investigating the impacts of three factors - program length, edit length, and pattern frequency. For the other, two factors vocabulary size and structure complexity, please check the respective scripts, data, and results in each tool.

- `User Study`: The user study response (along with instruction/protocol) PDF (where the author information has been removed), results and the respective figure.

- `generic_specific`: The code and results for the distribution of generic and specific vulnerabilities in RQ2.

- `Detectors`: The replication package and the respective results for our RQ3 experiments (i.e., validating the usefulness of the generated realistic vulnerability samples in improving DL-based vulnerability detectors).
	- `Devign`: The replication package and the respective results for one of the studied vulnerability detectors Devign.
	- `ReVeal`: The replication package and the respective results for the other studied vulnerability detector ReVeal.
	
## How to Use
As installing dependencies is complex, we highly recommend the users to use the Docker image directly. Once the users have Docker installed, go to https://zenodo.org/record/6897604 and download the Docker image "neural_editors_vulgen_docker.tar.xz".

Then, run the commends to install the image:

```
unxz neural_editors_vulgen_docker.tar.xz
docker import neural_editors_vulgen_docker.tar neural_editors_vulgen
docker run -it -d --gpus all neural_editors_vulgen bash
# Docker will create a container using the image and show the container id
docker exec -it <container id>
```
All the dependencies have been installed in the Docker containers.

When login into the Docker image container, get into the artifact directory:

```
cd /root/neural_editors_vulgen/
```

For reproducing the experiments in our paper, we have provided easy-to-use scripts for users to use. Users can directly use them to reproduce the experiments. As training the deep learning models takes considerable amount of time and expensive hardware resources, we have saved the trained models for all the tools so that the users can use these scripts to test the models on the testing datasets directly. 

To test the 3 neural code editors (Graph2Edit, SequenceR, Hoppity) and 2 vulnerability detectors (Devign, ReVeal) at a time, users can source the "run_all.sh" directly. The script will set up Python virtual environments for each tool and reproduce the experiments automatically.

```
source run_all.sh
```

Alternatively, users can manually set up the environments and run the experiments for each tool.

To test Graph2Edit, execute:
```
conda activate g2e
cd Graph2Edit
bash run_all.sh
```

To test SequenceR, execute:
```
conda activate sequencer
cd SequenceR/chai
bash run_all.sh
```

To test Hoppity, execute:
```
conda activate hoppity
cd Hoppity
bash run_all.sh
```

To test Devign, execute:
```
conda activate devign
cd Detectors/Devign
bash run_reproduction.sh
bash run_partial_replication.sh
bash run_full_replication.sh
```

To test ReVeal, execute:
```
conda activate reveal
cd Detectors/ReVeal
bash run_reproduction.sh
bash run_partial_replication.sh
bash run_full_replication.sh
```

To review our experiment results and raw data, please check output files in the respective folder corresponding to each experiment.

To reuse five tools (Graph2Edit, SequenceR, Hoppity, Devign, ReVeal) that our empirical study works on, please check the README.md files in each tool folder and check the scripts we wrote for starting the experiments.

## Expected Results
These scripts will automatically load the trained models for each experiment and prompt the respective results in the paper like this:
```
(sequencer) root@c0db2908ca27:~/neural_editors_vulgen/SequenceR/chai# bash run_all.sh 

running testing experiment for Table-1 row-4 (SequenceR) column-2 (Original).
This may take 30 min.

sequencer-test.sh start
Starting test data translation
[2022-07-27 00:21:23,196 INFO] Translating shard 0.
sequencer-test.sh done

Testing experiment for Table-1 row-4 (SequenceR) column-2 (Original) Done
Result:
acc: 0.722884012539185
```

Please note that the output values may not be exactly the same as the ones in our paper due to the randomness of the deep learning models. Please focus on the comparison of different techniques and the conclusion of our paper.

## Running Time Estimate
Pleaes check the output of the `run_all.sh` for the estimated running time (see the output example above). Generally, each experiment of Graph2Edit takes 30-60 minutes, each experiment of Hoppity takes about 60 minutes, each experiment of SequenceR takes about 30 minutes, each experiment of ReVeal takes about 1 minute.

## Case Studies Reproduction
The experiments above are for the results in Table 1, 5, and 9. Besides, we have some other case studies. Please refer to the files in `neural_editors_vulgen/Factors` and `neural_editors_vulgen/generic_specifc`, and `neural_editors_vulgen/User Study` for other results.

Specifically, in `neural_editors_vulgen/Factors/hoppity`, users can run `python checkacc_edit.py` `python checkacc_freq.py` `python checkacc_size.py` to get the row 2 (Hoppity) results in Tables 2, 3, and 4, respectively, and use the same way to check the Graph2Edit and SequenceR results in Tables 2, 3, and 4. 

In `neural_editors_vulgen/generic_specific`, users can check the raw information for Table 7. For example, in `neural_editors_vulgen/generic_specific/g2e/matched/specific`, the number of samples is 261 and in `neural_editors_vulgen/generic_specific/g2e/matched/generic`, the number of samples is 339. Thus, the % of domain `specific` samples for Table 7, row 3 (Exactly-match samples by Graph2Edit) is 261/(261+339)=43.50%. The numbers of the two other rows can be obtained in the same way.

In `neural_editors_vulgen/User Study`, users can find our original survey in `Realistic Code Survey.pdf` and see our statistics in `res.xlsx`.









