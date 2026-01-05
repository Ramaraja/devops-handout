
module "web" {
  source        = "./modules/ec2"
  ami_id        = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  name          = "web-server"
}
