# vpc.tf
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "3.0"
  name    = "eks-vpc"
  cidr    = "10.0.0.0/16"

  azs             = ["us-west-2a", "us-west-2b"]
  public_subnets  = ["10.0.1.0/24", "10.0.2.0/24"]
  private_subnets = ["10.0.3.0/24", "10.0.4.0/24"]

  enable_nat_gateway = true
  single_nat_gateway = true

  tags = {
    Name = "eks-vpc"
  }
}