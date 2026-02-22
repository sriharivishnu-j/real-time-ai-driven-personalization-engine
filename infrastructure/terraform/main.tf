provider "aws" {
  region = "us-west-2"
}

resource "aws_eks_cluster" "eks_cluster" {
  name     = "ai-personalization-cluster"
  role_arn = "${aws_iam_role.eks_cluster_role.arn}"

  vpc_config {
    subnet_ids = ["subnet-12345", "subnet-67890"]
  }
}