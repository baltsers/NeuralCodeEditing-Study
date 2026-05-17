# NeuralCodeEditing-Study

**Generating Realistic Vulnerabilities via Neural Code Editing: An Empirical Study**

| | |
|---|---|
| Original artifact | <https://zenodo.org/records/7048525> |
| Imported from | the publications page |
| Tool | `pubs2github` |


---

## Contents

The artifact contains 775 file(s) including Python, Java, C/C++, JavaScript/TS, Shell scripts, Config files, Data files, and Documentation.

```
├── Detectors
│   ├── Devign
│   │   ├── data_loader
│   │   ├── modules
│   │   ├── devign_devign_reveal_all4.py
│   │   ├── devign_devign_reveal_all4.sh
│   │   ├── devign_devign_reveal_all4.txt
│   │   ├── devign_devign_reveal_aug2.py
│   │   ├── devign_devign_reveal_aug2.sh
│   │   ├── devign_devign_reveal_aug2.txt
│   │   ├── devign_devign_reveal_gth2.py
│   │   ├── devign_devign_reveal_gth2.sh
│   │   ├── devign_devign_reveal_gth2.txt
│   │   ├── devign_devign_reveal_ori.py
│   │   ├── devign_devign_reveal_ori.sh
│   │   ├── devign_devign_reveal_ori.txt
│   │   ├── devign_devign_reveal_syn2.py
│   │   ├── devign_devign_reveal_syn2.sh
│   │   ├── devign_devign_reveal_syn2.txt
│   │   ├── devign_devign_xen_all4.py
│   │   ├── devign_devign_xen_all4.sh
│   │   ├── devign_devign_xen_all4.txt
│   │   ├── devign_devign_xen_aug2.py
│   │   ├── devign_devign_xen_aug2.sh
│   │   ├── devign_devign_xen_aug2.txt
│   │   ├── devign_devign_xen_gth2.py
│   │   ├── devign_devign_xen_gth2.sh
│   │   ├── devign_devign_xen_gth2.txt
│   │   ├── devign_devign_xen_ori.py
│   │   ├── devign_devign_xen_ori.sh
│   │   ├── devign_devign_xen_ori.txt
│   │   ├── devign_devign_xen_syn2.py
│   │   ├── devign_devign_xen_syn2.sh
│   │   ├── devign_devign_xen_syn2.txt
│   │   ├── devign_reveal_devign_all4.py
│   │   ├── devign_reveal_devign_all4.sh
│   │   ├── devign_reveal_devign_all4.txt
│   │   ├── devign_reveal_devign_aug2.py
│   │   ├── devign_reveal_devign_aug2.sh
│   │   ├── devign_reveal_devign_aug2.txt
│   │   ├── devign_reveal_devign_gth2.py
│   │   ├── devign_reveal_devign_gth2.sh
│   │   ├── devign_reveal_devign_gth2.txt
│   │   ├── devign_reveal_devign_ori.py
│   │   ├── devign_reveal_devign_ori.sh
│   │   ├── devign_reveal_devign_ori.txt
│   │   ├── devign_reveal_devign_syn2.py
│   │   ├── devign_reveal_devign_syn2.sh
│   │   ├── devign_reveal_devign_syn2.txt
│   │   ├── LICENSE
│   │   ├── README.md
│   │   ├── trainer.py
│   │   └── utils.py
│   └── ReVeal
│       ├── __init__.py
│       ├── devign_reveal_all4.txt
│       ├── devign_reveal_all4_api_test.py
│       ├── devign_reveal_aug.txt
│       ├── devign_reveal_aug_api_test.py
│       ├── devign_reveal_gth.txt
│       … (35 more items)
… (903 more items)
```

---

## Original `Readme.md` (from the upstream artifact)

# Exploring Realistic Vulnerability Data Generation via Neural Code Editing

Using a commonly used synthetic dataset and one real-world dataset, we investigate the potential and gaps of three state-of-the-art neural code editors (Graph2Edit, Hoppity, SequenceR) for DL-based realistic vulnerability data generation.

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
- `Factors`: The code and results that we had for investigating the impacts of three factors - program length, edit length, and pattern frequency. For the other two factors vocabulary size and structure complexity, please check the respective scripts, data, and results in each tool.
- `User Study`: The user study PDF(where the author information has been removed), results and the respective figure.
- `generic_specific`: The code and results for the distribution of generic and specific vulnerabilities in RQ2.
- `Detectors`: The replication package and the respective results for our RQ3 experiments (i.e., validating the usefulness of the generated realistic vulnerability samples in improving DL-based vulnerability detectors).
	- `Devign`: The replication package and the respective results for our studied vulnerability detector Devign.
	- `ReVeal`: The replication package and the respective results for our another studied vulnerability detector ReVeal.
	
## How to use

To review our experiment results and raw data, please check output files in each experiment folder.

To replicate our experiments of a tool, check the README.md files in each experiment folder and check the scripts we wrote for starting the experiments.

