
data "aws_vpc" "default" {
  default = true
}

resource "aws_instance" "example" {
  ami           = var.ami_id
  instance_type = var.instance_type
  subnet_id     = data.aws_vpc.default.default_network_acl_id
}
