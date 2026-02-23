provider "aws" {
  region = "us-west-2"
}

module "eks_cluster" {
  source          = "terraform-aws-modules/eks/aws"
  cluster_name    = "personalization-engine"
  cluster_version = "1.24"
  subnets         = var.subnets
  vpc_id          = var.vpc_id
}
