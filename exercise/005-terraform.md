### **Terraform Core Concepts**
| Concept | Description |
|---------|-------------|
| **Providers** | Interfaces with cloud providers (AWS, Azure, GCP). |
| **Resources** | Defines infrastructure components (VMs, networks, storage). |
| **Variables** | Stores dynamic values. |
| **State** | Keeps track of managed resources. |
| **Modules** | Reusable components for infrastructure. |

---
### **Terraform Exercises**
**Infrastructure as Code (IaC)**.  

---

### **1. Deploy an AWS EC2 Instance**
**Create an AWS EC2 instance using Terraform.**  

#### **Step 1: Create `main.tf`**
```hcl
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "my_instance" {
  ami           = "ami-0c55b159cbfafe1f0"  # Ubuntu AMI
  instance_type = "t2.micro"

  tags = {
    Name = "Terraform-Instance"
  }
}
```

#### **Step 2: Run Terraform**
```bash
terraform init
terraform apply -auto-approve
terraform destroy -auto-approve  # Cleanup
```

---

### **2. Use Terraform Variables**
**Modify the previous exercise to use variables.**  

#### **Step 1: Create `variables.tf`**
```hcl
variable "region" {
  default = "us-east-1"
}

variable "instance_type" {
  default = "t2.micro"
}

variable "ami_id" {
  default = "ami-0c55b159cbfafe1f0"
}
```

#### **Step 2: Update `main.tf`**
```hcl
provider "aws" {
  region = var.region
}

resource "aws_instance" "example" {
  ami           = var.ami_id
  instance_type = var.instance_type

  tags = {
    Name = "Terraform-Instance"
  }
}
```

#### **Step 3: Run Terraform**
```bash
terraform apply -auto-approve
```
**Your instance will now be created using variables.**  

---

### **3. Create an S3 Bucket**
**Use Terraform to create an AWS S3 bucket.**  

#### **Step 1: Create `s3.tf`**
```hcl
resource "aws_s3_bucket" "my_bucket" {
  bucket = "my-terraform-bucket-12345"

  tags = {
    Name = "MyS3Bucket"
  }
}
```

#### **Step 2: Run Terraform**
```bash
terraform init
terraform apply -auto-approve
```

**You can verify the bucket in AWS S3 Console.**  

---

### **4. Add an Output Variable**
**Get the Public IP of an EC2 instance.**  

#### **Update `main.tf`**
```hcl
output "instance_public_ip" {
  value = aws_instance.example.public_ip
}
```

#### **Run Terraform**
```bash
terraform apply -auto-approve
```
**Terraform will output the EC2 Public IP.**  

---

### **5. Use Terraform Remote State (S3)**
**Store Terraform state in AWS S3.**  

#### **Create `backend.tf`**
```hcl
terraform {
  backend "s3" {
    bucket = "my-terraform-state-bucket"
    key    = "terraform.tfstate"
    region = "us-east-1"
  }
}
```

#### **Run Terraform**
```bash
terraform init
```
**Terraform state will now be stored in S3.**  

---

### **6. Deploy an Nginx Server with Terraform and User Data**
**Launch an EC2 instance and install Nginx automatically.**  

#### **Create `nginx.tf`**
```hcl
resource "aws_instance" "nginx_server" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  user_data = <<-EOF
              #!/bin/bash
              sudo apt update
              sudo apt install -y nginx
              sudo systemctl start nginx
              sudo systemctl enable nginx
              EOF

  tags = {
    Name = "NginxServer"
  }
}

output "nginx_server_ip" {
  value = aws_instance.nginx_server.public_ip
}
```

#### **Run Terraform**
```bash
terraform apply -auto-approve
```
**Visit `http://<nginx_server_ip>` in your browser.**  

---

### **7. Deploy a VPC with Public and Private Subnets**
**Create a custom VPC, public subnet, and private subnet.**  

#### **Create `vpc.tf`**
```hcl
resource "aws_vpc" "my_vpc" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "public_subnet" {
  vpc_id     = aws_vpc.my_vpc.id
  cidr_block = "10.0.1.0/24"
}

resource "aws_subnet" "private_subnet" {
  vpc_id     = aws_vpc.my_vpc.id
  cidr_block = "10.0.2.0/24"
}
```

#### **Run Terraform**
```bash
terraform apply -auto-approve
```

---

### **8. Terraform Modules**
📌 **Encapsulate EC2 creation into a reusable module.**  

#### **Step 1: Create a Module (`modules/ec2/main.tf`)**
```hcl
resource "aws_instance" "example" {
  ami           = var.ami
  instance_type = var.instance_type

  tags = {
    Name = var.name
  }
}
```

#### **Step 2: Define Variables (`modules/ec2/variables.tf`)**
```hcl
variable "ami" {}
variable "instance_type" {}
variable "name" {}
```

#### **Step 3: Use the Module in `main.tf`**
```hcl
module "ec2_instance" {
  source        = "./modules/ec2"
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  name          = "MyModularEC2"
}
```

#### **Run Terraform**
```bash
terraform apply -auto-approve
```


---

### **9. CI/CD Pipeline for Terraform**
**Run Terraform in Jenkins pipeline.**  

#### **Step 1: Create `Jenkinsfile`**
```groovy
pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/myrepo/terraform.git'
            }
        }
        stage('Terraform Init') {
            steps {
                sh 'terraform init'
            }
        }
        stage('Terraform Plan') {
            steps {
                sh 'terraform plan'
            }
        }
        stage('Terraform Apply') {
            steps {
                sh 'terraform apply -auto-approve'
            }
        }
    }
}
```

#### **Step 2: Add to Jenkins Pipeline**
- Create a **Jenkins job**.
- Set **Pipeline Script from SCM**.
- Select **Git Repository** and enter the repo URL.
- Run the pipeline.

