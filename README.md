[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=7078972&assignment_repo_type=AssignmentRepo)

# Term project for serverless coders

Term Project repo

## 📂 Directory structure

- `s1`: This is the user service
- `s2`: This is the music service
- `s3`: This is the playlist service
- `db`: This is the for the database service
- `logs`: Where logs are stored
- `music_cli`: For the music cli

## ♐ Getting started

### 1. Install dependencies

- istioctl: [Link](https://istio.io/latest/docs/ops/diagnostic-tools/istioctl/)
- kubectl: [Link](https://kubernetes.io/docs/tasks/tools/)
- helm: [Link](https://helm.sh/docs/helm/helm_install/)
- aws: [Link](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- eksctl: [Link](https://docs.aws.amazon.com/eks/latest/userguide/eksctl.html)

### 2. Generating the make files from templates

Fill in `clusters/tpl-vars.txt` with the appropriate information. Then run:

```sh
make -f k8s-tpl.mak templates
```

### 3. Login using aws configure (use if not using `tools/shell.sh`)

```
aws configure
```

and copy-paste the info from `clusterse/tpl-vars.txt` into the prompts
