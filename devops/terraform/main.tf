provider "aws" {
  region = "us-west-2"
}

resource "aws_eks_cluster" "personalization_cluster" {
  name     = "personalization-cluster"
  role_arn = aws_iam_role.eks_cluster_role.arn

  vpc_config {
    subnet_ids = [aws_subnet.eks_subnet.id]
  }
}