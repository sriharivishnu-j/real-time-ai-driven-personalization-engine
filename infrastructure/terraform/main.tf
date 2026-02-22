provider "aws" {
  region = "us-west-2"
}

module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  cluster_name    = "personalization-engine"
  cluster_version = "1.21"
  subnets         = ["subnet-12345678", "subnet-87654321"]
  vpc_id          = "vpc-12345678"
}
