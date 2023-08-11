# English to Hindi Translation Project

This project focuses on implementing an English-to-Hindi translation system using the Hugging Face Transformers library. The project utilizes the `cfilt/iitb-english-hindi` dataset and the pre-trained `Helsinki-NLP/opus-mt-en-hi` model to achieve the translation task. The translation process is broken down into several stages, each contributing to the overall success of the project.
## Project Structure
```
├───.github
│   └───workflows
├───config
├───research
├───src
│   ├───translator
│   │   ├───components
│   │   ├───config
│   │   ├───constants
│   │   ├───entity
│   │   ├───logging
│   │   ├───pipeline
│   │   ├───utils
```
The project structure is organized as follows:
- `config.yaml`: Configuration file that contains project-specific settings and parameters.
- `research`: Contains notebook experiments which were performed before modular code implementation
- `params.yaml`: Parameter file that stores model-specific parameters and configurations.
- `entity`: Directory containing entity definitions and related files.
- `src/config`: Directory containing the configuration manager for accessing project configurations.
- `components`: Directory containing various components used in the translation pipeline.
- `pipeline`: Directory containing the main text translation pipeline implementation.
- `main.py`: Main script that orchestrates the text translation process.
- `.github/workflows`:Contains code for CICD .

## Stages of the Project

### Stage 01: Data Ingestion (`stage_01_data_ingestion.py`)

This stage sets up a configuration manager, reads project configurations, and manages data ingestion settings. It provides functions to download and extract data from a remote source (`cfilt/iitb-english-hindi`) if it is not already available locally. The primary goal of this stage is to ensure that the necessary directories are created and errors are handled gracefully during the data ingestion process.

### Stage 02: Data Validation (`stage_02_data_validation.py`)

In this stage, the focus is on data validation. It ensures the presence of required files for data validation in the specified directory. The validation status is written to a status file. This step is crucial to verify the availability of necessary data files before proceeding to further stages or model training. 

### Stage 03: Data Transformation (`stage_03_data_transformation.py`)

The data transformation stage performs the actual translation using a tokenizer from the Transformers library. It transforms the English text into Hindi using the `Helsinki-NLP/opus-mt-en-hi` model and saves the transformed dataset to disk. This dataset will be utilized during model training or evaluation in the subsequent stages of the project.

### Stage 04: Model Trainer (`stage_04_model_trainer.py`)

In the model training stage, the project sets up the `Helsinki-NLP/opus-mt-en-hi`, tokenizer, and trainer for model training. The `Helsinki-NLP/opus-mt-en-hi` model is fine-tuned for English-to-Hindi translation using the transformed dataset. The trained model and tokenizer are saved to disk for future use in the project.

### Stage 05: Model Evaluation (`stage_05_model_evaluation.py`)

The final stage involves evaluating the trained Pegasus model on a test dataset. It calculates ScaredBLEU scores for the generated Hindi summaries compared to the ground-truth translations. The evaluation results are saved to a CSV file for further analysis and comparison. Note that this evaluation is demonstrated on a small subset of the test dataset (first 10 examples) for illustration purposes.

## Getting Started

To get started with the project, please follow these steps:

1. Clone the repository:
```
git clone https://github.com/Pratik94229/English-to-Hindi-Translator.git
```

2. Create a conda environment and activate it:
```
conda create -p venv python==3.8 
conda activate venv/
```

3. Install the required dependencies:
```
pip install -r requirements.txt
```
4. Run the application:
```
python app.py
```

5. Access the application:
Open your web browser and go to `http://localhost:8080` to access the translator service.

## AWS-CICD-Deployment-with-Github-Actions

#### 1. Login to AWS console.
#### 2. Create IAM user for deployment
```
#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws

#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2


#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess

```
#### 3. Create ECR repo to store/save docker image
```- Save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/text-s```
#### 4. Create EC2 machine (Ubuntu)
#### 5. Open EC2 and Install docker in EC2 Machine:
```
#optional

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess

```
#### 3. Create ECR repo to store/save docker image
newgrp docker
```
#### 6. Configure EC2 as self-hosted runner:
```
setting>actions>runner>new self hosted runner> choose os> then run command one by one
```
#### 7. Setup github secrets:
```
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = simple-app
```

For any inquiries or questions, please feel free to contact me at pratik.941@gmail.com.


## Conclusion

This English to Hindi Translation project demonstrates the end-to-end process of setting up a translation system using the Hugging Face Transformers library. Each stage plays a crucial role in the successful execution of the project, from data ingestion and validation to model training and evaluation. The project showcases how to leverage powerful pre-trained models to achieve accurate translation results.
