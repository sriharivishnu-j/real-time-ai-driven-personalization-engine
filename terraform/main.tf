provider "aws" {
  region = "us-west-2"
}

module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  cluster_name    = "personalization-cluster"
  cluster_version = "1.21"
  subnets         = ["subnet-12345", "subnet-67890"]
  vpc_id          = "vpc-abcde"
}
