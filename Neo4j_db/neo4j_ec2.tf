# neo4j_ec2.tf

provider "aws" {
  region = "us-west-2"
}

resource "aws_security_group" "neo4j_sg" {
  name        = "neo4j-sg"
  description = "Security group for Neo4j"

  # Allow inbound traffic for Neo4j HTTP and Bolt
  ingress {
    from_port   = 7474
    to_port     = 7474
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Adjust based on your network policy
  }

  ingress {
    from_port   = 7687
    to_port     = 7687
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Adjust based on your network policy
  }

  # Allow SSH access for setup and maintenance
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Adjust for specific IP range
  }

  # Outbound rules
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "neo4j-security-group"
  }
}

resource "aws_instance" "neo4j" {
  ami           = "ami-0c55b159cbfafe1f0" # Ubuntu AMI in us-west-2 (update as needed)
  instance_type = "t3.medium"
  key_name      = "your-ec2-keypair"
  subnet_id     = "your-subnet-id" # Replace with an appropriate subnet in the VPC

  # Attach security group
  vpc_security_group_ids = [aws_security_group.neo4j_sg.id]

  # Configure root EBS volume for persistence
  root_block_device {
    volume_type = "gp2"
    volume_size = 20 # Increase based on your storage requirements
    delete_on_termination = true
  }

  # User data to install Neo4j on launch
  user_data = <<-EOF
      #!/bin/bash
      sudo apt update
      sudo apt install -y wget gnupg
      wget -O - https://debian.neo4j.com/neotechnology.gpg.key | sudo apt-key add -
      echo "deb https://debian.neo4j.com stable 4.4" | sudo tee -a /etc/apt/sources.list.d/neo4j.list
      sudo apt update
      sudo apt install -y neo4j
      sudo systemctl enable neo4j
      sudo systemctl start neo4j
  EOF

  tags = {
    Name = "neo4j-ec2-instance"
  }
}
