
resource "aws_instance" "demo" {
  ami           = "ami-0c55b159cbfafe1f0" # Amazon Linux 2
  instance_type = "t2.micro"
  tags = {
    Name = "terraform-demo"
  }
}
