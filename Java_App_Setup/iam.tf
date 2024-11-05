# iam.tf
module "eks_iam_role" {
  source = "terraform-aws-modules/iam/aws//modules/eks-role"

  role_name           = "eks-cluster-role"
  attach_eks_policies = true
  tags = {
    Name = "eks-cluster-role"
  }
}
