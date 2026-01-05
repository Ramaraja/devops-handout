
module "vpc" {
  source = "terraform-aws-modules/vpc/aws"
  name   = "prod-vpc"
  cidr   = "10.0.0.0/16"
  azs    = ["us-east-1a", "us-east-1b"]
  public_subnets  = ["10.0.1.0/24", "10.0.2.0/24"]
  private_subnets = ["10.0.3.0/24", "10.0.4.0/24"]
}

resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  subnet_id     = module.vpc.public_subnets[0]
  tags = { Name = "web-server" }
}

resource "aws_db_instance" "rds" {
  allocated_storage = 20
  engine            = "mysql"
  engine_version    = "8.0"
  instance_class    = "db.t3.micro"
  username          = "admin"
  password          = "Password123!"
  skip_final_snapshot = true
  vpc_security_group_ids = [module.vpc.default_security_group_id]
}
