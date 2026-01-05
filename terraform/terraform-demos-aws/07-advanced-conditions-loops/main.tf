
variable "create_instance" {
  default = true
}

variable "servers" {
  default = {
    app1 = "t2.micro"
    app2 = "t2.small"
  }
}

resource "aws_instance" "apps" {
  for_each      = var.create_instance ? var.servers : {}
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = each.value
  tags = { Name = each.key }
}
