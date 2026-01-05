
terraform {
  backend "s3" {
    bucket         = "my-tf-demo-bucket"
    key            = "dev/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "tf-lock-table"
    encrypt        = true
  }
}
