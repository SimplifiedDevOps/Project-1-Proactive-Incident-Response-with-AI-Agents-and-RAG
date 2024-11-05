# cloudwatch.tf
resource "aws_cloudwatch_log_group" "eks_log_group" {
  name              = "/aws/eks/cluster/my-eks-cluster"
  retention_in_days = 7
}
